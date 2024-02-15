# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractScrollArea,QApplication,QScrollArea, QComboBox,QLayout,QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
import icons_rc

class UI_LoginWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 460)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 68, 149);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(120, 70, 120, 80)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(38, 68, 149);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.txt_username = QLineEdit(self.frame_2)
        self.txt_username.setObjectName(u"txt_username")
        self.txt_username.setGeometry(QRect(50, 90, 241, 31))
        self.txt_username.setStyleSheet(u"border-radius:6px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color: rgb(159, 159, 159);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 8pt \"Segoe UI\";")
        self.txt_senha_login = QLineEdit(self.frame_2)
        self.txt_senha_login.setObjectName(u"txt_senha_login")
        self.txt_senha_login.setGeometry(QRect(50, 140, 241, 31))
        self.txt_senha_login.setFocusPolicy(Qt.StrongFocus)
        self.txt_senha_login.setStyleSheet(u"border-radius:6px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color: rgb(159, 159, 159);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 8pt \"Segoe UI\";")
        self.txt_senha_login.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.txt_senha_login.setEchoMode(QLineEdit.Password)
        self.bt_login = QPushButton(self.frame_2)
        self.bt_login.setObjectName(u"bt_login")
        self.bt_login.setGeometry(QRect(120, 210, 101, 31))
        self.bt_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_login.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.checkBox_lembrar_senha = QCheckBox(self.frame_2)
        self.checkBox_lembrar_senha.setObjectName(u"checkBox_lembrar_senha")
        self.checkBox_lembrar_senha.setGeometry(QRect(50, 180, 111, 20))
        self.checkBox_lembrar_senha.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.bt_logo_techtools = QPushButton(self.frame_2)
        self.bt_logo_techtools.setObjectName(u"bt_logo_techtools")
        self.bt_logo_techtools.setGeometry(QRect(10, 10, 321, 61))
        self.bt_logo_techtools.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/icons/image/TECH TOOLS TITULO LOGO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_logo_techtools.setIcon(icon)
        self.bt_logo_techtools.setIconSize(QSize(280, 280))

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.label_dados_tech = QLabel(self.frame_3)
        self.label_dados_tech.setObjectName(u"label_dados_tech")
        self.label_dados_tech.setGeometry(QRect(50, 10, 261, 16))

        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.txt_senha_login.setInputMask("")
        self.txt_senha_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.bt_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.checkBox_lembrar_senha.setText(QCoreApplication.translate("MainWindow", u"Lembrar senha", None))
        self.bt_logo_techtools.setText("")
        self.label_dados_tech.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt; font-weight:700; color:#ffffff;\">Tech Tools v4.0.0 Copyright \u00a9 2023-2024, Eduardo Ferreira.</span></p></body></html>", None))
    # retranslateUi



