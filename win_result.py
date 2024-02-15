# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win_result.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,QFileDialog,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import sys
from openpyxl import Workbook
import csv
import os
import icons_rc

class SQLWindow(QMainWindow,object):
    def setupUi(self, SQLWindown):
        if not SQLWindown.objectName():
            SQLWindown.setObjectName(u"SQLWindown")
        SQLWindown.resize(1072, 638)
        SQLWindown.setCursor(QCursor(Qt.ArrowCursor))
        SQLWindown.setStyleSheet(u"background-color: rgb(38, 68, 149);")
        appIcon = QIcon(u"img\\TECH NEW LOGO.png")
        self.setWindowIcon(appIcon)
        self.centralwidget = QWidget(SQLWindown)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.tableWidget_query = QTableWidget(self.frame_2)
        self.tableWidget_query.setObjectName(u"tableWidget")
        self.tableWidget_query.setGeometry(QRect(10, 10, 1031, 551))
        self.tableWidget_query.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148,148,148);\n"
"	color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color:rgb(252,252,252);\n"
"}")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(960, 570, 81, 41))
        self.pushButton.setStyleSheet(u"\n"
"\n"
"QPushButton:hover{\n"
"	border:none;\n"
"	background-color: rgb(251, 99, 4);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/image/salvar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(850, 580, 101, 16))

        self.verticalLayout.addWidget(self.frame_2)

        SQLWindown.setCentralWidget(self.centralwidget)

        self.retranslateUi(SQLWindown)

        QMetaObject.connectSlotsByName(SQLWindown)
    # setupUi
        self.pushButton.clicked.connect(self.save_data)

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
            except Exception as e:
                print(f"Erro ao salvar o arquivo: {e}")

    def retranslateUi(self, SQLWindown):
        SQLWindown.setWindowTitle(QCoreApplication.translate("SQLWindown", u"MainWindow", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("SQLWindown", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Salvar resultados</span></p></body></html>", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    window = SQLWindow()
    window.show()
    app.exec_()