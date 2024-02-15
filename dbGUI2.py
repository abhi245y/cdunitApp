import sys
from PyQt5 import QtWidgets, QtGui
from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
from datetime import datetime, timedelta, time
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, pyqtSignal, QTimer, Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem
import distro
import os
import json
import db
import pytz
import math
import threading
import time



filename = 'db_config.json'

with open(filename, 'r') as f:
    db_config = json.load(f)
    QT_QPA_PLATFORM_ENABLED = db_config['QT_QPA_PLATFORM']

if QT_QPA_PLATFORM_ENABLED == True:
    if distro.info()["id"] == "ubuntu" and distro.info()["version"] == "22.04":
        os.environ["QT_QPA_PLATFORM"] = "xcb"


collection = db.cdUnitDB['bundleDetails']

class RecentDataWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modify Database")
        icon = QIcon()
        icon.addFile(u"data/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.initUI()

    def initUI(self):
        _translate = QtCore.QCoreApplication.translate
        # Layout
        layout = QtWidgets.QVBoxLayout()

        # Buttons Layout
        buttons_layout = QtWidgets.QHBoxLayout()

        # Fetch Button
        self.fetch_button = QtWidgets.QPushButton('Fetch Recent Data', self)
        self.fetch_button.clicked.connect(self.fetch_recent_data)
        buttons_layout.addWidget(self.fetch_button)

        # Delete Button
        self.delete_button = QtWidgets.QPushButton('Delete Selected Rows', self)
        self.delete_button.clicked.connect(self.delete_selected_rows)
        buttons_layout.addWidget(self.delete_button)

        # Update Button
        self.update_button = QtWidgets.QPushButton('Update Changes', self)
        # self.update_button.clicked.connect(self.update_changes)
        self.update_button.clicked.connect(self.update)
        buttons_layout.addWidget(self.update_button)

        layout.addLayout(buttons_layout)
        
        # Create QDateEdit widgets and  Create labels for the date edits
        self.start_date_label = QtWidgets.QLabel("Start Date")
        self.start_date_edit = QtWidgets.QDateEdit()
        self.start_date_edit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.start_date_edit.setCalendarPopup(True)
        self.start_date_edit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.end_date_label = QtWidgets.QLabel("End Date (Currently Disabled)")
        self.end_date_edit = QtWidgets.QDateEdit()
        self.end_date_edit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.end_date_edit.setCalendarPopup(True)
        self.end_date_edit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.end_date_edit.setEnabled(False)
        

        # Create a new QHBoxLayout to accommodate the labels and QDateEdits
        self.date_layout = QtWidgets.QHBoxLayout()

        # Add the widgets to the new layout
        self.date_layout.addWidget(self.start_date_label)
        self.date_layout.addWidget(self.start_date_edit)
        self.date_layout.addWidget(self.end_date_label)
        self.date_layout.addWidget(self.end_date_edit)

        # Add the new layout to the existing layout
        layout.addLayout(self.date_layout)

        # Code For Sorting Elements
        self.sortEditLayout = QtWidgets.QHBoxLayout()

        self.sort_by_recive_date_label = QtWidgets.QLabel("Enter Received Date")
        self.sort_by_recive_date = QtWidgets.QDateEdit()
        self.sort_by_recive_date.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.sort_by_recive_date.setCalendarPopup(True)
        self.sort_by_recive_date.setDateTime(QtCore.QDateTime.currentDateTime())
        self.sortEditLayout.addWidget(self.sort_by_recive_date_label)
        self.sortEditLayout.addWidget(self.sort_by_recive_date)

        self.sort_now_btn = QtWidgets.QPushButton('Sort', self)
        self.sort_now_btn.clicked.connect(self.initSorting)
        self.sortEditLayout.addWidget(self.sort_now_btn)

        self.clear_sorting_btn = QtWidgets.QPushButton('Clear Sorting', self)
        self.clear_sorting_btn.clicked.connect(self.clearSorting)
        self.sortEditLayout.addWidget(self.clear_sorting_btn)

        layout.addLayout(self.sortEditLayout)

        # Search Layout and edit text
        self.searchEditLayout = QtWidgets.QHBoxLayout()
        self.leSearchTable = QtWidgets.QLineEdit()
        self.leSearchTable.setObjectName("leSearchTable")
        self.searchEditLayout.addWidget(self.leSearchTable)
        layout.addLayout(self.searchEditLayout)
        self.leSearchTable.setPlaceholderText(_translate("AddBundleDetails", "Enter Data To Search"))
        self.leSearchTable.textChanged.connect(self.search)


        # Table View
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(["Date of Entry", "QP Series", "QP Code","Nill Bundle","Received Date", "Messenger", "College Name", "Remarks", "DB _id"])
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.itemSelectionChanged.connect(self.onItemSelected)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        layout.addWidget(self.table)

        self.table.horizontalHeader().sectionClicked.connect(self.sort_columns)

        self.Hlayout = QtWidgets.QHBoxLayout()

        self.bottomLineText = QtWidgets.QLabel("")
        
        self.Hlayout.addWidget(self.bottomLineText)

        self.db_label = QtWidgets.QLabel()
        self.pixmap = QtGui.QPixmap("./db_okay.png")
        self.db_label.setPixmap(self.pixmap)
        self.Hlayout.addStretch()
        self.Hlayout.addWidget(self.db_label)

        layout.addLayout(self.Hlayout)


        self.setLayout(layout)
        self.resize(1000, 800)
        self.fetch_recent_data()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_status)
        interval = 5000
        self.timer.start(interval)

    def update_status(self):
        db_status = db.check_db_connection()
        if db_status:
            self.pixmap = QtGui.QPixmap("./db_okay.png")
            self.db_label.setPixmap(self.pixmap)
        else:
            self.pixmap = QtGui.QPixmap("./db_failed.png")
            self.db_label.setPixmap(self.pixmap)
    
    def sort_columns(self, column_index):
        column_labels = [self.table.horizontalHeaderItem(i).text().replace('▼ ','').replace('▲ ','') for i in range(9)]

        if column_index in [0, 1, 3, 4, 5,6]:
            # Initialize sort order indicator if not set
            self._sort_order = getattr(self, '_sort_order', Qt.AscendingOrder)

            # Toggle order and update header text
            if self._sort_order == Qt.AscendingOrder:
                new_order = Qt.DescendingOrder
                arrow_text = '▲ '+column_labels[column_index]
            else:
                new_order = Qt.AscendingOrder
                arrow_text = '▼ '+column_labels[column_index]

            self.table.sortItems(column_index, new_order)
            self.table.horizontalHeaderItem(column_index).setText(arrow_text)

            # Update _sort_order for next click
            self._sort_order = new_order
        else:
            return

    def onItemSelected(self):
        if len(self.table.selectedItems()) != 0:
            selected_items = str(math.floor(len(self.table.selectedItems())/self.table.columnCount()))  
            self.bottomLineText.setText(f"Number of selected items: {selected_items}")
        else:
            self.bottomLineText.setText(f"Number of selected items: {len(self.table.selectedItems())}")
               
    def initSorting(self):
        dateToSortQDate = self.sort_by_recive_date.date()
        dateToSort = datetime(dateToSortQDate.year(),dateToSortQDate.month(),dateToSortQDate.day()).strftime("%a %b %d %Y")
        print(dateToSort)
        self.search(dateToSort)
    
    def clearSorting(self):
        self.search("")

    def onEditTextChanged(self):
        text = self.leSearchTable.text()
        if str(text).endswith(" "): # Check if the text ends with a space
            # Remove the trailing space
            self.search(text)

    def mousePressEvent(self, event):
        # Check if the source of the event (the widget that was clicked) is not the QTableWidget
        if event.source() != self.table:
            # Deselect rows in the QTableWidget
            self.table.clearSelection()
        super().mousePressEvent(event)

    def search(self, s):
        for row in range(self.table.rowCount()):
            row_text = " ".join([self.table.item(row, col).text() for col in range(self.table.columnCount())])
            if s.lower() in row_text.lower():
                self.table.setRowHidden(row, False)
            else:
                self.table.setRowHidden(row, True)

    def get_objectid_from_specific_date(self, qDate,hour=0, minute=0, second=0, timezone='UTC'):
        """Return ObjectId for a specific date and time."""
        # Set the desired date and time
        specific_datetime = datetime(qDate.year(),qDate.month(),qDate.day())
    
        # Localize the datetime to the specified timezone
        tz = pytz.timezone(timezone)
        localized_datetime = tz.localize(specific_datetime)

        # Convert the localized datetime back to an ObjectId.
        oid_bytes = int(localized_datetime.timestamp()).to_bytes(4, byteorder="big") + b'\x00\x00\x00\x00\x00\x00\x00\x00'
        specific_oid = ObjectId(oid_bytes)

        return specific_oid

    def get_objectid_24_hours_before(self, object_id):
        """Return ObjectId for 10:00 AM of the day before the date in the given ObjectId."""
        # Extract the date from the ObjectId
        date = object_id.generation_time.date()

        # Calculate the date for "yesterday"
        yesterday = date - timedelta(days=1)

        # Set the time to 10:00 AM in IST
        ist_timezone = pytz.timezone('Asia/Kolkata')
        dt_yesterday_10am = ist_timezone.localize(datetime.combine(yesterday, time(10, 0)))


        # Convert the datetime back to an ObjectId.
        # The timestamp is the first 4 bytes of the ObjectId, so we'll manually construct it.
        oid_bytes = int(dt_yesterday_10am.timestamp()).to_bytes(4, byteorder="big") + b'\x00\x00\x00\x00\x00\x00\x00\x00'
        oid_yesterday_10am = ObjectId(oid_bytes)

        return oid_yesterday_10am

    def fetch_recent_data(self):
        self.table.clearContents()
        self.table.setRowCount(0)
 

        doc = collection.find_one(sort=[("_id", -1)])  # Get the last added document
        last_oid = doc["_id"]

        # start_oid = self.get_objectid_24_hours_before(last_oid)
        startQDate = self.start_date_edit.date()
        # print(self.start_date_edit.date().year(),self.start_date_edit.date().month(),self.start_date_edit.date().day())
        start_oid = self.get_objectid_from_specific_date(qDate=startQDate, timezone='Asia/Kolkata')

        print(start_oid)
        print(ObjectId(start_oid).generation_time, ObjectId(last_oid).generation_time)
        
        datas = list(collection.find({"_id": {"$gte": start_oid}}).sort([("_id", pymongo.DESCENDING)]))

        for data in datas:
            if isinstance(data['receivedDate'], datetime):   
                recivedDate = data['receivedDate'].strftime("%a %b %d %Y")
            qpSeries = data['qpSeries']
            qpCode = data['qpCode'] 
            messengerName = data['messenger']
            clgName = data['collegeName']
            remarks = data['remarks']

            rowPosition = self.table.rowCount()
            # print(query)

            dateOfEntry = ObjectId(data['_id']).generation_time.strftime("%a %b %d %Y")

            self.table.setRowCount(rowPosition + 1)
            self.table.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(dateOfEntry)))
            self.table.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(qpSeries))
            self.table.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(qpCode))
            self.table.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(data['isNil'])))
            self.table.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(recivedDate))
            self.table.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(messengerName))
            self.table.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(clgName))
            self.table.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(remarks))
            self.table.setItem(rowPosition, 8, QtWidgets.QTableWidgetItem(str(data['_id'])))


    def delete_selected_rows(self):
        selected_rows = list(set(index.row() for index in self.table.selectedIndexes()))
        if not selected_rows:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'No rows selected!')
            return

        confirmation = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete the selected rows?',
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirmation == QtWidgets.QMessageBox.Yes:

            for row in sorted(selected_rows, reverse=True):
                _id = self.table.item(row, 8).text()
                collection.delete_one({"_id": ObjectId(_id)})
                self.table.removeRow(row)

            QtWidgets.QMessageBox.information(self, 'Success', 'Selected rows deleted successfully!')

    def update_changes(self):
        def add_data_to_db(self):
            confirmation = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to save the changes?',
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if confirmation == QtWidgets.QMessageBox.Yes:
                keys = ["_id", "qpSeries", "qpCode", "receivedDate", "messenger", "collegeName", "isNull", "remarks"]
                for row in range(self.table.rowCount()):
                    updated_data = {key: self.table.item(row, col).text() for col, key in enumerate(keys)}
                    updated_data["_id"] = ObjectId(updated_data["_id"])
                    collection.replace_one({"_id": updated_data["_id"]}, updated_data)

                QtWidgets.QMessageBox.information(self, 'Success', 'Changes saved successfully!')

        if db.check_db_connection():
            add_data_to_db(self)
        else:
            reply = QMessageBox.question(self, 'Database Error', 'Database connection failed. Try again?',
                                         QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                update_changes(self)
    
    def update(self):
        rowCount = self.table.rowCount()
        columnCount = self.table.columnCount()
        finalData = []
        db_data = list(collection.find({}))
        for row in range(rowCount):
            rowData = []
            for column in range(columnCount):
                widgetItem = self.table.item(row, column)
                if column == 2:
                    # pass
                    # rowData.append(widgetItem.checkState())
                    rowData.append(widgetItem.text())
                elif widgetItem and widgetItem.text:
                    # print(widgetItem.text())
                    rowData.append(widgetItem.text())
                else:
                    rowData.append('NULL')
                # keys = ["_id", "qpSeries", "qpCode", "receivedDate", "messenger", "collegeName", "isNull", "remarks"]
            query = {"_id":rowData[8],"qpSeries": rowData[1], "qpCode": rowData[2], "isNil": eval(rowData[3]),
                              "receivedDate": datetime.strptime(rowData[4], '%a %b %d %Y'), "messenger": rowData[5],
                              "collegeName": rowData[6],"remarks":str(rowData[7])}
            # print(query)
            # print(ObjectId(query['_id']).generation_time)
            for doc in collection.find({'_id':ObjectId(query['_id'])},{'_id': 0 }):
                for key in doc.keys():
                    if query[key] != doc[key]:
                        collection.update_one({"_id": ObjectId(query['_id'])}, {"$set": {key: query[key]}})

    def update_database_changes(self):
        # 1. Retrieve Data from the Table
        table_data = []
        for row in range(self.table.rowCount()):
            row_data = {}
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item:
                    header = self.table.horizontalHeaderItem(col).text()
                    row_data[header] = item.text()
                    # print(row_data,'\n')
            table_data.append(row_data)

        db_data = list(collection.find({}))

        # 3. Compare the Data
        rows_to_update = []
        for t_data, db_data_row in zip(table_data, db_data):
            differences = {}
            for key, value in t_data.items():   
                print(key,value, type(value))
                if key !='_id':
                    if db_data_row.get(key) != value:
                        differences[key] = value
                    if differences:
                        # print(differences)
                        rows_to_update.append({"_id": db_data_row["_id"], "changes": differences})
                elif key == 'isNull':
                    print(key,value)
                    if db_data_row.get(key) != value or db_data_row.get(key) != bool(value):
                        differences[key] = value
                    if differences:
                        # print(differences)
                        rows_to_update.append({"_id": db_data_row["_id"], "changes": differences})

        # 4. Update the Database
        for row_update in rows_to_update:
            # print(row_update)
            pass
            # collection.update_one({"_id": row_update["_id"]}, {"$set": row_update["changes"]})


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RecentDataWindow()
    window.show()
    sys.exit(app.exec_())
