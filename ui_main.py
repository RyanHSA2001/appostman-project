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
        MainWindow.resize(1152, 785)
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
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line_6 = QFrame(self.frame_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.btn_home = QPushButton(self.frame_2)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy2)
        self.btn_home.setMinimumSize(QSize(222, 50))
        self.btn_home.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setFamilies([u"Candara"])
        font2.setPointSize(16)
        font2.setBold(False)
        self.btn_home.setFont(font2)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 2);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"resources/appostman others icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(33, 33))

        self.verticalLayout_3.addWidget(self.btn_home)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_configurations = QPushButton(self.frame_2)
        self.btn_configurations.setObjectName(u"btn_configurations")
        sizePolicy2.setHeightForWidth(self.btn_configurations.sizePolicy().hasHeightForWidth())
        self.btn_configurations.setSizePolicy(sizePolicy2)
        self.btn_configurations.setMinimumSize(QSize(222, 50))
        self.btn_configurations.setMaximumSize(QSize(16777215, 60))
        self.btn_configurations.setFont(font2)
        self.btn_configurations.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_configurations.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 2);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"resources/appostman others icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_configurations.setIcon(icon1)
        self.btn_configurations.setIconSize(QSize(33, 33))

        self.verticalLayout_3.addWidget(self.btn_configurations)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.btn_recipients = QPushButton(self.frame_2)
        self.btn_recipients.setObjectName(u"btn_recipients")
        sizePolicy2.setHeightForWidth(self.btn_recipients.sizePolicy().hasHeightForWidth())
        self.btn_recipients.setSizePolicy(sizePolicy2)
        self.btn_recipients.setMinimumSize(QSize(222, 50))
        self.btn_recipients.setMaximumSize(QSize(16777215, 60))
        self.btn_recipients.setFont(font2)
        self.btn_recipients.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recipients.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 2);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"resources/appostman others icons/people.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_recipients.setIcon(icon2)
        self.btn_recipients.setIconSize(QSize(33, 33))

        self.verticalLayout_3.addWidget(self.btn_recipients)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.btn_messages = QPushButton(self.frame_2)
        self.btn_messages.setObjectName(u"btn_messages")
        sizePolicy2.setHeightForWidth(self.btn_messages.sizePolicy().hasHeightForWidth())
        self.btn_messages.setSizePolicy(sizePolicy2)
        self.btn_messages.setMinimumSize(QSize(152, 50))
        self.btn_messages.setMaximumSize(QSize(16777215, 60))
        self.btn_messages.setFont(font2)
        self.btn_messages.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_messages.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 2);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"resources/appostman others icons/message.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_messages.setIcon(icon3)
        self.btn_messages.setIconSize(QSize(33, 33))

        self.verticalLayout_3.addWidget(self.btn_messages)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.btn_help = QPushButton(self.frame_2)
        self.btn_help.setObjectName(u"btn_help")
        sizePolicy2.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy2)
        self.btn_help.setMinimumSize(QSize(222, 50))
        self.btn_help.setMaximumSize(QSize(16777215, 60))
        self.btn_help.setFont(font2)
        self.btn_help.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_help.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 2);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"resources/appostman others icons/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon4)
        self.btn_help.setIconSize(QSize(33, 33))

        self.verticalLayout_3.addWidget(self.btn_help)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.btn_about = QPushButton(self.frame_2)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(222, 50))
        self.btn_about.setMaximumSize(QSize(222, 50))
        font3 = QFont()
        font3.setFamilies([u"Candara"])
        font3.setPointSize(16)
        self.btn_about.setFont(font3)
        self.btn_about.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 2);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"resources/appostman others icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon5)
        self.btn_about.setIconSize(QSize(33, 33))

        self.verticalLayout_3.addWidget(self.btn_about)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.line_5 = QFrame(self.frame_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(98, 182, 255);")

        self.verticalLayout_3.addWidget(self.label_6, 0, Qt.AlignBottom)


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
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy3)
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle.setStyleSheet(u"background-color: rgba(0, 0, 0, 2);")
        icon6 = QIcon()
        icon6.addFile(u"resources/menu-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon6)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_page_title = QLabel(self.top_frame)
        self.label_page_title.setObjectName(u"label_page_title")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_page_title.sizePolicy().hasHeightForWidth())
        self.label_page_title.setSizePolicy(sizePolicy4)
        self.label_page_title.setMinimumSize(QSize(100, 0))
        self.label_page_title.setMaximumSize(QSize(100, 55))
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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1128, 640))
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
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.verticalLayout_15 = QVBoxLayout(self.page_about)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6 = QScrollArea(self.page_about)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 878, 640))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_7 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_7)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_15.addWidget(self.scrollArea_6)

        self.pages.addWidget(self.page_about)
        self.page_configurations = QWidget()
        self.page_configurations.setObjectName(u"page_configurations")
        self.verticalLayout_4 = QVBoxLayout(self.page_configurations)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.page_configurations)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 878, 640))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea_2)

        self.pages.addWidget(self.page_configurations)
        self.page_recipients = QWidget()
        self.page_recipients.setObjectName(u"page_recipients")
        self.verticalLayout_9 = QVBoxLayout(self.page_recipients)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.page_recipients)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 878, 640))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_9.addWidget(self.scrollArea_3)

        self.pages.addWidget(self.page_recipients)
        self.page_messages = QWidget()
        self.page_messages.setObjectName(u"page_messages")
        self.verticalLayout_11 = QVBoxLayout(self.page_messages)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.page_messages)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 878, 640))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.label_4)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_11.addWidget(self.scrollArea_4)

        self.pages.addWidget(self.page_messages)
        self.page_help = QWidget()
        self.page_help.setObjectName(u"page_help")
        self.verticalLayout_13 = QVBoxLayout(self.page_help)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.page_help)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 878, 640))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_5 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_5)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_13.addWidget(self.scrollArea_5)

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
        QWidget.setTabOrder(self.btn_home, self.btn_configurations)
        QWidget.setTabOrder(self.btn_configurations, self.btn_recipients)
        QWidget.setTabOrder(self.btn_recipients, self.btn_messages)
        QWidget.setTabOrder(self.btn_messages, self.btn_help)
        QWidget.setTabOrder(self.btn_help, self.btn_about)
        QWidget.setTabOrder(self.btn_about, self.btn_toggle)
        QWidget.setTabOrder(self.btn_toggle, self.scrollArea_6)
        QWidget.setTabOrder(self.scrollArea_6, self.scrollArea_4)
        QWidget.setTabOrder(self.scrollArea_4, self.scrollArea_5)
        QWidget.setTabOrder(self.scrollArea_5, self.scrollArea_2)
        QWidget.setTabOrder(self.scrollArea_2, self.scrollArea_3)
        QWidget.setTabOrder(self.scrollArea_3, self.scrollArea)

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
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Vers\u00e3o 1.0/2023</span></p></body></html>", None))
        self.btn_toggle.setText("")
        self.label_page_title.setText("")
        self.label_tempo_funcionamento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Tempo de funcionamento: 0</span></p></body></html>", None))
        self.label_emails_enviados.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">E-mails Enviados: 0</span></p></body></html>", None))
        self.label_emails_respondidos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">E-mails Respondidos: 0</span></p></body></html>", None))
        self.label_erros_no_envio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Erros no Envio: 0</span></p></body></html>", None))
        self.label_destinatarios_cadastrados.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Destinat\u00e1rios Cadastrados: 0</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Sobre</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Configura\u00e7\u00f5es</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Destinat\u00e1rios</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Mensagens</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Ajuda</span></p></body></html>", None))
        self.label_botton.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Para solucionar d\u00favidas: suporte@appostman.com.br</span></p></body></html>", None))
    # retranslateUi

