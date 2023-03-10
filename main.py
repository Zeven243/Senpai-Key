import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLineEdit
from PyQt5 import QtWidgets, QtGui
import sys
from PyQt5.uic import loadUi
import sqlite3



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("SenpaiKey.ui", self)
        self.add_entry_btn.clicked.connect(self.addbuttonclicked)
        self.get_entry_btn.clicked.connect(self.getbuttonclicked)

    def addbuttonclicked(self):
        entry = sqlite3.connect('data.db')
        c = entry.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS userdata (
            website_name text,
            user_name text,
            password text
            )""")

        c.execute("INSERT INTO userdata VALUES (?, ?, ?)", (self.website_input.text(), self.username_input.text(), self.password_input.text()))
        entry.commit()

        self.website_input.clear()
        self.username_input.clear()
        self.password_input.clear()

    def getbuttonclicked(self):
        entry = sqlite3.connect('data.db')
        c = entry.cursor()
        c.execute('SELECT * FROM userdata')
        data = c.fetchall()

        for x in data:
            if x[0] == self.website_input.text():
                self.username_input.setText(x[1])
                self.password_input.setEchoMode(self.password_input.Normal)
                self.password_input.setText(x[2])
            elif x[0] != self.website_input.text():
                self.username_input.setText("NO DATA")
                self.password_input.setEchoMode(self.password_input.Normal)
                self.password_input.setText("NO DATA")






# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
# input = QLineEdit.set
mainwindow.show()
try:
    sys.exit(app.exec_())
except:
    print("exiting...")