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

class Ui_signup(object):
    def setupUi(self, signup):
        if not signup.objectName():
            signup.setObjectName(u"signup")
        signup.resize(459, 420)
        signup.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u"resources/appostman others icons/appostman-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        signup.setWindowIcon(icon)
        signup.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame = QFrame(signup)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 70, 401, 281))
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFocusPolicy(Qt.StrongFocus)
        self.frame.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.username_lineEdit = QLineEdit(self.frame)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setGeometry(QRect(40, 30, 321, 31))
        font1 = QFont()
        font1.setFamilies([u"Candara"])
        font1.setPointSize(14)
        self.username_lineEdit.setFont(font1)
        self.username_lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.username_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.username_lineEdit.setMaxLength(20)
        self.username_lineEdit.setAlignment(Qt.AlignCenter)
        self.email_lineEdit = QLineEdit(self.frame)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setGeometry(QRect(40, 80, 321, 31))
        self.email_lineEdit.setFont(font1)
        self.email_lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.email_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.email_lineEdit.setMaxLength(50)
        self.email_lineEdit.setAlignment(Qt.AlignCenter)
        self.password_lineEdit = QLineEdit(self.frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(40, 130, 321, 31))
        self.password_lineEdit.setFont(font1)
        self.password_lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.password_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.password_lineEdit.setMaxLength(20)
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.password_lineEdit.setAlignment(Qt.AlignCenter)
        self.password_repeat_lineEdit = QLineEdit(self.frame)
        self.password_repeat_lineEdit.setObjectName(u"password_repeat_lineEdit")
        self.password_repeat_lineEdit.setGeometry(QRect(40, 180, 321, 31))
        self.password_repeat_lineEdit.setFont(font1)
        self.password_repeat_lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.password_repeat_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.password_repeat_lineEdit.setMaxLength(20)
        self.password_repeat_lineEdit.setEchoMode(QLineEdit.Password)
        self.password_repeat_lineEdit.setAlignment(Qt.AlignCenter)
        self.btn_cadastrar = QPushButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(140, 230, 121, 31))
        font2 = QFont()
        font2.setFamilies([u"Candara"])
        font2.setPointSize(12)
        self.btn_cadastrar.setFont(font2)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setFocusPolicy(Qt.StrongFocus)
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
        self.label = QLabel(signup)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 131, 31))
        font3 = QFont()
        font3.setFamilies([u"Candara"])
        font3.setPointSize(20)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_return = QPushButton(signup)
        self.btn_return.setObjectName(u"btn_return")
        self.btn_return.setGeometry(QRect(20, 370, 81, 31))
        self.btn_return.setFont(font)
        self.btn_return.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_return.setFocusPolicy(Qt.StrongFocus)
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
        QWidget.setTabOrder(self.frame, self.username_lineEdit)
        QWidget.setTabOrder(self.username_lineEdit, self.email_lineEdit)
        QWidget.setTabOrder(self.email_lineEdit, self.password_lineEdit)
        QWidget.setTabOrder(self.password_lineEdit, self.password_repeat_lineEdit)
        QWidget.setTabOrder(self.password_repeat_lineEdit, self.btn_cadastrar)
        QWidget.setTabOrder(self.btn_cadastrar, self.btn_return)

        self.retranslateUi(signup)

        QMetaObject.connectSlotsByName(signup)
    # setupUi

    def retranslateUi(self, signup):
        signup.setWindowTitle(QCoreApplication.translate("signup", u"Form", None))
        self.username_lineEdit.setText("")
        self.username_lineEdit.setPlaceholderText(QCoreApplication.translate("signup", u"NOME DE USU\u00c1RIO", None))
        self.email_lineEdit.setText("")
        self.email_lineEdit.setPlaceholderText(QCoreApplication.translate("signup", u"E-MAIL", None))
        self.password_lineEdit.setText("")
        self.password_lineEdit.setPlaceholderText(QCoreApplication.translate("signup", u"SENHA", None))
        self.password_repeat_lineEdit.setPlaceholderText(QCoreApplication.translate("signup", u"DIGITE A SENHA NOVAMENTE", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("signup", u"CADASTRAR", None))
        self.label.setText(QCoreApplication.translate("signup", u"CADASTRO", None))
        self.btn_return.setText(QCoreApplication.translate("signup", u"Voltar", None))
    # retranslateUi

