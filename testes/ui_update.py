# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Update.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Updating(object):
    def setupUi(self, Updating):
        if not Updating.objectName():
            Updating.setObjectName(u"Updating")
        Updating.resize(423, 180)
        Updating.setStyleSheet(u"background-color: rgb(38, 68, 149);")
        self.centralwidget = QWidget(Updating)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_version = QLabel(self.frame_2)
        self.lb_version.setObjectName(u"lb_version")

        self.gridLayout.addWidget(self.lb_version, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.bt_sim = QPushButton(self.frame_3)
        self.bt_sim.setObjectName(u"bt_sim")
        self.bt_sim.setGeometry(QRect(100, 10, 75, 31))
        self.bt_sim.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.bt_nao = QPushButton(self.frame_3)
        self.bt_nao.setObjectName(u"bt_nao")
        self.bt_nao.setGeometry(QRect(220, 10, 75, 31))
        self.bt_nao.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"	\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"}")

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.progressBar_instalao = QProgressBar(self.frame_4)
        self.progressBar_instalao.setObjectName(u"progressBar_instalao")
        self.progressBar_instalao.setCursor(QCursor(Qt.ForbiddenCursor))
        self.progressBar_instalao.setValue(1)
        self.progressBar_instalao.setAlignment(Qt.AlignCenter)
        self.progressBar_instalao.setOrientation(Qt.Horizontal)
        self.progressBar_instalao.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar_instalao)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        Updating.setCentralWidget(self.centralwidget)

        self.retranslateUi(Updating)

        QMetaObject.connectSlotsByName(Updating)
    # setupUi

    def retranslateUi(self, Updating):
        Updating.setWindowTitle(QCoreApplication.translate("Updating", u"MainWindow", None))
        self.lb_version.setText(QCoreApplication.translate("Updating", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#ffffff;\">teste</span></p></body></html>", None))
        self.bt_sim.setText(QCoreApplication.translate("Updating", u"Sim", None))
        self.bt_nao.setText(QCoreApplication.translate("Updating", u"N\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("Updating", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Por favor aguarde! O sistema est\u00e1 instalando a nova vers\u00e3o.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.progressBar_instalao.setToolTip(QCoreApplication.translate("Updating", u"<html><head/><body><p><span style=\" font-size:7pt; font-weight:700;\">O interrompimento da atualiza\u00e7\u00e3o, pode causar m\u00e1 funcionamento no sistema.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

