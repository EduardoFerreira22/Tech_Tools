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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
import icons_rc

class Ui_ProcessCSV(object):
    def setupUi(self, ProcessCSV):
        if not ProcessCSV.objectName():
            ProcessCSV.setObjectName(u"ProcessCSV")
        ProcessCSV.resize(1365, 786)
        ProcessCSV.setStyleSheet(u"background-color: rgb(38, 68, 149);")
        self.centralwidget = QWidget(ProcessCSV)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 130))
        self.frame_4.setFrameShape(QFrame.Panel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
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
        self.comboBox_op_busca.setObjectName(u"comboBox_op_busca")
        self.comboBox_op_busca.setGeometry(QRect(10, 50, 189, 20))
        self.comboBox_op_busca.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"font:600 9pt \"Segoe UI\";")
        self.comboBox_op_busca.setEditable(True)
        self.comboBox_op_busca.setDuplicatesEnabled(False)
        self.bt_buscar_opcoes = QPushButton(self.frame_3)
        self.bt_buscar_opcoes.setObjectName(u"bt_buscar_opcoes")
        self.bt_buscar_opcoes.setGeometry(QRect(232, 48, 75, 24))
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
        self.txt_buscar_ncm = QLineEdit(self.frame_3)
        self.txt_buscar_ncm.setObjectName(u"txt_buscar_ncm")
        self.txt_buscar_ncm.setGeometry(QRect(10, 84, 191, 21))
        self.txt_buscar_ncm.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 600 9pt \"Segoe UI\";")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 16, 98, 16))
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Panel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(235, 16777215))
        self.frame_8.setFrameShape(QFrame.Panel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.comboBox_op_processamentos = QComboBox(self.frame_8)
        self.comboBox_op_processamentos.addItem("")
        self.comboBox_op_processamentos.addItem("")
        self.comboBox_op_processamentos.addItem("")
        self.comboBox_op_processamentos.addItem("")
        self.comboBox_op_processamentos.setObjectName(u"comboBox_op_processamentos")
        self.comboBox_op_processamentos.setGeometry(QRect(10, 46, 215, 20))
        self.comboBox_op_processamentos.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 127);\n"
"font:600 9pt \"Segoe UI\";")
        self.comboBox_op_processamentos.setEditable(True)
        self.comboBox_op_processamentos.setDuplicatesEnabled(False)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 15, 151, 16))
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.bt_executar_combo_process = QPushButton(self.frame_8)
        self.bt_executar_combo_process.setObjectName(u"bt_executar_combo_process")
        self.bt_executar_combo_process.setGeometry(QRect(150, 77, 75, 24))
        self.bt_executar_combo_process.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")

        self.gridLayout_2.addWidget(self.frame_8, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Panel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.bt_setas_ncm = QPushButton(self.frame_7)
        self.bt_setas_ncm.setObjectName(u"bt_setas_ncm")
        self.bt_setas_ncm.setGeometry(QRect(190, 60, 31, 24))
        self.bt_setas_ncm.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/icons/image/direita-e-esquerda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_setas_ncm.setIcon(icon)
        self.bt_setas_ncm.setIconSize(QSize(20, 20))
        self.txt_alt_NCM1 = QLineEdit(self.frame_7)
        self.txt_alt_NCM1.setObjectName(u"txt_alt_NCM1")
        self.txt_alt_NCM1.setGeometry(QRect(10, 90, 181, 21))
        self.txt_alt_NCM1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 600 9pt \"Segoe UI\";")
        self.txt_alt_NCM1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_alt_NCM2 = QLineEdit(self.frame_7)
        self.txt_alt_NCM2.setObjectName(u"txt_alt_NCM2")
        self.txt_alt_NCM2.setGeometry(QRect(220, 90, 181, 21))
        self.txt_alt_NCM2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 600 9pt \"Segoe UI\";")
        self.txt_alt_NCM2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.bt_executar_process = QPushButton(self.frame_7)
        self.bt_executar_process.setObjectName(u"bt_executar_process")
        self.bt_executar_process.setGeometry(QRect(430, 90, 75, 24))
        self.bt_executar_process.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        self.lb_atencao_substituir = QLabel(self.frame_7)
        self.lb_atencao_substituir.setObjectName(u"lb_atencao_substituir")
        self.lb_atencao_substituir.setGeometry(QRect(10, 10, 421, 16))
        self.combo_column1 = QComboBox(self.frame_7)
        self.combo_column1.setObjectName(u"combo_column1")
        self.combo_column1.setGeometry(QRect(10, 40, 181, 22))
        self.combo_column1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 127);\n"
