# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\水果识别系统\QT.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("水果识别系统")
        Form.resize(1008, 667)
        Form.setMinimumSize(QtCore.QSize(251, 291))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "   border: none;\n"
                                    "   background-color: transparent;\n"
                                    "}\n"
                                    "")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                      "   border: none;\n"
                                      "   background-color: transparent;\n"
                                      "}\n"
                                      "")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
                                      "   border: none;\n"
                                      "   background-color: transparent;\n"
                                      "}\n"
                                      "")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
                                      "   border: none;\n"
                                      "   background-color: transparent;\n"
                                      "}\n"
                                      "")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
                                      "   border: none;\n"
                                      "   background-color: transparent;\n"
                                      "}\n"
                                      "")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
                                      "   border: none;\n"
                                      "   background-color: transparent;\n"
                                      "}\n"
                                      "")
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.apple = QtWidgets.QLineEdit(Form)
        self.apple.setStyleSheet("QLineEdit {\n"
                                 "    border: 1px solid gray;\n"
                                 "    border-radius: 5px;\n"
                                 "    padding: 0 8px;\n"
                                 "    background: white;\n"
                                 "}\n"
                                 "")
        self.apple.setObjectName("apple")
        self.verticalLayout_2.addWidget(self.apple)
        self.banana = QtWidgets.QLineEdit(Form)
        self.banana.setStyleSheet("QLineEdit {\n"
                                  "    border: 1px solid gray;\n"
                                  "    border-radius: 5px;\n"
                                  "    padding: 0 8px;\n"
                                  "    background: white;\n"
                                  "}\n"
                                  "")
        self.banana.setObjectName("banana")
        self.verticalLayout_2.addWidget(self.banana)
        self.watermelon = QtWidgets.QLineEdit(Form)
        self.watermelon.setStyleSheet("QLineEdit {\n"
                                      "    border: 1px solid gray;\n"
                                      "    border-radius: 5px;\n"
                                      "    padding: 0 8px;\n"
                                      "    background: white;\n"
                                      "}\n"
                                      "")
        self.watermelon.setObjectName("watermelon")
        self.verticalLayout_2.addWidget(self.watermelon)
        self.kg = QtWidgets.QLineEdit(Form)
        self.kg.setStyleSheet("QLineEdit {\n"
                              "    border: 1px solid gray;\n"
                              "    border-radius: 5px;\n"
                              "    padding: 0 8px;\n"
                              "    background: white;\n"
                              "}\n"
                              "")
        self.kg.setObjectName("kg")
        self.verticalLayout_2.addWidget(self.kg)
        self.recognize = QtWidgets.QLineEdit(Form)
        self.recognize.setStyleSheet("QLineEdit {\n"
                                     "    border: 1px solid gray;\n"
                                     "    border-radius: 5px;\n"
                                     "    padding: 0 8px;\n"
                                     "    background: white;\n"
                                     "}\n"
                                     "")
        self.recognize.setReadOnly(True)
        self.recognize.setPlaceholderText("")
        self.recognize.setObjectName("recognize")
        self.verticalLayout_2.addWidget(self.recognize)
        self.result = QtWidgets.QLineEdit(Form)
        self.result.setStyleSheet("QLineEdit {\n"
                                  "    border: 1px solid gray;\n"
                                  "    border-radius: 5px;\n"
                                  "    padding: 0 8px;\n"
                                  "    background: white;\n"
                                  "}\n"
                                  "")
        self.result.setInputMask("")
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.verticalLayout_2.addWidget(self.result)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(350, 250))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.shot = QtWidgets.QPushButton(Form)
        self.shot.setObjectName("shot")
        self.verticalLayout_3.addWidget(self.shot)
        self.open = QtWidgets.QPushButton(Form)
        self.open.setObjectName("open")
        self.verticalLayout_3.addWidget(self.open)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.recognition = QtWidgets.QPushButton(Form)
        self.recognition.setObjectName("recognition")
        self.verticalLayout_4.addWidget(self.recognition)
        self.chooseButton = QtWidgets.QPushButton(Form)
        self.chooseButton.setObjectName("chooseButton")
        self.verticalLayout_4.addWidget(self.chooseButton)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "水果识别系统"))
        self.lineEdit.setText(_translate("Form", "苹果/元："))
        self.lineEdit_2.setText(_translate("Form", "香蕉/元："))
        self.lineEdit_3.setText(_translate("Form", "西瓜/元："))
        self.lineEdit_4.setText(_translate("Form", "重量/kg："))
        self.lineEdit_5.setText(_translate("Form", "识别结果："))
        self.lineEdit_6.setText(_translate("Form", "计重结果："))
        self.label.setText(_translate("Form", "请打开一张图"))
        self.shot.setText(_translate("Form", "拍摄"))
        self.open.setText(_translate("Form", "打开摄像头"))
        self.recognition.setText(_translate("Form", "识别计重"))
        self.chooseButton.setText(_translate("Form", "选择"))