if __name__ == "__main__":
    app = QApplication([])
    window = UI_LoginWindow()
    window.show()
    app.exec()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(642, 473)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 68, 149);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMaximumSize(QSize(120, 16777215))
        self.left_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.left_frame.setFrameShape(QFrame.Panel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_frame)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 4, 4, 4)
        self.frame_box_buttons = QFrame(self.left_frame)
        self.frame_box_buttons.setObjectName(u"frame_box_buttons")
        self.frame_box_buttons.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_box_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_box_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_box_buttons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame_box_buttons)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setEnabled(True)
        self.toolBox.setCursor(QCursor(Qt.SizeVerCursor))
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:rgb(255,255,255);\n"
"	\n"
"	background-color: rgb(251, 99, 4);\n"
"}")
        self.toolBox.setFrameShape(QFrame.NoFrame)
        self.box_buttons = QWidget()
        self.box_buttons.setObjectName(u"box_buttons")
        self.box_buttons.setGeometry(QRect(0, 0, 93, 367))
        self.verticalLayout_4 = QVBoxLayout(self.box_buttons)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.bt_home = QPushButton(self.box_buttons)
        self.bt_home.setObjectName(u"bt_home")
        self.bt_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_home.setToolTipDuration(0)
        icon = QIcon()
        icon.addFile(u":/icons/image/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_home.setIcon(icon)
        self.bt_home.setIconSize(QSize(45, 45))

        self.verticalLayout_4.addWidget(self.bt_home, 0, Qt.AlignHCenter)

        self.bt_data_base = QPushButton(self.box_buttons)
        self.bt_data_base.setObjectName(u"bt_data_base")
        self.bt_data_base.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/image/data-server.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_data_base.setIcon(icon1)
        self.bt_data_base.setIconSize(QSize(45, 45))

        self.verticalLayout_4.addWidget(self.bt_data_base, 0, Qt.AlignHCenter)

        self.bt_printers = QPushButton(self.box_buttons)
        self.bt_printers.setObjectName(u"bt_printers")
        self.bt_printers.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/image/printer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_printers.setIcon(icon2)
        self.bt_printers.setIconSize(QSize(45, 45))

        self.verticalLayout_4.addWidget(self.bt_printers, 0, Qt.AlignHCenter)

        self.bt_instaladores = QPushButton(self.box_buttons)
        self.bt_instaladores.setObjectName(u"bt_instaladores")
        self.bt_instaladores.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/image/repair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_instaladores.setIcon(icon3)
        self.bt_instaladores.setIconSize(QSize(45, 45))

        self.verticalLayout_4.addWidget(self.bt_instaladores, 0, Qt.AlignHCenter)

        self.bt_scripts = QPushButton(self.box_buttons)
        self.bt_scripts.setObjectName(u"bt_scripts")
        self.bt_scripts.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/image/bracket.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_scripts.setIcon(icon4)
        self.bt_scripts.setIconSize(QSize(45, 45))

        self.verticalLayout_4.addWidget(self.bt_scripts)

        self.bt_executaveis = QPushButton(self.box_buttons)
        self.bt_executaveis.setObjectName(u"bt_executaveis")
        icon5 = QIcon()
        icon5.addFile(u":/icons/image/exe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_executaveis.setIcon(icon5)
        self.bt_executaveis.setIconSize(QSize(45, 45))

        self.verticalLayout_4.addWidget(self.bt_executaveis)

        self.bt_ncm_page = QPushButton(self.box_buttons)
        self.bt_ncm_page.setObjectName(u"bt_ncm_page")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setBold(True)
        self.bt_ncm_page.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/image/lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_ncm_page.setIcon(icon6)
        self.bt_ncm_page.setIconSize(QSize(25, 30))

        self.verticalLayout_4.addWidget(self.bt_ncm_page)

        self.verticalSpacer = QSpacerItem(20, 155, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.box_buttons, icon, u"Home")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 93, 367))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 200, 91, 111))
        self.bt_sobre = QPushButton(self.widget)
        self.bt_sobre.setObjectName(u"bt_sobre")
        self.bt_sobre.setGeometry(QRect(10, 20, 75, 24))
        self.bt_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_termos = QPushButton(self.widget)
        self.bt_termos.setObjectName(u"bt_termos")
        self.bt_termos.setGeometry(QRect(10, 50, 75, 24))
        self.bt_termos.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_users = QPushButton(self.widget)
        self.bt_users.setObjectName(u"bt_users")
        self.bt_users.setGeometry(QRect(10, 310, 75, 24))
        self.bt_users.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolBox.addItem(self.widget, u"Informa\u00e7\u00f5es")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout.addWidget(self.frame_box_buttons)


        self.horizontalLayout.addWidget(self.left_frame)

        self.frame_right = QFrame(self.centralwidget)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setFrameShape(QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.frame_rigth_top = QFrame(self.frame_right)
        self.frame_rigth_top.setObjectName(u"frame_rigth_top")
        self.frame_rigth_top.setGeometry(QRect(10, 0, 481, 60))
        self.frame_rigth_top.setMaximumSize(QSize(16777215, 60))
        self.frame_rigth_top.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:rgb(255,255,255)\n"
"}")
        self.frame_rigth_top.setFrameShape(QFrame.Panel)
        self.frame_rigth_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_rigth_top)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, -1, -1, -1)
        self.btn_tech_tools = QPushButton(self.frame_rigth_top)
        self.btn_tech_tools.setObjectName(u"btn_tech_tools")
        self.btn_tech_tools.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/image/TECH NEW LOGO - BRANCO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tech_tools.setIcon(icon7)
        self.btn_tech_tools.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.btn_tech_tools, 0, Qt.AlignLeft)

        self.frame_pages = QFrame(self.frame_right)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setGeometry(QRect(0, 65, 491, 361))
        self.frame_pages.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_pages.setFocusPolicy(Qt.NoFocus)
        self.frame_pages.setLayoutDirection(Qt.LeftToRight)
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.pages = QStackedWidget(self.frame_right)
        self.pages.setObjectName(u"pages")
        self.pages.setGeometry(QRect(0, 60, 501, 401))
        self.pages.setCursor(QCursor(Qt.PointingHandCursor))
        self.pages.setStyleSheet(u"QStackedWidget{\n"
"	background-color: rgb(3, 51, 100);\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"	color:rgb(255,255,255)\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"	background-color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"")
        self.pages.setFrameShape(QFrame.NoFrame)
        self.pages.setFrameShadow(QFrame.Raised)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.pushButton_4 = QPushButton(self.pg_home)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 10, 451, 371))
        self.pushButton_4.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/image/LOGO BRANCO - TEXTO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon8)
        self.pushButton_4.setIconSize(QSize(400, 500))
        self.pages.addWidget(self.pg_home)
        self.pg_Data_base = QWidget()
        self.pg_Data_base.setObjectName(u"pg_Data_base")
        self.verticalLayout_2 = QVBoxLayout(self.pg_Data_base)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.pg_Data_base)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.title_db = QLabel(self.frame)
        self.title_db.setObjectName(u"title_db")
        self.title_db.setGeometry(QRect(30, 10, 101, 20))
        self.txt_server_db = QLineEdit(self.frame)
        self.txt_server_db.setObjectName(u"txt_server_db")
        self.txt_server_db.setGeometry(QRect(30, 40, 261, 21))
        self.txt_server_db.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.txt_dataBase_db = QLineEdit(self.frame)
        self.txt_dataBase_db.setObjectName(u"txt_dataBase_db")
        self.txt_dataBase_db.setGeometry(QRect(30, 90, 71, 21))
        self.txt_dataBase_db.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.txt_user_db = QLineEdit(self.frame)
        self.txt_user_db.setObjectName(u"txt_user_db")
        self.txt_user_db.setGeometry(QRect(120, 90, 71, 21))
        self.txt_user_db.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.txt_pass_db = QLineEdit(self.frame)
        self.txt_pass_db.setObjectName(u"txt_pass_db")
        self.txt_pass_db.setGeometry(QRect(220, 90, 71, 21))
        self.txt_pass_db.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(38, 68, 149);color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.comboBox_dataBases_db = QComboBox(self.frame)
        self.comboBox_dataBases_db.addItem("")
        self.comboBox_dataBases_db.addItem("")
        self.comboBox_dataBases_db.addItem("")
        self.comboBox_dataBases_db.addItem("")
        self.comboBox_dataBases_db.setObjectName(u"comboBox_dataBases_db")
        self.comboBox_dataBases_db.setGeometry(QRect(310, 40, 91, 22))
        self.comboBox_dataBases_db.setCursor(QCursor(Qt.ArrowCursor))
        self.comboBox_dataBases_db.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.bt_conectar_db = QPushButton(self.frame)
        self.bt_conectar_db.setObjectName(u"bt_conectar_db")
        self.bt_conectar_db.setGeometry(QRect(320, 90, 81, 25))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(9)
        self.bt_conectar_db.setFont(font1)
        self.bt_conectar_db.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_conectar_db.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.txt_server_db_2 = QLineEdit(self.frame)
        self.txt_server_db_2.setObjectName(u"txt_server_db_2")
        self.txt_server_db_2.setEnabled(True)
        self.txt_server_db_2.setGeometry(QRect(30, 140, 261, 21))
        self.txt_server_db_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.bt_conectar_db_2 = QPushButton(self.frame)
        self.bt_conectar_db_2.setObjectName(u"bt_conectar_db_2")
        self.bt_conectar_db_2.setEnabled(True)
        self.bt_conectar_db_2.setGeometry(QRect(320, 140, 81, 25))
        self.bt_conectar_db_2.setFont(font1)
        self.bt_conectar_db_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_conectar_db_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(22, 180, 441, 171))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.plainTextEdit = QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 20, 421, 101))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 0, 111, 16))
        self.bt_conectar_db_3 = QPushButton(self.frame_2)
        self.bt_conectar_db_3.setObjectName(u"bt_conectar_db_3")
        self.bt_conectar_db_3.setGeometry(QRect(10, 140, 81, 25))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        self.bt_conectar_db_3.setFont(font2)
        self.bt_conectar_db_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_conectar_db_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.bt_mostrar_tabelas = QPushButton(self.frame_2)
        self.bt_mostrar_tabelas.setObjectName(u"bt_mostrar_tabelas")
        self.bt_mostrar_tabelas.setGeometry(QRect(110, 140, 111, 24))
        self.bt_mostrar_tabelas.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.bt_conectar_db_4 = QPushButton(self.frame)
        self.bt_conectar_db_4.setObjectName(u"bt_conectar_db_4")
        self.bt_conectar_db_4.setEnabled(True)
        self.bt_conectar_db_4.setGeometry(QRect(320, 130, 81, 61))
        self.bt_conectar_db_4.setFont(font1)
        self.bt_conectar_db_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_conectar_db_4.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(251, 99, 4);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/image/ibExp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_conectar_db_4.setIcon(icon9)
        self.bt_conectar_db_4.setIconSize(QSize(50, 50))
        self.label_conectando = QLabel(self.frame)
        self.label_conectando.setObjectName(u"label_conectando")
        self.label_conectando.setGeometry(QRect(30, 120, 111, 20))
        self.label_conectado = QLabel(self.frame)
        self.label_conectado.setObjectName(u"label_conectado")
        self.label_conectado.setGeometry(QRect(30, 120, 111, 20))
        self.label_servidores = QLabel(self.frame)
        self.label_servidores.setObjectName(u"label_servidores")
        self.label_servidores.setGeometry(QRect(130, 10, 301, 20))
        self.tooltip_sql_server = QLabel(self.frame)
        self.tooltip_sql_server.setObjectName(u"tooltip_sql_server")
        self.tooltip_sql_server.setGeometry(QRect(460, 40, 21, 16))
        self.tooltip_sqlite = QLabel(self.frame)
        self.tooltip_sqlite.setObjectName(u"tooltip_sqlite")
        self.tooltip_sqlite.setGeometry(QRect(460, 150, 21, 16))

        self.verticalLayout_2.addWidget(self.frame)

        self.pages.addWidget(self.pg_Data_base)
        self.pg_show_tables = QWidget()
        self.pg_show_tables.setObjectName(u"pg_show_tables")
        self.verticalLayout_8 = QVBoxLayout(self.pg_show_tables)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_8 = QFrame(self.pg_show_tables)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Panel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_tabelas = QLabel(self.frame_8)
        self.label_tabelas.setObjectName(u"label_tabelas")
        self.label_tabelas.setGeometry(QRect(40, 20, 411, 31))

        self.verticalLayout_8.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.pg_show_tables)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 300))
        self.frame_11.setFrameShape(QFrame.Panel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.tableWidget_show_tables = QTableWidget(self.frame_11)
        if (self.tableWidget_show_tables.columnCount() < 1):
            self.tableWidget_show_tables.setColumnCount(1)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font3 = QFont()
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget_show_tables.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget_show_tables.setObjectName(u"tableWidget_show_tables")
        self.tableWidget_show_tables.setGeometry(QRect(10, 10, 461, 281))
        self.tableWidget_show_tables.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148,148,148);\n"
