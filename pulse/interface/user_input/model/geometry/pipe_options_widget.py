from copy import deepcopy
import warnings

from PyQt5.QtWidgets import QWidget, QLineEdit, QComboBox, QPushButton, QSlider, QLabel
from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

from molde.stylesheets import set_qproperty
from opps.model import Pipe, Bend

from pulse import app, UI_DIR
from pulse.interface.user_input.model.setup.cross_section.cross_section_widget import CrossSectionWidget


class PipeOptionsWidget(QWidget):
    edited = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        ui_path = UI_DIR / "model/geometry/pipe_option_widget.ui"
        uic.loadUi(ui_path, self)

        self.pipeline = app().project.pipeline
        self.render_widget = app().main_window.geometry_widget

        self.structure_type = Pipe
        self.add_function = self.pipeline.add_bent_pipe
        self.attach_function = self.pipeline.connect_bent_pipes
        self.cross_section_info = None
        self.user_defined_bending_radius = 0

        self._define_qt_variables()
        self._create_connections()
        self._initialize()

    def _define_qt_variables(self):
        self.bending_options_combobox: QComboBox
        self.bending_radius_line_edit: QLineEdit

        self.set_section_button: QPushButton
        self.cross_section_widget: CrossSectionWidget = self.parent().cross_section_widget

    def _config_layout(self):
        self.cross_section_widget._add_icon_and_title()
        self.cross_section_widget.set_inputs_to_geometry_creator()     
        self.cross_section_widget.hide_all_tabs()     
        self.cross_section_widget.tabWidget_general.setTabVisible(0, True)
        self.cross_section_widget.tabWidget_pipe_section.setTabVisible(0, True)
        self.cross_section_widget.lineEdit_outside_diameter.setFocus()
        self.cross_section_widget.hide()

    def _create_connections(self):
        self.bending_options_combobox.currentTextChanged.connect(self.bending_options_changed_callback)
        self.bending_radius_line_edit.textEdited.connect(self.bending_radius_changed_callback)
        self.set_section_button.clicked.connect(self.show_cross_section_widget_callback)
        self.cross_section_widget.pushButton_confirm_pipe.clicked.connect(self.define_cross_section_callback)

    def _initialize(self):
        self.bending_options_changed_callback("long radius")
        self.set_section_button.setProperty("warning", True)
        self.style().polish(self.set_section_button)

    def get_parameters(self) -> dict:
        if self.cross_section_info is None:
            return

        parameters = self.cross_section_info.get("section_parameters")
        if parameters is None:
            return

        kwargs = dict()
        kwargs["diameter"] = parameters[0]
        kwargs["thickness"] = parameters[1]
        kwargs["curvature_radius"] = self.get_bending_radius(parameters[0])
        kwargs["extra_info"] = dict(
            structural_element_type = "pipe_1",
            cross_section_info = deepcopy(self.cross_section_info),
        )
        return kwargs

    def show_cross_section_widget_callback(self):
        self._config_layout()
        self.cross_section_widget.show()

    def define_cross_section_callback(self):
        if not self.isVisible():
            return

        if self.cross_section_widget.get_constant_section_pipe_parameters():
            return

        self.cross_section_info = self.cross_section_widget.pipe_section_info
        self.cross_section_widget.hide()
        set_qproperty(self.set_section_button, status="default")
        self.edited.emit()

    def get_bending_radius(self, diameter):
        if (self.bending_option == "long radius") or (self.bending_option == "short radius"):
            return self.bending_factor * diameter

        elif self.bending_option == "user-defined":
            return self.user_defined_bending_radius

        else:
            return 0

    def bending_options_changed_callback(self, text: str):
        self.bending_factor = 0
        self.bending_option = text.lower().strip()
        self.bending_radius_line_edit.setDisabled(True)

        if self.bending_option == "long radius":
            self.bending_factor = 1.5
            self.bending_radius_line_edit.setText("1.5 * D")

        elif self.bending_option == "short radius":
            self.bending_factor = 1
            self.bending_radius_line_edit.setText("1.0 * D")

        elif self.bending_option == "user-defined":
            r = str(round(self.user_defined_bending_radius, 4))
            self.bending_radius_line_edit.setText(r)
            self.bending_radius_line_edit.setDisabled(False)
            self.bending_radius_line_edit.setFocus()

        elif self.bending_option == "disabled":
            self.bending_factor = 0
            self.bending_radius_line_edit.setText("disabled")

        else:
            warnings.warn(f'Bending option "{self.bending_option}" not available.')

        self._apply_bending_radius_to_selection()
        self.edited.emit()

    def bending_radius_changed_callback(self, text: str):
        try:
            self.user_defined_bending_radius = float(text)

        except ValueError:
            self.user_defined_bending_radius = 0

        else:
            self._apply_bending_radius_to_selection()
            self.edited.emit()

    def _apply_bending_radius_to_selection(self):
        for bend in self.pipeline.selected_structures:
            if not isinstance(bend, Bend):
                continue
            bend.curvature = self.get_bending_radius(bend.diameter)
        self.pipeline.recalculate_curvatures()
