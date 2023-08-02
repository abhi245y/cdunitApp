import sys
from PyQt5 import QtWidgets, QtGui
from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
import datetime
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class RecentDataWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modify Database")
        icon = QIcon()
        icon.addFile(u"data/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.initUI()

    def initUI(self):
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
        self.update_button.clicked.connect(self.update_changes)
        buttons_layout.addWidget(self.update_button)

        layout.addLayout(buttons_layout)

        # Table View
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["_id", "qpSeries", "qpCode", "receivedDate", "messenger", "collegeName", "isNull", "remarks"])
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # header = self.table.horizontalHeader()
#         header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
#         header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
#         header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
#         header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
#         header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
#         header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
#         header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
#         header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.resize(1000, 800)
        self.fetch_recent_data()

    def fetch_recent_data(self):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['cd_unit']
        collection = db['bundleDetails']

        # Fetch data from the collection
        data = list(collection.find().sort([("_id", pymongo.DESCENDING)]))

        self.table.setRowCount(len(data))
        keys = ["_id", "qpSeries", "qpCode", "receivedDate", "messenger", "collegeName", "isNull", "remarks"]
        for row, item in enumerate(data):
            for col, key in enumerate(keys):
                value = item.get(key, "")
                if key == "_id":
                    value = str(value)
                elif key == "receivedDate" and value and isinstance(value, datetime.datetime):
                    value = value.strftime("%Y-%m-%d %H:%M:%S")
                self.table.setItem(row, col, QtWidgets.QTableWidgetItem(str(value)))

    def delete_selected_rows(self):
        selected_rows = list(set(index.row() for index in self.table.selectedIndexes()))
        if not selected_rows:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'No rows selected!')
            return

        confirmation = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete the selected rows?',
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirmation == QtWidgets.QMessageBox.Yes:
            client = MongoClient('localhost', 27017)
            db = client['cd_unit']
            collection = db['bundleDetails']

            for row in sorted(selected_rows, reverse=True):
                _id = self.table.item(row, 0).text()
                collection.delete_one({"_id": ObjectId(_id)})
                self.table.removeRow(row)

            QtWidgets.QMessageBox.information(self, 'Success', 'Selected rows deleted successfully!')

    def update_changes(self):
        confirmation = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to save the changes?',
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirmation == QtWidgets.QMessageBox.Yes:
            client = MongoClient('localhost', 27017)
            db = client['cd_unit']
            collection = db['bundleDetails']

            keys = ["_id", "qpSeries", "qpCode", "receivedDate", "messenger", "collegeName", "isNull", "remarks"]
            for row in range(self.table.rowCount()):
                updated_data = {key: self.table.item(row, col).text() for col, key in enumerate(keys)}
                updated_data["_id"] = ObjectId(updated_data["_id"])
                collection.replace_one({"_id": updated_data["_id"]}, updated_data)

            QtWidgets.QMessageBox.information(self, 'Success', 'Changes saved successfully!')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RecentDataWindow()
    window.show()
    sys.exit(app.exec_())
