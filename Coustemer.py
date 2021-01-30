# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Coustemer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1163, 427)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/Icons/accessibility_new.svg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(Qt.RightToLeft)
        Form.setLocale(QLocale(QLocale.Hebrew, QLocale.Israel))
        self.verticalLayout_15 = QVBoxLayout(Form)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.QCCusType = QComboBox(Form)
        self.QCCusType.addItem("")
        self.QCCusType.addItem("")
        self.QCCusType.addItem("")
        self.QCCusType.setObjectName(u"QCCusType")

        self.verticalLayout_7.addWidget(self.QCCusType)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_9)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.QCProjType = QComboBox(Form)
        self.QCProjType.addItem("")
        self.QCProjType.addItem("")
        self.QCProjType.addItem("")
        self.QCProjType.setObjectName(u"QCProjType")

        self.verticalLayout_8.addWidget(self.QCProjType)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.QLProject_name = QLineEdit(Form)
        self.QLProject_name.setObjectName(u"QLProject_name")
        self.QLProject_name.setMinimumSize(QSize(400, 0))
        self.QLProject_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.QLProject_name)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.QCProject_type = QComboBox(Form)
        self.QCProject_type.addItem("")
        self.QCProject_type.addItem("")
        self.QCProject_type.addItem("")
        self.QCProject_type.setObjectName(u"QCProject_type")

        self.verticalLayout_6.addWidget(self.QCProject_type)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.QLCoustemer_name = QLineEdit(Form)
        self.QLCoustemer_name.setObjectName(u"QLCoustemer_name")
        self.QLCoustemer_name.setMinimumSize(QSize(200, 0))
        self.QLCoustemer_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.QLCoustemer_name)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.QLGush = QLineEdit(Form)
        self.QLGush.setObjectName(u"QLGush")
        self.QLGush.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.QLGush)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_10)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_10.addWidget(self.label_10)

        self.QLChelca = QLineEdit(Form)
        self.QLChelca.setObjectName(u"QLChelca")
        self.QLChelca.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.QLChelca)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)


        self.verticalLayout_15.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.QLPhone_number = QLineEdit(Form)
        self.QLPhone_number.setObjectName(u"QLPhone_number")
        self.QLPhone_number.setLayoutDirection(Qt.LeftToRight)
        self.QLPhone_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.QLPhone_number)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.QLAddress = QLineEdit(Form)
        self.QLAddress.setObjectName(u"QLAddress")
        self.QLAddress.setMinimumSize(QSize(300, 0))
        self.QLAddress.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.QLAddress)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_13)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_13.addWidget(self.label_13)

        self.QLEmail = QLineEdit(Form)
        self.QLEmail.setObjectName(u"QLEmail")
        self.QLEmail.setMinimumSize(QSize(300, 0))
        self.QLEmail.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.QLEmail)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)


        self.verticalLayout_15.addLayout(self.horizontalLayout_4)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_2)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_14)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_14.addWidget(self.label_14)

        self.QTAddedInfo = QTextEdit(Form)
        self.QTAddedInfo.setObjectName(u"QTAddedInfo")

        self.verticalLayout_14.addWidget(self.QTAddedInfo)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.QBCreate = QPushButton(Form)
        self.QBCreate.setObjectName(u"QBCreate")

        self.horizontalLayout.addWidget(self.QBCreate)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.QBClear = QPushButton(Form)
        self.QBClear.setObjectName(u"QBClear")

        self.horizontalLayout.addWidget(self.QBClear)

        self.QBDir = QPushButton(Form)
        self.QBDir.setObjectName(u"QBDir")

        self.horizontalLayout.addWidget(self.QBDir)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.QBCancle = QPushButton(Form)
        self.QBCancle.setObjectName(u"QBCancle")

        self.horizontalLayout.addWidget(self.QBCancle)


        self.verticalLayout_15.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u05d3\u05e3 \u05dc\u05e7\u05d5\u05d7", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u05e1\u05d5\u05d2 \u05d4\u05dc\u05e7\u05d5\u05d7", None))
        self.QCCusType.setItemText(0, QCoreApplication.translate("Form", u"\u05e4\u05d5\u05d8\u05e0\u05e6\u05d9\u05d0\u05dc", None))
        self.QCCusType.setItemText(1, QCoreApplication.translate("Form", u"\u05d1\u05d1\u05d9\u05e6\u05d5\u05e2", None))
        self.QCCusType.setItemText(2, QCoreApplication.translate("Form", u"\u05d2\u05de\u05d5\u05e8", None))

        self.label_8.setText(QCoreApplication.translate("Form", u"\u05e1\u05d5\u05d2 \u05d4\u05e4\u05e8\u05d5\u05d9\u05e7\u05d8", None))
        self.QCProjType.setItemText(0, QCoreApplication.translate("Form", u"\u05e9\u05d9\u05e4\u05d5\u05e5", None))
        self.QCProjType.setItemText(1, QCoreApplication.translate("Form", u"\u05d1\u05e0\u05d9\u05d9\u05d4 \u05d7\u05d3\u05e9\u05d4", None))
        self.QCProjType.setItemText(2, QCoreApplication.translate("Form", u"\u05e2\u05d9\u05e6\u05d5\u05d1 \u05e4\u05e0\u05d9\u05dd", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"\u05e9\u05dd \u05e4\u05e8\u05d5\u05d9\u05e7\u05d8", None))
