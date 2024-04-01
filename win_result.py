# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win_result.ui'
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
from PySide6.QtWidgets import (QApplication,QFileDialog, QFrame, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
from openpyxl import Workbook
from functions.logs import App_logs
import os
import csv
import icons_rc

class SQLWindown(QMainWindow,object):
    def setupUi(self, SQLWindown):
        if not SQLWindown.objectName():
            SQLWindown.setObjectName(u"SQLWindown")
        SQLWindown.resize(1072, 638)
        SQLWindown.setCursor(QCursor(Qt.ArrowCursor))
        SQLWindown.setStyleSheet(u"background-color: rgb(38, 68, 149);")
        self.centralwidget = QWidget(SQLWindown)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(49,147,0)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/image/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1, Qt.AlignRight)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1, Qt.AlignLeft)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget_query = QTableWidget(self.frame)
        self.tableWidget_query.setObjectName(u"tableWidget_query")
        self.tableWidget_query.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148,148,148);\n"
"	color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:rgb(252,252,252);\n"
"}")
        self.tableWidget_query.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.tableWidget_query, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        SQLWindown.setCentralWidget(self.centralwidget)

        self.retranslateUi(SQLWindown)

        QMetaObject.connectSlotsByName(SQLWindown)
    # setupUi


        self.pushButton.clicked.connect(self.save_data)
            #LOGS ----------------------------------------------------------------------------------------------------------
            # Obtém o nome do arquivo atual
        self.file_name = os.path.splitext(os.path.basename(__file__))[0] if __name__ != "__main__" else "win_result"
        self.path_logs = 'logs'
        self.class_name = self.__class__.__name__
        self.log = App_logs()

    def update_table_data(self, column_names, data):
            self.tableWidget_query.clearContents()
            self.tableWidget_query.setRowCount(len(data))
            self.tableWidget_query.setColumnCount(len(column_names))

            # Set column headers
            self.tableWidget_query.setHorizontalHeaderLabels(column_names)

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget_query.setItem(row_idx, col_idx, item)

    def save_data(self):
        # Abre um diálogo de salvamento de arquivo
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setDefaultSuffix(".csv")
        file_dialog.setNameFilter("CSV UTF-8 (*.csv);;CSV separado por vírgula (*.csv);;XLSX (*.xlsx)")

        if file_dialog.exec_():
            # Obtém o caminho do arquivo selecionado
            file_path = file_dialog.selectedFiles()[0]

            # Obtém os dados da tabela
            table_data = []
            for row in range(self.tableWidget_query.rowCount()):
                row_data = []
                for column in range(self.tableWidget_query.columnCount()):
                    item = self.tableWidget_query.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")
                table_data.append(row_data)

            # Obtém os nomes das colunas
            column_names = [self.tableWidget_query.horizontalHeaderItem(i).text() for i in range(self.tableWidget_query.columnCount())]

            # Salva os dados no arquivo selecionado
            try:
                selected_filter = file_dialog.selectedNameFilter()
                if selected_filter == "XLSX (*.xlsx)":
                    # Salva em formato XLSX
                    wb = Workbook()
                    ws = wb.active
                    ws.append(column_names)
                    for row in table_data:
                        ws.append(row)
                    wb.save(file_path)
                elif selected_filter == "CSV separado por vírgula (*.csv)":
                    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow(column_names)
                        writer.writerows(table_data)
                elif selected_filter == "CSV UTF-8 (*.csv)":
                    with open(file_path, mode='w', newline='', encoding='utf-8-sig') as file:
                        writer = csv.writer(file,delimiter=';')
                        writer.writerow(column_names)
                        writer.writerows(table_data)
                else:
                    print("Formato de arquivo não suportado.")
                    self.log.logs(name_file=self.file_name,path=self.path_logs,msg=f"save_data Formato de arquivo não suportado.")
            except Exception as e:
                self.log.logs(name_file=self.file_name,path=self.path_logs,msg=f"save_data Erro: {e}")
                print(f"Erro ao salvar o arquivo: {e}")


    def retranslateUi(self, SQLWindown):
        SQLWindown.setWindowTitle(QCoreApplication.translate("SQLWindown", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("SQLWindown", u"<html><head/><body><p><span style=\" font-size:8pt; color:#00007f;\">Salvar em .csv</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("SQLWindown", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Dados retornados pela consulta.</span></p></body></html>", None))
    # retranslateUi

