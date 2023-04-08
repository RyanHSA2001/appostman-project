# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'verification-code.ui'
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

class Ui_VerificationCode(object):
    def setupUi(self, verificationCode):
        if not verificationCode.objectName():
            verificationCode.setObjectName(u"verificationCode")
        verificationCode.resize(400, 246)
        verificationCode.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame = QFrame(verificationCode)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 60, 301, 171))
        self.frame.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 10, 211, 21))
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.code_lineEdit = QLineEdit(self.frame)
        self.code_lineEdit.setObjectName(u"code_lineEdit")
        self.code_lineEdit.setGeometry(QRect(70, 50, 161, 31))
        font1 = QFont()
        font1.setFamilies([u"Candara"])
        font1.setPointSize(14)
        self.code_lineEdit.setFont(font1)
        self.code_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.code_lineEdit.setInputMethodHints(Qt.ImhNone)
        self.code_lineEdit.setMaxLength(10)
        self.code_lineEdit.setAlignment(Qt.AlignCenter)
        self.btn_resend = QPushButton(self.frame)
        self.btn_resend.setObjectName(u"btn_resend")
        self.btn_resend.setGeometry(QRect(50, 140, 201, 23))
        self.btn_resend.setStyleSheet(u"QPushButton{\n"
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
        self.btn_verify = QPushButton(self.frame)
        self.btn_verify.setObjectName(u"btn_verify")
        self.btn_verify.setGeometry(QRect(100, 100, 101, 31))
        self.btn_verify.setStyleSheet(u"QPushButton{\n"
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
        self.label = QLabel(verificationCode)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 341, 21))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(verificationCode)

        QMetaObject.connectSlotsByName(verificationCode)
    # setupUi

    def retranslateUi(self, verificationCode):
        verificationCode.setWindowTitle(QCoreApplication.translate("verificationCode", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("verificationCode", u"Digite o c\u00f3digo de verifica\u00e7\u00e3o", None))
        self.btn_resend.setText(QCoreApplication.translate("verificationCode", u"N\u00e3o recebeu o c\u00f3digo de verifica\u00e7\u00e3o?", None))
        self.btn_verify.setText(QCoreApplication.translate("verificationCode", u"Verificar", None))
        self.label.setText(QCoreApplication.translate("verificationCode", u"Um c\u00f3digo de verifica\u00e7\u00e3o foi enviado ao seu e-mail", None))
    # retranslateUi

