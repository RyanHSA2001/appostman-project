# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forget-password.ui'
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

class Ui_forgetpassword(object):
    def setupUi(self, forgetpassword):
        if not forgetpassword.objectName():
            forgetpassword.setObjectName(u"forgetpassword")
        forgetpassword.resize(409, 346)
        forgetpassword.setMinimumSize(QSize(409, 346))
        forgetpassword.setMaximumSize(QSize(409, 346))
        forgetpassword.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame = QFrame(forgetpassword)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 20, 271, 301))
        self.frame.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.password_lineEdit = QLineEdit(self.frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(30, 110, 211, 31))
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(14)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password_lineEdit.setMaxLength(20)
        self.repeat_password_lineEdit = QLineEdit(self.frame)
        self.repeat_password_lineEdit.setObjectName(u"repeat_password_lineEdit")
        self.repeat_password_lineEdit.setGeometry(QRect(30, 180, 211, 31))
        self.repeat_password_lineEdit.setFont(font)
        self.repeat_password_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.repeat_password_lineEdit.setMaxLength(20)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 90, 101, 21))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 160, 211, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 240, 111, 31))
        font1 = QFont()
        font1.setFamilies([u"Candara"])
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.email_lineEdit = QLineEdit(self.frame)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setGeometry(QRect(30, 40, 211, 31))
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.email_lineEdit.setMaxLength(50)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 20, 141, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(forgetpassword)

        QMetaObject.connectSlotsByName(forgetpassword)
    # setupUi

    def retranslateUi(self, forgetpassword):
        forgetpassword.setWindowTitle(QCoreApplication.translate("forgetpassword", u"Form", None))
        self.label.setText(QCoreApplication.translate("forgetpassword", u"Nova senha", None))
        self.label_2.setText(QCoreApplication.translate("forgetpassword", u"Digite a senha novamente", None))
        self.pushButton.setText(QCoreApplication.translate("forgetpassword", u"REDEFINIR", None))
        self.label_3.setText(QCoreApplication.translate("forgetpassword", u"E-mail cadastrado", None))
    # retranslateUi

