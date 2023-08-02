from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from threading import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox
from qt_material import apply_stylesheet
import db
import os
import distro

if distro.info()["id"] == "ubuntu" and distro.info()["version"] == "22.04":
    os.environ["QT_QPA_PLATFORM"] = "xcb"


class Ui_AddBundleDetails(object):
    def setupUi(self, AddBundleDetails):
        AddBundleDetails.setObjectName("AddBundleDetails")
        AddBundleDetails.resize(902, 534)
        self.centralwidget = QtWidgets.QWidget(AddBundleDetails)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gbSlipDetailsGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.gbSlipDetailsGroup.setObjectName("gbSlipDetailsGroup")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.gbSlipDetailsGroup)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.collegeDetailsLayout = QtWidgets.QHBoxLayout()
        self.collegeDetailsLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.collegeDetailsLayout.setObjectName("collegeDetailsLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lablelRoute = QtWidgets.QLabel(self.gbSlipDetailsGroup)
        self.lablelRoute.setObjectName("lablelRoute")
        self.verticalLayout_8.addWidget(self.lablelRoute)
        self.cbRouteList = QtWidgets.QComboBox(self.gbSlipDetailsGroup)
        self.cbRouteList.setMinimumSize(QtCore.QSize(50, 0))
        self.cbRouteList.setEditable(False)
        self.cbRouteList.setObjectName("cbRouteList")
        self.verticalLayout_8.addWidget(self.cbRouteList)
        self.collegeDetailsLayout.addLayout(self.verticalLayout_8)
        self.line = QtWidgets.QFrame(self.gbSlipDetailsGroup)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.collegeDetailsLayout.addWidget(self.line)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelCollegeList = QtWidgets.QLabel(self.gbSlipDetailsGroup)
        self.labelCollegeList.setObjectName("labelCollegeList")
        self.verticalLayout_5.addWidget(self.labelCollegeList)
        self.cbCollegeList = QtWidgets.QComboBox(self.gbSlipDetailsGroup)
        self.cbCollegeList.setMinimumSize(QtCore.QSize(0, 0))
        self.cbCollegeList.setEditable(True)
        self.cbCollegeList.setObjectName("cbCollegeList")
        self.verticalLayout_5.addWidget(self.cbCollegeList)
        self.collegeDetailsLayout.addLayout(self.verticalLayout_5)
        self.line_3 = QtWidgets.QFrame(self.gbSlipDetailsGroup)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.collegeDetailsLayout.addWidget(self.line_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelBundleSlipDate = QtWidgets.QLabel(self.gbSlipDetailsGroup)
        self.labelBundleSlipDate.setObjectName("labelBundleSlipDate")
        self.verticalLayout_6.addWidget(self.labelBundleSlipDate)
        self.deBundleSlipDate = QtWidgets.QDateEdit(self.gbSlipDetailsGroup)
        self.deBundleSlipDate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.deBundleSlipDate.setCalendarPopup(True)
        self.deBundleSlipDate.setObjectName("deBundleSlipDate")
        self.verticalLayout_6.addWidget(self.deBundleSlipDate)
        self.collegeDetailsLayout.addLayout(self.verticalLayout_6)
        self.line_4 = QtWidgets.QFrame(self.gbSlipDetailsGroup)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.collegeDetailsLayout.addWidget(self.line_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelMessengerList = QtWidgets.QLabel(self.gbSlipDetailsGroup)
        self.labelMessengerList.setObjectName("labelMessengerList")
        self.verticalLayout_7.addWidget(self.labelMessengerList)
        self.cbMessenger = QtWidgets.QComboBox(self.gbSlipDetailsGroup)
        self.cbMessenger.setEditable(True)
        self.cbMessenger.setObjectName("cbMessenger")
        self.verticalLayout_7.addWidget(self.cbMessenger)
        self.collegeDetailsLayout.addLayout(self.verticalLayout_7)
        self.collegeDetailsLayout.setStretch(2, 20)
        self.verticalLayout_12.addLayout(self.collegeDetailsLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelQpSeriesList = QtWidgets.QLabel(self.gbSlipDetailsGroup)
        self.labelQpSeriesList.setObjectName("labelQpSeriesList")
        self.verticalLayout_2.addWidget(self.labelQpSeriesList)
        self.cbQpSeries = QtWidgets.QComboBox(self.gbSlipDetailsGroup)
        self.cbQpSeries.setMinimumSize(QtCore.QSize(50, 0))
        self.cbQpSeries.setObjectName("cbQpSeries")
        self.verticalLayout_2.addWidget(self.cbQpSeries)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.gbSlipDetailsGroup)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelQpCode = QtWidgets.QLabel(self.gbSlipDetailsGroup)
        self.labelQpCode.setObjectName("labelQpCode")
        self.verticalLayout_4.addWidget(self.labelQpCode)
        self.leQpCode = QtWidgets.QLineEdit(self.gbSlipDetailsGroup)
        self.leQpCode.setObjectName("leQpCode")
        self.verticalLayout_4.addWidget(self.leQpCode)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(30, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.sbBundleMulti = QtWidgets.QSpinBox(self.gbSlipDetailsGroup)
        self.sbBundleMulti.setProperty("value", 1)
        self.sbBundleMulti.setObjectName("sbBundleMulti")
        self.verticalLayout_3.addWidget(self.sbBundleMulti)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 20, -1, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ticBoxNillStatment = QtWidgets.QCheckBox(self.gbSlipDetailsGroup)
        self.ticBoxNillStatment.setObjectName("ticBoxNillStatment")
        self.verticalLayout.addWidget(self.ticBoxNillStatment)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_5 = QtWidgets.QFrame(self.gbSlipDetailsGroup)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btnAddQpCode = QtWidgets.QPushButton(self.gbSlipDetailsGroup)
        self.btnAddQpCode.setMinimumSize(QtCore.QSize(0, 0))
        self.btnAddQpCode.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnAddQpCode.setAutoDefault(False)
        self.btnAddQpCode.setObjectName("btnAddQpCode")
        self.verticalLayout_11.addWidget(self.btnAddQpCode)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        self.labelRemarks = QtWidgets.QLabel(self.gbSlipDetailsGroup)
        self.labelRemarks.setObjectName("labelRemarks")
        self.verticalLayout_12.addWidget(self.labelRemarks)
        self.pteRemarks = QtWidgets.QPlainTextEdit(self.gbSlipDetailsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteRemarks.sizePolicy().hasHeightForWidth())
        self.pteRemarks.setSizePolicy(sizePolicy)
        self.pteRemarks.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pteRemarks.setObjectName("pteRemarks")
        self.verticalLayout_12.addWidget(self.pteRemarks)
        self.verticalLayout_10.addWidget(self.gbSlipDetailsGroup)
        self.leSearchTable = QtWidgets.QLineEdit(self.centralwidget)
        self.leSearchTable.setObjectName("leSearchTable")
        self.verticalLayout_10.addWidget(self.leSearchTable)
        self.twBundleDetails = QtWidgets.QTableWidget(self.centralwidget)
        self.twBundleDetails.setMinimumSize(QtCore.QSize(773, 0))
        self.twBundleDetails.setWhatsThis("")
        self.twBundleDetails.setWordWrap(False)
        self.twBundleDetails.setObjectName("twBundleDetails")
        self.twBundleDetails.setColumnCount(7)
        self.twBundleDetails.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(6, item)
        self.verticalLayout_10.addWidget(self.twBundleDetails)
        self.bottomBtnsLayout = QtWidgets.QHBoxLayout()
        self.bottomBtnsLayout.setContentsMargins(0, 0, -1, -1)
        self.bottomBtnsLayout.setObjectName("bottomBtnsLayout")
        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubmit.setObjectName("btnSubmit")
        self.bottomBtnsLayout.addWidget(self.btnSubmit)
        self.btnDeleteSelectedRow = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteSelectedRow.setObjectName("btnDeleteSelectedRow")
        self.bottomBtnsLayout.addWidget(self.btnDeleteSelectedRow)
        self.btnClearTable = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearTable.setObjectName("btnClearTable")
        self.bottomBtnsLayout.addWidget(self.btnClearTable)
        self.verticalLayout_10.addLayout(self.bottomBtnsLayout)
        AddBundleDetails.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddBundleDetails)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 23))
        self.menubar.setObjectName("menubar")
        AddBundleDetails.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddBundleDetails)
        self.statusbar.setObjectName("statusbar")
        AddBundleDetails.setStatusBar(self.statusbar)

        self.retranslateUi(AddBundleDetails)

        self.deBundleSlipDate.setDateTime(QtCore.QDateTime.currentDateTime())
        icon = QIcon()
        icon.addFile(u"data/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        AddBundleDetails.setWindowIcon(icon)
        header = self.twBundleDetails.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)

        AddBundleDetails.keyPressEvent = self.pressEnter

        # self.twBundleDetails.setSelectionMode(QAbstractItemView.MultiSelection)
        self.cbCollegeList.setEnabled(False)
        self.loadComboBoxes()
        self.sortListThread()
        self.cbRouteList.activated.connect(self.sortListThread)
        self.btnAddQpCode.clicked.connect(self.addDataToTable)
        self.btnSubmit.clicked.connect(self.getSubmittedData)
        self.leSearchTable.textChanged.connect(self.search)
        self.btnDeleteSelectedRow.clicked.connect(self.deleteSelectedRow)
        self.btnClearTable.clicked.connect(self.deleteAllTableData)

        QtCore.QMetaObject.connectSlotsByName(AddBundleDetails)

    def popUpResponse(self, i):
        if i.text() == "OK":
            self.twBundleDetails.clearContents()
            self.twBundleDetails.setRowCount(0)
        else:
            return False

    def deleteAllTableData(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Attention")
        msgBox.setText("You Are About To Delete All Entered Data")
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Cancel)
        msgBox.buttonClicked.connect(self.popUpResponse)
        msgBox.exec_()

    def deleteSelectedRow(self):
        # print("Invoked", self.twBundleDetails.selectionModel().selection())
        for ix in self.twBundleDetails.selectionModel().selection():
            for index in ix.indexes():
                # print(index.row())
                self.twBundleDetails.removeRow(index.row())
            # print('Selected Cell Location Row: {0}, Column: {1}'.format(ix.row(), ix.column()))

    def pressEnter(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.cbCollegeList.currentText() and self.cbRouteList.currentText() and self.cbMessenger.currentText() and self.leQpCode.text() != "":
                qpSeries = self.cbQpSeries.currentText()
                qpCode = self.leQpCode.text()
                slipDate = self.deBundleSlipDate.date().toString()
                messengerName = self.cbMessenger.currentText()
                clgName = self.cbCollegeList.currentText()
                
                query = {"qpSeries": qpSeries, "qpCode": qpCode, "isNil": bool(self.ticBoxNillStatment.checkState()),
                              "receivedDate": datetime.strptime(slipDate, '%a %b %d %Y'), "messenger": messengerName,
                              "collegeName": clgName}
                              
                if db.checkForBundles("bundleDetails", query) is False:
                    self.addDataToTable()
                    self.leQpCode.clear()
                    self.sbBundleMulti.setValue(1)
                else:
                    print("Bundle Already Present: ", query)
                    self.showMessage(QMessageBox.Critical, "Already Present")
            else:
                self.showMessage(QMessageBox.Warning, "Please Enter details in all fields", "Error")

    @staticmethod
    def showMessage(msgType, data, titleName="Info"):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(titleName)
        msgBox.setText(data)
        msgBox.setIcon(msgType)
        msgBox.exec_()

    def search(self, s):
        items = self.twBundleDetails.findItems(s, Qt.MatchContains)
        if items:  # we have found something
            item = items[0]  # take the first
            self.twBundleDetails.setCurrentItem(item)

    def getSubmittedData(self):
        rowCount = self.twBundleDetails.rowCount()
        columnCount = self.twBundleDetails.columnCount()
        finalData = []

        for row in range(rowCount):
            rowData = []
            for column in range(columnCount):
                widgetItem = self.twBundleDetails.item(row, column)
                if column == 2:
                    rowData.append(widgetItem.checkState())
                elif widgetItem and widgetItem.text:
                    # print(widgetItem.text())
                    rowData.append(widgetItem.text())
                else:
                    rowData.append('NULL')
            query = {"qpSeries": rowData[0], "qpCode": rowData[1], "isNil": bool(rowData[2]),
                              "receivedDate": datetime.strptime(rowData[3], '%a %b %d %Y'), "messenger": rowData[4],
                              "collegeName": rowData[5],"remarks":str(rowData[6])}

            if db.checkForBundles("bundleDetails", query) is False:
                finalData.append(query)
            else:
                print("Bundle Already Present: ", query)
                self.showMessage(QMessageBox.Critical, rowData[0]+" "+rowData[1]+" Already Present")
                              
        result, resCode = db.addDataToDB("bundleDetails", finalData)
        # print(result, resCode)
        # result = True
        resCode = ""
        print(finalData)
        if result is True:
            self.showMessage(QMessageBox.Information, "Collection Added To Database")
            self.twBundleDetails.clearContents()
            self.twBundleDetails.setRowCount(0)
        else:
            self.showMessage(QMessageBox.Critical, resCode)

    def sortListThread(self):
        self.cbCollegeList.setEnabled(False)
        t1 = Thread(target=self.sortCollegeListBasedOnRoute)
        t1.start()

    def sortCollegeListBasedOnRoute(self):
        self.cbCollegeList.clear()
        clgList = db.sortAndGetData("collegeList", "Route", self.cbRouteList.currentText())
        for data in clgList:
            self.cbCollegeList.addItem(data["College Name"] + " " + data["Place"])

        self.cbCollegeList.setEnabled(True)

    def loadComboBoxes(self):
        configs, messengers = db.getConfig()

        for messenger in messengers:
            self.cbMessenger.addItem(messenger["name"])

        self.cbQpSeries.addItems(configs['qp_series'])
        self.cbRouteList.addItems(configs['routes'])

    def addDataToTable(self):

        qpSeries = self.cbQpSeries.currentText()
        qpCode = self.leQpCode.text()
        slipDate = self.deBundleSlipDate.date().toString()
        messengerName = self.cbMessenger.currentText()
        clgName = self.cbCollegeList.currentText()
        bundlesMulti = self.sbBundleMulti.value()
        remarks = self.pteRemarks.toPlainText()

        if len(qpCode) >4:
            remarks = remarks+" (SLCM Bundle)"


        isNilCheckBox = QTableWidgetItem()
        isNilCheckBox.setTextAlignment(Qt.AlignHCenter)
        isNilCheckBox.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        isNilCheckBox.setCheckState(self.ticBoxNillStatment.checkState())

        i = 1
        while i<=bundlesMulti:
            rowPosition = self.twBundleDetails.rowCount()

            self.twBundleDetails.setRowCount(rowPosition + 1)
            self.twBundleDetails.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(qpSeries))
            self.twBundleDetails.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(qpCode))
            self.twBundleDetails.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(isNilCheckBox))
            self.twBundleDetails.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(slipDate))
            self.twBundleDetails.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(messengerName))
            self.twBundleDetails.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(clgName))
            self.twBundleDetails.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(remarks))
            i += 1
        self.twBundleDetails.scrollToBottom()

    def retranslateUi(self, AddBundleDetails):
        _translate = QtCore.QCoreApplication.translate
        AddBundleDetails.setWindowTitle(_translate("AddBundleDetails", "Add Bundles To Collection"))
        self.gbSlipDetailsGroup.setTitle(_translate("AddBundleDetails", "Collection Slip Details"))
        self.lablelRoute.setText(_translate("AddBundleDetails", "Select Route"))
        self.labelCollegeList.setText(_translate("AddBundleDetails", "Select College"))
        self.cbCollegeList.setStatusTip(_translate("AddBundleDetails", "Enter College Name"))
        self.cbCollegeList.setPlaceholderText(_translate("AddBundleDetails", "Select College Name"))
        self.labelBundleSlipDate.setText(_translate("AddBundleDetails", "Select Received Date"))
        self.labelMessengerList.setText(_translate("AddBundleDetails", "Select Messenger"))
        self.cbMessenger.setStatusTip(_translate("AddBundleDetails", "Enter Messenger Name"))
        self.cbMessenger.setPlaceholderText(_translate("AddBundleDetails", "Select Messenger"))
        self.labelQpSeriesList.setText(_translate("AddBundleDetails", "Select QP Series"))
        self.cbQpSeries.setAccessibleName(_translate("AddBundleDetails", "QP Series"))
        self.cbQpSeries.setPlaceholderText(_translate("AddBundleDetails", "Test"))
        self.labelQpCode.setText(_translate("AddBundleDetails", "Enter QP Code"))
        self.leQpCode.setStatusTip(_translate("AddBundleDetails", "Enter QP Code"))
        self.ticBoxNillStatment.setText(_translate("AddBundleDetails", "Check If Bundle Is Nil"))
        self.leQpCode.setValidator(QIntValidator(1, 999999999))
        self.leQpCode.setMaxLength(8)
        self.leQpCode.setPlaceholderText("Enter QP Code")
        self.btnAddQpCode.setText(_translate("AddBundleDetails", "Add To List"))
        self.labelRemarks.setText(_translate("AddBundleDetails", "Remarks(If any)"))
        self.leSearchTable.setPlaceholderText(_translate("AddBundleDetails", "Enter Data To Search"))
        item = self.twBundleDetails.horizontalHeaderItem(0)
        item.setText(_translate("AddBundleDetails", "Series"))
        item = self.twBundleDetails.horizontalHeaderItem(1)
        item.setText(_translate("AddBundleDetails", "QP Code"))
        item = self.twBundleDetails.horizontalHeaderItem(2)
        item.setText(_translate("AddBundleDetails", "Nil"))
        item = self.twBundleDetails.horizontalHeaderItem(3)
        item.setText(_translate("AddBundleDetails", "Bundle Slip Date"))
        item = self.twBundleDetails.horizontalHeaderItem(4)
        item.setText(_translate("AddBundleDetails", "Messenger Name"))
        item = self.twBundleDetails.horizontalHeaderItem(5)
        item.setText(_translate("AddBundleDetails", "College Name"))
        item = self.twBundleDetails.horizontalHeaderItem(6)
        item.setText(_translate("AddBundleDetails", "Remarks"))
        self.btnSubmit.setText(_translate("AddBundleDetails", "Submit"))
        self.btnClearTable.setText(_translate("AddBundleDetails", "Clear Table"))
        self.btnDeleteSelectedRow.setText(_translate("AddBundleDetails", "Delete Selected Rows"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddBundleDetails = QtWidgets.QMainWindow()
    ui = Ui_AddBundleDetails()
    ui.setupUi(AddBundleDetails)
    # apply_stylesheet(app, theme='dark_teal.xml')
    AddBundleDetails.show()
    sys.exit(app.exec_())