"	color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:rgb(252,252,252);\n"
"}")
        self.tableWidget_show_tables.setGridStyle(Qt.SolidLine)
        self.tableWidget_show_tables.setColumnCount(1)
        self.tableWidget_show_tables.horizontalHeader().setMinimumSectionSize(460)

        self.verticalLayout_8.addWidget(self.frame_11)

        self.pages.addWidget(self.pg_show_tables)
        self.pg_printers = QWidget()
        self.pg_printers.setObjectName(u"pg_printers")
        self.horizontalLayout_3 = QHBoxLayout(self.pg_printers)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 9, 9, -1)
        self.frame_left_pg3 = QFrame(self.pg_printers)
        self.frame_left_pg3.setObjectName(u"frame_left_pg3")
        self.frame_left_pg3.setMaximumSize(QSize(300, 16777215))
        self.frame_left_pg3.setFrameShape(QFrame.Panel)
        self.frame_left_pg3.setFrameShadow(QFrame.Raised)
        self.table_printers = QTableWidget(self.frame_left_pg3)
        if (self.table_printers.columnCount() < 1):
            self.table_printers.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_printers.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.table_printers.setObjectName(u"table_printers")
        self.table_printers.setGeometry(QRect(10, 10, 221, 351))
        self.table_printers.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148,148,148);\n"
"	color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:rgb(252,252,252);\n"
"}")
        self.table_printers.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_printers.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_printers.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_printers.setAutoScrollMargin(10)
        self.table_printers.horizontalHeader().setMinimumSectionSize(25)
        self.table_printers.horizontalHeader().setDefaultSectionSize(220)
        self.table_printers.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_printers.horizontalHeader().setStretchLastSection(False)
        self.table_printers.verticalHeader().setDefaultSectionSize(24)

        self.horizontalLayout_3.addWidget(self.frame_left_pg3)

        self.frame_right_pg3 = QFrame(self.pg_printers)
        self.frame_right_pg3.setObjectName(u"frame_right_pg3")
        self.frame_right_pg3.setFrameShape(QFrame.StyledPanel)
        self.frame_right_pg3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_right_pg3)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.frame_6 = QFrame(self.frame_right_pg3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(500, 16777215))
        self.frame_6.setLayoutDirection(Qt.LeftToRight)
        self.frame_6.setFrameShape(QFrame.Panel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.txt_nome_printers = QLineEdit(self.frame_6)
        self.txt_nome_printers.setObjectName(u"txt_nome_printers")
        self.txt_nome_printers.setGeometry(QRect(10, 80, 191, 21))
        self.txt_nome_printers.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.txt_link_printers = QLineEdit(self.frame_6)
        self.txt_link_printers.setObjectName(u"txt_link_printers")
        self.txt_link_printers.setGeometry(QRect(10, 110, 191, 21))
        self.txt_link_printers.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.bt_novo_printers = QPushButton(self.frame_6)
        self.bt_novo_printers.setObjectName(u"bt_novo_printers")
        self.bt_novo_printers.setGeometry(QRect(40, 190, 120, 30))
        self.bt_novo_printers.setMinimumSize(QSize(0, 0))
        self.bt_novo_printers.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        self.bt_novo_printers.setFont(font4)
        self.bt_novo_printers.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_novo_printers.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.bt_alterar_printers = QPushButton(self.frame_6)
        self.bt_alterar_printers.setObjectName(u"bt_alterar_printers")
        self.bt_alterar_printers.setGeometry(QRect(40, 230, 120, 30))
        self.bt_alterar_printers.setMinimumSize(QSize(120, 30))
        self.bt_alterar_printers.setMaximumSize(QSize(16777215, 16777215))
        self.bt_alterar_printers.setFont(font4)
        self.bt_alterar_printers.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_alterar_printers.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(251, 99, 4);\n"
"}")
        self.bt_baixar_printers = QPushButton(self.frame_6)
        self.bt_baixar_printers.setObjectName(u"bt_baixar_printers")
        self.bt_baixar_printers.setGeometry(QRect(40, 150, 120, 30))
        self.bt_baixar_printers.setMinimumSize(QSize(120, 30))
        self.bt_baixar_printers.setMaximumSize(QSize(16777215, 16777215))
        self.bt_baixar_printers.setFont(font4)
        self.bt_baixar_printers.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_baixar_printers.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.label_printer = QLabel(self.frame_6)
        self.label_printer.setObjectName(u"label_printer")
        self.label_printer.setGeometry(QRect(20, 10, 181, 16))
        font5 = QFont()
        font5.setFamilies([u"Arial Black"])
        font5.setPointSize(10)
        self.label_printer.setFont(font5)
        self.txt_id_printer = QLineEdit(self.frame_6)
        self.txt_id_printer.setObjectName(u"txt_id_printer")
        self.txt_id_printer.setGeometry(QRect(10, 50, 41, 21))
        self.txt_id_printer.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_5.addWidget(self.frame_6)


        self.horizontalLayout_3.addWidget(self.frame_right_pg3)

        self.pages.addWidget(self.pg_printers)
        self.pg_instaladores = QWidget()
        self.pg_instaladores.setObjectName(u"pg_instaladores")
        self.horizontalLayout_4 = QHBoxLayout(self.pg_instaladores)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.pg_instaladores)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(300, 16777215))
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.table_arquivos = QTableWidget(self.frame_3)
        if (self.table_arquivos.columnCount() < 1):
            self.table_arquivos.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_arquivos.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        self.table_arquivos.setObjectName(u"table_arquivos")
        self.table_arquivos.setGeometry(QRect(10, 10, 251, 351))
        self.table_arquivos.setMaximumSize(QSize(300, 16777215))
        self.table_arquivos.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148,148,148);\n"
