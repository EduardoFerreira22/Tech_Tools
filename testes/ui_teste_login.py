# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste_login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 460)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 68, 149);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bt_atualizacao_login = QPushButton(self.centralwidget)
        self.bt_atualizacao_login.setObjectName(u"bt_atualizacao_login")
        self.bt_atualizacao_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_atualizacao_login.setStyleSheet(u"border:none;\n"
"background-color: rgb(38, 68, 149);\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/image/D_updatin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_atualizacao_login.setIcon(icon)
        self.bt_atualizacao_login.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.bt_atualizacao_login, 0, Qt.AlignRight)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 7pt \"Segoe UI\";")
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
        self.txt_username.setGeometry(QRect(50, 80, 241, 31))
        self.txt_username.setStyleSheet(u"border-radius:6px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color: rgb(159, 159, 159);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 8pt \"Segoe UI\";")
        self.txt_senha_login = QLineEdit(self.frame_2)
        self.txt_senha_login.setObjectName(u"txt_senha_login")
        self.txt_senha_login.setGeometry(QRect(50, 120, 241, 31))
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
        self.bt_login.setGeometry(QRect(120, 190, 101, 31))
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
        self.checkBox_lembrar_senha.setGeometry(QRect(50, 160, 111, 20))
        self.checkBox_lembrar_senha.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.bt_logo_techtools = QPushButton(self.frame_2)
        self.bt_logo_techtools.setObjectName(u"bt_logo_techtools")
        self.bt_logo_techtools.setGeometry(QRect(10, 10, 321, 61))
        self.bt_logo_techtools.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/image/TECH TOOLS TITULO LOGO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_logo_techtools.setIcon(icon1)
        self.bt_logo_techtools.setIconSize(QSize(280, 280))

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 7pt \"Segoe UI\";")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.label_dados_tech = QLabel(self.frame_3)
        self.label_dados_tech.setObjectName(u"label_dados_tech")
        self.label_dados_tech.setGeometry(QRect(40, 0, 51, 20))
        self.lb_login_version = QLabel(self.frame_3)
        self.lb_login_version.setObjectName(u"lb_login_version")
        self.lb_login_version.setGeometry(QRect(90, 0, 31, 21))
        self.lb_login_version_2 = QLabel(self.frame_3)
        self.lb_login_version_2.setObjectName(u"lb_login_version_2")
        self.lb_login_version_2.setGeometry(QRect(120, 0, 191, 21))

        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.bt_atualizacao_login.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt; font-weight:700; color:#ffffff;\">Uma nova vers\u00e3o desse programa est\u00e1 dispon\u00edvel</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_atualizacao_login.setText("")
        self.txt_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.txt_senha_login.setInputMask("")
        self.txt_senha_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.bt_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.checkBox_lembrar_senha.setText(QCoreApplication.translate("MainWindow", u"Lembrar senha", None))
        self.bt_logo_techtools.setText("")
        self.label_dados_tech.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Tech Tools </span></p></body></html>", None))
        self.lb_login_version.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.lb_login_version_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">- Copyright \u00a9 2023-2024, Eduardo Ferreira.</span></p></body></html>", None))
    # retranslateUi

