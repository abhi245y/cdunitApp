from PyQt5 import QtWidgets, QtGui
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from addBundlesUI import Ui_AddBundleDetails
from dbGUI2 import RecentDataWindow
import distro
import os
import json

filename = "db_config.json"

with open(filename, "r") as f:
    db_config = json.load(f)
    QT_QPA_PLATFORM_ENABLED = db_config["QT_QPA_PLATFORM"]

if QT_QPA_PLATFORM_ENABLED is True:
    if distro.info()["id"] == "ubuntu" and distro.info()["version"] == "22.04":
        os.environ["QT_QPA_PLATFORM"] = "xcb"


class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C.D Unit App")
        self.resize(500, 200)
        icon = QIcon()
        icon.addFile("data/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.initUI()

    def initUI(self):
        central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        add_bundles_btn = QtWidgets.QPushButton("Add Bundles")
        add_bundles_btn.clicked.connect(self.launchAddBundlesUI)
        layout.addWidget(add_bundles_btn)

        modify_db_btn = QtWidgets.QPushButton("View and Modify Database")
        modify_db_btn.clicked.connect(self.launchDbGUI2)
        layout.addWidget(modify_db_btn)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def launchAddBundlesUI(self):
        self.add_bundle_window = QtWidgets.QMainWindow()
        self.add_bundle_ui = Ui_AddBundleDetails()
        self.add_bundle_ui.setupUi(self.add_bundle_window)
        self.add_bundle_window.show()

    def launchDbGUI2(self):
        self.db_gui2_window = RecentDataWindow()
        self.db_gui2_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    splash_pix = QtGui.QPixmap("data/splash.png")
    splash = QtWidgets.QSplashScreen(splash_pix)
    splash.show()

    main_ui = MainUI()
    main_ui.show()

    splash.finish(main_ui)

    sys.exit(app.exec_())