"	color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:rgb(252,252,252);\n"
"}")
        self.table_arquivos.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_arquivos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_arquivos.horizontalHeader().setMinimumSectionSize(24)
        self.table_arquivos.horizontalHeader().setDefaultSectionSize(250)
        self.table_arquivos.verticalHeader().setDefaultSectionSize(24)

        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.pg_instaladores)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(210, 16777215))
        self.frame_4.setFrameShape(QFrame.Panel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.bt_novo_arquivo = QPushButton(self.frame_4)
        self.bt_novo_arquivo.setObjectName(u"bt_novo_arquivo")
        self.bt_novo_arquivo.setGeometry(QRect(40, 190, 120, 31))
        self.bt_novo_arquivo.setMinimumSize(QSize(120, 30))
        self.bt_novo_arquivo.setFont(font4)
        self.bt_novo_arquivo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_novo_arquivo.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.label_arquivos = QLabel(self.frame_4)
        self.label_arquivos.setObjectName(u"label_arquivos")
        self.label_arquivos.setGeometry(QRect(20, 20, 181, 16))
        self.label_arquivos.setFont(font5)
        self.txt_nome_arquivo = QLineEdit(self.frame_4)
        self.txt_nome_arquivo.setObjectName(u"txt_nome_arquivo")
        self.txt_nome_arquivo.setGeometry(QRect(10, 80, 191, 21))
        self.txt_nome_arquivo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.bt_baixar_arquivo = QPushButton(self.frame_4)
        self.bt_baixar_arquivo.setObjectName(u"bt_baixar_arquivo")
        self.bt_baixar_arquivo.setGeometry(QRect(40, 150, 120, 30))
        self.bt_baixar_arquivo.setMinimumSize(QSize(120, 30))
        self.bt_baixar_arquivo.setFont(font4)
        self.bt_baixar_arquivo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_baixar_arquivo.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.bt_alter_arquivo = QPushButton(self.frame_4)
        self.bt_alter_arquivo.setObjectName(u"bt_alter_arquivo")
        self.bt_alter_arquivo.setGeometry(QRect(40, 230, 120, 31))
        self.bt_alter_arquivo.setMinimumSize(QSize(120, 30))
        self.bt_alter_arquivo.setFont(font4)
        self.bt_alter_arquivo.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_alter_arquivo.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(251, 99, 4);\n"
"}")
        self.txt_link_arquivo = QLineEdit(self.frame_4)
        self.txt_link_arquivo.setObjectName(u"txt_link_arquivo")
        self.txt_link_arquivo.setGeometry(QRect(10, 110, 191, 21))
        self.txt_link_arquivo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.txt_id_instaler = QLineEdit(self.frame_4)
        self.txt_id_instaler.setObjectName(u"txt_id_instaler")
        self.txt_id_instaler.setGeometry(QRect(10, 50, 41, 21))
        self.txt_id_instaler.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.frame_4)

        self.pages.addWidget(self.pg_instaladores)
        self.pg_scripts = QWidget()
        self.pg_scripts.setObjectName(u"pg_scripts")
        self.verticalLayout_6 = QVBoxLayout(self.pg_scripts)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.pg_scripts)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 30))
        self.frame_5.setFrameShape(QFrame.Panel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.txt_descript_script = QLineEdit(self.frame_5)
        self.txt_descript_script.setObjectName(u"txt_descript_script")
        self.txt_descript_script.setGeometry(QRect(70, 70, 301, 21))
        self.txt_descript_script.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.comboBox_Scripts = QComboBox(self.frame_5)
        self.comboBox_Scripts.setObjectName(u"comboBox_Scripts")
        self.comboBox_Scripts.setGeometry(QRect(20, 30, 351, 22))
        self.comboBox_Scripts.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.bt_new_scripts = QPushButton(self.frame_5)
        self.bt_new_scripts.setObjectName(u"bt_new_scripts")
        self.bt_new_scripts.setGeometry(QRect(390, 30, 75, 24))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(10)
        self.bt_new_scripts.setFont(font6)
        self.bt_new_scripts.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_new_scripts.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.bt_alterar_script = QPushButton(self.frame_5)
        self.bt_alterar_script.setObjectName(u"bt_alterar_script")
        self.bt_alterar_script.setGeometry(QRect(390, 70, 75, 24))
        self.bt_alterar_script.setFont(font6)
        self.bt_alterar_script.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_alterar_script.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(251, 99, 4);\n"
"}")
        self.txt_id_script = QLineEdit(self.frame_5)
        self.txt_id_script.setObjectName(u"txt_id_script")
        self.txt_id_script.setGeometry(QRect(20, 70, 41, 21))
        self.txt_id_script.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.pg_scripts)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 250))
        self.frame_7.setFrameShape(QFrame.Panel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.txt_Scripts = QPlainTextEdit(self.frame_7)
        self.txt_Scripts.setObjectName(u"txt_Scripts")
        self.txt_Scripts.setGeometry(QRect(10, 40, 461, 201))
        self.txt_Scripts.setStyleSheet(u"color: rgb(255, 85, 0);")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 141, 16))
        self.bt_excluirScript = QPushButton(self.frame_7)
        self.bt_excluirScript.setObjectName(u"bt_excluirScript")
        self.bt_excluirScript.setGeometry(QRect(390, 10, 75, 24))
        self.bt_excluirScript.setFont(font6)
        self.bt_excluirScript.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_excluirScript.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(235, 8, 0);\n"
