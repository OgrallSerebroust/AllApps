from sys import argv, exit
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QStyleFactory
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor
from mainWidget import MainWidgetPart
from insertWindow import InsertWindow


class MainWindowPart(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window_program = InsertWindow()
        menubar = self.menuBar()
        menubar.setStyleSheet("""
            background: rgba(25, 255, 25, 0.43);
            color: #00FF00;
        """)
        file_menu = menubar.addMenu("File")
        close_action = QAction("Exit", self)
        close_action.triggered.connect(qApp.exit)
        file_menu.addAction(close_action)
        action_menu = menubar.addMenu("Actions")
        insert_action = QAction("Insert asset", self)
        insert_action.triggered.connect(self.show_insert_window)
        action_menu.addAction(insert_action)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#000000"))
        self.setPalette(palette)
        self.main_window_part = MainWidgetPart(parent=self)
        self.setCentralWidget(self.main_window_part)
        self.setWindowTitle("MyInvestBag")
        self.setWindowIcon(QIcon("source/img/icon.jpg"))
        self.setFont(QFont("assets/fonts/Oxanium-Medium", 14))
        self.resize(1000, 400)
        with open("source/css/style.css", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())

    def show_insert_window(self):
        self.window_program.show()


if __name__ == "__main__":
    application = QApplication(argv)
    application.setStyle(QStyleFactory.create('Fusion'))
    program = MainWindowPart()
    program.show()
    exit(application.exec_())
