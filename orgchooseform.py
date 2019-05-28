# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orgchooseform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogOrgChoose(object):
    def setupUi(self, DialogOrgChoose):
        DialogOrgChoose.setObjectName("DialogOrgChoose")
        DialogOrgChoose.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogOrgChoose.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/Icons/finance/014.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogOrgChoose.setWindowIcon(icon)
        DialogOrgChoose.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(DialogOrgChoose)
        self.gridLayout.setObjectName("gridLayout")
        self.frameButtons = QtWidgets.QFrame(DialogOrgChoose)
        self.frameButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameButtons.setObjectName("frameButtons")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frameButtons)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnOrgAdd = QtWidgets.QPushButton(self.frameButtons)
        self.btnOrgAdd.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/Icons/basic/058.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOrgAdd.setIcon(icon1)
        self.btnOrgAdd.setObjectName("btnOrgAdd")
        self.gridLayout_2.addWidget(self.btnOrgAdd, 0, 3, 1, 1)
        self.btnOrgCancel = QtWidgets.QPushButton(self.frameButtons)
        self.btnOrgCancel.setObjectName("btnOrgCancel")
        self.gridLayout_2.addWidget(self.btnOrgCancel, 0, 1, 1, 1)
        self.btnOrgChoose = QtWidgets.QPushButton(self.frameButtons)
        self.btnOrgChoose.setObjectName("btnOrgChoose")
        self.gridLayout_2.addWidget(self.btnOrgChoose, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frameButtons, 5, 1, 1, 1)
        self.frameOrganization = QtWidgets.QFrame(DialogOrgChoose)
        self.frameOrganization.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameOrganization.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameOrganization.setObjectName("frameOrganization")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frameOrganization)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelOrgCode = QtWidgets.QLabel(self.frameOrganization)
        self.labelOrgCode.setObjectName("labelOrgCode")
        self.gridLayout_3.addWidget(self.labelOrgCode, 1, 0, 1, 1)
        self.lineEditOrgCode = QtWidgets.QLineEdit(self.frameOrganization)
        self.lineEditOrgCode.setObjectName("lineEditOrgCode")
        self.gridLayout_3.addWidget(self.lineEditOrgCode, 1, 1, 1, 1)
        self.labelOrgName = QtWidgets.QLabel(self.frameOrganization)
        self.labelOrgName.setObjectName("labelOrgName")
        self.gridLayout_3.addWidget(self.labelOrgName, 0, 0, 1, 1)
        self.labelOrgAddress = QtWidgets.QLabel(self.frameOrganization)
        self.labelOrgAddress.setObjectName("labelOrgAddress")
        self.gridLayout_3.addWidget(self.labelOrgAddress, 2, 0, 1, 1)
        self.plainTextEditOrgAddress = QtWidgets.QPlainTextEdit(self.frameOrganization)
        self.plainTextEditOrgAddress.setObjectName("plainTextEditOrgAddress")
        self.gridLayout_3.addWidget(self.plainTextEditOrgAddress, 2, 1, 1, 1)
        self.lineEditOrgName = QtWidgets.QLineEdit(self.frameOrganization)
        self.lineEditOrgName.setObjectName("lineEditOrgName")
        self.gridLayout_3.addWidget(self.lineEditOrgName, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frameOrganization, 1, 1, 1, 1)
        self.listViewOrganizations = QtWidgets.QListView(DialogOrgChoose)
        self.listViewOrganizations.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.listViewOrganizations.setProperty("showDropIndicator", False)
        self.listViewOrganizations.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listViewOrganizations.setAlternatingRowColors(True)
        self.listViewOrganizations.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listViewOrganizations.setModelColumn(0)
        self.listViewOrganizations.setBatchSize(100)
        self.listViewOrganizations.setSelectionRectVisible(True)
        self.listViewOrganizations.setObjectName("listViewOrganizations")
        self.gridLayout.addWidget(self.listViewOrganizations, 0, 1, 1, 1)

        self.retranslateUi(DialogOrgChoose)
        QtCore.QMetaObject.connectSlotsByName(DialogOrgChoose)

    def retranslateUi(self, DialogOrgChoose):
        _translate = QtCore.QCoreApplication.translate
        DialogOrgChoose.setWindowTitle(_translate("DialogOrgChoose", "Вибір установи"))
        self.btnOrgAdd.setToolTip(_translate("DialogOrgChoose", "Додати установу/підрозділ"))
        self.btnOrgCancel.setText(_translate("DialogOrgChoose", "Скасувати"))
        self.btnOrgChoose.setText(_translate("DialogOrgChoose", "Обрати"))
        self.labelOrgCode.setText(_translate("DialogOrgChoose", "ЄДРПОУ"))
        self.labelOrgName.setText(_translate("DialogOrgChoose", "Назва"))
        self.labelOrgAddress.setText(_translate("DialogOrgChoose", "Адреса"))

import icons

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogOrgChoose = QtWidgets.QDialog()
    ui = Ui_DialogOrgChoose()
    ui.setupUi(DialogOrgChoose)
    DialogOrgChoose.show()
    sys.exit(app.exec_())
