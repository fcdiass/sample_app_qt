# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_person_windowunbwIf.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_d_person(object):
    def setupUi(self, d_person):
        if not d_person.objectName():
            d_person.setObjectName(u"d_person")
        d_person.setWindowModality(Qt.WindowModality.ApplicationModal)
        d_person.resize(465, 187)
        font = QFont()
        font.setPointSize(12)
        d_person.setFont(font)
        self.gridLayout = QGridLayout(d_person)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Submit = QPushButton(d_person)
        self.pb_Submit.setObjectName(u"pb_Submit")

        self.gridLayout.addWidget(self.pb_Submit, 2, 1, 1, 1)

        self.pb_Close = QPushButton(d_person)
        self.pb_Close.setObjectName(u"pb_Close")

        self.gridLayout.addWidget(self.pb_Close, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.gb_Person = QGroupBox(d_person)
        self.gb_Person.setObjectName(u"gb_Person")
        self.gb_Person.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.gb_Person)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.gb_Person)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_FristName = QLineEdit(self.gb_Person)
        self.le_FristName.setObjectName(u"le_FristName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_FristName)

        self.label_2 = QLabel(self.gb_Person)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_LastName = QLineEdit(self.gb_Person)
        self.le_LastName.setObjectName(u"le_LastName")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_LastName)


        self.gridLayout.addWidget(self.gb_Person, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 3)

        self.lb_Message = QLabel(d_person)
        self.lb_Message.setObjectName(u"lb_Message")

        self.gridLayout.addWidget(self.lb_Message, 3, 0, 1, 3)


        self.retranslateUi(d_person)

        QMetaObject.connectSlotsByName(d_person)
    # setupUi

    def retranslateUi(self, d_person):
        d_person.setWindowTitle(QCoreApplication.translate("d_person", u"Sample Application", None))
        self.pb_Submit.setText(QCoreApplication.translate("d_person", u"Submit", None))
        self.pb_Close.setText(QCoreApplication.translate("d_person", u"Close", None))
        self.gb_Person.setTitle(QCoreApplication.translate("d_person", u"Add Person", None))
        self.label.setText(QCoreApplication.translate("d_person", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("d_person", u"Last Name", None))
        self.lb_Message.setText(QCoreApplication.translate("d_person", u"Message", None))
    # retranslateUi

