# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_process_csv.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
import icons_rc

class Ui_ProcessCSV(object):
    def setupUi(self, ProcessCSV):
        if not ProcessCSV.objectName():
            ProcessCSV.setObjectName(u"ProcessCSV")
        ProcessCSV.resize(1269, 745)
        ProcessCSV.setStyleSheet(u"background-color: rgb(38, 68, 149);")
        self.centralwidget = QWidget(ProcessCSV)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 65))
        self.frame_5.setFrameShape(QFrame.Panel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.txt_path_filecsv = QLineEdit(self.frame_5)
        self.txt_path_filecsv.setObjectName(u"txt_path_filecsv")
        self.txt_path_filecsv.setGeometry(QRect(10, 30, 311, 31))
        self.txt_path_filecsv.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.bt_buscar_filecsv = QPushButton(self.frame_5)
        self.bt_buscar_filecsv.setObjectName(u"bt_buscar_filecsv")
        self.bt_buscar_filecsv.setGeometry(QRect(320, 30, 75, 31))
        self.bt_buscar_filecsv.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.bt_processar_arquivo_csv = QPushButton(self.frame_5)
        self.bt_processar_arquivo_csv.setObjectName(u"bt_processar_arquivo_csv")
        self.bt_processar_arquivo_csv.setGeometry(QRect(420, 30, 81, 31))
        self.bt_processar_arquivo_csv.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 6, 131, 16))

        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_output_logs = QPlainTextEdit(self.frame)
        self.txt_output_logs.setObjectName(u"txt_output_logs")
        self.txt_output_logs.setGeometry(QRect(10, 10, 181, 181))
        self.txt_output_logs.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 8pt \"Segoe UI\";\n"
"font: 700 7pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.frame, 0, 1, 2, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.tb_dados_csv = QTableWidget(self.frame_2)
        self.tb_dados_csv.setObjectName(u"tb_dados_csv")
        self.tb_dados_csv.setGeometry(QRect(10, 10, 1231, 501))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.tb_dados_csv.setFont(font)
        self.tb_dados_csv.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148,148,148);\n"
"	color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:rgb(252,252,252);\n"
"}")
        self.tb_dados_csv.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 130))
        self.frame_4.setFrameShape(QFrame.Panel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(360, 16777215))
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.comboBox_op_busca = QComboBox(self.frame_3)
        self.comboBox_op_busca.addItem("")
        self.comboBox_op_busca.addItem("")
        self.comboBox_op_busca.addItem("")
        self.comboBox_op_busca.addItem("")
        self.comboBox_op_busca.addItem("")
        self.comboBox_op_busca.setObjectName(u"comboBox_op_busca")
        self.comboBox_op_busca.setGeometry(QRect(10, 40, 191, 20))
        self.comboBox_op_busca.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"font:600 9pt \"Segoe UI\";")
        self.comboBox_op_busca.setEditable(True)
        self.comboBox_op_busca.setDuplicatesEnabled(False)
        self.bt_buscar_opcoes = QPushButton(self.frame_3)
        self.bt_buscar_opcoes.setObjectName(u"bt_buscar_opcoes")
        self.bt_buscar_opcoes.setGeometry(QRect(220, 80, 91, 24))
        self.bt_buscar_opcoes.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 80, 191, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 600 9pt \"Segoe UI\";")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 98, 16))
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Panel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.comboBox_op_processamentos = QComboBox(self.frame_6)
        self.comboBox_op_processamentos.addItem("")
        self.comboBox_op_processamentos.addItem("")
        self.comboBox_op_processamentos.addItem("")
        self.comboBox_op_processamentos.addItem("")
        self.comboBox_op_processamentos.setObjectName(u"comboBox_op_processamentos")
        self.comboBox_op_processamentos.setGeometry(QRect(10, 30, 191, 20))
        self.comboBox_op_processamentos.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 127);\n"
