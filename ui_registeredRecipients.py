# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registered_recipients.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QLabel, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_RegisteredRecipients(object):
    def setupUi(self, RegisteredRecipients):
        if not RegisteredRecipients.objectName():
            RegisteredRecipients.setObjectName(u"RegisteredRecipients")
        RegisteredRecipients.resize(830, 730)
        icon = QIcon()
        icon.addFile(u"resources/appostman others icons/appostman-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        RegisteredRecipients.setWindowIcon(icon)
        RegisteredRecipients.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.verticalLayout = QVBoxLayout(RegisteredRecipients)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(RegisteredRecipients)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.registered_recipients = QLabel(self.frame)
        self.registered_recipients.setObjectName(u"registered_recipients")
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.registered_recipients.setFont(font)
        self.registered_recipients.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.registered_recipients)

        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableView\n"
"{\n"
"	background-color: rgb(48, 48, 48);\n"
"}\n"
"\n"
"QTableView::Corner\n"
"{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(48, 48, 48);\n"
"    width: 18px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(20, 20, 20);\n"
"    min-height: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {    \n"
"    background-color: rgb(170, 170, 170);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:ver"
                        "tical:hover {    \n"
"    background-color: rgb(49, 49, 49);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(132, 132, 132);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* ARROW - SCROLLBAR */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    \n"
"	\n"
"	background-color: rgb(84, 84, 84);\n"
"    height: 15px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-r"
                        "adius: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical:hover, QScrollBar::down-arrow:vertical:hover {    \n"
"    \n"
"	background-color: rgb(170, 170, 170);\n"
"}\n"
"QScrollBar::up-arrow:vertical:pressed, QScrollBar::down-arrow:vertical:pressed {    \n"
"    background-color: rgb(132, 132, 132);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(48, 48, 48);\n"
"    height: 18px;\n"
"    margin: 0 15px 0 15px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* HANDLE BAR HORIZONTAL */\n"
"QScrollBar::handle:horizontal {    \n"
"    background-color: rgb(20, 20, 20);\n"
"    min-width: 30px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {    \n"
"    background-color: rgb(170, 170, 170);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {    \n"
"    background-color: rgb("
                        "20, 20, 20);\n"
"}\n"
"\n"
"/* BTN LEFT - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    width: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {    \n"
"    background-color: rgb(49, 49, 49);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN RIGHT - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(132, 132, 132);\n"
"    width: 15px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {    \n"
"    background-color: rgb"
                        "(185, 0, 92);\n"
"}\n"
"\n"
"/* ARROW - SCROLLBAR */\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: none;\n"
"    \n"
"    background-color: rgb(84, 84, 84);\n"
"    width: 15px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal:hover, QScrollBar::right-arrow:horizontal:hover {    \n"
"    background-color: rgb(170, 170, 170);\n"
"}\n"
"QScrollBar::left-arrow:horizontal:pressed, QScrollBar::right-arrow:horizontal:pressed {    \n"
"    background-color: rgb(132, 132, 132);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}")
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.NoPen)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(RegisteredRecipients)

        QMetaObject.connectSlotsByName(RegisteredRecipients)
    # setupUi

    def retranslateUi(self, RegisteredRecipients):
        RegisteredRecipients.setWindowTitle(QCoreApplication.translate("RegisteredRecipients", u"Form", None))
        self.registered_recipients.setText(QCoreApplication.translate("RegisteredRecipients", u"Destinat\u00e1rios cadastrados:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("RegisteredRecipients", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("RegisteredRecipients", u"E-mail", None));
    # retranslateUi

