from mainform import Ui_MainWindow
import inspform, orgform, baseform
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem,QListView,QFileDialog
import os, pathlib, datetime, sqlite3

conn = sqlite3.connect('revisor.sqlite3')
curs = conn.cursor()

class MainApp(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.Init_Ui()

#-------------------------------------------------
#РОБОТА З ГОЛОВНОЮ ФОРМОЮ
#-------------------------------------------------

    def Init_Ui(self):
        '''Відображення основної форми та робота її елементів'''
        self.setupUi(self)
        self.LoadDataInspectionTable()                                          #Виклик функції завантаження даних в таблицю =Перевірки= основної форми
        self.show()
        self.btnInspectionAdd.clicked.connect(self.InspectionAdd)               #Натиснення кнопки <Додати>, виклик пустої форми =Перевірки= і функції додавання запису
        self.btnInspectionView.clicked.connect(self.InspectionView)             #Натиснення кнопки <Переглянути>, виклик форми =Перевірки=, завантаження даних обраного запису
        self.btnInspectionEdit.clicked.connect(self.InspectionEdit)             #Натиснення кнопки <Редагувати>, виклик форми =Перевірки=, функції редагування обраного запису
        self.btnInspectionDelete.clicked.connect(self.InspectionDelete)         #Натиснення кнопки <Видалити> і виклик функції видалення обраного запису
        self.btnInspectionDeleteAll.clicked.connect(self.InspectionDeleteAll)   #Натиснення кнопки <Видалити все> і виклик функції видалення всіх записів

#-------------------------------------------------
#РОБОТА З ФОРМОЮ "ЕТАПИ ПРОВЕДЕННЯ ПЕРЕВІРКИ"
#-------------------------------------------------

    def InspectionAdd(self):
        '''Обробка сигналу натиснення кнопки <Додати> вкладки =Перевірки= основної форми'''
        self.editing = InspectionWindow()
        res = conn.execute("SELECT orgname FROM organizations ORDER BY id")
        objlist = res.fetchall()
        cmblist = [i[0] for i in objlist]
        conn.commit()
        self.editing.comboBoxObjectName.addItems(cmblist)
        self.editing.comboBoxObjectName.setCurrentIndex(-1)
        self.LoadDataBasisTable()
        self.editing.cmbType1.currentIndexChanged.connect(self.InspectionValidations) #Виклик функції валідації в частині обробки подій в групі Вид перевірки
        self.editing.comboBoxObjectName.activated.connect(self.LoadObjectData)
        self.editing.btnObject.clicked.connect(self.OrgEdit)
        self.editing.btnBasisAdd.clicked.connect(self.BasisAdd)
        self.editing.btnSave.clicked.connect(self.InspectionAddData)            #Натиснення кнопки <Зберегти> та виклик функції додавання нового запису
        self.editing.exec_()

    def InspectionView(self):
        '''Обробка сигналу натиснення кнопки <Переглянути> вкладки =Перевірки= основної форми'''
        self.editing = InspectionWindow()
        self.editing.btnSave.setDisabled(True)
        self.editing.grpType.setDisabled(True)
        self.editing.grpObject.setDisabled(True)
        self.editing.frameBasisControl.setDisabled(True)
        self.editing.frameGroupControl.setDisabled(True)
        self.editing.frameStopControl.setDisabled(True)
        self.editing.frameRefuseControl.setDisabled(True)
        self.editing.frameResultControl.setDisabled(True)
        self.editing.frameViolationControl.setDisabled(True)
        self.editing.frameAssignmentControl.setDisabled(True)
        self.editing.framePropositions.setDisabled(True)
        self.LoadDataInspectionForm()
        self.LoadDataBasisTable()
        self.editing.exec_()

    def InspectionEdit(self):
        '''Обробка сигналу натиснення кнопки <Редагувати> вкладки =Перевірки= основної форми'''
        self.editing = InspectionWindow()
        res = conn.execute("SELECT orgname FROM organizations ORDER BY id")
        objlist = res.fetchall()
        cmblist = [i[0] for i in objlist]
        conn.commit()
        self.editing.comboBoxObjectName.addItems(cmblist)
        self.LoadDataInspectionForm()
        self.LoadDataBasisTable()
        self.editing.comboBoxObjectName.currentTextChanged.connect(self.LoadObjectData)
        self.editing.btnObject.clicked.connect(self.OrgEdit)
        self.editing.btnBasisAdd.clicked.connect(self.BasisAdd)
        self.editing.btnSave.clicked.connect(self.InspectionEditData)           #Натиснення кнопки =Зберегти= та виклик функції редагування запису
        self.editing.exec_()

    def InspectionAddData(self):
        '''Додавання нового запису (перевірки) до таблиці inspections бази даних'''
        self.UploadDataInspectionForm() #Присвоєння значень змінним даних форми =Етапи проведення перевірки=
        try:
            curs.execute("INSERT INTO inspections (type1, type2, type3, object_name, object_code, object_address, purpose, inspdate_from, inspdate_to, perdate_from, perdate_to, control_date, remove_date, chkstop, chkrefuse, chkresult, chkenforce, chksecure, chkfinish, chkviolate, tcharges, chkassign, chkpropose) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (type1,type2,type3,objname,objcode,objaddress,insppurp,idfrom,idto,pdfrom,pdto,idcontrol,nidcontrol,chkstop,chkrefuse,chkresult,chkenforce,chksecure,chkfinish,chkviolate,tcharges,chkassign,chkpropose))
            conn.commit()
            self.LoadDataInspectionTable()
            self.editing.close()
        except Exception as Error:
            msg=QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(Error)
            msg.setWindowTitle("Помилка")
            msg.setStandardButtons(QMessageBox.Ok)
            btnOk = msg.button(QMessageBox.Ok)
            msg.exec_()
            if msg.clickedButton() == btnOk:
                msg.close()

    def InspectionEditData(self):
        '''Редагування (оновлення) запису в таблиці inspections бази даних'''
        self.UploadDataInspectionForm() #Присвоєння значень змінним даних форми =Етапи проведення перевірки=
        try:
            curs.execute("UPDATE inspections SET type1=?, type2=?, type3=?, object_name=?, object_code=?, object_address=?, purpose=?, inspdate_from=?, inspdate_to=?, perdate_from=?, perdate_to=?, control_date=?, remove_date=?, chkstop=?, chkrefuse=?, chkresult=?, chkenforce=?, chksecure=?, chkfinish=?, chkviolate=?, tcharges=?, chkassign=?, chkpropose=? WHERE id=?", (type1,type2,type3,objname,objcode,objaddress,insppurp,idfrom,idto,pdfrom,pdto,idcontrol,nidcontrol,chkstop,chkrefuse,chkresult,chkenforce,chksecure,chkfinish,chkviolate,tcharges,chkassign,chkpropose,inspid))
            conn.commit()
            self.LoadDataInspectionTable()
            self.editing.close()
        except Exception as Error:
            msg=QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(str(Error))
            msg.setWindowTitle("Помилка")
            msg.setStandardButtons(QMessageBox.Ok)
            btnOk = msg.button(QMessageBox.Ok)
            msg.exec_()
            if msg.clickedButton() == btnOk:
                msg.close()

    def InspectionDelete(self):
        '''Видалення запису в таблиці inspections бази даних'''
        msg=QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setText("УВАГА!!!")
        msg.setInformativeText("Ви впевнені, що бажаєте видалити цей запис?")
        msg.setWindowTitle("Попередження")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        btnY = msg.button(QMessageBox.Yes)
        btnY.setText('Так')
        btnN = msg.button(QMessageBox.No)
        btnN.setText('Ні')
        msg.exec_()
        if msg.clickedButton() == btnY:
            inspcontent = "SELECT * FROM inspections"
            res = conn.execute(inspcontent)
            for row in enumerate(res):
                if row[0] == self.tableWidgetInspections.currentRow():
                    data = row[1]
                    inspid = data[0]
                    curs.execute("DELETE FROM inspections WHERE id=?",(str(inspid),))
                    conn.commit()
                    self.LoadDataInspectionTable()
        elif msg.clickedButton() == btnN:
            msg.close()

    def InspectionDeleteAll(self):
        '''Видалення всіх записів в таблиці inspections бази даних'''
        msg=QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setText("УВАГА!!!")
        msg.setInformativeText("Ви впевнені, що бажаєте видалити всі записи?")
        msg.setWindowTitle("Попередження")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        btnY = msg.button(QMessageBox.Yes)
        btnY.setText('Так')
        btnN = msg.button(QMessageBox.No)
        btnN.setText('Ні')
        msg.exec_()
        if msg.clickedButton() == btnY:
            inspcontent = "SELECT * FROM inspections"
            res = conn.execute(inspcontent)
            curs.execute("DELETE FROM inspections ")
            conn.commit()
            self.LoadDataInspectionTable()
        elif msg.clickedButton() == btnN:
            msg.close()

    def LoadDataInspectionTable(self):
        '''Завантаження даних таблиці inspections у віджет QTableWidget вкладки =Перевірки= основної форми'''
        while self.tableWidgetInspections.rowCount() > 0:
            self.tableWidgetInspections.removeRow(0)
        inspcontent = "SELECT id, type1, type2, type3, object_name, object_code, inspdate_from, inspdate_to, control_date FROM inspections"
        res = conn.execute(inspcontent)
        for row_index, row_data in enumerate(res):
            self.tableWidgetInspections.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.tableWidgetInspections.setItem(row_index,col_index,QTableWidgetItem(str(col_data)))
        self.tableWidgetInspections.selectRow(0)
        return



    def LoadDataInspectionForm(self):
        '''Завантаження даних конкретного запису таблиці inspections в форму =Етапи проведення перевірки='''
        inspcontent = "SELECT * FROM inspections"
        res = conn.execute(inspcontent)
        for row in enumerate(res):
            if row[0] == self.tableWidgetInspections.currentRow():
                data = row[1]
                global inspid
                inspid = data[0]
                selrow = curs.execute("SELECT * FROM inspections WHERE id=?",(str(inspid),))
                seldata = selrow.fetchone()
                self.editing.cmbType1.setCurrentText(seldata[1])
                self.editing.cmbType2.setCurrentText(seldata[2])
                self.editing.cmbType3.setCurrentText(seldata[3])
                self.editing.comboBoxObjectName.setCurrentText(seldata[4])
                self.editing.fldObjectCode.setText(seldata[5])
                self.editing.fldObjectAddress.setText(seldata[6])
                self.editing.fldPurpose.setPlainText(seldata[7])
                self.editing.fldInspectionFrom.setDate(datetime.datetime.strptime(seldata[8],"%d.%m.%Y"))
                self.editing.fldInspectionTo.setDate(datetime.datetime.strptime(seldata[9],"%d.%m.%Y"))
                self.editing.fldPeriodFrom.setDate(datetime.datetime.strptime(seldata[10],"%d.%m.%Y"))
                self.editing.fldPeriodTo.setDate(datetime.datetime.strptime(seldata[11],"%d.%m.%Y"))
                self.editing.fldControlDate.setDate(datetime.datetime.strptime(seldata[12],"%d.%m.%Y"))
                self.editing.fldControlDate.setDate(datetime.datetime.strptime(seldata[13],"%d.%m.%Y"))
                if seldata[14]==1:
                    self.editing.grpStopContinue.setChecked(True)
                if seldata[15]==1:
                    self.editing.grpRefuse.setChecked(True)
                if seldata[16]==1:
                    self.editing.grpResultDocs.setChecked(True)
                if seldata[17]==1:
                    self.editing.chkEnforcement.setChecked(True)
                if seldata[18]==1:
                    self.editing.chkInternalSecurity.setChecked(True)
                if seldata[19]==1:
                    self.editing.chkFinish.setChecked(True)
                if seldata[20]==1:
                    self.editing.grpViolations.setChecked(True)
                self.editing.fldTotalCharges.setText(str(seldata[21]))
                if seldata[22]==1:
                    self.editing.grpAssignments.setChecked(True)
                if seldata[23]==1:
                    self.editing.grpPropositions.setChecked(True)
                conn.commit()

    def UploadDataInspectionForm(self):
        '''Присвоєння значень змінним даних форми =Етапи проведення перевірки='''
        global type1
        type1 = self.editing.cmbType1.currentText()
        global type2
        type2 = self.editing.cmbType2.currentText()
        global type3
        type3 = self.editing.cmbType3.currentText()
        global objname
        objname = self.editing.comboBoxObjectName.currentText()
        global objcode
        objcode = self.editing.fldObjectCode.text()
        global objaddress
        objaddress = self.editing.fldObjectAddress.text()
        global insppurp
        insppurp = self.editing.fldPurpose.toPlainText()
        global idfrom
        idfrom = self.editing.fldInspectionFrom.text()
        global idto
        idto = self.editing.fldInspectionTo.text()
        global pdfrom
        pdfrom = self.editing.fldPeriodFrom.text()
        global pdto
        pdto = self.editing.fldPeriodTo.text()
        global idcontrol
        idcontrol = self.editing.fldControlDate.text()
        global nidcontrol
        nidcontrol = self.editing.fldNewControlDate.text()
        global chkstop
        if self.editing.grpStopContinue.isChecked()==True:
            chkstop = 1
        else:
            chkstop = 0
        global chkrefuse
        if self.editing.grpRefuse.isChecked()==True:
            chkrefuse = 1
        else:
            chkrefuse = 0
        global chkresult
        if self.editing.grpResultDocs.isChecked()==True:
            chkresult = 1
        else:
            chkresult = 0
        global chkenforce
        if self.editing.chkEnforcement.isChecked()==True:
            chkenforce = 1
        else:
            chkenforce = 0
        global chksecure
        if self.editing.chkInternalSecurity.isChecked()==True:
            chksecure = 1
        else:
            chksecure = 0
        global chkfinish
        if self.editing.chkFinish.isChecked()==True:
            chkfinish = 1
        else:
            chkfinish = 0
        global chkviolate
        if self.editing.grpViolations.isChecked()==True:
            chkviolate = 1
        else:
            chkviolate = 0
        global tcharges
        tcharges = self.editing.fldTotalCharges.text()
        global chkassign
        if self.editing.grpAssignments.isChecked()==True:
            chkassign = 1
        else:
            chkassign = 0
        global chkpropose
        if self.editing.grpPropositions.isChecked()==True:
            chkpropose = 1
        else:
            chkpropose = 0


    def LoadObjectData(self):
        '''Завантаження даних конкретного підрозділу з таблиці organizations бази даних'''
        objindex = self.editing.comboBoxObjectName.currentIndex()
        if objindex is 0:
            self.editing.fldObjectCode.clear()
            self.editing.fldObjectAddress.clear()
        else:
            objname = self.editing.comboBoxObjectName.currentText()
            try:
                org = conn.execute("SELECT * FROM organizations WHERE orgname=?",(objname,))
                selldata = org.fetchone()
                self.editing.fldObjectCode.setText(selldata[2])
                self.editing.fldObjectAddress.setText(selldata[3])
                conn.commit()
            except Exception as Error:
                QMessageBox.about(self, "Error message", str(Error))

    def LoadDataBasisTable(self):
        '''Завантаження і відображення переліку підстав з таблиці organizations бази даних'''
        while self.editing.tblBasis.rowCount() > 0:
            self.editing.tblBasis.removeRow(0)
        bastab = conn.execute("SELECT initiator, doc_type, doc_number, doc_date, doc_file FROM inspections_basis WHERE insp_id=?",(str(inspid),))
        for row_index, row_data in enumerate(bastab):
            self.editing.tblBasis.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.editing.tblBasis.setItem(row_index,col_index,QTableWidgetItem(str(col_data)))
        return

    def InspectionValidations(self):
        '''Валідація даних форми =Етапи проведення перевірки='''
        if self.editing.cmbType1.currentIndex() is 1:
            self.editing.cmbType2.setCurrentIndex(1)
            self.editing.cmbType2.setDisabled(True)
            self.editing.cmbType3.setCurrentIndex(1)
            self.editing.cmbType3.setDisabled(True)
        else:
            self.editing.cmbType2.setDisabled(False)
            self.editing.cmbType3.setDisabled(False)

#--------------------------------------------------------------
#РОБОТА З ФОРМОЮ "ДОДАВАННЯ/РЕДАГУВАННЯ УСТАНОВА/ПІДРОЗДІЛІВ"
#--------------------------------------------------------------

    def OrgEdit(self):
        '''Відображення форми =Установи= і робота з її елементами'''
        self.object = OrgWindow()
        self.LoadOrgTableData()
        self.object.tableWidget.cellClicked.connect(self.LoadOrgFormData)
        self.object.btnOrgCancel.clicked.connect(self.object.close)
        self.object.btnOrgEdit.clicked.connect(self.OrgDataEdit)
        self.object.btnOrgAdd.clicked.connect(self.OrgDataAdd)
        self.object.btnOrgDelete.clicked.connect(self.OrgDataDelete)
        self.object.exec_()

    def LoadOrgTableData(self):
        '''Завантаження і відображення переліку установ з таблиці organizations бази даних'''
        while self.object.tableWidget.rowCount() > 0:
            self.object.tableWidget.removeRow(0)
        orgcontent = "SELECT orgname, orgcode, orgaddress FROM organizations"
        orgtab = conn.execute(orgcontent)
        for row_index, row_data in enumerate(orgtab):
            self.object.tableWidget.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.object.tableWidget.setItem(row_index,col_index,QTableWidgetItem(str(col_data)))
        return

    def LoadOrgFormData(self):
        '''Завантаження і відображення даних конкретної установи з таблиці organizations бази даних'''
        orgdata = "SELECT * FROM organizations"
        res = conn.execute(orgdata)
        for row in enumerate(res):
            if row[0] == self.object.tableWidget.currentRow():
                data = row[1]
                global orgid
                orgid = data[0]
                selrow = curs.execute("SELECT * FROM organizations WHERE id=?",(str(orgid),))
                selorgdata = selrow.fetchone()
                self.object.lineEditOrgName.setText(selorgdata[1])
                self.object.lineEditOrgCode.setText(selorgdata[2])
                self.object.lineEditOrgAddress.setText(selorgdata[3])
                conn.commit()

    def OrgDataEdit(self):
        '''Редагування даних конкретної установи та збереження в базі даних'''
        orgname = self.object.lineEditOrgName.text()
        orgcode = self.object.lineEditOrgCode.text()
        orgaddress = self.object.lineEditOrgAddress.text()
        try:
            curs.execute("UPDATE organizations SET orgname=?, orgcode=?, orgaddress=? WHERE id=?", (orgname,orgcode,orgaddress,orgid))
            conn.commit()
            self.LoadOrgTableData()
        except Exception as Error:
            msg=QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(str(Error))
            msg.setWindowTitle("Помилка")
            msg.setStandardButtons(QMessageBox.Ok)
            btnOk = msg.button(QMessageBox.Ok)
            msg.exec_()
            if msg.clickedButton() == btnOk:
                msg.close()

    def OrgDataAdd(self):
        '''Додавання даних нової установи в таблицю organizations бази даних'''
        orgname = self.object.lineEditOrgName.text()
        orgcode = self.object.lineEditOrgCode.text()
        orgaddress = self.object.lineEditOrgAddress.text()
        try:
            curs.execute("INSERT INTO organizations (orgname, orgcode, orgaddress) VALUES (?,?,?)", (orgname,orgcode,orgaddress))
            conn.commit()
            self.LoadOrgTableData()
        except Exception as Error:
            msg=QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(str(Error))
            msg.setWindowTitle("Помилка")
            msg.setStandardButtons(QMessageBox.Ok)
            btnOk = msg.button(QMessageBox.Ok)
            msg.exec_()
            if msg.clickedButton() == btnOk:
                msg.close()

    def OrgDataDelete(self):
        '''Видалення запису в таблиці inspections бази даних'''
        msg=QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setText("УВАГА!!!")
        msg.setInformativeText("Ви впевнені, що бажаєте видалити цей запис?")
        msg.setWindowTitle("Попередження")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        btnY = msg.button(QMessageBox.Yes)
        btnY.setText('Так')
        btnN = msg.button(QMessageBox.No)
        btnN.setText('Ні')
        msg.exec_()
        if msg.clickedButton() == btnY:
            orgcont = "SELECT * FROM organizations"
            res = conn.execute(orgcont)
            for row in enumerate(res):
                if row[0] == self.object.tableWidget.currentRow():
                    data = row[1]
                    inspid = data[0]
                    curs.execute("DELETE FROM organizations WHERE id=?",(str(orgid),))
                    conn.commit()
                    self.LoadOrgTableData()
        elif msg.clickedButton() == btnN:
            msg.close()

#------------------------------------------------------------
#РОБОТА З ФОРМОЮ =ПІДСТАВА ПРОВЕДЕННЯ ПЕРЕВІРКИ=
#------------------------------------------------------------

    def BasisAdd(self):
        '''Обробка сигналу натиснення кнопки <Додати підставу> вкладки =Перевірки= основної форми'''
        self.basis = BasisWindow()
        res = conn.execute("SELECT orgname FROM organizations ORDER BY id")
        objlist = res.fetchall()
        cmblist = [i[0] for i in objlist]
        conn.commit()
        self.basis.comboBoxBasisInitiator.addItems(cmblist)
        self.basis.comboBoxBasisInitiator.setCurrentIndex(-1)
        self.basis.pushButtonAdd.clicked.connect(self.BasisAddFile)
        self.basis.pushButtonDelete.clicked.connect(self.BasisDeleteFile)
        self.basis.pushButtonView.clicked.connect(self.BasisViewFile)
        self.basis.pushButtonSave.clicked.connect(self.BasisSaveData)
        self.basis.exec_()

    def BasisAddFile(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Оберіть файл для прикріплення", "", "PDF (*.pdf);; DOC(*.doc *.docx)", "")
        filepath = os.path.normpath(filepath)
        filename = filepath.split(os.sep)
        self.basis.listWidgetBasisFile.addItem(filename[-1])

        # filename = filepath.split("/")[-1]
        print(filepath)
        print(filename)

        # file, _ = QtWidgets.QFileDialog.getOpenFileUrl(self, "Оберіть файл для прикріплення", "", "(*)", "(*)")
        # filename = file[0].toLocalFile()
        # if filename:
        #     print(filename)

    def BasisDeleteFile(self):
        item = self.basis.listWidgetBasisFile.takeItem(self.basis.listWidgetBasisFile.currentRow())
        item = None

    def BasisViewFile(self):
        pass

    def BasisSaveData(self):
        pass

#=============================================================
#------------------------КЛАСИ--------------------------------
#=============================================================

class InspectionWindow(QDialog,inspform.Ui_InspectionDialog):
    def __init__(self,parent=None):
        super(InspectionWindow,self).__init__(parent)
        self.setupUi(self)


class OrgWindow(QDialog,orgform.Ui_DialogOrgChoose):
    def __init__(self,parent=None):
        super(OrgWindow,self).__init__(parent)
        self.setupUi(self)

class BasisWindow(QDialog,baseform.Ui_DialogBasis):
    def __init__(self,parent=None):
        super(BasisWindow,self).__init__(parent)
        self.setupUi(self)

app = QApplication([])
win = MainApp()
app.exec_()
