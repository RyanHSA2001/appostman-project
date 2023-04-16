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

class Ui_verificationCode(object):
    def setupUi(self, verificationCode):
        if not verificationCode.objectName():
            verificationCode.setObjectName(u"verificationCode")
        verificationCode.resize(459, 235)
        verificationCode.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame = QFrame(verificationCode)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 60, 401, 151))
        self.frame.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.code_lineEdit = QLineEdit(self.frame)
        self.code_lineEdit.setObjectName(u"code_lineEdit")
        self.code_lineEdit.setGeometry(QRect(40, 20, 321, 31))
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(14)
        self.code_lineEdit.setFont(font)
        self.code_lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.code_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.code_lineEdit.setInputMethodHints(Qt.ImhNone)
        self.code_lineEdit.setMaxLength(10)
        self.code_lineEdit.setAlignment(Qt.AlignCenter)
        self.btn_resend = QPushButton(self.frame)
        self.btn_resend.setObjectName(u"btn_resend")
        self.btn_resend.setGeometry(QRect(70, 120, 261, 23))
        font1 = QFont()
        font1.setFamilies([u"Candara"])
        font1.setPointSize(12)
        self.btn_resend.setFont(font1)
        self.btn_resend.setFocusPolicy(Qt.ClickFocus)
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
        self.btn_verify.setGeometry(QRect(150, 70, 101, 31))
        self.btn_verify.setFont(font1)
        self.btn_verify.setFocusPolicy(Qt.ClickFocus)
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
        self.label.setGeometry(QRect(30, 20, 421, 21))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(verificationCode)

        QMetaObject.connectSlotsByName(verificationCode)
    # setupUi

    def retranslateUi(self, verificationCode):
        verificationCode.setWindowTitle(QCoreApplication.translate("verificationCode", u"Form", None))
        self.code_lineEdit.setPlaceholderText(QCoreApplication.translate("verificationCode", u"C\u00d3DIGO DE VERIFICA\u00c7\u00c3O", None))
        self.btn_resend.setText(QCoreApplication.translate("verificationCode", u"N\u00e3o recebeu o c\u00f3digo de verifica\u00e7\u00e3o?", None))
        self.btn_verify.setText(QCoreApplication.translate("verificationCode", u"VERIFICAR", None))
        self.label.setText(QCoreApplication.translate("verificationCode", u"Um c\u00f3digo de verifica\u00e7\u00e3o foi enviado ao seu e-mail!", None))
    # retranslateUi