#if QT_CONFIG(tooltip)
        self.QLProject_name.setToolTip(QCoreApplication.translate("Form", u"\u05e9\u05dd \u05d4\u05e4\u05e8\u05d5\u05d9\u05e7\u05d8, \u05d6\u05d4 \u05de\u05d4 \u05e9\u05d9\u05d5\u05e4\u05d9\u05e2 \u05d1\u05ea\u05d9\u05d0\u05d5\u05e8 \u05e9\u05dc\u05d5", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"\u05e1\u05d5\u05d2 \u05d4\u05e0\u05db\u05e1", None))
        self.QCProject_type.setItemText(0, QCoreApplication.translate("Form", u"\u05d1\u05d9\u05ea \u05e7\u05e8\u05e7\u05e2", None))
        self.QCProject_type.setItemText(1, QCoreApplication.translate("Form", u"\u05d1\u05d9\u05ea \u05d3\u05d9\u05e8\u05d5\u05ea", None))
        self.QCProject_type.setItemText(2, QCoreApplication.translate("Form", u"\u05e2\u05e1\u05e7", None))

        self.label.setText(QCoreApplication.translate("Form", u"\u05e9\u05dd", None))
#if QT_CONFIG(tooltip)
        self.QLCoustemer_name.setToolTip(QCoreApplication.translate("Form", u"\u05e9\u05dd \u05d5\u05e9\u05dd \u05de\u05e9\u05e4\u05d7\u05d4 \u05e9\u05dc \u05d4\u05dc\u05e7\u05d5\u05d7", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.QLCoustemer_name.setWhatsThis(QCoreApplication.translate("Form", u"\u05e9\u05dd \u05d5\u05e9\u05dd \u05de\u05e9\u05e4\u05d7\u05d4 \u05e9\u05dc \u05d4\u05dc\u05e7\u05d5\u05d7", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("Form", u"\u05d2\u05d5\u05e9", None))
#if QT_CONFIG(tooltip)
        self.QLGush.setToolTip(QCoreApplication.translate("Form", u"\u05de\u05e1\u05e4\u05e8 \u05d2\u05d5\u05e9 \u05d7\u05dc\u05e7\u05d4", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.QLGush.setWhatsThis(QCoreApplication.translate("Form", u"\u05de\u05e1\u05e4\u05e8 \u05d2\u05d5\u05e9 \u05d7\u05dc\u05e7\u05d4", None))
#endif // QT_CONFIG(whatsthis)
        self.label_10.setText(QCoreApplication.translate("Form", u"\u05d7\u05dc\u05e7\u05d4", None))
#if QT_CONFIG(tooltip)
        self.QLChelca.setToolTip(QCoreApplication.translate("Form", u"\u05de\u05e1\u05e4\u05e8 \u05d2\u05d5\u05e9 \u05d7\u05dc\u05e7\u05d4", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.QLChelca.setWhatsThis(QCoreApplication.translate("Form", u"\u05de\u05e1\u05e4\u05e8 \u05d2\u05d5\u05e9 \u05d7\u05dc\u05e7\u05d4", None))
#endif // QT_CONFIG(whatsthis)
        self.label_5.setText(QCoreApplication.translate("Form", u"\u05de\u05e1\u05e4\u05e8 \u05e0\u05d9\u05d9\u05d3", None))
#if QT_CONFIG(whatsthis)
        self.QLPhone_number.setWhatsThis(QCoreApplication.translate("Form", u"\u05de\u05e1\u05e4\u05e8 \u05d8\u05dc\u05e4\u05d5\u05df \u05e9\u05dc \u05d4\u05dc\u05e7\u05d5\u05d7", None))
#endif // QT_CONFIG(whatsthis)
        self.QLPhone_number.setInputMask(QCoreApplication.translate("Form", u"000-0000000", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u05db\u05ea\u05d5\u05d1\u05ea", None))
#if QT_CONFIG(tooltip)
        self.QLAddress.setToolTip(QCoreApplication.translate("Form", u"\u05db\u05ea\u05d5\u05d1\u05ea \u05d4\u05dc\u05e7\u05d5\u05d7", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.QLAddress.setWhatsThis(QCoreApplication.translate("Form", u"\u05db\u05ea\u05d5\u05d1\u05ea \u05d4\u05dc\u05e7\u05d5\u05d7", None))
#endif // QT_CONFIG(whatsthis)
        self.label_13.setText(QCoreApplication.translate("Form", u"\u05d3\u05d5\u05d0\u05e8 \u05d0\u05dc\u05e7\u05d8\u05e8\u05d5\u05e0\u05d9", None))
#if QT_CONFIG(tooltip)
        self.QLEmail.setToolTip(QCoreApplication.translate("Form", u"\u05db\u05ea\u05d5\u05d1\u05ea \u05d4\u05d3\u05d5\u05d0\u05e8 \u05d0\u05dc\u05e7\u05d8\u05e8\u05d5\u05e0\u05d9 \u05e9\u05dc \u05d4\u05dc\u05e7\u05d5\u05d7", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.QLEmail.setWhatsThis(QCoreApplication.translate("Form", u"\u05db\u05ea\u05d5\u05d1\u05ea \u05d4\u05dc\u05e7\u05d5\u05d7", None))
#endif // QT_CONFIG(whatsthis)
        self.label_14.setText(QCoreApplication.translate("Form", u"\u05de\u05d4 \u05e2\u05d5\u05d3 \u05e6\u05e8\u05d9\u05da \u05dc\u05d3\u05e2\u05ea", None))
        self.QBCreate.setText(QCoreApplication.translate("Form", u"\u05e6\u05d5\u05e8", None))
        self.QBClear.setText(QCoreApplication.translate("Form", u"\u05e0\u05e7\u05d4 \u05de\u05e1\u05de\u05da", None))
        self.QBDir.setText(QCoreApplication.translate("Form", u"\u05ea\u05e7\u05d9\u05d9\u05d4 \u05e7\u05d9\u05d9\u05de\u05ea", None))
        self.QBCancle.setText(QCoreApplication.translate("Form", u"\u05d1\u05d9\u05d8\u05d5\u05dc", None))
    # retranslateUi