"}")
        self.bt_copiarScripts = QPushButton(self.frame_7)
        self.bt_copiarScripts.setObjectName(u"bt_copiarScripts")
        self.bt_copiarScripts.setGeometry(QRect(300, 10, 75, 24))
        self.bt_copiarScripts.setFont(font6)
        self.bt_copiarScripts.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_copiarScripts.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.label_script_copiado = QLabel(self.frame_7)
        self.label_script_copiado.setObjectName(u"label_script_copiado")
        self.label_script_copiado.setGeometry(QRect(380, 40, 51, 16))
        self.label_script_copiado.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 8pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.frame_7)

        self.pages.addWidget(self.pg_scripts)
        self.pg_Sobre = QWidget()
        self.pg_Sobre.setObjectName(u"pg_Sobre")
        self.label_sobre = QLabel(self.pg_Sobre)
        self.label_sobre.setObjectName(u"label_sobre")
        self.label_sobre.setGeometry(QRect(10, 10, 491, 361))
        sizePolicy.setHeightForWidth(self.label_sobre.sizePolicy().hasHeightForWidth())
        self.label_sobre.setSizePolicy(sizePolicy)
        font7 = QFont()
        font7.setBold(False)
        font7.setItalic(True)
        font7.setUnderline(False)
        font7.setStrikeOut(False)
        font7.setStyleStrategy(QFont.PreferDefault)
        self.label_sobre.setFont(font7)
        self.label_sobre.setFocusPolicy(Qt.NoFocus)
        self.label_sobre.setAcceptDrops(False)
        self.label_sobre.setLayoutDirection(Qt.LeftToRight)
        self.label_sobre.setAutoFillBackground(False)
        self.label_sobre.setFrameShape(QFrame.NoFrame)
        self.label_sobre.setFrameShadow(QFrame.Plain)
        self.label_sobre.setTextFormat(Qt.RichText)
        self.label_sobre.setScaledContents(True)
        self.label_sobre.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_sobre.setWordWrap(True)
        self.label_sobre.setMargin(0)
        self.label_sobre.setIndent(-30)
        self.label_sobre.setOpenExternalLinks(True)
        self.label_sobre.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        # Crie um QScrollArea e defina o QLabel como seu widget filho
        self.scroll_area = QScrollArea(self.pg_Sobre)
        self.scroll_area.setGeometry(10, 10, 491, 361)
        self.scroll_area.setWidget(self.label_sobre)            
        self.pages.addWidget(self.pg_Sobre)
        self.pg_terms = QWidget()
        self.pg_terms.setObjectName(u"pg_terms")
        self.plainTextEdit_3 = QPlainTextEdit(self.pg_terms)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(10, 10, 481, 361))
        font8 = QFont()
        font8.setFamilies([u"MS Shell Dlg 2"])
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setItalic(False)
        self.plainTextEdit_3.setFont(font8)
        self.plainTextEdit_3.setStyleSheet(u"background-color: rgb(38, 68, 149);\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit_3.setReadOnly(True)
        self.pages.addWidget(self.pg_terms)
        self.pg_users = QWidget()
        self.pg_users.setObjectName(u"pg_users")
        self.frame_users = QFrame(self.pg_users)
        self.frame_users.setObjectName(u"frame_users")
        self.frame_users.setGeometry(QRect(10, 10, 481, 371))
        self.frame_users.setFrameShape(QFrame.Panel)
        self.frame_users.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_users)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_9 = QFrame(self.frame_users)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Panel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.txt_id_user_login = QLineEdit(self.frame_9)
        self.txt_id_user_login.setObjectName(u"txt_id_user_login")
        self.txt_id_user_login.setGeometry(QRect(30, 40, 51, 21))
        self.txt_id_user_login.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.txt_user = QLineEdit(self.frame_9)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(30, 80, 201, 21))
        self.txt_user.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.txt_user.setPlaceholderText(u"User")
        self.txt_email_usre = QLineEdit(self.frame_9)
        self.txt_email_usre.setObjectName(u"txt_email_usre")
        self.txt_email_usre.setGeometry(QRect(30, 110, 391, 21))
        self.txt_email_usre.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.bt_alterar_user_login = QPushButton(self.frame_9)
        self.bt_alterar_user_login.setObjectName(u"bt_alterar_user_login")
        self.bt_alterar_user_login.setGeometry(QRect(130, 140, 75, 24))
        self.bt_alterar_user_login.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(251, 99, 4);\n"
"}")
        self.bt_novo_user_login = QPushButton(self.frame_9)
        self.bt_novo_user_login.setObjectName(u"bt_novo_user_login")
        self.bt_novo_user_login.setGeometry(QRect(30, 140, 75, 24))
        self.bt_novo_user_login.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.bt_excluir_user_login = QPushButton(self.frame_9)
        self.bt_excluir_user_login.setObjectName(u"bt_excluir_user_login")
        self.bt_excluir_user_login.setGeometry(QRect(230, 140, 75, 24))
        self.bt_excluir_user_login.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(235, 8, 0);\n"
"}")
        self.txt_senha = QLineEdit(self.frame_9)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(240, 80, 181, 21))
        self.txt_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.radioButton_user = QRadioButton(self.frame_9)
        self.radioButton_user.setObjectName(u"radioButton_user")
        self.radioButton_user.setGeometry(QRect(180, 10, 71, 20))
        self.radioButton_user.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.radioButton_login = QRadioButton(self.frame_9)
        self.radioButton_login.setObjectName(u"radioButton_login")
        self.radioButton_login.setGeometry(QRect(30, 10, 151, 20))
        self.radioButton_login.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.comboBox_tipo = QComboBox(self.frame_9)
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.setObjectName(u"comboBox_tipo")
        self.comboBox_tipo.setGeometry(QRect(100, 40, 131, 22))
        self.comboBox_tipo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.tooltip_login_user = QLabel(self.frame_9)
        self.tooltip_login_user.setObjectName(u"tooltip_login_user")
        self.tooltip_login_user.setGeometry(QRect(440, 10, 16, 16))

        self.verticalLayout_7.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_users)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Panel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.tableWidget_user_login = QTableWidget(self.frame_10)
        self.tableWidget_user_login.setObjectName(u"tableWidget_user_login")
        self.tableWidget_user_login.setGeometry(QRect(10, 10, 441, 151))
        self.tableWidget_user_login.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148,148,148);\n"
