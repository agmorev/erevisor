# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baseform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogBasis(object):
    def setupUi(self, DialogBasis):
        DialogBasis.setObjectName("DialogBasis")
        DialogBasis.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/Icons/documents/006.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogBasis.setWindowIcon(icon)
        DialogBasis.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(DialogBasis)
        self.gridLayout.setObjectName("gridLayout")
        self.frameBasisFile = QtWidgets.QFrame(DialogBasis)
        self.frameBasisFile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBasisFile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBasisFile.setObjectName("frameBasisFile")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frameBasisFile)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidgetBasisFile = QtWidgets.QListWidget(self.frameBasisFile)
        self.listWidgetBasisFile.setObjectName("listWidgetBasisFile")
        self.gridLayout_4.addWidget(self.listWidgetBasisFile, 0, 0, 1, 1)
        self.groupBoxBasisFile = QtWidgets.QGroupBox(self.frameBasisFile)
        self.groupBoxBasisFile.setObjectName("groupBoxBasisFile")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBoxBasisFile)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButtonView = QtWidgets.QPushButton(self.groupBoxBasisFile)
        self.pushButtonView.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/Icons/documents/006.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonView.setIcon(icon)
        self.pushButtonView.setObjectName("pushButtonView")
        self.gridLayout_6.addWidget(self.pushButtonView, 0, 0, 1, 1)
        self.pushButtonAdd = QtWidgets.QPushButton(self.groupBoxBasisFile)
        self.pushButtonAdd.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/Icons/basic/021.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAdd.setIcon(icon1)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.gridLayout_6.addWidget(self.pushButtonAdd, 1, 0, 1, 1)
        self.pushButtonDelete = QtWidgets.QPushButton(self.groupBoxBasisFile)
        self.pushButtonDelete.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ico/Icons/basic/022.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDelete.setIcon(icon2)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.gridLayout_6.addWidget(self.pushButtonDelete, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxBasisFile, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frameBasisFile, 5, 0, 1, 1)
        self.frameBasis = QtWidgets.QFrame(DialogBasis)
        self.frameBasis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBasis.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBasis.setObjectName("frameBasis")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frameBasis)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBoxBasisInitiator = QtWidgets.QComboBox(self.frameBasis)
        self.comboBoxBasisInitiator.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBoxBasisInitiator.setEditable(True)
        self.comboBoxBasisInitiator.setObjectName("comboBoxBasisInitiator")
        self.gridLayout_2.addWidget(self.comboBoxBasisInitiator, 1, 1, 1, 1)
        self.labelBasisInitiator = QtWidgets.QLabel(self.frameBasis)
        self.labelBasisInitiator.setObjectName("labelBasisInitiator")
        self.gridLayout_2.addWidget(self.labelBasisInitiator, 1, 0, 1, 1)
        self.labelBasisType = QtWidgets.QLabel(self.frameBasis)
        self.labelBasisType.setObjectName("labelBasisType")
        self.gridLayout_2.addWidget(self.labelBasisType, 4, 0, 1, 1)
        self.labelBasisNumber = QtWidgets.QLabel(self.frameBasis)
        self.labelBasisNumber.setObjectName("labelBasisNumber")
        self.gridLayout_2.addWidget(self.labelBasisNumber, 5, 0, 1, 1)
        self.labelBasisDate = QtWidgets.QLabel(self.frameBasis)
        self.labelBasisDate.setObjectName("labelBasisDate")
        self.gridLayout_2.addWidget(self.labelBasisDate, 6, 0, 1, 1)
        self.comboBoxBasisType = QtWidgets.QComboBox(self.frameBasis)
        self.comboBoxBasisType.setEditable(True)
        self.comboBoxBasisType.setObjectName("comboBoxBasisType")
        self.comboBoxBasisType.addItem("")
        self.comboBoxBasisType.addItem("")
        self.comboBoxBasisType.addItem("")
        self.comboBoxBasisType.addItem("")
        self.comboBoxBasisType.addItem("")
        self.comboBoxBasisType.addItem("")
        self.comboBoxBasisType.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxBasisType, 4, 1, 1, 1)
        self.lineEditBasisNumber = QtWidgets.QLineEdit(self.frameBasis)
        self.lineEditBasisNumber.setObjectName("lineEditBasisNumber")
        self.gridLayout_2.addWidget(self.lineEditBasisNumber, 5, 1, 1, 1)
        self.dateEditBasisDate = QtWidgets.QDateEdit(self.frameBasis)
        self.dateEditBasisDate.setCalendarPopup(True)
        self.dateEditBasisDate.setDate(QtCore.QDate(2019, 1, 1))
        self.dateEditBasisDate.setObjectName("dateEditBasisDate")
        self.gridLayout_2.addWidget(self.dateEditBasisDate, 6, 1, 1, 1)
        self.gridLayout.addWidget(self.frameBasis, 4, 0, 1, 1)
        self.frameBasisControl = QtWidgets.QFrame(DialogBasis)
        self.frameBasisControl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBasisControl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBasisControl.setObjectName("frameBasisControl")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frameBasisControl)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(197, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButtonSave = QtWidgets.QPushButton(self.frameBasisControl)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout_3.addWidget(self.pushButtonSave, 0, 1, 1, 1)
        self.pushButtonCancel = QtWidgets.QPushButton(self.frameBasisControl)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout_3.addWidget(self.pushButtonCancel, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frameBasisControl, 6, 0, 1, 1)

        self.retranslateUi(DialogBasis)
        self.comboBoxBasisType.setCurrentIndex(-1)
        self.comboBoxBasisType.setCurrentIndex(-1)
        self.pushButtonCancel.clicked.connect(DialogBasis.close)
        QtCore.QMetaObject.connectSlotsByName(DialogBasis)

    def retranslateUi(self, DialogBasis):
        _translate = QtCore.QCoreApplication.translate
        DialogBasis.setWindowTitle(_translate("DialogBasis", "Підстава проведення перевірки"))
        self.groupBoxBasisFile.setTitle(_translate("DialogBasis", "Файл"))
        self.pushButtonView.setToolTip(_translate("DialogBasis", "Перегляд"))
        self.pushButtonAdd.setToolTip(_translate("DialogBasis", "Додати"))
        self.pushButtonDelete.setToolTip(_translate("DialogBasis", "Видалити"))
        self.labelBasisInitiator.setText(_translate("DialogBasis", "Ініціатор"))
        self.labelBasisType.setText(_translate("DialogBasis", "Вид документа"))
        self.labelBasisNumber.setText(_translate("DialogBasis", "Номер"))
        self.labelBasisDate.setText(_translate("DialogBasis", "Дата"))
        self.comboBoxBasisType.setItemText(0, _translate("DialogBasis", "наказ ДФС"))
        self.comboBoxBasisType.setItemText(1, _translate("DialogBasis", "розпорядження"))
        self.comboBoxBasisType.setItemText(2, _translate("DialogBasis", "доручення"))
        self.comboBoxBasisType.setItemText(3, _translate("DialogBasis", "доповідна записка"))
        self.comboBoxBasisType.setItemText(4, _translate("DialogBasis", "звернення"))
        self.comboBoxBasisType.setItemText(5, _translate("DialogBasis", "скарга"))
        self.comboBoxBasisType.setItemText(6, _translate("DialogBasis", "лист"))
        self.pushButtonSave.setText(_translate("DialogBasis", "Зберегти"))
        self.pushButtonCancel.setText(_translate("DialogBasis", "Скасувати"))

import icons

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogBasis = QtWidgets.QDialog()
    ui = Ui_DialogBasis()
    ui.setupUi(DialogBasis)
    DialogBasis.show()
    sys.exit(app.exec_())