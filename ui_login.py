# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(459, 533)
        login.setMinimumSize(QSize(459, 533))
        login.setMaximumSize(QSize(459, 533))
        login.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u"resources/appostman others icons/appostman-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        login.setWindowIcon(icon)
        login.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 200, 341, 301))
        self.frame.setFocusPolicy(Qt.StrongFocus)
        self.frame.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.username_lineEdit = QLineEdit(self.frame)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setGeometry(QRect(40, 30, 261, 31))
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(14)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.username_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.username_lineEdit.setMaxLength(20)
        self.username_lineEdit.setAlignment(Qt.AlignCenter)
        self.password_lineEdit = QLineEdit(self.frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(40, 80, 261, 31))
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.password_lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.password_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password_lineEdit.setMaxLength(20)
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.password_lineEdit.setAlignment(Qt.AlignCenter)
        self.btn_entre = QPushButton(self.frame)
        self.btn_entre.setObjectName(u"btn_entre")
        self.btn_entre.setGeometry(QRect(110, 140, 121, 31))
        font1 = QFont()
        font1.setFamilies([u"Candara"])
        font1.setPointSize(12)
        self.btn_entre.setFont(font1)
        self.btn_entre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entre.setFocusPolicy(Qt.StrongFocus)
        self.btn_entre.setStyleSheet(u"QPushButton{\n"
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
        self.btn_entre.setAutoDefault(True)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 180, 41, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_cadastre = QPushButton(self.frame)
        self.btn_cadastre.setObjectName(u"btn_cadastre")
        self.btn_cadastre.setGeometry(QRect(110, 210, 121, 31))
        self.btn_cadastre.setFont(font1)
        self.btn_cadastre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastre.setFocusPolicy(Qt.StrongFocus)
        self.btn_cadastre.setStyleSheet(u"QPushButton{\n"
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
        self.forget_password_pushButton = QPushButton(self.frame)
        self.forget_password_pushButton.setObjectName(u"forget_password_pushButton")
        self.forget_password_pushButton.setGeometry(QRect(100, 260, 141, 23))
        self.forget_password_pushButton.setFont(font1)
        self.forget_password_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.forget_password_pushButton.setFocusPolicy(Qt.StrongFocus)
        self.forget_password_pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 2);\n"
"color: rgb(212, 170, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 100, 141, 81))
        self.label.setPixmap(QPixmap(u"resources/icon-login-red.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 20, 411, 71))
        font2 = QFont()
        font2.setFamilies([u"Candara"])
        font2.setPointSize(48)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        QWidget.setTabOrder(self.username_lineEdit, self.password_lineEdit)
        QWidget.setTabOrder(self.password_lineEdit, self.btn_entre)
        QWidget.setTabOrder(self.btn_entre, self.btn_cadastre)
        QWidget.setTabOrder(self.btn_cadastre, self.forget_password_pushButton)

        self.retranslateUi(login)

        self.btn_entre.setDefault(False)


        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.username_lineEdit.setText("")
        self.username_lineEdit.setPlaceholderText(QCoreApplication.translate("login", u"USU\u00c1RIO", None))
        self.password_lineEdit.setText("")
        self.password_lineEdit.setPlaceholderText(QCoreApplication.translate("login", u"SENHA", None))
        self.btn_entre.setText(QCoreApplication.translate("login", u"ENTRE", None))
        self.label_3.setText(QCoreApplication.translate("login", u"  OU", None))
        self.btn_cadastre.setText(QCoreApplication.translate("login", u"CADASTRE-SE", None))
        self.forget_password_pushButton.setText(QCoreApplication.translate("login", u" Esqueceu a senha?", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("login", u"APPOSTMAN", None))
    # retranslateUi