"font:600 9pt \"Segoe UI\";")
        self.comboBox_op_processamentos.setEditable(True)
        self.comboBox_op_processamentos.setDuplicatesEnabled(False)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 161, 16))
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.txt_alt_NCM1 = QLineEdit(self.frame_6)
        self.txt_alt_NCM1.setObjectName(u"txt_alt_NCM1")
        self.txt_alt_NCM1.setGeometry(QRect(220, 30, 113, 21))
        self.txt_alt_NCM1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 600 9pt \"Segoe UI\";")
        self.txt_alt_NCM2 = QLineEdit(self.frame_6)
        self.txt_alt_NCM2.setObjectName(u"txt_alt_NCM2")
        self.txt_alt_NCM2.setGeometry(QRect(380, 30, 113, 21))
        self.txt_alt_NCM2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 600 9pt \"Segoe UI\";")
        self.bt_setas_ncm = QPushButton(self.frame_6)
        self.bt_setas_ncm.setObjectName(u"bt_setas_ncm")
        self.bt_setas_ncm.setGeometry(QRect(340, 30, 41, 24))
        self.bt_setas_ncm.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/icons/image/direita-e-esquerda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_setas_ncm.setIcon(icon)
        self.bt_setas_ncm.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.frame_6)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        ProcessCSV.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProcessCSV)

        QMetaObject.connectSlotsByName(ProcessCSV)
    # setupUi

    def retranslateUi(self, ProcessCSV):
        ProcessCSV.setWindowTitle(QCoreApplication.translate("ProcessCSV", u"MainWindow", None))
        self.txt_path_filecsv.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"C:\\Caminho\\para\\o\\Arquivo.csv", None))
        self.bt_buscar_filecsv.setText(QCoreApplication.translate("ProcessCSV", u"Caminho", None))
#if QT_CONFIG(tooltip)
        self.bt_processar_arquivo_csv.setToolTip(QCoreApplication.translate("ProcessCSV", u"<html><head/><body><p><span style=\" font-size:8pt; color:#00007f;\">Processar arquivo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_processar_arquivo_csv.setText(QCoreApplication.translate("ProcessCSV", u"Processar", None))
        self.label.setText(QCoreApplication.translate("ProcessCSV", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Selecione o arquivo:</span></p></body></html>", None))
        self.comboBox_op_busca.setItemText(0, QCoreApplication.translate("ProcessCSV", u"Buscar por NCM", None))
        self.comboBox_op_busca.setItemText(1, QCoreApplication.translate("ProcessCSV", u"Buscar NCM's inv\u00e1lidos.", None))
        self.comboBox_op_busca.setItemText(2, QCoreApplication.translate("ProcessCSV", u"Localizar caracteres especiais.", None))
        self.comboBox_op_busca.setItemText(3, QCoreApplication.translate("ProcessCSV", u"Localizar Duplicados.", None))
        self.comboBox_op_busca.setItemText(4, QCoreApplication.translate("ProcessCSV", u"Tudo que cont\u00e9m.", None))

        self.comboBox_op_busca.setCurrentText("")
        self.comboBox_op_busca.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"Op\u00e7\u00f5es de busca", None))
        self.bt_buscar_opcoes.setText(QCoreApplication.translate("ProcessCSV", u"Pesquisar", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"Procurar por?", None))
        self.label_2.setText(QCoreApplication.translate("ProcessCSV", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Op\u00e7\u00f5es de busca:</span></p></body></html>", None))
        self.comboBox_op_processamentos.setItemText(0, QCoreApplication.translate("ProcessCSV", u"Substituir NCM.", None))
        self.comboBox_op_processamentos.setItemText(1, QCoreApplication.translate("ProcessCSV", u"Remover duplicados.", None))
        self.comboBox_op_processamentos.setItemText(2, QCoreApplication.translate("ProcessCSV", u"Substituir caracteres especiais.", None))
        self.comboBox_op_processamentos.setItemText(3, QCoreApplication.translate("ProcessCSV", u"Tudo que cont\u00e9m mude para...", None))

        self.comboBox_op_processamentos.setCurrentText("")
        self.comboBox_op_processamentos.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"Op\u00e7\u00f5es de busca", None))
        self.label_3.setText(QCoreApplication.translate("ProcessCSV", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Op\u00e7\u00f5es de processamento:</span></p></body></html>", None))
        self.txt_alt_NCM1.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"De 0000.00.00", None))
        self.txt_alt_NCM2.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"Para 0000.00.00", None))
        self.bt_setas_ncm.setText("")
    # retranslateUi

