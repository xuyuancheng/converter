# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converter_ui.ui'
#
# Created: Thu Dec 06 11:10:25 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_converter(object):
    def setupUi(self, converter):
        converter.setObjectName(_fromUtf8("converter"))
        converter.resize(774, 562)
        converter.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        converter.setWindowTitle(QtGui.QApplication.translate("converter", "Statistical-Converter", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        converter.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(converter)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Input = QtGui.QLineEdit(converter)
        self.Input.setObjectName(_fromUtf8("Input"))
        self.verticalLayout.addWidget(self.Input)
        self.Output = QtGui.QLineEdit(converter)
        self.Output.setObjectName(_fromUtf8("Output"))
        self.verticalLayout.addWidget(self.Output)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(converter)
        self.label_2.setText(QtGui.QApplication.translate("converter", "threshold value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.ratio = QtGui.QDoubleSpinBox(converter)
        self.ratio.setKeyboardTracking(True)
        self.ratio.setDecimals(3)
        self.ratio.setMinimum(0.001)
        self.ratio.setMaximum(0.5)
        self.ratio.setSingleStep(0.01)
        self.ratio.setProperty("value", 0.01)
        self.ratio.setObjectName(_fromUtf8("ratio"))
        self.horizontalLayout.addWidget(self.ratio)
        self.label = QtGui.QLabel(converter)
        self.label.setText(QtGui.QApplication.translate("converter", "        Sigma", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.sigma = QtGui.QSpinBox(converter)
        self.sigma.setMaximum(10)
        self.sigma.setObjectName(_fromUtf8("sigma"))
        self.horizontalLayout.addWidget(self.sigma)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.log = QtGui.QTextBrowser(converter)
        self.log.setStyleSheet(_fromUtf8("font: 75 9pt \"Consolas\";\n"
"background-color: rgb(226, 226, 226);"))
        self.log.setObjectName(_fromUtf8("log"))
        self.verticalLayout_3.addWidget(self.log)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 7, 1)
        self.Input_button = QtGui.QPushButton(converter)
        self.Input_button.setText(QtGui.QApplication.translate("converter", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.Input_button.setObjectName(_fromUtf8("Input_button"))
        self.gridLayout.addWidget(self.Input_button, 0, 1, 1, 1)
        self.Output_button = QtGui.QPushButton(converter)
        self.Output_button.setText(QtGui.QApplication.translate("converter", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.Output_button.setObjectName(_fromUtf8("Output_button"))
        self.gridLayout.addWidget(self.Output_button, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 355, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.Show_button = QtGui.QPushButton(converter)
        self.Show_button.setText(QtGui.QApplication.translate("converter", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.Show_button.setObjectName(_fromUtf8("Show_button"))
        self.gridLayout.addWidget(self.Show_button, 3, 1, 1, 1)
        self.Convert_button = QtGui.QPushButton(converter)
        self.Convert_button.setText(QtGui.QApplication.translate("converter", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.Convert_button.setObjectName(_fromUtf8("Convert_button"))
        self.gridLayout.addWidget(self.Convert_button, 4, 1, 1, 1)
        self.Result = QtGui.QPushButton(converter)
        self.Result.setText(QtGui.QApplication.translate("converter", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.Result.setObjectName(_fromUtf8("Result"))
        self.gridLayout.addWidget(self.Result, 5, 1, 1, 1)
        self.Close_button = QtGui.QPushButton(converter)
        self.Close_button.setText(QtGui.QApplication.translate("converter", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.Close_button.setObjectName(_fromUtf8("Close_button"))
        self.gridLayout.addWidget(self.Close_button, 6, 1, 1, 1)
        self.label_2.setBuddy(self.ratio)
        self.label.setBuddy(self.sigma)

        self.retranslateUi(converter)
        QtCore.QObject.connect(self.Close_button, QtCore.SIGNAL(_fromUtf8("clicked()")), converter.reject)
        QtCore.QMetaObject.connectSlotsByName(converter)
        converter.setTabOrder(self.Input_button, self.Input)
        converter.setTabOrder(self.Input, self.Output_button)
        converter.setTabOrder(self.Output_button, self.Output)
        converter.setTabOrder(self.Output, self.log)

    def retranslateUi(self, converter):
        pass

