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

class Ui_Login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(409, 483)
        Form.setMinimumSize(QSize(409, 483))
        Form.setMaximumSize(QSize(409, 483))
        Form.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 190, 271, 261))
        self.frame.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.username_lineEdit = QLineEdit(self.frame)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setGeometry(QRect(30, 20, 211, 31))
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(14)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.username_lineEdit.setMaxLength(20)
        self.username_lineEdit.setAlignment(Qt.AlignCenter)
        self.password_lineEdit = QLineEdit(self.frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(30, 60, 211, 31))
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.password_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password_lineEdit.setMaxLength(20)
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.password_lineEdit.setAlignment(Qt.AlignCenter)
        self.btn_entre = QPushButton(self.frame)
        self.btn_entre.setObjectName(u"btn_entre")
        self.btn_entre.setGeometry(QRect(80, 110, 111, 31))
        font1 = QFont()
        font1.setFamilies([u"Candara"])
        font1.setPointSize(12)
        self.btn_entre.setFont(font1)
        self.btn_entre.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.label_3.setGeometry(QRect(120, 150, 31, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_cadastre = QPushButton(self.frame)
        self.btn_cadastre.setObjectName(u"btn_cadastre")
        self.btn_cadastre.setGeometry(QRect(80, 180, 111, 31))
        self.btn_cadastre.setFont(font1)
        self.btn_cadastre.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.forget_password_pushButton.setGeometry(QRect(80, 230, 111, 23))
        font2 = QFont()
        font2.setFamilies([u"Candara"])
        font2.setPointSize(10)
        self.forget_password_pushButton.setFont(font2)
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
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 110, 111, 61))
        self.label.setPixmap(QPixmap(u"resources/icon-login-red.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 20, 361, 71))
        font3 = QFont()
        font3.setFamilies([u"Candara"])
        font3.setPointSize(48)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        QWidget.setTabOrder(self.username_lineEdit, self.password_lineEdit)
        QWidget.setTabOrder(self.password_lineEdit, self.btn_entre)
        QWidget.setTabOrder(self.btn_entre, self.btn_cadastre)
        QWidget.setTabOrder(self.btn_cadastre, self.forget_password_pushButton)

        self.retranslateUi(Form)

        self.btn_entre.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.username_lineEdit.setText("")
        self.username_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Usu\u00e1rio", None))
        self.password_lineEdit.setText("")
        self.password_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Senha", None))
        self.btn_entre.setText(QCoreApplication.translate("Form", u"ENTRE", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"OU", None))
        self.btn_cadastre.setText(QCoreApplication.translate("Form", u"CADASTRE-SE", None))
        self.forget_password_pushButton.setText(QCoreApplication.translate("Form", u"Esqueceu a senha?", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"APPOSTMAN", None))
    # retranslateUi