"font:600 9pt \"Segoe UI\";")
        self.combo_column2 = QComboBox(self.frame_7)
        self.combo_column2.setObjectName(u"combo_column2")
        self.combo_column2.setGeometry(QRect(220, 40, 180, 22))
        self.combo_column2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 127);\n"
"font:600 9pt \"Segoe UI\";")
        self.lb_info_ncm_subst = QLabel(self.frame_7)
        self.lb_info_ncm_subst.setObjectName(u"lb_info_ncm_subst")
        self.lb_info_ncm_subst.setGeometry(QRect(10, 10, 421, 16))

        self.gridLayout_2.addWidget(self.frame_7, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_6, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.txt_output_logs = QPlainTextEdit(self.frame)
        self.txt_output_logs.setObjectName(u"txt_output_logs")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(False)
        self.txt_output_logs.setFont(font)
        self.txt_output_logs.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 700 7pt \"Segoe UI\";")

        self.gridLayout_3.addWidget(self.txt_output_logs, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 1, 2, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tb_dados_csv = QTableWidget(self.frame_2)
        self.tb_dados_csv.setObjectName(u"tb_dados_csv")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.tb_dados_csv.setFont(font1)
        self.tb_dados_csv.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148,148,148);\n"
"	color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:rgb(252,252,252);\n"
"}")
        self.tb_dados_csv.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tb_dados_csv.setDragEnabled(True)
        self.tb_dados_csv.setDragDropMode(QAbstractItemView.InternalMove)
        self.tb_dados_csv.setAlternatingRowColors(True)
        self.tb_dados_csv.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tb_dados_csv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_dados_csv.setSortingEnabled(True)
        self.tb_dados_csv.verticalHeader().setVisible(False)

        self.gridLayout_5.addWidget(self.tb_dados_csv, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 2)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 65))
        self.frame_5.setFrameShape(QFrame.Panel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_9)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 0, 221, 51))
        self.pushButton.setMinimumSize(QSize(221, 51))
        self.pushButton.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/image/TECH TOOLS TITULO LOGO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(1500, 45))

        self.gridLayout_7.addWidget(self.frame_9, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(700, 65))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_10)
        self.gridLayout_6.setSpacing(2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.txt_path_filecsv = QLineEdit(self.frame_10)
        self.txt_path_filecsv.setObjectName(u"txt_path_filecsv")
        self.txt_path_filecsv.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 0);\n"
