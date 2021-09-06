from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt
from requests import get
from settings import insert_document


class InsertWindow(QWidget):
    def __init__(self):
        super(InsertWindow, self).__init__()
        asset_label = QLabel("Asset: ", self)
        self.asset_edit_line = QLineEdit()
        unit_price_label = QLabel("Unit price: ", self)
        self.unit_price_edit_line = QLineEdit()
        units_number_label = QLabel("Units count: ", self)
        self.units_number_edit_line = QLineEdit()
        invested_label = QLabel("Invested: ", self)
        self.invested_edit_line = QLineEdit()
        button_ok = QPushButton("Insert", self)
        button_ok.clicked.connect(self.insert_data_to_database)
        button_cancel = QPushButton("Cancel", self)
        button_cancel.clicked.connect(self.close_window)
        form_layout = QFormLayout()
        form_layout.addRow(asset_label, self.asset_edit_line)
        form_layout.addRow(unit_price_label, self.unit_price_edit_line)
        form_layout.addRow(units_number_label, self.units_number_edit_line)
        form_layout.addRow(invested_label, self.invested_edit_line)
        hbox_1 = QHBoxLayout()
        hbox_1.addLayout(form_layout)
        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(button_ok)
        hbox_2.addWidget(button_cancel)
        vbox_1 = QVBoxLayout()
        vbox_1.addLayout(hbox_1)
        vbox_1.addLayout(hbox_2)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#000000"))
        self.setPalette(palette)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setLayout(vbox_1)
        self.setFont(QFont("assets/fonts/Oxanium-Medium", 14))
        with open("source/css/style.css", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())

    def close_window(self):
        self.close()

    def insert_data_to_database(self):
        if self.asset_edit_line.text() == "ETH":
            resp = get("https://www.rbc.ru/crypto/ajax/values/?id=320915&_=1630589855773")
            eth_unit_price = (resp.json()["320915"]["closevalue"])
            data = {
                "asset": "ETH",
                "unitPrice": self.unit_price_edit_line.text(),
                "numberOfUnits": self.units_number_edit_line.text(),
                "invested": self.invested_edit_line.text(),
                "unitPriceRate": str(eth_unit_price)
            }
            insert_document(data)
        self.close_window()

