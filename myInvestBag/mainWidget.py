from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from pyqtgraph import TableWidget
from settings import get_db_name


class MainWidgetPart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        data_from_db = self.get_data_from_db(False)
        self.table_of_investment = TableWidget()
        self.table_of_investment.setData(data_from_db)
        self.table_of_investment.setHorizontalHeaderLabels(self.get_data_from_db(True))
        self.table_of_investment.verticalHeader().hide()
        self.table_of_investment.horizontalHeader().setStyleSheet("""
            color: #00FF00;
            background: rgba(25, 255, 25, 0.43);
        """)
        self.table_of_investment.resizeColumnsToContents()
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.table_of_investment)
        vbox_1 = QVBoxLayout()
        vbox_1.addLayout(hbox_1)
        self.setLayout(vbox_1)

    def get_data_from_db(self, headers):
        data_array, headers_array = [], []
        rows = get_db_name()["investmentCollection"].find()
        for row in rows:
            if headers:
                for header in row:
                    headers_array.append(header)
                headers_array.append("assetFullPrice")
                return headers_array
            else:
                row_array = list(row.values())
                row_array.append(str(self.make_calculations(row)))
                data_array.append(row_array)
        return data_array

    @staticmethod
    def make_calculations(array_for_calc):
        asset_full_price = float(array_for_calc["unitPriceRate"]) * float(array_for_calc["numberOfUnits"])
        return asset_full_price

    def update_table_data(self):
        self.table_of_investment.setHorizontalHeaderLabels(self.get_data_from_db(True))
        self.table_of_investment.setData(self.get_data_from_db(False))
