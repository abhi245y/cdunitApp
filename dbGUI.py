import sys
from pymongo import MongoClient
from PyQt5 import QtWidgets
from datetime import datetime
import datetime
from PyQt5.QtGui import  QIcon
from PyQt5.QtCore import QSize

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Database")
        icon = QIcon()
        icon.addFile(u"data/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        # Connect to MongoDB
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['cd_unit']
        self.collection = self.db['bundleDetails']

        # Layout for the search and sort controls
        controls_layout = QtWidgets.QHBoxLayout()

        # Search input
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setPlaceholderText('Search by qpCode, Messenger, or College Name')
        controls_layout.addWidget(self.search_input)

        # Sort by dropdown
        self.sort_combo = QtWidgets.QComboBox()
        self.sort_combo.addItem('Sort by...', '')
        self.sort_combo.addItem('qpCode', 'qpCode')
        self.sort_combo.addItem('Received Date', 'receivedDate')
        self.sort_combo.addItem('Messenger', 'messenger')
        self.sort_combo.addItem('College Name', 'collegeName')
        controls_layout.addWidget(self.sort_combo)

        # Search button
        search_button = QtWidgets.QPushButton('Search')
        search_button.clicked.connect(self.update_cards)
        controls_layout.addWidget(search_button)

        # Scroll area
        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)

        # Main window layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(controls_layout)
        layout.addWidget(self.scroll)

        # Set window properties
        self.resize(600, 800)

        # Load initial cards
        self.update_cards()

        self.show()

    def update_cards(self):
        # Retrieve search and sort parameters
        search_text = self.search_input.text().strip()
        sort_by = self.sort_combo.currentData()

        # Query MongoDB based on search and sort criteria
        query = {
            '$or': [
                {'qpCode': {'$regex': search_text, '$options': 'i'}},
                {'messenger': {'$regex': search_text, '$options': 'i'}},
                {'collegeName': {'$regex': search_text, '$options': 'i'}}
            ]
        } if search_text else {}

        cursor = self.collection.find(query)

        if sort_by:
            sort_order = [(sort_by, 1)]
            cursor.sort(sort_order)

        documents = list(cursor)

        # ... rest of the method ...


        # Scroll content
        scroll_content = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout(scroll_content)
        main_layout.setSpacing(20)

        # Card styling
        card_style = '''
            QWidget {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 15px;
                margin: 5px;
            }
        '''

        # Iterate through documents and create a card for each
        for document in documents:
            card_layout = QtWidgets.QVBoxLayout()
            card_widget = QtWidgets.QWidget()
            card_widget.setStyleSheet(card_style)

            if document['receivedDate'] and isinstance(document['receivedDate'], datetime.datetime):
                receivedDate = document['receivedDate'].strftime("%Y-%m-%d %H:%M:%S")
            else:
                receivedDate =document['receivedDate']

            card_layout.addWidget(QtWidgets.QLabel(f"Series: {document['qpSeries']}"))
            card_layout.addWidget(QtWidgets.QLabel(f"Code: {document['qpCode']}"))
            card_layout.addWidget(QtWidgets.QLabel(f"Received Date: {receivedDate}"))
            card_layout.addWidget(QtWidgets.QLabel(f"Messenger: {document['messenger']}"))
            card_layout.addWidget(QtWidgets.QLabel(f"College Name: {document['collegeName']}"))

            card_widget.setLayout(card_layout)
            main_layout.addWidget(card_widget)

        # Set scroll content layout
        scroll_content.setLayout(main_layout)

        # Add scroll content to scroll area
        self.scroll.setWidget(scroll_content)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
