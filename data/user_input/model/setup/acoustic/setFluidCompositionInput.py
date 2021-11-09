from operator import concat
from PyQt5.QtWidgets import QTreeWidgetItem, QLineEdit, QDialog, QTabWidget, QLabel, QCheckBox, QSpinBox, QPushButton, QWidget, QFileDialog, QComboBox, QTreeWidget
import os
from os.path import basename

from numpy.lib.utils import lookfor
from data.user_input.project.printMessageInput import PrintMessageInput
from data.user_input.project.callDoubleConfirmationInput import CallDoubleConfirmationInput
from pulse.utils import get_new_path
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import uic
from PyQt5.QtCore import Qt, QSize
import numpy as np
import sys
import configparser
from PyQt5 import uic

window_title_1 = "ERROR"

class SetFluidCompositionInput(QDialog):
    def __init__(self, project, opv, selected_fluid_to_edit=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('data/user_input/ui/model/setup/acoustic/setFluidCompositionInput.ui', self)
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowModality(Qt.WindowModal)

        icons_path = 'data\\icons\\'
        self.icon_pulse = QIcon(icons_path + 'pulse.png')
        self.setWindowIcon(self.icon_pulse)

        self.icon_animate = QIcon(icons_path + 'play_pause.png')

        self.project = project
        self.opv = opv
        self.opv.setInputObject(self)
        self.selected_fluid_to_edit = selected_fluid_to_edit

        self.save_path = ""
        self.export_file_path = ""
        self.userPath = os.path.expanduser('~')
        self.fluid_path = project.get_fluid_list_path()

        self.map_properties = { "D" : "fluid density",
                                "CP" : "specific heat Cp",
                                "CV" : "specific heat Cv",
                                "CP/CV" : "isentropic coefficient",
                                "W" : "speed of sound",
                                "VIS" : "dynamic viscosity",
                                "TCX" : "thermal conductivity",
                                "PRANDTL" : "Prandtl number",
                                "TD" : "thermal diffusivity",
                                "KV" : "kinematic viscosity" }

        self.selected_fluid = ""
        self.str_composition_value = ""
        self.composition_value = 0
        self.remaining_composition = 1
        self.list_fluids = []
        self.fluid_to_composition = {}
        self.fluid_states = {}
        self.complete = False

        self.label_selected_fluid = self.findChild(QLabel, 'label_selected_fluid')
        self.label_title_remaining_fraction = self.findChild(QLabel, 'label_title_remaining_fraction')
        self.label_remaining_composition = self.findChild(QLabel, 'label_remaining_composition')
        self.lineEdit_composition = self.findChild(QLineEdit, 'lineEdit_composition')
        self.lineEdit_fluid_name = self.findChild(QLineEdit, 'lineEdit_fluid_name')

        self.label_fluid_state_index = self.findChild(QLabel, 'label_fluid_state_index')
        self.lineEdit_temperature = self.findChild(QLineEdit, 'lineEdit_temperature')
        self.lineEdit_pressure = self.findChild(QLineEdit, 'lineEdit_pressure')
        
        # self.lineEdit_FileName = self.findChild(QLineEdit, 'lineEdit_FileName')
        # self.checkBox_export = self.findChild(QCheckBox, 'checkBox_export')
        # self.checkBox_export.clicked.connect(self.update_export_tabs)
        # self.checkBox_export.setVisible(False)
        # self.label_export_path = self.findChild(QLabel, 'label_export_path')

        self.comboBox_temperature_units = self.findChild(QComboBox, 'comboBox_temperature_units')
        self.comboBox_pressure_units = self.findChild(QComboBox, 'comboBox_pressure_units')
        
        self.pushButton_confirm = self.findChild(QPushButton, 'pushButton_confirm')
        self.pushButton_confirm.clicked.connect(self.get_fluid_properties)
        self.pushButton_reset_fluid = self.findChild(QPushButton, 'pushButton_reset_fluid')
        self.pushButton_reset_fluid.clicked.connect(self.reset_fluid)

        # self.pushButton_clean = self.findChild(QPushButton, 'pushButton_clean')
        # self.pushButton_clean.setVisible(False)
        # self.pushButton_clean.clicked.connect(self.reset_input_field)

        self.pushButton_add_gas = self.findChild(QPushButton, 'pushButton_add_gas')
        self.pushButton_add_gas.clicked.connect(self.add_selected_gas)
    
        self.pushButton_remove_gas = self.findChild(QPushButton, 'pushButton_remove_gas')
        self.pushButton_remove_gas.clicked.connect(self.remove_selected_gas)

        self.pushButton_add_fluid_state = self.findChild(QPushButton, 'pushButton_add_fluid_state')
        self.pushButton_add_fluid_state.clicked.connect(self.add_fluid_state)

        self.pushButton_remove_fluid_state = self.findChild(QPushButton, 'pushButton_remove_fluid_state')
        self.pushButton_remove_fluid_state.clicked.connect(self.remove_fluid_state)

        # self.pushButton_use_remaining_molar_fraction = self.findChild(QPushButton, 'pushButton_use_remaining_molar_fraction')
        # self.pushButton_use_remaining_molar_fraction.clicked.connect(self.use_remaining_molar_fraction)

        self.tabWidget_general = self.findChild(QTabWidget, 'tabWidget_general')
        self.tab_fluid_setup = self.tabWidget_general.findChild(QWidget, 'tab_main')
        self.tab_pretest_analysis = self.tabWidget_general.findChild(QWidget, 'tab_export')

        self.tabWidget_general.currentChanged.connect(self.update_state_treeWidget_info)
        
        self.treeWidget_reference_gases = self.findChild(QTreeWidget, 'treeWidget_reference_gases')
        self.treeWidget_reference_gases.itemClicked.connect(self.on_click_item_reference_gases)
        self.treeWidget_new_gas = self.findChild(QTreeWidget, 'treeWidget_new_gas')
        self.treeWidget_new_gas.itemClicked.connect(self.on_click_item_new_gas)
        self.treeWidget_new_gas.setColumnWidth(0, 376)

        self.treeWidget_new_gas.itemDoubleClicked.connect(self.on_double_click_item_new_gas)

        self.treeWidget_fluids_states = self.findChild(QTreeWidget, 'treeWidget_fluids_states')
        self.treeWidget_fluids_states.setColumnWidth(0, 60)
        self.treeWidget_fluids_states.setColumnWidth(1, 120)
        self.treeWidget_fluids_states.setColumnWidth(2, 150)
        self.treeWidget_fluids_states.itemClicked.connect(self.on_click_item_fluid_state)
        
        self.update_remainig_composition()
        # self.update_export_tabs()
        if self.default_library_gases():
            return
        self.load_default_gases_info()
        self.update_selected_fluid()
        self.exec()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.get_fluid_properties()
        elif event.key() == Qt.Key_Backspace or event.key() == Qt.Key_Delete:
            self.remove_selected_gas()
        elif event.key() == Qt.Key_Escape:
            self.close()

    def update_selected_fluid(self):
        if self.selected_fluid_to_edit:
            [fluid_name, temperature, pressure, key_mixture, molar_fractions] = self.selected_fluid_to_edit
            fluid_file_names = key_mixture.split(";")
            self.lineEdit_fluid_name.setText(fluid_name.split(" @ ")[0])
            self.lineEdit_temperature.setText(str(temperature))
            self.lineEdit_pressure.setText(str(pressure))

            for index, fluid_file_name in enumerate(fluid_file_names):
                final_name = self.fluid_file_to_final_name[fluid_file_name]
                str_molar_fraction = str(round(molar_fractions[index]*100, 5))
                self.fluid_to_composition[final_name] = [str_molar_fraction, molar_fractions[index], fluid_file_name]

            self.load_new_gas_composition_info()
            self.update_remainig_composition()

    def use_remaining_molar_fraction(self):
        self.lineEdit_composition.setText(str(self.remaining_composition))

    def add_selected_gas(self):
        if self.label_selected_fluid.text() != "":
            if self.check_composition_input():
                return
            self.load_new_gas_composition_info()
            self.update_remainig_composition()  
        else:
            title = "None 'Fluid' selected"
            message = "Dear user, it is necessary to select a fluid in the list to proceed"
            PrintMessageInput([title, message, window_title_1])   
    
    def update_remainig_composition(self):
        self.remaining_composition = 1
        for [_, composition_value, _] in self.fluid_to_composition.values():
            self.remaining_composition -= composition_value

        if round(abs(self.remaining_composition),5) > 0:
            self.label_remaining_composition.setVisible(True)
            self.label_title_remaining_fraction.setVisible(True)
            _remain = round(self.remaining_composition*100, 5)
            self.label_remaining_composition.setText(str(_remain))
        else:
            self.label_remaining_composition.setText("")
            self.label_remaining_composition.setVisible(False)
            self.label_title_remaining_fraction.setVisible(False)
        
    def create_font(self, size):
        self.font = QFont()
        self.font.setPointSize(size)
        self.font.setItalic(False)

    def remove_selected_gas(self):
        if self.label_selected_fluid.text() != "":
            _fluid = self.label_selected_fluid.text()
            if _fluid in self.fluid_to_composition.keys():
                self.fluid_to_composition.pop(_fluid)
                self.load_new_gas_composition_info()
                self.update_remainig_composition() 

    def reset_fluid(self):
            title = f"Resetting of the current 'Fluid Composition'"
            message = "Do you really want to reset the current Fluid Composition?\n\n"
            
            message += "\n\nPress the Continue button to proceed with the resetting or press Cancel or "
            message += "\nClose buttons to abort the current operation."
            read = CallDoubleConfirmationInput(title, message, leftButton_label='Cancel', rightButton_label='Continue')

            if read._stop:
                return

            self.fluid_to_composition.clear()
            self.load_new_gas_composition_info()
            self.update_remainig_composition()

    def load_default_gases_info(self):
        self.treeWidget_reference_gases.clear()
        self.treeWidget_reference_gases.setGeometry(10, 142, 376, 400)
        self.treeWidget_reference_gases.headerItem().setText(0, "Default fluid library")
        for gas in self.list_gases.keys():
            new = QTreeWidgetItem([gas])
            new.setTextAlignment(0, Qt.AlignCenter)
            self.treeWidget_reference_gases.addTopLevelItem(new)
        
    def load_new_gas_composition_info(self):
        # if self.selected_fluid != "":
        self.treeWidget_new_gas.clear()
        self.treeWidget_new_gas.setGeometry(576, 142, 509, 400)
        self.treeWidget_new_gas.headerItem().setText(0, "Fluid")
        self.treeWidget_new_gas.headerItem().setText(1, "Composition [%]")
        for fluid, [str_composition, _, _] in self.fluid_to_composition.items():
            new = QTreeWidgetItem([fluid, str_composition])
            new.setTextAlignment(0, Qt.AlignCenter)
            new.setTextAlignment(1, Qt.AlignCenter)
            self.treeWidget_new_gas.addTopLevelItem(new)
        self.label_selected_fluid.setText("")
        self.lineEdit_composition.setText("")

    def check_composition_input(self):
        self.str_composition_value = self.lineEdit_composition.text()
        if self.str_composition_value != "":
            title = "Invalid input value to the fluid Composition"
            message = ""
            value = None
            try:
                value = float(self.str_composition_value)
            except Exception as log_error:
                message = "Dear user, you have typed an invalid entry at the fluid Composition input. "
                message += "\nPlease, check the typed value to proceed with the fluid setup.\n\n"
                message += str(log_error)
            
            if value is not None:             
                if value>100 or value<0:
                    message = "Dear user, you have typed an invalid entry at the fluid Composition input. "
                    message += "The value must be a positive value less or equals to 100."
                    message += "\nPlease, check the typed value to proceed with the fluid setup."

            if round(value/100, 5) >  round(self.remaining_composition, 5):
                _remain = round(self.remaining_composition*100, 5)
                message = "Dear user, you have typed an invalid entry at the Fluid Composition input. "
                message += f"The value must be a positive value less or equals to {_remain}%."
                message += "\nPlease, check the typed value to proceed with the fluid setup."

            if message == "":
                
                self.composition_value = value/100
                fluid_file_name, _, _ = self.list_gases[self.selected_fluid]
                self.fluid_to_composition[self.selected_fluid] = [  self.str_composition_value, 
                                                                    self.composition_value, 
                                                                    fluid_file_name  ]
                if self.composition_value == 0:
                    if self.selected_fluid in self.fluid_to_composition.keys():
                        self.fluid_to_composition.pop(self.selected_fluid)       
                return False
            else:
                PrintMessageInput([title, message, window_title_1])
                return True
        else:
            title = "Empty entry at molar fraction input field"
            message = "An Empty entry has been detected at molar fraction input field. "
            message += "You should to inform a valid positive float number less than 1 to proceed."
            PrintMessageInput([title, message, window_title_1])
            return True

    def update_label_selected_fluid_font(self):
        if len(self.selected_fluid) < 20:
            fontsize = 12
        elif len(self.selected_fluid) < 40:
            fontsize = 11
        elif len(self.selected_fluid) < 60:
            fontsize = 10
        elif len(self.selected_fluid) < 70:
            fontsize = 9
        else:
            fontsize = 8
        self.create_font(fontsize)
        self.label_selected_fluid.setFont(self.font)

    def on_click_item_reference_gases(self, item):
        self.selected_fluid = item.text(0)
        self.label_selected_fluid.setText(self.selected_fluid)
        self.update_label_selected_fluid_font()
    
    def on_double_click_item_new_gas(self, item):
        return

    def on_click_item_new_gas(self, item):
        self.selected_fluid = item.text(0)
        self.label_selected_fluid.setText(item.text(0))
        self.lineEdit_composition.setText(item.text(1))
        self.update_label_selected_fluid_font()
        
    def get_fluid_properties(self):
        message = ""
        self.fluid_setup = []
        self.errors = {}
        if round(self.remaining_composition, 5) == 0:
            if self.lineEdit_fluid_name.text() != "":
                self.fluid_properties = {}
                units = self.RefProp.GETENUMdll(0, "MASS BASE SI").iEnum

                fluids_string = ""
                molar_fractions = []
                for _, _fraction, file_name in self.fluid_to_composition.values():
                    fluids_string += file_name + ";"
                    molar_fractions.append(_fraction)
                fluids_string = fluids_string[:-1]

                values = self.check_input_values_with_units()
                if values is None:
                    return
                else:
                    [temperature_K, pressure_Pa] = values
                    self.fluid_properties["temperature"] = temperature_K
                    self.fluid_properties["pressure"] = pressure_Pa

                self.fluid_properties["fluid name"] = self.lineEdit_fluid_name.text()
                self.fluid_properties["id"] = ""
                self.fluid_properties["color"] = ""
                
                for key_prop in ["D", "CV", "CP", "CP/CV", "W", "VIS", "TCX"]:#, "PRANDTL", "TD", "KV"]:
                    read = self.RefProp.REFPROPdll( fluids_string, "TP", key_prop, units, 0, 0, 
                                                    temperature_K, pressure_Pa, molar_fractions )

                    if read.herr:
                        self.errors[self.map_properties[key_prop]] = read.herr
                    # print(self.map_properties[key_prop], f" {read.Output[0]} ", read.hUnits)
                    self.fluid_properties[self.map_properties[key_prop]] = read.Output[0]

                self.fluid_properties["impedance"] = self.fluid_properties["fluid density"]*self.fluid_properties["speed of sound"]
                self.fluid_setup = [fluids_string, molar_fractions]
                
                if self.process_errors():
                    return
                self.complete = True
                self.close()
            else:
                title = "Additional input required"
                message = "Define a fluid name at specific input field to proceed."
                self.lineEdit_fluid_name.setFocus()
        else:
            title = "Fluid composition not finished"
            message = "Dear user, you should to complete the fluid mixture composition to proceed.\n"
            message += "The sum of all fluids molar fractions must be equals to 1. It is recommended "
            message += "to check the inserted molar fractions until this requirement is met."
        if message != "":
            PrintMessageInput([title, message, "ERROR"])

    def process_errors(self):
        if len(self.errors) != 0:
            title = "REFPROP: Error while processing fluid properties"
            message = "The following errors were found while processing the fluid properties.\n\n"
            for key, _error in self.errors.items():
                message += f"{str(key)}: {str(_error)}\n"
            message += "\nIt is recommended to check the fluid composition and state properties to proceed."
            PrintMessageInput([title, message, "ERROR"], fontsizes=[13, 10])
            return True

    def get_fluid_state_index(self):
        index = len(self.fluid_states) + 1
        if str(index) in self.fluid_states.keys():
            index = 1
            while str(index) in self.fluid_states.keys():
                index += 1
        self.label_fluid_state_index.setText(str(index))
        return index

    def add_fluid_state(self):
        index = self.get_fluid_state_index()
        values = self.check_input_values_with_units()
        if values is None:
            return
        else:
            key = self.label_fluid_state_index.text()
            self.fluid_states[key] = values
        self.update_state_treeWidget_info()

    def check_temperature_value(self):
        temperature = None
        str_value = self.lineEdit_temperature.text()
        if str_value != "":
            try:
                temperature = float(str_value)
            except Exception as log_error:
                title = "Invalid entry to the temperature"
                message = "Dear user, you have typed an invalid value at the temperature input field."
                message += "You should to inform a valid float number to proceed."
                window_title = "ERROR"
                PrintMessageInput([title, message, window_title])
        else:
            title = "Empty temperature input field"
            message = "Dear user, the temperature input field is empty. Please, inform a valid float number to proceed."
            window_title = "ERROR"
            PrintMessageInput([title, message, window_title])
            self.lineEdit_temperature.setFocus()
        return temperature

    def check_pressure_value(self):
        pressure = None
        str_value = self.lineEdit_pressure.text()
        if str_value != "":
            try:
                pressure = float(str_value)
            except Exception as log_error:
                title = "Invalid entry to the pressure"
                message = "Dear user, you have typed an invalid value at the pressure input field."
                message += "You should to inform a valid float number to proceed."
                window_title = "ERROR"
                PrintMessageInput([title, message, window_title])
        else:
            title = "Empty pressure input field"
            message = "Dear user, the pressure input field is empty. Please, inform a valid float number to proceed."
            window_title = "ERROR"
            PrintMessageInput([title, message, window_title])
            self.lineEdit_pressure.setFocus()        
        return pressure

    def remove_fluid_state(self):
        key = self.label_fluid_state_index.text()
        if key in self.fluid_states.keys():
            self.fluid_states.pop(key)
            self.update_state_treeWidget_info()

    def get_unit_labels_for_temperature_and_pressure(self):
        temperature_unit_labels = ["K", "°C", "°F"]
        pressure_unit_labels = ["Pa", "kPa", "bar", "psi"]
        index_temperature = self.comboBox_temperature_units.currentIndex()
        index_pressure = self.comboBox_pressure_units.currentIndex()
        label_temperature = temperature_unit_labels[index_temperature]
        label_pressure = pressure_unit_labels[index_pressure]
        return label_temperature, label_pressure

    def check_input_values_with_units(self):
        unit_temperature, unit_pressure = self.get_unit_labels_for_temperature_and_pressure()

        _temperature_value = self.check_temperature_value()
        if _temperature_value is None:
            return None

        if unit_temperature == "°C" :
            temperature = _temperature_value + 273.15
        elif unit_temperature == "°F" :
            temperature = (_temperature_value-32)*(5/9) + 273.15
        else:
            temperature = _temperature_value
        if temperature < 0:
            title = "Invalid entry to the temperature"
            message = "The typed value at temperature input field reaches a negative value in Kelvin scale."
            message += "It is necessary to enter a value that maintains the physicall coherence and consistence "
            message += "to proceed with the fluid setup."
            PrintMessageInput([title, message, window_title_1])
            return None

        _pressure_value = self.check_pressure_value()
        if _pressure_value is None:
            return None

        if unit_pressure == "kPa":
            _pressure_value *= 1e3
        elif unit_pressure == "bar":
            _pressure_value *= 101325
        elif unit_pressure == "psi":
            _pressure_value *= 6894.75729
        else:
            pressure = _pressure_value
        if pressure < 0:
            title = "Invalid entry to the pressure"
            message = "The typed value at pressure input field reaches a negative value in Pascal scale."
            message += "It is necessary to enter a value that maintains the physicall coherence and consistence "
            message += "to proceed with the fluid setup."
            PrintMessageInput([title, message, window_title_1])
            return None

        return [temperature, pressure]

    def update_fluid_state_header(self):
        unit_temperature, unit_pressure = self.get_unit_labels_for_temperature_and_pressure()
        self.treeWidget_fluids_states.headerItem().setText(0, f"Index")
        self.treeWidget_fluids_states.headerItem().setText(1, f"Temperature [{unit_temperature}]")
        self.treeWidget_fluids_states.headerItem().setText(2, f"Pressure [{unit_pressure}]")
        self.treeWidget_fluids_states.headerItem().setText(3, "Status")
        for i in range(4):
            self.treeWidget_fluids_states.headerItem().setTextAlignment(i, Qt.AlignCenter)

    def update_state_treeWidget_info(self):
        if self.tabWidget_general.currentIndex() == 1:
            self.update_fluid_state_header()
            self.treeWidget_fluids_states.clear()
            # self.treeWidget_fluids_states.setGeometry(592, 68, 509, 400)
            for index, [temperature, pressure] in self.fluid_states.items():
                new = QTreeWidgetItem([index, str(temperature), str(pressure), "not checked"])
                for i in range(4):
                    new.setTextAlignment(i, Qt.AlignCenter)
                self.treeWidget_fluids_states.addTopLevelItem(new)
            self.lineEdit_temperature.setText("")
            self.lineEdit_pressure.setText("")
            self.label_fluid_state_index.setText("")

    def on_click_item_fluid_state(self, item):
        str_index = item.text(0)
        if str_index != "":
            self.label_fluid_state_index.setText(str_index)

    def run_pretest_analysis(self):
        pass

    def default_library_gases(self):
        try:
            self.list_gases = {}
            self.fluid_file_to_final_name = {}
            from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary
            self.RefProp = REFPROPFunctionLibrary(os.environ['RPPREFIX'])
            self.RefProp.SETPATHdll(os.environ['RPPREFIX'])
            refProp_path = os.getenv("SystemDrive") + "\\Program Files (x86)\\REFPROP"

            if os.path.exists(refProp_path):
                refProp_fluids_path = get_new_path(refProp_path, "FLUIDS")
                list_files = os.listdir(refProp_fluids_path)
                count = 0
                for fluid_file in list_files:
                    if ".BNC" not in fluid_file:
                        filepath = get_new_path(refProp_fluids_path, fluid_file)
                        
                        f = open(filepath, 'r')
                        line_0 = f.readline()
                        line_1 = f.readline()
                        line_2 = f.readline()

                        f.close()
                        short_name = line_0.split("!")[0]
                        full_name = line_2.split("!")[0]
                
                        letter = " "
                        while letter == " ":
                            short_name = short_name[:-1]
                            letter = short_name[-1]
                            
                        letter = " "
                        while letter == " ":
                            full_name = full_name[:-1]
                            letter = full_name[-1]

                        final_name = short_name if short_name == full_name else f"{short_name} ({full_name})"
                        self.list_gases[final_name] = [fluid_file, short_name, full_name]
                        self.fluid_file_to_final_name[fluid_file] = final_name
            else:
                title = "REFPROP installation not detected"
                message = "Dear user, the REFPROP application files cannot be found in the 'Program Files (x86)' folder. "
                message += "Please, install the REFPROP on your computer to enable the set-up of the fluids mixture."
                PrintMessageInput([title, message, "ERROR"])
                return True

        except Exception as log_error:
            title = "Error while loading REFPROP"
            message = "An error has been reached while trying to load REFPROP data."
            message += f"\n\n{str(log_error)}"
            PrintMessageInput([title, message, "ERROR"])
            return True