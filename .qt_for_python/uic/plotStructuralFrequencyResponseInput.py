# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Kula\Petrobras\OpenPulse\data\user_input\ui\Plots\Results\Structural\plotStructuralFrequencyResponseInput.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(472, 411)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(472, 411))
        Dialog.setMaximumSize(QtCore.QSize(472, 411))
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Kula\\Petrobras\\OpenPulse\\data\\user_input\\ui\\Plots\\Results\\Structural\\../../../../../../Downloads/load - Copia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWhatsThis("")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 472, 41))
        self.frame.setMinimumSize(QtCore.QSize(472, 0))
        self.frame.setMaximumSize(QtCore.QSize(472, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 6, 452, 30))
        self.label.setMinimumSize(QtCore.QSize(452, 30))
        self.label.setMaximumSize(QtCore.QSize(452, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 40, 472, 371))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 341))
        self.frame_2.setMaximumSize(QtCore.QSize(472, 400))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.tabWidget_plot_results = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget_plot_results.setGeometry(QtCore.QRect(12, 22, 450, 329))
        self.tabWidget_plot_results.setMinimumSize(QtCore.QSize(450, 0))
        self.tabWidget_plot_results.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tabWidget_plot_results.setFont(font)
        self.tabWidget_plot_results.setObjectName("tabWidget_plot_results")
        self.tab_plot = QtWidgets.QWidget()
        self.tab_plot.setObjectName("tab_plot")
        self.pushButton = QtWidgets.QPushButton(self.tab_plot)
        self.pushButton.setGeometry(QtCore.QRect(82, 258, 283, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(283, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(283, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.frame_4 = QtWidgets.QFrame(self.tab_plot)
        self.frame_4.setGeometry(QtCore.QRect(260, 48, 165, 120))
        self.frame_4.setMinimumSize(QtCore.QSize(165, 120))
        self.frame_4.setMaximumSize(QtCore.QSize(165, 120))
        self.frame_4.setSizeIncrement(QtCore.QSize(0, 110))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.frame_4)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(16, 28, 145, 87))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.radioButton_plotAbs = QtWidgets.QRadioButton(self.verticalLayoutWidget_10)
        self.radioButton_plotAbs.setMinimumSize(QtCore.QSize(140, 22))
        self.radioButton_plotAbs.setMaximumSize(QtCore.QSize(140, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_plotAbs.setFont(font)
        self.radioButton_plotAbs.setIconSize(QtCore.QSize(30, 30))
        self.radioButton_plotAbs.setChecked(True)
        self.radioButton_plotAbs.setObjectName("radioButton_plotAbs")
        self.verticalLayout_10.addWidget(self.radioButton_plotAbs)
        self.radioButton_plotReal = QtWidgets.QRadioButton(self.verticalLayoutWidget_10)
        self.radioButton_plotReal.setMinimumSize(QtCore.QSize(140, 22))
        self.radioButton_plotReal.setMaximumSize(QtCore.QSize(140, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_plotReal.setFont(font)
        self.radioButton_plotReal.setObjectName("radioButton_plotReal")
        self.verticalLayout_10.addWidget(self.radioButton_plotReal)
        self.radioButton_plotImag = QtWidgets.QRadioButton(self.verticalLayoutWidget_10)
        self.radioButton_plotImag.setMinimumSize(QtCore.QSize(140, 22))
        self.radioButton_plotImag.setMaximumSize(QtCore.QSize(140, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_plotImag.setFont(font)
        self.radioButton_plotImag.setObjectName("radioButton_plotImag")
        self.verticalLayout_10.addWidget(self.radioButton_plotImag)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 165, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(165, 21))
        self.label_8.setMaximumSize(QtCore.QSize(165, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setIndent(0)
        self.label_8.setObjectName("label_8")
        self.frame_5 = QtWidgets.QFrame(self.tab_plot)
        self.frame_5.setGeometry(QtCore.QRect(12, 48, 240, 120))
        self.frame_5.setMinimumSize(QtCore.QSize(240, 120))
        self.frame_5.setMaximumSize(QtCore.QSize(240, 120))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 240, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(240, 25))
        self.label_3.setMaximumSize(QtCore.QSize(240, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(64, 30, 109, 85))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_uz = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_uz.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_uz.setFont(font)
        self.radioButton_uz.setChecked(False)
        self.radioButton_uz.setObjectName("radioButton_uz")
        self.gridLayout.addWidget(self.radioButton_uz, 2, 0, 1, 1)
        self.radioButton_uy = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_uy.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_uy.setFont(font)
        self.radioButton_uy.setChecked(False)
        self.radioButton_uy.setObjectName("radioButton_uy")
        self.gridLayout.addWidget(self.radioButton_uy, 1, 0, 1, 1)
        self.radioButton_ux = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_ux.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_ux.setFont(font)
        self.radioButton_ux.setChecked(True)
        self.radioButton_ux.setObjectName("radioButton_ux")
        self.gridLayout.addWidget(self.radioButton_ux, 0, 0, 1, 1)
        self.radioButton_rz = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_rz.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_rz.setFont(font)
        self.radioButton_rz.setChecked(False)
        self.radioButton_rz.setObjectName("radioButton_rz")
        self.gridLayout.addWidget(self.radioButton_rz, 2, 1, 1, 1)
        self.radioButton_ry = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_ry.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_ry.setFont(font)
        self.radioButton_ry.setChecked(False)
        self.radioButton_ry.setObjectName("radioButton_ry")
        self.gridLayout.addWidget(self.radioButton_ry, 1, 1, 1, 1)
        self.radioButton_rx = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_rx.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_rx.setFont(font)
        self.radioButton_rx.setChecked(False)
        self.radioButton_rx.setObjectName("radioButton_rx")
        self.gridLayout.addWidget(self.radioButton_rx, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_plot)
        self.label_10.setGeometry(QtCore.QRect(48, 10, 125, 25))
        self.label_10.setMinimumSize(QtCore.QSize(0, 25))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_nodeID = QtWidgets.QLineEdit(self.tab_plot)
        self.lineEdit_nodeID.setGeometry(QtCore.QRect(178, 10, 108, 25))
        self.lineEdit_nodeID.setMinimumSize(QtCore.QSize(108, 25))
        self.lineEdit_nodeID.setMaximumSize(QtCore.QSize(108, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_nodeID.setFont(font)
        self.lineEdit_nodeID.setStyleSheet("color: rgb(0, 0, 255);")
        self.lineEdit_nodeID.setText("")
        self.lineEdit_nodeID.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_nodeID.setObjectName("lineEdit_nodeID")
        self.frame_3 = QtWidgets.QFrame(self.tab_plot)
        self.frame_3.setGeometry(QtCore.QRect(14, 182, 417, 63))
        self.frame_3.setMinimumSize(QtCore.QSize(417, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(417, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.radioButton_NoneDiff = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_NoneDiff.setGeometry(QtCore.QRect(6, 30, 70, 25))
        self.radioButton_NoneDiff.setMinimumSize(QtCore.QSize(70, 25))
        self.radioButton_NoneDiff.setMaximumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_NoneDiff.setFont(font)
        self.radioButton_NoneDiff.setIconSize(QtCore.QSize(30, 30))
        self.radioButton_NoneDiff.setChecked(True)
        self.radioButton_NoneDiff.setObjectName("radioButton_NoneDiff")
        self.radioButton_SingleDiff = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_SingleDiff.setGeometry(QtCore.QRect(78, 30, 162, 25))
        self.radioButton_SingleDiff.setMinimumSize(QtCore.QSize(162, 25))
        self.radioButton_SingleDiff.setMaximumSize(QtCore.QSize(162, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_SingleDiff.setFont(font)
        self.radioButton_SingleDiff.setObjectName("radioButton_SingleDiff")
        self.radioButton_DoubleDiff = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_DoubleDiff.setGeometry(QtCore.QRect(244, 30, 162, 25))
        self.radioButton_DoubleDiff.setMinimumSize(QtCore.QSize(162, 25))
        self.radioButton_DoubleDiff.setMaximumSize(QtCore.QSize(162, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_DoubleDiff.setFont(font)
        self.radioButton_DoubleDiff.setObjectName("radioButton_DoubleDiff")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 417, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(417, 25))
        self.label_11.setMaximumSize(QtCore.QSize(417, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setIndent(0)
        self.label_11.setObjectName("label_11")
        self.tabWidget_plot_results.addTab(self.tab_plot, "")
        self.tab_export_import = QtWidgets.QWidget()
        self.tab_export_import.setObjectName("tab_export_import")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_export_import)
        self.tabWidget_2.setGeometry(QtCore.QRect(6, 52, 433, 195))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(133, 10, 249, 27))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_Absolute = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_Absolute.setMinimumSize(QtCore.QSize(90, 25))
        self.radioButton_Absolute.setMaximumSize(QtCore.QSize(90, 25))
        self.radioButton_Absolute.setChecked(True)
        self.radioButton_Absolute.setObjectName("radioButton_Absolute")
        self.horizontalLayout.addWidget(self.radioButton_Absolute)
        self.radioButton_Real_Imaginary = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_Real_Imaginary.setMinimumSize(QtCore.QSize(140, 25))
        self.radioButton_Real_Imaginary.setMaximumSize(QtCore.QSize(140, 25))
        self.radioButton_Real_Imaginary.setChecked(False)
        self.radioButton_Real_Imaginary.setObjectName("radioButton_Real_Imaginary")
        self.horizontalLayout.addWidget(self.radioButton_Real_Imaginary)
        self.toolButton_ExportResults = QtWidgets.QToolButton(self.tab_3)
        self.toolButton_ExportResults.setGeometry(QtCore.QRect(154, 124, 120, 30))
        self.toolButton_ExportResults.setMinimumSize(QtCore.QSize(120, 30))
        self.toolButton_ExportResults.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.toolButton_ExportResults.setFont(font)
        self.toolButton_ExportResults.setObjectName("toolButton_ExportResults")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(2, 86, 125, 25))
        self.label_5.setMinimumSize(QtCore.QSize(125, 25))
        self.label_5.setMaximumSize(QtCore.QSize(125, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_SaveResultsPath = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_SaveResultsPath.setGeometry(QtCore.QRect(132, 86, 221, 25))
        self.lineEdit_SaveResultsPath.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_SaveResultsPath.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit_SaveResultsPath.setFont(font)
        self.lineEdit_SaveResultsPath.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_SaveResultsPath.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_SaveResultsPath.setObjectName("lineEdit_SaveResultsPath")
        self.toolButton_ChooseFolderExport = QtWidgets.QToolButton(self.tab_3)
        self.toolButton_ChooseFolderExport.setGeometry(QtCore.QRect(358, 86, 60, 25))
        self.toolButton_ChooseFolderExport.setMinimumSize(QtCore.QSize(60, 25))
        self.toolButton_ChooseFolderExport.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.toolButton_ChooseFolderExport.setFont(font)
        self.toolButton_ChooseFolderExport.setObjectName("toolButton_ChooseFolderExport")
        self.lineEdit_FileName = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_FileName.setGeometry(QtCore.QRect(132, 46, 221, 25))
        self.lineEdit_FileName.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_FileName.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_FileName.setFont(font)
        self.lineEdit_FileName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_FileName.setText("")
        self.lineEdit_FileName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_FileName.setObjectName("lineEdit_FileName")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(2, 46, 125, 25))
        self.label_6.setMinimumSize(QtCore.QSize(125, 25))
        self.label_6.setMaximumSize(QtCore.QSize(125, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(24, 14, 100, 20))
        self.label_7.setMinimumSize(QtCore.QSize(100, 20))
        self.label_7.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_AddImportedPlot = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_AddImportedPlot.setGeometry(QtCore.QRect(60, 120, 310, 30))
        self.pushButton_AddImportedPlot.setMinimumSize(QtCore.QSize(310, 30))
        self.pushButton_AddImportedPlot.setMaximumSize(QtCore.QSize(310, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_AddImportedPlot.setFont(font)
        self.pushButton_AddImportedPlot.setObjectName("pushButton_AddImportedPlot")
        self.spinBox = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox.setGeometry(QtCore.QRect(270, 72, 42, 25))
        self.spinBox.setMinimumSize(QtCore.QSize(0, 25))
        self.spinBox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(106, 72, 160, 25))
        self.label_12.setMinimumSize(QtCore.QSize(160, 25))
        self.label_12.setMaximumSize(QtCore.QSize(160, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(18, 26, 100, 25))
        self.label_9.setMinimumSize(QtCore.QSize(100, 25))
        self.label_9.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_ImportResultsPath = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_ImportResultsPath.setGeometry(QtCore.QRect(120, 26, 229, 25))
        self.lineEdit_ImportResultsPath.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_ImportResultsPath.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit_ImportResultsPath.setFont(font)
        self.lineEdit_ImportResultsPath.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_ImportResultsPath.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ImportResultsPath.setObjectName("lineEdit_ImportResultsPath")
        self.toolButton_ChooseFolderImport = QtWidgets.QToolButton(self.tab_4)
        self.toolButton_ChooseFolderImport.setGeometry(QtCore.QRect(354, 26, 60, 25))
        self.toolButton_ChooseFolderImport.setMinimumSize(QtCore.QSize(0, 25))
        self.toolButton_ChooseFolderImport.setMaximumSize(QtCore.QSize(65, 25))
        self.toolButton_ChooseFolderImport.setSizeIncrement(QtCore.QSize(65, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.toolButton_ChooseFolderImport.setFont(font)
        self.toolButton_ChooseFolderImport.setObjectName("toolButton_ChooseFolderImport")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget_plot_results.addTab(self.tab_export_import, "")
        self.toolButton_ResetPlot = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_ResetPlot.setGeometry(QtCore.QRect(374, 8, 85, 30))
        self.toolButton_ResetPlot.setMinimumSize(QtCore.QSize(85, 30))
        self.toolButton_ResetPlot.setMaximumSize(QtCore.QSize(85, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.toolButton_ResetPlot.setFont(font)
        self.toolButton_ResetPlot.setStyleSheet("background-color: rgb(159, 247, 245);")
        self.toolButton_ResetPlot.setObjectName("toolButton_ResetPlot")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(282, 8, 85, 30))
        self.frame_6.setMinimumSize(QtCore.QSize(85, 30))
        self.frame_6.setMaximumSize(QtCore.QSize(85, 30))
        self.frame_6.setSizeIncrement(QtCore.QSize(0, 110))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.checkBox_cursor = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_cursor.setGeometry(QtCore.QRect(8, 2, 75, 26))
        self.checkBox_cursor.setMinimumSize(QtCore.QSize(75, 26))
        self.checkBox_cursor.setMaximumSize(QtCore.QSize(75, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_cursor.setFont(font)
        self.checkBox_cursor.setChecked(False)
        self.checkBox_cursor.setObjectName("checkBox_cursor")

        self.retranslateUi(Dialog)
        self.tabWidget_plot_results.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Plot frequency response"))
        self.label.setText(_translate("Dialog", "Get the structural frequency response at node"))
        self.pushButton.setText(_translate("Dialog", "Plot the frequency response"))
        self.radioButton_plotAbs.setText(_translate("Dialog", "Absolute"))
        self.radioButton_plotReal.setText(_translate("Dialog", "Real part"))
        self.radioButton_plotImag.setText(_translate("Dialog", "Imaginary part"))
        self.label_8.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Y-axis plot controls</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the DOF to get response</p></body></html>"))
        self.radioButton_uz.setText(_translate("Dialog", "Uz"))
        self.radioButton_uy.setText(_translate("Dialog", "Uy"))
        self.radioButton_ux.setText(_translate("Dialog", "Ux"))
        self.radioButton_rz.setText(_translate("Dialog", "Rz"))
        self.radioButton_ry.setText(_translate("Dialog", "Ry"))
        self.radioButton_rx.setText(_translate("Dialog", "Rx"))
        self.label_10.setText(_translate("Dialog", "Insert a Node ID:"))
        self.radioButton_NoneDiff.setText(_translate("Dialog", "None"))
        self.radioButton_SingleDiff.setText(_translate("Dialog", "Single differentiate"))
        self.radioButton_DoubleDiff.setText(_translate("Dialog", "Double differentiate"))
        self.label_11.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Modify output spectrum</p></body></html>"))
        self.tabWidget_plot_results.setTabText(self.tabWidget_plot_results.indexOf(self.tab_plot), _translate("Dialog", "Plot"))
        self.radioButton_Absolute.setText(_translate("Dialog", "Absolute"))
        self.radioButton_Real_Imaginary.setText(_translate("Dialog", "Real / Imaginary"))
        self.toolButton_ExportResults.setText(_translate("Dialog", "Export results"))
        self.label_5.setText(_translate("Dialog", "Choose a folder:"))
        self.toolButton_ChooseFolderExport.setText(_translate("Dialog", "Search"))
        self.label_6.setText(_translate("Dialog", "Insert a name:"))
        self.label_7.setText(_translate("Dialog", "Data to save:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Dialog", "Export"))
        self.pushButton_AddImportedPlot.setText(_translate("Dialog", "Add imported results to the main plot"))
        self.label_12.setText(_translate("Dialog", "Header rows to skip:"))
        self.label_9.setText(_translate("Dialog", "Load results:"))
        self.toolButton_ChooseFolderImport.setText(_translate("Dialog", "Search"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Dialog", "Import"))
        self.tabWidget_plot_results.setTabText(self.tabWidget_plot_results.indexOf(self.tab_export_import), _translate("Dialog", "Export / Import results"))
        self.toolButton_ResetPlot.setText(_translate("Dialog", "Reset plot"))
        self.checkBox_cursor.setText(_translate("Dialog", "Cursor"))
