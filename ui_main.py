# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1075, 742)
        MainWindow.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"\n"
"border none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_container.sizePolicy().hasHeightForWidth())
        self.left_container.setSizePolicy(sizePolicy)
        self.left_container.setMinimumSize(QSize(0, 0))
        self.left_container.setMaximumSize(QSize(0, 16777215))
        self.left_container.setStyleSheet(u"background-color: rgb(75, 75, 75);\n"
"")
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 5, 3, 5)
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(98, 182, 255);")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Candara"])
        font1.setPointSize(14)
        self.frame_2.setFont(font1)
        self.frame_2.setStyleSheet(u"background-color: rgb(75, 75, 75);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line_6 = QFrame(self.frame_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.btn_home = QPushButton(self.frame_2)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(152, 50))
        font2 = QFont()
        font2.setFamilies([u"Candara"])
        font2.setPointSize(16)
        font2.setBold(False)
        self.btn_home.setFont(font2)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 53, 161);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:2px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_configurations = QPushButton(self.frame_2)
        self.btn_configurations.setObjectName(u"btn_configurations")
        self.btn_configurations.setMinimumSize(QSize(152, 50))
        self.btn_configurations.setFont(font2)
        self.btn_configurations.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_configurations.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 53, 161);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:2px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_configurations)

        self.btn_recipients = QPushButton(self.frame_2)
        self.btn_recipients.setObjectName(u"btn_recipients")
        self.btn_recipients.setMinimumSize(QSize(152, 50))
        self.btn_recipients.setFont(font2)
        self.btn_recipients.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recipients.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 53, 161);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:2px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_recipients)

        self.btn_messages = QPushButton(self.frame_2)
        self.btn_messages.setObjectName(u"btn_messages")
        self.btn_messages.setMinimumSize(QSize(152, 50))
        self.btn_messages.setFont(font2)
        self.btn_messages.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_messages.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 53, 161);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:2px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_messages)

        self.btn_help = QPushButton(self.frame_2)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(152, 50))
        self.btn_help.setFont(font2)
        self.btn_help.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_help.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 53, 161);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:2px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_help)

        self.line_5 = QFrame(self.frame_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy2)
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle.setStyleSheet(u"background-color: rgba(0, 0, 0, 2);")
        icon = QIcon()
        icon.addFile(u"resources/menu-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_page_title = QLabel(self.top_frame)
        self.label_page_title.setObjectName(u"label_page_title")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_page_title.sizePolicy().hasHeightForWidth())
        self.label_page_title.setSizePolicy(sizePolicy3)
        self.label_page_title.setMinimumSize(QSize(100, 0))
        self.label_page_title.setMaximumSize(QSize(100, 55))
        font3 = QFont()
        font3.setFamilies([u"Candara"])
        font3.setPointSize(16)
        self.label_page_title.setFont(font3)
        self.label_page_title.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_page_title.setPixmap(QPixmap(u"resources/icon-login-blue.png"))
        self.label_page_title.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_page_title)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy1.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy1)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pages = QStackedWidget(self.main_frame)
        self.pages.setObjectName(u"pages")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_6 = QVBoxLayout(self.page_home)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_home)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(127, 127, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1051, 597))
        self.scrollAreaWidgetContents_3.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setKerning(True)
        self.scrollAreaWidgetContents_3.setFont(font4)
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_tempo_funcionamento = QLabel(self.scrollAreaWidgetContents_3)
        self.label_tempo_funcionamento.setObjectName(u"label_tempo_funcionamento")
        font5 = QFont()
        font5.setFamilies([u"Candara"])
        self.label_tempo_funcionamento.setFont(font5)
        self.label_tempo_funcionamento.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_tempo_funcionamento)

        self.line = QFrame(self.scrollAreaWidgetContents_3)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: rgb(114, 140, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.label_emails_enviados = QLabel(self.scrollAreaWidgetContents_3)
        self.label_emails_enviados.setObjectName(u"label_emails_enviados")
        self.label_emails_enviados.setFont(font5)
        self.label_emails_enviados.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_emails_enviados)

        self.line_2 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.label_emails_respondidos = QLabel(self.scrollAreaWidgetContents_3)
        self.label_emails_respondidos.setObjectName(u"label_emails_respondidos")
        self.label_emails_respondidos.setFont(font5)
        self.label_emails_respondidos.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_emails_respondidos)

        self.line_3 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_3)

        self.label_erros_no_envio = QLabel(self.scrollAreaWidgetContents_3)
        self.label_erros_no_envio.setObjectName(u"label_erros_no_envio")
        self.label_erros_no_envio.setFont(font5)
        self.label_erros_no_envio.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_erros_no_envio)

        self.line_4 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_4)

        self.label_destinatarios_cadastrados = QLabel(self.scrollAreaWidgetContents_3)
        self.label_destinatarios_cadastrados.setObjectName(u"label_destinatarios_cadastrados")
        self.label_destinatarios_cadastrados.setFont(font5)
        self.label_destinatarios_cadastrados.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_destinatarios_cadastrados)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.pages.addWidget(self.page_home)
        self.page_configurations = QWidget()
        self.page_configurations.setObjectName(u"page_configurations")
        self.pages.addWidget(self.page_configurations)
        self.page_recipients = QWidget()
        self.page_recipients.setObjectName(u"page_recipients")
        self.pages.addWidget(self.page_recipients)
        self.page_messages = QWidget()
        self.page_messages.setObjectName(u"page_messages")
        self.pages.addWidget(self.page_messages)
        self.page_help = QWidget()
        self.page_help.setObjectName(u"page_help")
        self.pages.addWidget(self.page_help)

        self.verticalLayout_5.addWidget(self.pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.botton_frame = QFrame(self.main_container)
        self.botton_frame.setObjectName(u"botton_frame")
        self.botton_frame.setFrameShape(QFrame.StyledPanel)
        self.botton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.botton_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_botton = QLabel(self.botton_frame)
        self.label_botton.setObjectName(u"label_botton")
        self.label_botton.setStyleSheet(u"color: rgb(98, 182, 255);")
        self.label_botton.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_botton)


        self.verticalLayout.addWidget(self.botton_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">APPOSTMAN</p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.btn_configurations.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.btn_recipients.setText(QCoreApplication.translate("MainWindow", u"Destinat\u00e1rios", None))
        self.btn_messages.setText(QCoreApplication.translate("MainWindow", u"Mensagens", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.btn_toggle.setText("")
        self.label_page_title.setText("")
        self.label_tempo_funcionamento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Tempo de funcionamento:</span></p></body></html>", None))
        self.label_emails_enviados.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">E-mails Enviados:</span></p></body></html>", None))
        self.label_emails_respondidos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">E-mails Respondidos:</span></p></body></html>", None))
        self.label_erros_no_envio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Erros no Envio:</span></p></body></html>", None))
        self.label_destinatarios_cadastrados.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Destinat\u00e1rios Cadastrados:</span></p></body></html>", None))
        self.label_botton.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Para solucionar d\u00favidas: suporte@appostman.com.br</span></p></body></html>", None))
    # retranslateUi

