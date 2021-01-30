import sys
import codecs
from os.path import isdir, join, basename
from json import dump, load
from PySide2.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QWidget, QMessageBox, QFileDialog, \
    QLineEdit, QTextEdit, QComboBox
from PySide2.QtCore import Qt, QSize, Signal, Slot, QModelIndex
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon
from MainWin import Ui_MainWindow
from Coustemer import Ui_Form

main_json_file = 'data.json'


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(['מצב'])
        self.customer_widget = None
        # self.model_view = QAbstractItemView()
        # self.model_view.setSelectionModel().selectionChanged.connect(self.tree_selection_changed)
        self.ui.QTMainTree.clicked.connect(self.tree_selection_changed)
        self.ui.QTMainTree.setModel(self.model)
        with open('data.json', 'rb') as j_file:
            self.main_dic = load(j_file)
        self.setup_tree()
        self.ui_setup()

    def ui_setup(self):
        self.ui.QMNewClient.triggered.connect(self.new_customer)

    def setup_tree(self):
        for name in self.main_dic:
            if name != 'main dir':
                base_name = self.main_dic[name]
                base = QStandardItem(name)
                if 'icon' in base_name:
                    icon = QIcon(base_name['icon'])
                    base.setIcon(icon)
                if 'children' in base_name:
                    for child_dic in base_name['children']:
                        for child in child_dic:
                            child_item = QStandardItem(child)
                            if 'icon' in child_dic[child]:
                                icon = QIcon(child_dic[child]['icon'])
                                child_item.setIcon(icon)
                            base.appendRow(child_item)
                self.model.appendRow(base)

    def save_json(self):
        with codecs.open(main_json_file, 'wb', encoding='utf-8') as f_json:
            dump(self.main_dic, f_json)

    @Slot(QModelIndex)
    def tree_selection_changed(self, item):
        t = self.ui.QTMainTree.selectedIndexes()[0]
        if t.parent().data() is not None:
            for child in self.main_dic[t.parent().data()]['children']:
                if t.data() in child:
                    print(t.data(), child[t.data()])

    @Slot()
    def new_customer(self):
        if self.customer_widget is None or not self.customer_widget.isVisible():
            self.customer_widget = CustomerWidget(main_dir=self.main_dic['main dir'])
            self.customer_widget.setWindowFlags(self.customer_widget.windowFlags() | Qt.Window)
            self.customer_widget.return_dic.connect(self.get_dic)
            self.customer_widget.setWindowModality(Qt.WindowModal)
            # self.customer_widget.setParent(self)
            self.customer_widget.show()
        else:
            msg = QMessageBox.warning(self, 'Look Around', 'יש חלון לקוח פתוח')
            msg.exec_()

    @Slot(dict)
    def get_dic(self, return_dic):
        if return_dic:
            print(return_dic)
        self.customer_widget = None


class CustomerWidget(QWidget):
    return_dic = Signal(dict)

    def __init__(self, parent=None, new=True, main_dir=''):
        super(CustomerWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        if not new:
            self.ui.QBCreate.setText('עדקן')
        self.main_dir = main_dir
        self.ui.QBDir.clicked.connect(self.get_name)
        self.ui.QBCreate.clicked.connect(self.the_end)
        self.ui.QBCancle.clicked.connect(self.the_end)
        self.ui.QLProject_name.textChanged.connect(self.check_dir)
        self.ui.QBClear.clicked.connect(self.clear_forum)
        self.ret_dic = {'name': self.ui.QLProject_name,
                        'client_name': self.ui.QLCoustemer_name,
                        'גוש': self.ui.QLGush,
                        'חלקה': self.ui.QLChelca,
                        'phone': self.ui.QLPhone_number,
                        'address': self.ui.QLAddress,
                        'email': self.ui.QLEmail,
                        'added text': self.ui.QTAddedInfo,
                        'סוג לקוח': self.ui.QCCusType,
                        'סוג פרויקט': self.ui.QCProjType,
                        'סוג נכס': self.ui.QCProject_type}

    def get_name(self):
        dir_dialog = QFileDialog.getExistingDirectory(self, 'תקיית הפרויקט',
                                                      self.main_dir,
                                                      QFileDialog.ShowDirsOnly)
        if dir_dialog:
            self.ui.QLProject_name.setText(basename(dir_dialog))
            self.ui.QLProject_name.setEnabled(False)

    # @Slot()
    def the_end(self):
        who = self.sender()
        if who is self.ui.QBCreate:
            ret_dic = {}
            for name in self.ret_dic:
                val = self.ret_dic[name]
                if isinstance(val, QLineEdit):
                    ret_dic[name] = val.text()
                elif isinstance(val, QTextEdit):
                    ret_dic[name] = val.toPlainText()
                elif isinstance(val, QComboBox):
                    ret_dic[name] = val.currentText()
            self.return_dic.emit(ret_dic)

        else:
            self.return_dic.emit({})
        self.close()

    @Slot()
    def check_dir(self):
        if isdir(join(self.main_dir, self.ui.QLProject_name.text())):
            self.ui.QLProject_name.setStyleSheet('color: red;')
        else:
            self.ui.QLProject_name.setStyleSheet('')

    @Slot()
    def clear_forum(self):
        for name in self.ret_dic:
            val = self.ret_dic[name]
            if isinstance(val, QLineEdit):
                val.setText('')
            elif isinstance(val, QTextEdit):
                val.setText('')
            elif isinstance(val, QComboBox):
                val.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setLayoutDirection(Qt.RightToLeft)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
