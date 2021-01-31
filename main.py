import sys
import codecs
from os.path import isdir, join, basename
from json import dump, load
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QFileDialog, \
    QLineEdit, QTextEdit, QComboBox, QShortcut
from PySide2.QtCore import Qt, Signal, Slot, QModelIndex
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon, QKeySequence
from MainWin import Ui_MainWindow
from Coustemer import Ui_Form

main_json_file = 'data.json'

dic_translator = {'name': 'name',
                  'client_name': 'Client Name',
                  'גוש': 'גוש',
                  'חלקה': 'חלקה',
                  'phone': 'Phone Number',
                  'address': 'Address',
                  'email': 'Email',
                  'added text': 'Additional Text',
                  'סוג לקוח': 'Customer Type',
                  'סוג פרויקט': 'Project Type',
                  'סוג נכס': 'Project Type'}


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(['מצב'])
        self.customer_widget = None
        self.previous_dict = []
        self.previous_location = -1
        self.set_shortcut = QShortcut(QKeySequence("Ctrl+Z"), self)
        self.set_shortcut.activated.connect(self.backup)
        # self.model_view = QAbstractItemView()
        # self.model_view.setSelectionModel().selectionChanged.connect(self.tree_selection_changed)
        self.ui.QTMainTree.pressed.connect(self.tree_selection_changed)
        self.ui.QTMainTree.setModel(self.model)
        with open(main_json_file, 'rb') as j_file:
            self.main_dic = load(j_file)
        self.ui.QBSave.clicked.connect(self.save_json)
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
                            child_item.setFlags(
                                Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                            base.appendRow(child_item)
                self.model.appendRow(base)

    def add_to_tree(self, new_val):
        for i in range(self.model.rowCount()):
            base = self.model.item(i)
            if base.text() == new_val['סוג לקוח']:
                child_item = QStandardItem(new_val['name'])
                if 'icon' in new_val:
                    icon = QIcon(new_val['icon'])
                    child_item.setIcon(icon)
                child_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                base.appendRow(child_item)
                break

    @Slot()
    def save_json(self):
        with codecs.open(main_json_file, 'wb', encoding='utf-8') as f_json:
            dump(self.main_dic, f_json)

    @Slot(QModelIndex)
    def tree_selection_changed(self, item):
        t = self.ui.QTMainTree.selectedIndexes()[0]
        parent = t.parent().data()
        if parent is not None:
            for child in self.main_dic[parent]['children']:
                if t.data() in child:
                    print(t.data(), child[t.data()])
                # else:  # Name changed
                #     print(t.data(), t.column(), parent)
                #     print(item.data())

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
            print(self.main_dic.keys())
            return_dic["icon"] = ":/Icons/perm_data_setting.svg"
            # output = {return_dic['name']: {}}
            # for name, or_name in dic_translator.items():
            #     output[return_dic['name']][name] = return_dic[or_name]
            # self.main_dic[return_dic['סוג לקוח']]['children'].append(output)
            self.previous_dict.append(self.copy())
            self.previous_location += 1
            self.main_dic[return_dic['סוג לקוח']]['children'].append({return_dic['name']: {name: return_dic[or_name] for or_name, name in dic_translator.items()}})

            self.add_to_tree(return_dic)
        self.customer_widget = None

    @Slot()
    def backup(self):
        print('backup')

class CustomerWidget(QWidget):
    return_dic = Signal(dict)
    is_there = Signal(str)

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
