import sys
from re import search
from PySide2.QtCore import QAbstractTableModel, Qt
from PySide2.QtWidgets import QMainWindow, QTableView, QApplication
from PySide2.QtGui import QColor
from datetime import datetime


def isHebrew(text):
    if search('[\u0590-\u05FF]', text):
        return True
    else:
        return False

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def flags(self, index):
        value = self._data[index.row()][index.column()]
        fl = Qt.ItemIsEnabled | Qt.ItemIsSelectable
        if isinstance(value, bool):
            fl |= Qt.ItemIsUserCheckable
        else:
            fl |= Qt.ItemIsEditable
        return fl

    def data(self, index, role):
        value = self._data[index.row()][index.column()]
        if role == Qt.DisplayRole:
            if isinstance(value, bool):
                return Qt.Checked if value else Qt.Unchecked
            if isinstance(value, float):
                return f'{value:.2f}'
            if isinstance(value, int):
                return f'{value:d}'
            if isinstance(value, datetime):
                return value.strftime('%Y-%m-%d')

            return value

        if role == Qt.BackgroundRole:
            if (isinstance(value, int) or isinstance(value, float)) and value < 0:
                return QColor

        if role == Qt.TextAlignmentRole:
            if isinstance(value, str) and isHebrew(value):
                return Qt.AlignRight
            return Qt.AlignLeft

        # if role == Qt.BackgroundRole:
        #     return QColor()

    def setData(self, index, value, role):
        value = self._data[index.row()][index.column()]
        row = index.row()
        col = index.column()


    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QTableView()

        data = [
          ['Hello', True, 2],
          [1, 0, 0],
          [3, -5, 'שלום'],
          [True, 3, -2],
          [7, 8, datetime(2021, 1, 28)],
        ]
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()
