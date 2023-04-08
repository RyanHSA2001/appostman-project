# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign-up.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Signup(object):
    def setupUi(self, cadastro):
        if not cadastro.objectName():
            cadastro.setObjectName(u"cadastro")
        cadastro.resize(409, 483)
        cadastro.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame = QFrame(cadastro)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 70, 271, 371))
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.username_lineEdit = QLineEdit(self.frame)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setGeometry(QRect(30, 60, 211, 31))
        font1 = QFont()
        font1.setFamilies([u"Candara"])
        font1.setPointSize(14)
        self.username_lineEdit.setFont(font1)
        self.username_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.username_lineEdit.setMaxLength(20)
        self.username_lineEdit.setAlignment(Qt.AlignCenter)
        self.email_lineEdit = QLineEdit(self.frame)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setGeometry(QRect(30, 120, 211, 31))
        self.email_lineEdit.setFont(font1)
        self.email_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.email_lineEdit.setMaxLength(50)
        self.email_lineEdit.setAlignment(Qt.AlignCenter)
        self.password_lineEdit = QLineEdit(self.frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(30, 180, 211, 31))
        self.password_lineEdit.setFont(font1)
        self.password_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.password_lineEdit.setMaxLength(20)
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.password_lineEdit.setAlignment(Qt.AlignCenter)
        self.password_repeat_lineEdit = QLineEdit(self.frame)
        self.password_repeat_lineEdit.setObjectName(u"password_repeat_lineEdit")
        self.password_repeat_lineEdit.setGeometry(QRect(30, 240, 211, 31))
        self.password_repeat_lineEdit.setFont(font1)
        self.password_repeat_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.password_repeat_lineEdit.setMaxLength(20)
        self.password_repeat_lineEdit.setEchoMode(QLineEdit.Password)
        self.password_repeat_lineEdit.setAlignment(Qt.AlignCenter)
        self.btn_cadastrar = QPushButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(80, 300, 111, 31))
        font2 = QFont()
        font2.setFamilies([u"Candara"])
        font2.setPointSize(12)
        self.btn_cadastrar.setFont(font2)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(20, 39, 203);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 40, 191, 21))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 100, 71, 21))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 160, 191, 21))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 220, 211, 21))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(cadastro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 30, 131, 31))
        font3 = QFont()
        font3.setFamilies([u"Candara"])
        font3.setPointSize(20)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_return = QPushButton(cadastro)
        self.btn_return.setObjectName(u"btn_return")
        self.btn_return.setGeometry(QRect(10, 450, 75, 23))
        self.btn_return.setFont(font)
        self.btn_return.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(206, 0, 3);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.retranslateUi(cadastro)

        QMetaObject.connectSlotsByName(cadastro)
    # setupUi

    def retranslateUi(self, cadastro):
        cadastro.setWindowTitle(QCoreApplication.translate("cadastro", u"Form", None))
        self.username_lineEdit.setText("")
        self.email_lineEdit.setText("")
        self.password_lineEdit.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("cadastro", u"CADASTRAR", None))
        self.label_2.setText(QCoreApplication.translate("cadastro", u"Nome de usu\u00e1rio", None))
        self.label_3.setText(QCoreApplication.translate("cadastro", u"E-mail", None))
        self.label_4.setText(QCoreApplication.translate("cadastro", u"Senha", None))
        self.label_5.setText(QCoreApplication.translate("cadastro", u"Digite a senha novamente", None))
        self.label.setText(QCoreApplication.translate("cadastro", u"CADASTRO", None))
        self.btn_return.setText(QCoreApplication.translate("cadastro", u"Voltar", None))
    # retranslateUi