"	color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:rgb(252,252,252);\n"
"}")

        self.verticalLayout_7.addWidget(self.frame_10)

        self.pages.addWidget(self.pg_users)
        self.pg_ncm = QWidget()
        self.pg_ncm.setObjectName(u"pg_ncm")
        self.frame_12 = QFrame(self.pg_ncm)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 10, 481, 381))
        self.frame_12.setFrameShape(QFrame.Panel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, -1)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Panel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.txt_ncm = QLineEdit(self.frame_13)
        self.txt_ncm.setObjectName(u"txt_ncm")
        self.txt_ncm.setGeometry(QRect(10, 30, 161, 21))
        self.txt_ncm.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.txt_ncm.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 81, 16))
        self.tooltip_ncm = QLabel(self.frame_13)
        self.tooltip_ncm.setObjectName(u"tooltip_ncm")
        self.tooltip_ncm.setGeometry(QRect(450, 10, 16, 16))

        self.verticalLayout_9.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 300))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.tableWidget_ncm = QTableWidget(self.frame_14)
        if (self.tableWidget_ncm.columnCount() < 3):
            self.tableWidget_ncm.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_ncm.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_ncm.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_ncm.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget_ncm.setObjectName(u"tableWidget_ncm")
        self.tableWidget_ncm.setGeometry(QRect(0, 40, 471, 261))
        self.tableWidget_ncm.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148,148,148);\n"
"	color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:rgb(252,252,252);\n"
"}")
        self.tableWidget_ncm.setFrameShape(QFrame.NoFrame)
        self.tableWidget_ncm.horizontalHeader().setMinimumSectionSize(24)
        self.tableWidget_ncm.horizontalHeader().setDefaultSectionSize(156)
        self.tableWidget_ncm.verticalHeader().setDefaultSectionSize(24)
        self.bt_salvar_ncm = QPushButton(self.frame_14)
        self.bt_salvar_ncm.setObjectName(u"bt_salvar_ncm")
        self.bt_salvar_ncm.setGeometry(QRect(420, 3, 51, 31))
        self.bt_salvar_ncm.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/image/salvar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_salvar_ncm.setIcon(icon10)
        self.bt_salvar_ncm.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.frame_14)

        self.pages.addWidget(self.pg_ncm)
        self.pg_executaveis = QWidget()
        self.pg_executaveis.setObjectName(u"pg_executaveis")
        self.frame_15 = QFrame(self.pg_executaveis)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(10, 10, 481, 381))
        self.frame_15.setFrameShape(QFrame.Panel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.comboBox_executaveis = QComboBox(self.frame_15)
        self.comboBox_executaveis.addItem("")
        icon11 = QIcon()
        icon11.addFile(u":/icons/image/icons8-anydesk-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_executaveis.addItem(icon11, "")
        self.comboBox_executaveis.addItem("")
        self.comboBox_executaveis.addItem("")
        self.comboBox_executaveis.addItem("")
        self.comboBox_executaveis.addItem("")
        self.comboBox_executaveis.addItem("")
        self.comboBox_executaveis.setObjectName(u"comboBox_executaveis")
        self.comboBox_executaveis.setGeometry(QRect(30, 80, 411, 22))
        self.comboBox_executaveis.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.label = QLabel(self.frame_15)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 111, 21))
        self.bt_executar_exe = QPushButton(self.frame_15)
        self.bt_executar_exe.setObjectName(u"bt_executar_exe")
        self.bt_executar_exe.setGeometry(QRect(300, 50, 141, 24))
        self.bt_executar_exe.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}\n"
"")
        self.pages.addWidget(self.pg_executaveis)

        self.horizontalLayout.addWidget(self.frame_right)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(5)
        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.bt_home.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00007f;\">Home</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_home.setText("")
#if QT_CONFIG(tooltip)
        self.bt_data_base.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00007f;\">Data Bases</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_data_base.setText("")
#if QT_CONFIG(tooltip)
        self.bt_printers.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00007f;\">Impressoras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_printers.setText("")
#if QT_CONFIG(tooltip)
        self.bt_instaladores.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00007f;\">Arq. de Instala\u00e7\u00e3o</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_instaladores.setText("")
#if QT_CONFIG(tooltip)
        self.bt_scripts.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00007f;\">Scripts</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_scripts.setText("")
        self.bt_executaveis.setText("")
        self.bt_ncm_page.setText(QCoreApplication.translate("MainWindow", u"NCM", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.box_buttons), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:700;\">vers\u00e3o: 4.0.0</span></p><p align=\"center\"><span style=\" font-size:7pt; font-weight:700;\">Copyright \u00a9 </span></p><p align=\"center\"><span style=\" font-size:7pt; font-weight:700;\">2023-2024</span></p><p align=\"center\"><span style=\" font-size:7pt; font-weight:700;\">TechTools.</span></p></body></html>", None))
        self.bt_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.bt_termos.setText(QCoreApplication.translate("MainWindow", u"Termos", None))
        self.bt_users.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.btn_tech_tools.setText("")
        self.pushButton_4.setText("")
        self.title_db.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Servidores Ativos:</p></body></html>", None))
        self.txt_server_db.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Server\\Instance", None))
        self.txt_dataBase_db.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Base", None))
        self.txt_user_db.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User", None))
        self.txt_pass_db.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.comboBox_dataBases_db.setItemText(0, QCoreApplication.translate("MainWindow", u"SQL Server", None))
        self.comboBox_dataBases_db.setItemText(1, QCoreApplication.translate("MainWindow", u"MySQL", None))
        self.comboBox_dataBases_db.setItemText(2, QCoreApplication.translate("MainWindow", u"SQLite3", None))
        self.comboBox_dataBases_db.setItemText(3, QCoreApplication.translate("MainWindow", u"FireBird", None))

        self.bt_conectar_db.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.txt_server_db_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Caminho para o .db", None))
        self.bt_conectar_db_2.setText(QCoreApplication.translate("MainWindow", u"Buscar .db", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua query aqui.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Consulta SQL", None))
        self.bt_conectar_db_3.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.bt_mostrar_tabelas.setText(QCoreApplication.translate("MainWindow", u"Mostrar tabelas", None))
        self.bt_conectar_db_4.setText("")
        self.label_conectando.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ff5500;\">Conectando ...</span></p></body></html>", None))
        self.label_conectado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#00ff7f;\">Conectado.</span></p></body></html>", None))
        self.label_servidores.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p/></body></html>", None))
