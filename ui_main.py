# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainVmxiyd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AddBundleDetails(object):
    def setupUi(self, AddBundleDetails):
        if not AddBundleDetails.objectName():
            AddBundleDetails.setObjectName(u"AddBundleDetails")
        AddBundleDetails.resize(800, 600)
        self.centralwidget = QWidget(AddBundleDetails)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gbSlipDetails = QGroupBox(self.centralwidget)
        self.gbSlipDetails.setObjectName(u"gbSlipDetails")
        self.gbSlipDetails.setGeometry(QRect(20, 40, 771, 91))
        self.cbCollegeList = QComboBox(self.gbSlipDetails)
        self.cbCollegeList.addItem("")
        self.cbCollegeList.addItem("")
        self.cbCollegeList.setObjectName(u"cbCollegeList")
        self.cbCollegeList.setGeometry(QRect(20, 40, 221, 22))
        self.bundleSlipDate = QDateEdit(self.gbSlipDetails)
        self.bundleSlipDate.setObjectName(u"bundleSlipDate")
        self.bundleSlipDate.setGeometry(QRect(310, 40, 110, 22))
        self.bundleSlipDate.setMinimumDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.bundleSlipDate.setCalendarPopup(True)
        self.cbMessenger = QComboBox(self.gbSlipDetails)
        self.cbMessenger.addItem("")
        self.cbMessenger.addItem("")
        self.cbMessenger.setObjectName(u"cbMessenger")
        self.cbMessenger.setGeometry(QRect(470, 40, 161, 22))
        self.gbQpDetails = QGroupBox(self.centralwidget)
        self.gbQpDetails.setObjectName(u"gbQpDetails")
        self.gbQpDetails.setGeometry(QRect(20, 140, 771, 71))
        self.btnAddQpCode = QPushButton(self.gbQpDetails)
        self.btnAddQpCode.setObjectName(u"btnAddQpCode")
        self.btnAddQpCode.setGeometry(QRect(630, 30, 75, 23))
        self.cbQpSeries = QComboBox(self.gbQpDetails)
        self.cbQpSeries.addItem("")
        self.cbQpSeries.addItem("")
        self.cbQpSeries.addItem("")
        self.cbQpSeries.setObjectName(u"cbQpSeries")
        self.cbQpSeries.setGeometry(QRect(20, 30, 31, 22))
        self.leQpCode = QLineEdit(self.gbQpDetails)
        self.leQpCode.setObjectName(u"leQpCode")
        self.leQpCode.setGeometry(QRect(60, 30, 113, 20))
        self.twBundleDetails = QTableWidget(self.centralwidget)
        if (self.twBundleDetails.columnCount() < 5):
            self.twBundleDetails.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.twBundleDetails.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.twBundleDetails.rowCount() < 2):
            self.twBundleDetails.setRowCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.twBundleDetails.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.twBundleDetails.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.twBundleDetails.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.twBundleDetails.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.twBundleDetails.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.twBundleDetails.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.twBundleDetails.setItem(0, 4, __qtablewidgetitem11)
        self.twBundleDetails.setObjectName(u"twBundleDetails")
        self.twBundleDetails.setGeometry(QRect(20, 220, 771, 192))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 470, 75, 23))
        AddBundleDetails.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AddBundleDetails)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        AddBundleDetails.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AddBundleDetails)
        self.statusbar.setObjectName(u"statusbar")
        AddBundleDetails.setStatusBar(self.statusbar)

        self.retranslateUi(AddBundleDetails)

        QMetaObject.connectSlotsByName(AddBundleDetails)
    # setupUi

    def retranslateUi(self, AddBundleDetails):
        AddBundleDetails.setWindowTitle(QCoreApplication.translate("AddBundleDetails", u"MainWindow", None))
        self.gbSlipDetails.setTitle(QCoreApplication.translate("AddBundleDetails", u"Collection Slip Details", None))
        self.cbCollegeList.setItemText(0, QCoreApplication.translate("AddBundleDetails", u"Govt College", None))
        self.cbCollegeList.setItemText(1, QCoreApplication.translate("AddBundleDetails", u"Iqbal College", None))

#if QT_CONFIG(statustip)
        self.cbCollegeList.setStatusTip(QCoreApplication.translate("AddBundleDetails", u"Enter College Name", None))
#endif // QT_CONFIG(statustip)
        self.cbCollegeList.setPlaceholderText(QCoreApplication.translate("AddBundleDetails", u"Select College Name", None))
        self.cbMessenger.setItemText(0, QCoreApplication.translate("AddBundleDetails", u"Rajesh", None))
        self.cbMessenger.setItemText(1, QCoreApplication.translate("AddBundleDetails", u"Vinesh", None))

#if QT_CONFIG(statustip)
        self.cbMessenger.setStatusTip(QCoreApplication.translate("AddBundleDetails", u"Enter Messenger Name", None))
#endif // QT_CONFIG(statustip)
        self.cbMessenger.setPlaceholderText(QCoreApplication.translate("AddBundleDetails", u"Select Messenger", None))
        self.gbQpDetails.setTitle(QCoreApplication.translate("AddBundleDetails", u"QP Code Details", None))
        self.btnAddQpCode.setText(QCoreApplication.translate("AddBundleDetails", u"Add To List", None))
        self.cbQpSeries.setItemText(0, QCoreApplication.translate("AddBundleDetails", u"M", None))
        self.cbQpSeries.setItemText(1, QCoreApplication.translate("AddBundleDetails", u"N", None))
        self.cbQpSeries.setItemText(2, QCoreApplication.translate("AddBundleDetails", u"P", None))

#if QT_CONFIG(statustip)
        self.leQpCode.setStatusTip(QCoreApplication.translate("AddBundleDetails", u"Enter QP Code", None))
#endif // QT_CONFIG(statustip)
        ___qtablewidgetitem = self.twBundleDetails.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddBundleDetails", u"Series", None));
        ___qtablewidgetitem1 = self.twBundleDetails.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AddBundleDetails", u"QP Code", None));
        ___qtablewidgetitem2 = self.twBundleDetails.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AddBundleDetails", u"Bundle Slip Date", None));
        ___qtablewidgetitem3 = self.twBundleDetails.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AddBundleDetails", u"Messenger Name", None));
        ___qtablewidgetitem4 = self.twBundleDetails.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AddBundleDetails", u"College Name", None));
        ___qtablewidgetitem5 = self.twBundleDetails.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AddBundleDetails", u"1", None));
        ___qtablewidgetitem6 = self.twBundleDetails.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AddBundleDetails", u"2", None));

        __sortingEnabled = self.twBundleDetails.isSortingEnabled()
        self.twBundleDetails.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.twBundleDetails.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AddBundleDetails", u"N", None));
        ___qtablewidgetitem8 = self.twBundleDetails.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AddBundleDetails", u"6730", None));
        ___qtablewidgetitem9 = self.twBundleDetails.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AddBundleDetails", u"02/02/2015", None));
        ___qtablewidgetitem10 = self.twBundleDetails.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("AddBundleDetails", u"Rajesh", None));
        ___qtablewidgetitem11 = self.twBundleDetails.item(0, 4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("AddBundleDetails", u"Govt College", None));
        self.twBundleDetails.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("AddBundleDetails", u"Submit", None))
    # retranslateUi

