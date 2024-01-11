import pymongo
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QMovie
import os


os.environ["QT_QPA_PLATFORM"] = "xcb"
        
    
class ConnectionUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Database Connection")
        self.setGeometry(400, 200, 300, 200)
        

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()

        # # Loading animation
        # self.loading_animation_label = QLabel(self)
        # self.loading_movie = QMovie("./loading.gif")
        # self.loading_animation_label.setMovie(self.loading_movie)

        # Create a label for the rotating loading animation
        self.loading_animation_label = QLabel(self)
        self.loading_animation_label.setAlignment(Qt.AlignCenter)
        self.loading_animation_label.setFixedSize(QSize(640, 640))  # Set fixed size for the QLabel

        self.loading_movie = QMovie("./loading.gif")
        self.loading_animation_label.setMovie(self.loading_movie)
        self.loading_movie.start()

        layout.addWidget(self.loading_animation_label)

        # Retry button
        self.retry_button = QPushButton("Retry", self)
        self.retry_button.clicked.connect(self.establish_connection)
        self.retry_button.hide()

        layout.addWidget(self.loading_animation_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.retry_button)

        central_widget.setLayout(layout)

        self.establish_connection()

    def establish_connection(self):
        try:
            address = "10.20.9.3"  # Replace with your server address
            client = pymongo.MongoClient("mongodb://{}/".format(address))
            cdUnitDB = client["cd_unit"]
            # If you reach here, connection is successful
            self.set_status("Connected")
        except:
            # If there's an exception, connection failed
            self.set_status("Failed to Connect")

    def set_status(self, status):
        if status == "Failed to Connect":
            self.loading_movie.stop()
            self.loading_animation_label.hide()
            self.retry_button.show()
        elif status == "Connected":
            self.loading_movie.stop()
            self.loading_animation_label.hide()
            # Close this window and open your main application window
            self.close()
        else:
            self.loading_movie.start()
            self.loading_animation_label.show()

if __name__ == "__main__":
    app = QApplication([])
    window = ConnectionUI()
    window.show()
    app.exec_()