#if QT_CONFIG(tooltip)
        self.tooltip_sql_server.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt;\">Forne\u00e7a os dados para a conex\u00e3o em Bd's como SQL Server, MySQL e outros.</span></p><p><span style=\" font-size:7pt; font-weight:700;\">1- Forne\u00e7a os dados do servidor\\inst\u00e2ncia;</span></p><p><span style=\" font-size:7pt; font-weight:700;\">2- Nome do Banco de dados;</span></p><p><span style=\" font-size:7pt; font-weight:700;\">3- Usu\u00e1rio do banco de dados;</span></p><p><span style=\" font-size:7pt; font-weight:700;\">4- Senha do banco de dedos;</span></p><p><span style=\" font-size:7pt; font-weight:700;\">5- Selecione o banco dedados que deseja conectar;</span></p><p><span style=\" font-size:7pt; font-weight:700;\">6- Clique em &quot;CONECTAR&quot;.</span></p><p><span style=\" font-size:7pt;\">Ap\u00f3s \u00e0 conex\u00e3o ser aberta j\u00e1 ser\u00e1 poss\u00edvel realizar consultas, e visualizar </span></p><p><span style=\" font-size:7pt;\">as tabelas do banco.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tooltip_sql_server.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">?</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.tooltip_sqlite.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt;\">Para realizar a </span><span style=\" font-size:7pt; font-weight:700;\">CONEX\u00c3O</span><span style=\" font-size:7pt;\"> com o </span><span style=\" font-size:7pt; font-weight:700;\">SQLite3.</span></p><p><span style=\" font-size:7pt; font-weight:700;\">1- Clique no bot\u00e3o BUSCAR .DB;</span></p><p><span style=\" font-size:7pt; font-weight:700;\">2- Encontre o arquivo do banco de dados desejado;</span></p><p><span style=\" font-size:7pt; font-weight:700;\">3- Ap\u00f3s encontrar o arquivo de banco de dados clique em &quot;CONECTAR&quot;;</span></p><p><span style=\" font-size:7pt;\"> Agora a conex\u00e3o est\u00e1 aberta e poder\u00e1 ver as tabelas do banco de dados clicando em </span><span style=\" font-size:7pt; font-weight:700;\">&quot;MOSTRAR TABELAS&quot;,</span></p><p><span style=\" font-size:7pt;\">ou execute a query desejada.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tooltip_sqlite.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">?</span></p></body></html>", None))
        self.label_tabelas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Tabelas existentes no banco de dados</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget_show_tables.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Tabelas", None));
        ___qtablewidgetitem1 = self.table_printers.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Lista de Impressoras", None));
        self.table_printers.verticalHeader().hide()
        self.txt_nome_printers.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome da Impressora", None))
        self.txt_link_printers.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.bt_novo_printers.setText(QCoreApplication.translate("MainWindow", u"Novo", None))
        self.bt_alterar_printers.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.bt_baixar_printers.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.label_printer.setText(QCoreApplication.translate("MainWindow", u"Impressora selecionada", None))
        self.txt_id_printer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem2 = self.table_arquivos.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Lista de Intaladores", None));
        self.table_arquivos.verticalHeader().hide()
        self.bt_novo_arquivo.setText(QCoreApplication.translate("MainWindow", u"Novo", None))
        self.label_arquivos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Arquivo selecionado</p></body></html>", None))
        self.txt_nome_arquivo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do istalador", None))
        self.bt_baixar_arquivo.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.bt_alter_arquivo.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.txt_link_arquivo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.txt_id_instaler.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.txt_descript_script.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.comboBox_Scripts.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Scripts", None))
        self.bt_new_scripts.setText(QCoreApplication.translate("MainWindow", u"Novo", None))
        self.bt_alterar_script.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.txt_id_script.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Insira ou copie sua query.", None))
        self.bt_excluirScript.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.bt_copiarScripts.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
        self.label_script_copiado.setText(QCoreApplication.translate("MainWindow", u"Copiado!", None))
        self.label_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Como o TechTools surgiu?</span></p><p>O <span style=\" font-weight:700;\">TechTools</span> foi inicialmente projetado para estabelecer conex\u00e3o com o banco de dados SQL Server e executar consultas pr\u00e9-definidas dentro do c\u00f3digo do programa.</p><p>O projeto, inicialmente, visava agilizar o processo de migra\u00e7\u00e3o de dados entre sistemas de gest\u00e3o diferentes. Facilitava a conex\u00e3o e apresentava os dados formatados, economizando tempo para o t\u00e9cnico respons\u00e1vel pela tarefa.</p><p>Com o tempo, o <span style=\" font-weight:700;\">TechTools</span> recebeu novas vers\u00f5es e adquiriu a capacidade de se conectar com outros bancos de dados, como <span style=\" font-weight:700;\">MySQL</span> e <span style=\" font-weight:700;\">SQL Server</span>. Logo, passou a apresentar os dados em uma tela em formato de tabela e a exibir as tabelas existentes no banco de dados, permitindo ao usu\u00e1rio "
                        "conhecer o banco de dados com o qual estava trabalhando. Al\u00e9m disso, recebeu a capacidade de executar consultas mais complexas, como <span style=\" font-weight:700;\">DML</span>, utilizando a linguagem <span style=\" font-weight:700;\">T-SQL</span>.</p><p>Com o decorrer do tempo, percebeu-se a necessidade de o TechTools se tornar a principal ferramenta de trabalho para t\u00e9cnicos de <span style=\" font-weight:700;\">T.I</span>. Assim, ele passou a oferecer uma ampla gama dos principais drivers de impressoras e os principais arquivos de instala\u00e7\u00e3o de programas usados por esses profissionais.</p><p>Atualmente, o TechTools \u00e9 uma ferramenta completa em seu contexto, mas est\u00e1 em constante atualiza\u00e7\u00e3o, com novas ferramentas sendo adicionadas ao programa com o objetivo de melhorar e facilitar os processos realizados por n\u00f3s, profissionais de T.I.</p><p><br/></p><p><span style=\" font-weight:700;\">Tech Tools v4.0.0 Copyright \u00a9 Todos os direitos reservados 2023-2024.</sp"
                        "an></p><p><span style=\" font-weight:700;\">Criador: Eduardo Ferreira</span></p><p><span style=\" font-weight:700;\">Colabora\u00e7\u00e3o: Design de imagens -  by M.R</span></p><p><span style=\" font-weight:700;\">E-mail: eduardoferreira_of@outlook.com</span></p></body></html>", None))
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # Defina a largura da barra de rolagem vertical
        self.scroll_bar = self.scroll_area.verticalScrollBar()
        self.scroll_bar.setStyleSheet("QScrollBar:vertical { width: 8px; }")
        # Defina a política de tamanho do QScrollArea para permitir a rolagem horizontal
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # Permita que o widget filho redimensione a área de visualização
        self.scroll_area.setWidgetResizable(True)
        # Defina a largura da barra de rolagem horizontal
        self.horizontal_scroll_bar = self.scroll_area.horizontalScrollBar()
        self.horizontal_scroll_bar.setStyleSheet("QScrollBar:horizontal { height: 8px; }")          
        
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"TERMOS DE USO DO PROGRAMA TECH TOOLS\n"
"\n"
"\n"
"1. Propriedade Intelectual\n"
"\n"
"O programa Tech Tools \u00e9 um software de c\u00f3digo aberto criado por Eduardo Ferreira (\"Detentor da Propriedade Intelectual\"). O Detentor da Propriedade Intelectual possui todos os direitos de propriedade intelectual relacionados ao Programa.\n"
"\n"
"2. Licen\u00e7a de Uso\n"
"\n"
"O Programa \u00e9 disponibilizado para uso gratuito e \u00e9 licenciado sob a licen\u00e7a GPL para qualquer pessoa que deseje us\u00e1-lo e realizar altera\u00e7\u00f5es no mesmo, conforme os termos e condi\u00e7\u00f5es desta licen\u00e7a.\n"
"\n"
"3. Uso Permitido\n"
"\n"
"3.1. Os usu\u00e1rios est\u00e3o autorizados a usar o Programa para qualquer finalidade, incluindo o uso comercial e n\u00e3o comercial.\n"
"\n"
"3.2. Os usu\u00e1rios t\u00eam permiss\u00e3o para realizar altera\u00e7\u00f5es no Programa, incluindo a implementa\u00e7\u00e3o de novas funcionalidades e modifica\u00e7\u00f5es no c\u00f3digo-fonte.\n"
"\n"
"3.3. Os usu\u00e1"
                        "rios podem compartilhar o Programa, seja em sua forma original ou modificada, com terceiros, desde que os termos desta licen\u00e7a sejam mantidos.\n"
