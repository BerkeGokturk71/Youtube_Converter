from PyQt5.QtWidgets import *
from indirilen_ui import Ui_Database
import sqlite3
from PyQt5 import QtGui

class Quest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.quest = Ui_Database()
        self.quest.setupUi(self)


        self.conn = sqlite3.connect("audio1.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("Create Table IF NOT EXISTS audio1 (liste TEXT,liste2 TEXT)")


        self.cursor.execute("Select liste from audio1")
        indirilen_goster = self.cursor.fetchall()
        satir_sayisi = -1
        self.quest.tableWidget.setRowCount(len(indirilen_goster))
        self.quest.tableWidget.setColumnWidth(0,200)
        for i in indirilen_goster:
            satir_sayisi += 1
            self.quest.tableWidget.setItem(satir_sayisi, 0, QTableWidgetItem(str(i)))






