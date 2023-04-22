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
        forgetpassword.resize(459, 332)
        forgetpassword.setFocusPolicy(Qt.NoFocus)
        forgetpassword.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frame = QFrame(forgetpassword)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 70, 401, 231))
        self.frame.setFocusPolicy(Qt.StrongFocus)
        self.frame.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.password_lineEdit = QLineEdit(self.frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(40, 70, 321, 31))
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(14)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.password_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password_lineEdit.setMaxLength(20)
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.password_lineEdit.setAlignment(Qt.AlignCenter)
        self.repeat_password_lineEdit = QLineEdit(self.frame)
        self.repeat_password_lineEdit.setObjectName(u"repeat_password_lineEdit")
        self.repeat_password_lineEdit.setGeometry(QRect(40, 120, 321, 31))
        self.repeat_password_lineEdit.setFont(font)
        self.repeat_password_lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.repeat_password_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.repeat_password_lineEdit.setMaxLength(20)
        self.repeat_password_lineEdit.setEchoMode(QLineEdit.Password)
        self.repeat_password_lineEdit.setAlignment(Qt.AlignCenter)
        self.btn_redefine = QPushButton(self.frame)
        self.btn_redefine.setObjectName(u"btn_redefine")
        self.btn_redefine.setGeometry(QRect(140, 180, 121, 31))
        font1 = QFont()
        font1.setFamilies([u"Candara"])
        font1.setPointSize(12)
        self.btn_redefine.setFont(font1)
        self.btn_redefine.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_redefine.setFocusPolicy(Qt.StrongFocus)
        self.btn_redefine.setStyleSheet(u"QPushButton{\n"
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
        self.email_lineEdit.setGeometry(QRect(40, 20, 321, 31))
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.email_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.email_lineEdit.setMaxLength(50)
        self.email_lineEdit.setAlignment(Qt.AlignCenter)
        self.label = QLabel(forgetpassword)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 291, 31))
        font2 = QFont()
        font2.setFamilies([u"Candara"])
        font2.setPointSize(20)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        QWidget.setTabOrder(self.frame, self.email_lineEdit)
        QWidget.setTabOrder(self.email_lineEdit, self.password_lineEdit)
        QWidget.setTabOrder(self.password_lineEdit, self.repeat_password_lineEdit)
        QWidget.setTabOrder(self.repeat_password_lineEdit, self.btn_redefine)

        self.retranslateUi(forgetpassword)

        QMetaObject.connectSlotsByName(forgetpassword)
    # setupUi

    def retranslateUi(self, forgetpassword):
        forgetpassword.setWindowTitle(QCoreApplication.translate("forgetpassword", u"Form", None))
        self.password_lineEdit.setPlaceholderText(QCoreApplication.translate("forgetpassword", u"NOVA SENHA", None))
        self.repeat_password_lineEdit.setPlaceholderText(QCoreApplication.translate("forgetpassword", u"DIGITE A SENHA NOVAMENTE", None))
        self.btn_redefine.setText(QCoreApplication.translate("forgetpassword", u"REDEFINIR", None))
        self.email_lineEdit.setPlaceholderText(QCoreApplication.translate("forgetpassword", u"E-MAIL CADASTRADO", None))
        self.label.setText(QCoreApplication.translate("forgetpassword", u"REDEFINI\u00c7\u00c3O DE SENHA", None))
    # retranslateUi