"\n"
"4. Restri\u00e7\u00f5es\n"
"\n"
"4.1. N\u00e3o \u00e9 permitido renomear o Programa, a menos que uma permiss\u00e3o expressa seja concedida pelo Detentor da Propriedade Intelectual.\n"
"\n"
"4.2. Os usu\u00e1rios n\u00e3o est\u00e3o autorizados a reivindicar a propriedade do Programa original ou de suas modifica\u00e7\u00f5es.\n"
"\n"
"5. Responsabilidades e Garantias\n"
"\n"
"5.1. O Programa \u00e9 fornecido \"no estado em que se encontra\", sem garantias de qualquer tipo, expressas ou impl\u00edcitas.\n"
"\n"
"5.2. O Detentor da Propriedade Intelectual n\u00e3o assume qualquer responsabilidade por danos ou problemas causados pelo uso ou modifica\u00e7\u00e3o do Programa.\n"
"\n"
"6. Altera\u00e7\u00f5es dos Termos\n"
"\n"
"O Detentor da Propriedade Intelectual reserva o direito de atualizar ou modificar estes termos de uso a qualquer momento. Os usu\u00e1"
                        "rios ser\u00e3o notificados sobre essas mudan\u00e7as por meio do [reposit\u00f3rio oficial do projeto no GitHub](https://github.com/EduardoFerreira22/Tech_Tools).\n"
"\n"
"7. Aceita\u00e7\u00e3o dos Termos\n"
"\n"
"Ao usar o Programa, voc\u00ea concorda em cumprir estes termos de uso. Se voc\u00ea n\u00e3o concorda com os termos, n\u00e3o use o Programa.\n"
"\n"
"8. Contato\n"
"\n"
"Para entrar em contato com o Detentor da Propriedade Intelectual ou relatar viola\u00e7\u00f5es destes termos, envie um e-mail para  eduardoferreira_of@outlook.com", None))
        self.txt_id_user_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.txt_email_usre.setText("")
        self.txt_email_usre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.bt_alterar_user_login.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.bt_novo_user_login.setText(QCoreApplication.translate("MainWindow", u"Novo", None))
        self.bt_excluir_user_login.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.txt_senha.setText("")
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User ou Email", None))
        self.radioButton_user.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.radioButton_login.setText(QCoreApplication.translate("MainWindow", u"Gerenciador de Login", None))
        self.comboBox_tipo.setItemText(0, QCoreApplication.translate("MainWindow", u"User", None))
        self.comboBox_tipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Super-admin", None))
        self.comboBox_tipo.setItemText(2, "")

        self.comboBox_tipo.setCurrentText("")
        self.comboBox_tipo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User", None))
#if QT_CONFIG(tooltip)
        self.tooltip_login_user.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt;\">Para cadastrar seus logins selecione a op\u00e7\u00e3o &quot;</span><span style=\" font-size:7pt; font-weight:700;\">GERENCIADOR DE LOGIN</span><span style=\" font-size:7pt;\">&quot;,</span></p><p><span style=\" font-size:7pt;\">para cadastrar um novo usu\u00e1rio selecione a op\u00e7\u00e3o</span><span style=\" font-size:7pt; font-weight:700;\"> &quot;USER&quot;</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tooltip_login_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">?</span></p></body></html>", None))
        self.txt_ncm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Formato 0000.00.00", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Buscar NCM:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.tooltip_ncm.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt;\">Digite o </span><span style=\" font-size:7pt; font-weight:700;\">NCM </span><span style=\" font-size:7pt;\">no formato desejado no entry.</span></p><p><span style=\" font-size:7pt;\">Clique no bot\u00e3o salvar para salvar todos os </span><span style=\" font-size:7pt; font-weight:700;\">NCM</span></p><p><span style=\" font-size:7pt;\">em formato </span><span style=\" font-size:7pt; font-weight:700;\">.csv</span><span style=\" font-size:7pt;\">.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tooltip_ncm.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">?</span></p></body></html>", None))
        ___qtablewidgetitem3 = self.tableWidget_ncm.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem4 = self.tableWidget_ncm.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tableWidget_ncm.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None));
        # Esconder a primeira coluna que mostra os números das linhas
        self.tableWidget_ncm.verticalHeader().hide()
        self.tableWidget_ncm.setColumnWidth(0, 80)
        self.tableWidget_ncm.setColumnWidth(1, 300)
#if QT_CONFIG(tooltip)
        self.bt_salvar_ncm.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt;\">Salvar .csv</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_salvar_ncm.setText("")
        self.comboBox_executaveis.setItemText(0, QCoreApplication.translate("MainWindow", u"Advanced_IP_Scanner", None))
        self.comboBox_executaveis.setItemText(1, QCoreApplication.translate("MainWindow", u"AnyDesk", None))
        self.comboBox_executaveis.setItemText(2, QCoreApplication.translate("MainWindow", u"Ativador M\u00e1gico", None))
        self.comboBox_executaveis.setItemText(3, QCoreApplication.translate("MainWindow", u"CrystalDiskInfo", None))
        self.comboBox_executaveis.setItemText(4, QCoreApplication.translate("MainWindow", u"Drives de Rede 3DP", None))
        self.comboBox_executaveis.setItemText(5, QCoreApplication.translate("MainWindow", u"Rufus", None))
        self.comboBox_executaveis.setItemText(6, QCoreApplication.translate("MainWindow", u"WinToHDD_Free", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Execut\u00e1veis</span></p></body></html>", None))
        self.bt_executar_exe.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
    # retranslateUi