"font: 9pt \"Segoe UI\";")

        self.gridLayout_6.addWidget(self.txt_path_filecsv, 1, 0, 1, 1)

        self.bt_buscar_filecsv = QPushButton(self.frame_10)
        self.bt_buscar_filecsv.setObjectName(u"bt_buscar_filecsv")
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

        self.gridLayout_6.addWidget(self.bt_buscar_filecsv, 1, 1, 1, 1)

        self.bt_processar_arquivo_csv = QPushButton(self.frame_10)
        self.bt_processar_arquivo_csv.setObjectName(u"bt_processar_arquivo_csv")
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

        self.gridLayout_6.addWidget(self.bt_processar_arquivo_csv, 1, 2, 1, 1)


        self.gridLayout_7.addWidget(self.frame_10, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        ProcessCSV.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProcessCSV)

        QMetaObject.connectSlotsByName(ProcessCSV)
    # setupUi

    def retranslateUi(self, ProcessCSV):
        ProcessCSV.setWindowTitle(QCoreApplication.translate("ProcessCSV", u"MainWindow", None))
        self.comboBox_op_busca.setItemText(0, QCoreApplication.translate("ProcessCSV", u"Selecione", None))
        self.comboBox_op_busca.setItemText(1, QCoreApplication.translate("ProcessCSV", u"Buscar NCM's inv\u00e1lidos.", None))
        self.comboBox_op_busca.setItemText(2, QCoreApplication.translate("ProcessCSV", u"Buscar por NCM", None))
        self.comboBox_op_busca.setItemText(3, QCoreApplication.translate("ProcessCSV", u"Tudo que cont\u00e9m.", None))

        self.comboBox_op_busca.setCurrentText("")
        self.comboBox_op_busca.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"Op\u00e7\u00f5es de busca", None))
        self.bt_buscar_opcoes.setText(QCoreApplication.translate("ProcessCSV", u"Pesquisar", None))
        self.txt_buscar_ncm.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"Procurar por?", None))
        self.label_2.setText(QCoreApplication.translate("ProcessCSV", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Op\u00e7\u00f5es de busca:</span></p></body></html>", None))
        self.comboBox_op_processamentos.setItemText(0, QCoreApplication.translate("ProcessCSV", u"Selecione", None))
        self.comboBox_op_processamentos.setItemText(1, QCoreApplication.translate("ProcessCSV", u"Substituir NCM.", None))
        self.comboBox_op_processamentos.setItemText(2, QCoreApplication.translate("ProcessCSV", u"Tudo que cont\u00e9m mude para", None))
        self.comboBox_op_processamentos.setItemText(3, QCoreApplication.translate("ProcessCSV", u"P. X da Coluna A , Coluna B Recebe", None))

        self.comboBox_op_processamentos.setCurrentText("")
        self.comboBox_op_processamentos.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"Op\u00e7\u00f5es de busca", None))
        self.label_3.setText(QCoreApplication.translate("ProcessCSV", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Op\u00e7\u00f5es de processamento:</span></p></body></html>", None))
        self.bt_executar_combo_process.setText(QCoreApplication.translate("ProcessCSV", u"Executar", None))
        self.bt_setas_ncm.setText("")
        self.txt_alt_NCM1.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"De", None))
        self.txt_alt_NCM2.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"Para", None))
        self.bt_executar_process.setText(QCoreApplication.translate("ProcessCSV", u"Executar", None))
        self.lb_atencao_substituir.setText(QCoreApplication.translate("ProcessCSV", u"<html><head/><body><p><span style=\" font-size:7pt; color:#ffffff;\">Aten\u00e7\u00e3o! Todos os dados do </span><span style=\" font-size:7pt; font-weight:700; color:#ffffff;\">PRIMEIRO</span><span style=\" font-size:7pt; color:#ffffff;\"> quadro ser\u00e3o substitu\u00eddos pelos dados do</span><span style=\" font-size:7pt; font-weight:700; color:#ffffff;\"> SEGUNDO.</span></p></body></html>", None))
        self.lb_info_ncm_subst.setText(QCoreApplication.translate("ProcessCSV", u"<html><head/><body><p><span style=\" font-size:7pt; color:#ffffff;\">Para mudan\u00e7a de de </span><span style=\" font-size:7pt; font-weight:700; color:#ffffff;\">NCM's</span><span style=\" font-size:7pt; color:#ffffff;\"> deve-se respeitar o formato </span><span style=\" font-size:7pt; font-weight:700; color:#ffffff;\">0000.00.00</span></p></body></html>", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("ProcessCSV", u"<html><head/><body><p><span style=\" font-weight:700; color:#ffffff;\">Selecione o arquivo:</span></p></body></html>", None))
        self.txt_path_filecsv.setPlaceholderText(QCoreApplication.translate("ProcessCSV", u"C:\\Caminho\\para\\o\\Arquivo.csv", None))
        self.bt_buscar_filecsv.setText(QCoreApplication.translate("ProcessCSV", u"Buscar", None))
#if QT_CONFIG(tooltip)
        self.bt_processar_arquivo_csv.setToolTip(QCoreApplication.translate("ProcessCSV", u"<html><head/><body><p><span style=\" font-size:8pt; color:#00007f;\">Processar arquivo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_processar_arquivo_csv.setText(QCoreApplication.translate("ProcessCSV", u"Processar", None))
    # retranslateUi

