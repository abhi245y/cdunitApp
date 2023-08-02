from PyQt5 import QtWidgets, QtGui
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from addBundlesUI import Ui_AddBundleDetails
from dbGUI import App as DbGUI
from dbGUI2 import RecentDataWindow
import time

class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C.D Unit App")
        self.resize(500, 200)
        icon = QIcon()
        icon.addFile(u"data/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.initUI()

    def initUI(self):
        central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        
        add_bundles_btn = QtWidgets.QPushButton('Add Bundles')
        add_bundles_btn.clicked.connect(self.launchAddBundlesUI)
        layout.addWidget(add_bundles_btn)

        view_db_btn = QtWidgets.QPushButton('View Database')
        view_db_btn.clicked.connect(self.launchDbGUI)
        layout.addWidget(view_db_btn)

        modify_db_btn = QtWidgets.QPushButton('Modify Database')
        modify_db_btn.clicked.connect(self.launchDbGUI2)
        layout.addWidget(modify_db_btn)

        central_widget.setLayout(layout)
        

        self.setCentralWidget(central_widget)
       

    def launchAddBundlesUI(self):
        self.add_bundle_window = QtWidgets.QMainWindow()
        self.add_bundle_ui = Ui_AddBundleDetails()
        self.add_bundle_ui.setupUi(self.add_bundle_window)
        self.add_bundle_window.show()

    def launchDbGUI(self): 
        self.db_gui_window = DbGUI()
        self.db_gui_window.show()

    def launchDbGUI2(self):
        self.db_gui2_window = RecentDataWindow()
        self.db_gui2_window.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    # Create and display the splash screen
    splash_pix = QtGui.QPixmap(u"data/splash.png")  # Path to your image
    splash = QtWidgets.QSplashScreen(splash_pix)
    splash.show()

    # Simulate some initialization work (e.g., loading resources, connecting to databases)
    # time.sleep(2)  # Show the splash screen for 2 seconds - adjust as needed

    # Create and display the main application window
    main_ui = MainUI()
    main_ui.show()

    # Close the splash screen
    splash.finish(main_ui)
    
    sys.exit(app.exec_())
