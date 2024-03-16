from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
from PyQt5.uic.properties import QtWidgets, QtGui 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from mysql.connector import cursor
from fpdf import FPDF
import pandas as pd
import traceback

ui, _ =loadUiType('collegeresult.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.menuBar().setVisible(False)
        self.menu34.setVisible(False)
        self.menu35.setVisible(False)
        self.gb32.setVisible(False)
        self.gb42.setVisible(False)
        self.b25.setVisible(False)
        self.b26.setVisible(False)
        self.label_44.setVisible(False)
        self.b43.setVisible(False)
        self.tf41.setVisible(False)

        # self.b01_2.clicked.connect(self.test1)
        # self.b02.clicked.connect(self.test1)
        self.b02.clicked.connect(self.test1)
        self.b01.clicked.connect(self.login)
        self.b01.clicked.connect(self.login2)
        self.b11.clicked.connect(self.register1)
        #self.b21.clicked.connect(self.insertmarks)
        self.b22.clicked.connect(self.insertmarks)
        self.b23.clicked.connect(self.viewmarks)
        self.b24.clicked.connect(self.studentdetails)
        self.b25.clicked.connect(self.register)
        self.b26.clicked.connect(self.delete_user)
        self.b31.clicked.connect(self.insertmarks1)
        self.b32.clicked.connect(self.insertmarkssem1it)
        self.b33.clicked.connect(self.uploadmarks)
        self.b41.clicked.connect(self.viewmarks1)
        self.b44.clicked.connect(self.print_table_to_pdf)
        self.b43.clicked.connect(self.viewmarks_basedonindividaul)
        self.b51.clicked.connect(self.delete_user1)
        self.b61.clicked.connect(self.insertstudentdetails)
        self.b62.clicked.connect(self.insertstudentdetails1)


        self.menu11.triggered.connect(self.insertmarks)
        self.menu12.triggered.connect(self.viewmarks)
        self.menu21.triggered.connect(self.home)
        self.menu31.triggered.connect(self.insertmarks)
        self.menu32.triggered.connect(self.viewmarks)
        self.menu33.triggered.connect(self.studentdetails)
        self.menu34.triggered.connect(self.register)
        self.menu35.triggered.connect(self.delete_user)
        self.menu41.triggered.connect(self.helo_light)
        self.menu42.triggered.connect(self.helo_dark)
        self.menu51.triggered.connect(self.backtologin)


        self.tf301.activated.connect(self.insertmarks3)

        self.label_19.setText("Welcome User")

        self.number = 0


        self.admin_branch_list = ["Computer","Information technology","Artificial intelligence and data science","Electronics and telecommunication","Mechanical"]




    def test1(self):

        self.number += 1
        print(self.number)
        if(self.number % 2 == 0):
            self.helo_dark()

        else :
            self.helo_light()


    def helo_light(self):
        pixmap = QPixmap('C:/Users/HARSH/PycharmProjects/pythonProject2/projectphoto2.jpeg')
        self.label_22.setPixmap(pixmap)

        self.b02.setText("Switch to dark mode")

        #buttons
        self.b01.setStyleSheet("QWidget {background-color: rgb(50, 52, 55); color: rgb(209, 208, 197); }")
        self.b31.setStyleSheet("QWidget {background-color: rgb(50, 52, 55); color: rgb(209, 208, 197); }")
        self.b32.setStyleSheet("QWidget {background-color: rgb(50, 52, 55); color: rgb(209, 208, 197); }")
        self.b33.setStyleSheet("QWidget {background-color: rgb(50, 52, 55); color: rgb(209, 208, 197); }")
        self.b11.setStyleSheet("QWidget {background-color: rgb(50, 52, 55); color: rgb(209, 208, 197); }")
        self.b41.setStyleSheet("QWidget {background-color: rgb(50, 52, 55); color: rgb(209, 208, 197); }")
        self.b43.setStyleSheet("QWidget {background-color: rgb(50, 52, 55); color: rgb(209, 208, 197); }")
        self.b44.setStyleSheet("QWidget {background-color: rgb(50, 52, 55); color: rgb(209, 208, 197); }")
        self.b51.setStyleSheet("QWidget {background-color: rgb(50, 52, 55); color: rgb(209, 208, 197); }")
        self.b61.setStyleSheet("QWidget {background-color: rgb(50, 52, 55); color: rgb(209, 208, 197); }")

        #main window
        self.setStyleSheet("QWidget {font: 57 12pt \"Roboto Mono Medium\"; background-color: rgb(225, 225, 227) ; border-color: rgb(225, 225, 227)}")
        #tab
        self.tabWidget.setStyleSheet("QWidget {height: 100px;background-color: rgb(225, 225, 227) }")

        #groupbox

        #insert marks gb
        self.gb31.setStyleSheet("QWidget {color: rgb(225, 225, 227) }")
        self.gb32.setStyleSheet("QWidget {color: rgb(225, 225, 227) }")
        #view marks gb
        self.gb41.setStyleSheet("QWidget {color: rgb(225, 225, 227) }")
        self.gb42.setStyleSheet("QWidget {color: rgb(225, 225, 227) }")
        #delete user page gb
        self.gb51.setStyleSheet("QWidget {color: rgb(225, 225, 227) }")

        #table widgets
        self.tableWidget.setStyleSheet("QWidget {background-color: rgb(225, 225, 227); color: rgb(50, 52, 55); gridline-color: rgb(50, 52, 55);}")
        self.tableWidget_3.setStyleSheet("QWidget {background-color: rgb(225, 225, 227); color: rgb(50, 52, 55); gridline-color: rgb(50, 52, 55);}")

        #labels

        #login labels
        self.label_2.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\"; }")
        self.label_3.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\"; }")
        self.label_4.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\"; }")
        #home labels
        self.label_20.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\"; }")
        #register labels
        self.label_48.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_8.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_7.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_6.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        #insert marks labels
        self.label_23.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_24.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim301.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim302.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim303.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim304.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim305.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim306.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim307.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim308.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim309.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim310.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim311.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim312.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim313.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim314.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.lbim315.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")

        #view marks labels
        self.label_41.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_42.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_44.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_45.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_50.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 9pt \"Roboto Mono Medium\";}")
        #add student page labels
        self.label_17.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_18.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_15.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_52.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_35.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        #delete user page labels
        self.label_46.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")
        self.label_47.setStyleSheet("QWidget {color: rgb(50, 52, 55); font: 57 14pt \"Roboto Mono Medium\";}")



        #textbox

        #login page textbox
        self.tf01.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf02.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")

        #register page textbox
        self.tf11.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf12.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf13.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")

        #insert page textbox
        self.tf301.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf302.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf303.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf304.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf305.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf306.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf307.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf308.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf309.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf310.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf311.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf312.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf313.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf314.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf315.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")

        #view page textbox
        self.tf41.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")

        #add student page textbox
        self.tf61.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")
        self.tf62.setStyleSheet("QWidget {background-color: rgb(209, 211, 216); color: rgb(50, 52, 55); }")


        #menubar
        self.menubar.setStyleSheet("QWidget {background-color:rgb(200, 205, 211); selection-color: rgb(209, 208, 197); selection-background-color: rgb(50, 52, 55);border-color:rgb(50, 52, 55);border-color: rgb(50, 52, 55);gridline-color:rgb(50, 52, 55); font: 57 12pt \"Roboto Mono Medium\"; }")
        '''selection - color: rgb(209, 208, 197);
        selection - background - color: rrgb(50, 52, 55);'''


    def helo_dark(self):
        pixmap = QPixmap('C:\\Users\\HARSH\\PycharmProjects\\pythonProject2\\projectphoto.jpg')
        self.label_22.setPixmap(pixmap)

        self.b02.setText("Switch to light mode")
        self.label_4.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.setStyleSheet("font: 57 12pt \"Roboto Mono Medium\";\n"
                                 "selection-background-color: rgb(50, 52, 55);\n"
                                 "background-color: rgb(50, 52, 55);\n"
                                 "alternate-background-color: rgb(50, 52, 55);\n"
                                 "border-color: rgb(50, 52, 55);\n"
                                 "border-top-color: rgb(50, 52, 55);\n"
                                 "selection-color: rgb(50, 52, 55);")

        # insert marks gb
        self.gb31.setStyleSheet("QWidget {color:  rgb(50, 52, 55) }")
        self.gb32.setStyleSheet("QWidget {color:  rgb(50, 52, 55) }")
        # view marks gb
        self.gb41.setStyleSheet("QWidget {color:  rgb(50, 52, 55) }")
        self.gb42.setStyleSheet("QWidget {color:  rgb(50, 52, 55) }")
        # delete user page gb
        self.gb51.setStyleSheet("QWidget {color:  rgb(50, 52, 55) }")

        self.centralwidget.setStyleSheet("background-color: rgb(50, 52, 55);\n"
                                         "color: rgb(50, 52, 55);")

        self.tabWidget.setStyleSheet("background-color: rgb(50, 52, 55);\n"
                                     "border-color: rgb(50, 52, 55);")

        self.label.setStyleSheet("color: rgb(226, 183, 20);\n"
                                 "font: 63 28pt \"Roboto Mono SemiBold\";\n"
                                 "")

        self.label_2.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")

        self.label_3.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")

        self.tf01.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                "color: rgb(209, 208, 197);")

        self.tf02.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                "color: rgb(209, 208, 197);")

        self.b01.setStyleSheet("background-color: rgb(209, 208, 197);\n"
                               "color: rgb(100, 102, 105);")

        self.label_5.setStyleSheet("color: rgb(226, 183, 20);\n"
                                   "font: 63 28pt \"Roboto Mono SemiBold\";\n"
                                   "")

        self.label_6.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")

        self.label_7.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")

        self.tf12.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                "color: rgb(209, 208, 197);")



        self.b11.setStyleSheet("background-color: rgb(209, 208, 197);\n"
                               "color: rgb(100, 102, 105);")

        self.label_8.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")

        self.tf11.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                "color: rgb(209, 208, 197);")

        self.tf13.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                "color: rgb(209, 208, 197);")

        self.cb11.setStyleSheet("color: rgb(202, 71, 84);\n"
                                "selection-color: rgb(100, 102, 105);\n"
                                "selection-background-color: rgb(226, 183, 20);")
        self.label_48.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.label_19.setStyleSheet("color: rgb(226, 183, 20);\n"
                                    "font: 63 32pt \"Roboto Mono SemiBold\";\n"
                                    "")
        self.b22.setStyleSheet("color: rgb(100, 102, 105);\n"
                               "font: 57 12pt \"Roboto Mono Medium\";\n"
                               "background-color: rgb(209, 208, 197);")
        self.b23.setStyleSheet("color: rgb(100, 102, 105);\n"
                               "font: 57 12pt \"Roboto Mono Medium\";\n"
                               "background-color: rgb(209, 208, 197);")
        self.label_20.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.b24.setStyleSheet("color: rgb(100, 102, 105);\n"
                               "font: 57 12pt \"Roboto Mono Medium\";\n"
                               "background-color: rgb(209, 208, 197);")
        self.b25.setStyleSheet("color: rgb(100, 102, 105);\n"
                               "font: 57 12pt \"Roboto Mono Medium\";\n"
                               "background-color: rgb(209, 208, 197);")
        self.b26.setStyleSheet("color: rgb(100, 102, 105);\n"
                               "font: 57 12pt \"Roboto Mono Medium\";\n"
                               "background-color: rgb(209, 208, 197);")
        self.label_21.setStyleSheet("color: rgb(226, 183, 20);\n"
                                    "font: 63 28pt \"Roboto Mono SemiBold\";\n"
                                    "")
        self.label_24.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.label_23.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")

        self.cb31.setStyleSheet("color: rgb(202, 71, 84);\n"
                                "selection-color: rgb(100, 102, 105);\n"
                                "selection-background-color: rgb(226, 183, 20);")
        self.cb32.setStyleSheet("color: rgb(202, 71, 84);\n"
                                "selection-color: rgb(100, 102, 105);\n"
                                "selection-background-color: rgb(226, 183, 20);")
        self.b31.setStyleSheet("background-color: rgb(209, 208, 197);\n"
                               "color: rgb(100, 102, 105);")
        self.label_25.setStyleSheet("color: rgb(226, 183, 20);\n"
                                    "font: 63 28pt \"Roboto Mono SemiBold\";\n"
                                    "")
        self.lbim301.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.lbim302.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.lbim303.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf303.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                 "color: rgb(209, 208, 197);")
        self.lbim304.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf304.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                 "color: rgb(209, 208, 197);")
        self.lbim305.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf305.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                 "color: rgb(209, 208, 197);")
        self.lbim306.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf306.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                    "color: rgb(209, 208, 197);")
        self.lbim307.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf307.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                 "color: rgb(209, 208, 197);")
        self.lbim312.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.lbim311.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf314.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                 "color: rgb(209, 208, 197);")
        self.lbim314.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf309.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                 "color: rgb(209, 208, 197);")
        self.tf308.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                 "color: rgb(209, 208, 197);")
        self.lbim310.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf310.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                 "color: rgb(209, 208, 197);")
        self.tf311.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                "color: rgb(209, 208, 197);")
        self.lbim309.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.lbim308.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.lbim313.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf312.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                 "color: rgb(209, 208, 197);")
        self.tf313.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                 "color: rgb(209, 208, 197);")
        self.b32.setStyleSheet("background-color: rgb(209, 208, 197);\n"
                               "color: rgb(100, 102, 105);")
        self.tf315.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                 "color: rgb(209, 208, 197);")
        self.lbim315.setStyleSheet("color: rgb(209, 208, 197);\n"
                                   "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf301.setStyleSheet("color: rgb(202, 71, 84);\n"
                                 "selection-color: rgb(100, 102, 105);\n"
                                 "selection-background-color: rgb(226, 183, 20);")
        self.tf302.setStyleSheet("color: rgb(202, 71, 84);\n"
                                 "selection-color: rgb(100, 102, 105);\n"
                                 "selection-background-color: rgb(226, 183, 20);")
        self.b33.setStyleSheet("background-color: rgb(209, 208, 197);\n"
                               "color: rgb(100, 102, 105);")
        self.label_40.setStyleSheet("color: rgb(226, 183, 20);\n"
                                    "font: 63 28pt \"Roboto Mono SemiBold\";\n"
                                    "")
        self.label_41.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.label_42.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.label_50.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 9pt \"Roboto Mono Medium\";")
        self.cb41.setStyleSheet("color: rgb(202, 71, 84);\n"
                                "selection-color: rgb(100, 102, 105);\n"
                                "selection-background-color: rgb(226, 183, 20);")
        self.cb42.setStyleSheet("color: rgb(202, 71, 84);\n"
                                "selection-color: rgb(100, 102, 105);\n"
                                "selection-background-color: rgb(226, 183, 20);")
        self.b41.setStyleSheet("background-color: rgb(209, 208, 197);\n"
                               "color: rgb(100, 102, 105);")
        self.cb43.setStyleSheet("color: rgb(202, 71, 84);\n"
                                "selection-color: rgb(100, 102, 105);\n"
                                "selection-background-color: rgb(226, 183, 20);")
        self.label_45.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.label_43.setStyleSheet("color: rgb(226, 183, 20);\n"
                                    "font: 63 28pt \"Roboto Mono SemiBold\";\n"
                                    "")
        self.tableWidget.setStyleSheet("background-color: rgb(50, 52, 55);\n"
                                       "color: rgb(170, 170, 127);")
        self.b44.setStyleSheet("background-color: rgb(209, 208, 197);\n"
                               "color: rgb(100, 102, 105);")
        self.b43.setStyleSheet("background-color: rgb(209, 208, 197);\n"
                               "color: rgb(100, 102, 105);")
        self.label_44.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf41.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                "color: rgb(209, 208, 197);")
        self.label_49.setStyleSheet("color: rgb(226, 183, 20);\n"
                                    "font: 63 28pt \"Roboto Mono SemiBold\";\n"
                                    "")
        self.tableWidget_3.setStyleSheet("background-color: rgb(50, 52, 55);\n"
                                         "color: rgb(170, 170, 127);")
        self.b51.setStyleSheet("background-color: rgb(209, 208, 197);\n"
                               "color: rgb(100, 102, 105);")
        self.cb501.setStyleSheet("color: rgb(202, 71, 84);\n"
                                 "selection-color: rgb(100, 102, 105);\n"
                                 "selection-background-color: rgb(226, 183, 20);")
        self.label_46.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.label_47.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.label_15.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.label_16.setStyleSheet("color: rgb(226, 183, 20);\n"
                                    "font: 63 28pt \"Roboto Mono SemiBold\";\n"
                                    "")
        self.label_52.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.tf62.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                "color: rgb(209, 208, 197);")
        self.cb61.setStyleSheet("color: rgb(202, 71, 84);\n"
                                "selection-color: rgb(100, 102, 105);\n"
                                "selection-background-color: rgb(226, 183, 20);")
        self.label_17.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.label_18.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.b61.setStyleSheet("background-color: rgb(209, 208, 197);\n"
                               "color: rgb(100, 102, 105);")
        self.tf61.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                "color: rgb(209, 208, 197);")
        self.cb62.setStyleSheet("color: rgb(202, 71, 84);\n"
                                "selection-color: rgb(100, 102, 105);\n"
                                "selection-background-color: rgb(226, 183, 20);")
        self.b62.setStyleSheet("color: rgb(100, 102, 105);\n"
                               "font: 57 12pt \"Roboto Mono Medium\";\n"
                               "background-color: rgb(209, 208, 197);")
        self.label_35.setStyleSheet("color: rgb(209, 208, 197);\n"
                                    "font: 57 14pt \"Roboto Mono Medium\";")
        self.menubar.setStyleSheet("background-color: rgb(44, 46, 49);\n"
                                   "\n"
                                   "selection-background-color: rgb(209, 208, 197);\n"
                                   "color: rgb(226, 183, 20);\n"
                                   "font: 57 12pt \"Roboto Mono Medium\";\n"
                                   "border-color: rgb(209, 208, 197);")




    def login(self):
      self.b25.setVisible(False)
      self.b26.setVisible(False)
      self.menu34.setVisible(False)
      self.menu35.setVisible(False)
      self.menuBar().setVisible(False)
      self.cb31.clear()
      self.cb41.clear()


      try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abesaale123",
            database="college_result_management_sys"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM register WHERE id= %s and password= %s"

        un = self.tf01.text()
        pw = self.tf02.text()
        cursor.execute(query, (un,pw))
        self.login_result = cursor.fetchall()


        if len(self.login_result) > 0:
            self.menuBar().setVisible(True)
            self.tabWidget.setCurrentIndex(2)
            self.label_19.setText("Welcome User")
        elif(un=="admin" and pw=="admin"):
            self.b25.setVisible(True)
            self.b26.setVisible(True)
            self.menu34.setVisible(True)
            self.menu35.setVisible(True)
            self.menuBar().setVisible(True)
            self.tabWidget.setCurrentIndex(2)
            self.label_19.setText("Welcome Admin")
            self.cb31.addItems(self.admin_branch_list)
            self.cb41.addItems(self.admin_branch_list)

        else:
            QMessageBox.information(self,"college result management system","Invalid login, try again!")
      except Exception as e:
          QMessageBox.information(self,"Error", "Error in database connection or query execution: {}".format(e))
      finally:
          cursor.close()
          conn.close()

    def login2(self):
        un = self.tf01.text()
        pw = self.tf02.text()
        if (un == "admin" and pw == "admin"):
            pass
        else:
            print(self.login_result)
            index = 0
            get_string = self.login_result[index]
            print(get_string)
            my_list = list(get_string)
            index_to_keep = 3
            del my_list[:index_to_keep]
            print(my_list)
            self.cb31.addItems(my_list)
            self.cb41.addItems(my_list)

    def login1(self):
        self.menuBar().setVisible(True)
        self.tabWidget.setCurrentIndex(2)

    def register(self):
            self.tabWidget.setCurrentIndex(1)

    def register1(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abesaale123",
            database="college_result_management_sys"
        )
        name = self.tf11.text()
        un1 = self.tf12.text()
        pw1 = self.tf13.text()
        branch_teachers = self.cb11.currentText()
        cursor = conn.cursor()
        querry = "Insert into register(name,id,password,BRANCH)values(%s,%s,%s,%s)"
        cursor.execute(querry, (name, un1, pw1, branch_teachers))
        conn.commit()
        QMessageBox.information(self,"Message", "Done Registeration")
        cursor.close()
        conn.close()



    def backtologin(self):
        self.menuBar().setVisible(False)
        self.tabWidget.setCurrentIndex(0)

    def home(self):
        if(self.menu21.triggered):
            self.tabWidget.setCurrentIndex(2)

    def insertmarks(self):
        if (self.b22.clicked):
            self.tabWidget.setCurrentIndex(3)






    def insertmarks1(self):
        branch = self.cb31.currentText()
        semester = self.cb32.currentText()
        self.tf301.clear()
        self.tf302.clear()

        if(self.b31.clicked):
            try:
                # Establish a connection to the MySQL database
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="abesaale123",
                    database="college_result_management_sys"
                )

                # Define a cursor object to interact with the database
                my = mydb.cursor()

                # Define the semester and branch variables

                # Write a SQL query to select the data you want to display in the combobox
                sql_query = "SELECT Roll_no FROM  studdetails where Semester=%s AND Branch=%s"
                my.execute(sql_query, (semester, branch))

                # Fetch the results of the query and store them in a variable
                result = my.fetchall()

                # Print the results to the console
                print(result)

                # Clear any existing items from the combobox
                self.tf301.clear()

                # Populate the combobox with the results of the query
                for item in result:
                    self.tf301.addItem(str(item[0]))


            except mysql.connector.Error as error:
                print("Failed to connect to MySQL database: {}".format(error))

            self.gb32.setVisible(True)

            self.lbim301.setVisible(True)
            self.lbim302.setVisible(True)
            self.lbim303.setVisible(True)
            self.lbim304.setVisible(True)
            self.lbim305.setVisible(True)
            self.lbim306.setVisible(True)
            self.lbim307.setVisible(True)
            self.lbim308.setVisible(True)
            self.lbim309.setVisible(True)
            self.lbim310.setVisible(True)
            self.lbim311.setVisible(True)
            self.lbim312.setVisible(True)
            self.lbim313.setVisible(True)
            self.lbim314.setVisible(True)
            self.lbim315.setVisible(True)

            self.tf301.setVisible(True)
            self.tf302.setVisible(True)
            self.tf303.setVisible(True)
            self.tf304.setVisible(True)
            self.tf305.setVisible(True)
            self.tf306.setVisible(True)
            self.tf307.setVisible(True)
            self.tf308.setVisible(True)
            self.tf309.setVisible(True)
            self.tf310.setVisible(True)
            self.tf311.setVisible(True)
            self.tf312.setVisible(True)
            self.tf313.setVisible(True)
            self.tf314.setVisible(True)
            self.tf315.setVisible(True)

            if (semester == "Semester 1"):

                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM-I (FEC101)")
                self.lbim304.setText("Phy-I (FEC102)")
                self.lbim305.setText("Chem-I (FEC103)")
                self.lbim306.setText("Mech (FEC104)")
                self.lbim307.setText("BEE (FEC105)")
                self.lbim308.setText("Phy-I lab(FEL101)")
                self.lbim309.setText("Chem-I lab(FEL102)")
                self.lbim310.setText("Mech lab(FEL103)")
                self.lbim311.setText("BEE lab(FEL104)")
                self.lbim312.setText("BWP-I (FEL105)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)






            elif (semester == "Semester 2"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM-II (FEC201)")
                self.lbim304.setText("Phy-II (FEC202)")
                self.lbim305.setText("Chem-II (FEC203)")
                self.lbim306.setText("EG (FEC204)")
                self.lbim307.setText("CP (FEC105)")
                self.lbim308.setText("PCE-I(FEC206)")
                self.lbim309.setText("Phy-II lab(FEL201)")
                self.lbim310.setText("Chem-II lab(FEL202)")
                self.lbim311.setText("EG lab(FEL203)")
                self.lbim312.setText("CP lab (FEL204)")
                self.lbim313.setText("PCE-I lab(FEL205)")
                self.lbim314.setText("BWP-II (FEL206)")
                self.lbim315.setVisible(False)
                self.tf315.setVisible(False)

                # mechanical
            elif (branch == "Mechanical" and semester == "Semester 3"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM3 (MEC301)")
                self.lbim304.setText("SOM (MEC302)")
                self.lbim305.setText("PP (MEC303)")
                self.lbim306.setText("MAM (MEC304)")
                self.lbim307.setText("TD (MEC305)")
                self.lbim308.setText("MT (MEL301)")
                self.lbim309.setText("CAD (MEL302)")
                self.lbim310.setText("MSP (MEL303)")
                self.lbim311.setText("MSP1 (MEL304)")
                self.lbim312.setVisible(False)
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf312.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)





            elif (branch == "Mechanical" and semester == "Semester 4"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM-IV (MEC401)")
                self.lbim304.setText("FM (MEC402)")
                self.lbim305.setText("KM (MEC403)")
                self.lbim306.setText("CAD (MEC404)")
                self.lbim307.setText("IE (MEC405)")
                self.lbim308.setText("IE (MEL401)")
                self.lbim309.setText("KM (MEL402)")
                self.lbim310.setText("PP (MEL403)")
                self.lbim311.setText("CNC&3D (MEL404)")
                self.lbim312.setText("MP (MEL405)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)




            elif (branch == "Mechanical" and semester == "Semester 5"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("MMAC (MEC501)")
                self.lbim304.setText("TE (MEC502)")
                self.lbim305.setText("DOM (MEC503)")
                self.lbim306.setText("FEA (MEC504)")
                self.lbim307.setText("DLOC1 (MEDLO501X)")
                self.lbim308.setText("TEL (MEL501)")
                self.lbim309.setText("DOM (MEL502)")
                self.lbim310.setText("FEA (MEL503)")
                self.lbim311.setText("PCE2 (MEL504)")
                self.lbim312.setText("MP2A (MEL505)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Mechanical" and semester == "Semester 6"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("MD (MEC601)")
                self.lbim304.setText("TM (MEC602)")
                self.lbim305.setText("HVACAR (MEC603)")
                self.lbim306.setText("AAAI (MEC604)")
                self.lbim307.setText("DLOC2 (MEDLO602X)")
                self.lbim308.setText("MD (MEL601)")
                self.lbim309.setText("TM (MEL602)")
                self.lbim310.setText("HVACAR (MEL603)")
                self.lbim311.setText("MAA (MEL604)")
                self.lbim312.setText("MP2B (MEL605)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)



            elif (branch == "Mechanical" and semester == "Semester 7"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("MD (MEC701)")
                self.lbim304.setText("CAD (MEC702)")
                self.lbim305.setText("MUS (MEC703)")
                self.lbim306.setText("PPC (MEC704)")
                self.lbim307.setText("PLM (ILO701X)")
                self.lbim308.setText("PPE (MEL701)")
                self.lbim309.setText("EM (MEL702)")
                self.lbim310.setText("SCM (MEL703)")
                self.lbim311.setText("CFD (MEP704)")
                self.lbim312.setVisible(False)
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf312.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)



            elif (branch == "Mechanical" and semester == "Semester 8"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("DOMC (MEC801)")
                self.lbim304.setText("IEAM (MEC802)")
                self.lbim305.setText("PE (MEC803)")
                self.lbim306.setText("DLOC4 (MEDLO804X)")
                self.lbim307.setText("ILOC2(ILO802X)")
                self.lbim308.setText("DOMS (MEL801)")
                self.lbim309.setText("PE (MEL802)")
                self.lbim310.setText("PROJECT2 (MEP803)")
                self.lbim311.setVisible(False)
                self.lbim312.setVisible(False)
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf311.setVisible(False)
                self.tf312.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

                # it

            elif (branch == "Information technology" and semester == "Semester 3"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM-III (ITC301)")
                self.lbim304.setText("DSA (ITC302)")
                self.lbim305.setText("DBMS (ITC303)")
                self.lbim306.setText("POC (ITC304)")
                self.lbim307.setText("PCPF (ITC305)")
                self.lbim308.setText("DS LAB (ITL301)")
                self.lbim309.setText("SQL LAB(ITL302)")
                self.lbim310.setText("CPP LAB (ITL303)")
                self.lbim311.setText("JAVA LAB(ITL304)")
                self.lbim312.setText("MP-1A (ITL305)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Information technology" and semester == "Semester 4"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM-IV (ITC401)")
                self.lbim304.setText("CNND (ITC402)")
                self.lbim305.setText("OS(ITC403)")
                self.lbim306.setText("AT (ITC404)")
                self.lbim307.setText("COA (ITC405)")
                self.lbim308.setText("NETWORK LAB(ITL401)")
                self.lbim309.setText("Unix LAB(ITL402)")
                self.lbim310.setText("MP LAB (ITL403)")
                self.lbim311.setText("PYTHON LAB(ITL404)")
                self.lbim312.setText("MP-1b (ITL405)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Information technology" and semester == "Semester 5"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("IP (ITC501)")
                self.lbim304.setText("CNS (ITC502)")
                self.lbim305.setText("EEB (ITC503)")
                self.lbim306.setText("SE (ITC504)")
                self.lbim307.setText("OC (ITC505)")
                self.lbim308.setText("IP LAB(ITL501)")
                self.lbim309.setText("Security LAB(ITL502)")
                self.lbim310.setText("DO LAB (ITL503)")
                self.lbim311.setText("AdvanceDO LAB(ITL504)")
                self.lbim312.setText("PCE-II (ITL505)")
                self.lbim313.setText("MP2A (ITM501)")
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Information technology" and semester == "Semester 6"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("DMBI (ITC601)")
                self.lbim304.setText("WX.O(ITC602)")
                self.lbim305.setText("WT (ITC603)")
                self.lbim306.setText("AIDS (ITC604)")
                self.lbim307.setText("OC2 (ITC605)")
                self.lbim308.setText("BI LAB(ITL601)")
                self.lbim309.setText("Web LAB(ITL602)")
                self.lbim310.setText("SensorLAB (ITL603)")
                self.lbim311.setText("MAD LAB(ITL604)")
                self.lbim312.setText("DSP LAB (ITL605)")
                self.lbim313.setText("MP2B (ITM601")
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Information technology" and semester == "Semester 7"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("AIDS2 (ITC701)")
                self.lbim304.setText("IOE(ITC702)")
                self.lbim305.setText("OC3 (ITC703)")
                self.lbim306.setText("OC4 (ITC704)")
                self.lbim307.setText("Elective-I(ITC705)")
                self.lbim308.setText("DSL (ITL701)")
                self.lbim309.setText("IOE (ITL702)")
                self.lbim310.setText("SAD(ITL703)")
                self.lbim311.setText("ROSPL(ITL704)")
                self.lbim312.setText("MP1 (ITP701)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Information technology" and semester == "Semester 8"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("BCADLT (ITC801)")
                self.lbim304.setText("DOC5(ITD801X)")
                self.lbim305.setText("DOC6 (ITD802X)")
                self.lbim306.setText("IOC2 (ITIO801X)")
                self.lbim307.setText("BLCKCNL (ITl801)")
                self.lbim308.setText("CC (ITL802)")
                self.lbim309.setText("MP2 (ITP801)")
                self.lbim310.setVisible(False)
                self.lbim311.setVisible(False)
                self.lbim312.setVisible(False)
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf310.setVisible(False)
                self.tf311.setVisible(False)
                self.tf312.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

                # computer
            elif (branch == "Computer" and semester == "Semester 3"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM-III (CSC301)")
                self.lbim304.setText("DSGT(CSC302)")
                self.lbim305.setText("DS (CSC303)")
                self.lbim306.setText("DLCA (CSC304)")
                self.lbim307.setText("CG (CSC305)")
                self.lbim308.setText("DS Lab (CSL301)")
                self.lbim309.setText("DLCA Lab (CSL302)")
                self.lbim310.setText("CG lab(CSL303)")
                self.lbim311.setText("SBL (CSL304)")
                self.lbim312.setText("MP-1A (CSM301)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Computer" and semester == "Semester 4"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM-IV(CSC041)")
                self.lbim304.setText("AOA(CSC402)")
                self.lbim305.setText("DBMS (CSC403)")
                self.lbim306.setText("OS (CSC404)")
                self.lbim307.setText("Microprocessor (CSC405)")
                self.lbim308.setText("AOA Lab (CSL401)")
                self.lbim309.setText("DBMS Lab (CSL402)")
                self.lbim310.setText("OS lab(CSL403)")
                self.lbim311.setText("MP (CSL404)")
                self.lbim312.setText("SBLPP (CSL405)")
                self.lbim313.setText("MP1B (CSM401)")
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Computer" and semester == "Semester 5"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("TCS(CSC501)")
                self.lbim304.setText("SE(CSC502)")
                self.lbim305.setText("CN (CSC503)")
                self.lbim306.setText("DWM (CSC504)")
                self.lbim307.setText("DLOP1 (CSDL501X)")
                self.lbim308.setText("SE Lab (CSL501)")
                self.lbim309.setText("CN Lab (CSL502)")
                self.lbim310.setText("DWM lab(CSL503)")
                self.lbim311.setText("BCE-II (CSL504)")
                self.lbim312.setText("MP-2A (CSM501)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Computer" and semester == "Semester 6"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("SPCC(CSC601)")
                self.lbim304.setText("CSS(CSC602)")
                self.lbim305.setText("MC (CSC603)")
                self.lbim306.setText("AI (CSC604)")
                self.lbim307.setText("DLOP (CSC605)")
                self.lbim308.setText("SPCC Lab (CSL601)")
                self.lbim309.setText("CSS Lab (CSL602)")
                self.lbim310.setText("MC lab(CSL603)")
                self.lbim311.setText("AI (CSL604)")
                self.lbim312.setText("MP-2B (CSM601)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Computer" and semester == "Semester 7"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("ML(CSC701)")
                self.lbim304.setText("BDA(CSC702)")
                self.lbim305.setText("DLOP-3(CSDC701X)")
                self.lbim306.setText("DLOP-4 (CSDC702X)")
                self.lbim307.setText("ILO1 (ILO701X)")
                self.lbim308.setText("ML Lab (CSL701)")
                self.lbim309.setText("BDA Lab (CSL702)")
                self.lbim310.setText("DLOP-3 lab(CSL703)")
                self.lbim311.setText("DLOP-4 (CSL704)")
                self.lbim312.setText("ILOL (CSL705)")
                self.lbim313.setText("MP1 (CSP701)")
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)


            elif (branch == "Computer" and semester == "Semester 8"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("HMI (CSC801)")
                self.lbim304.setText("DC (CSC802)")
                self.lbim305.setText("DLO-4(CSDC801X)")
                self.lbim306.setText("IL0-2(ILO801X)")
                self.lbim307.setText("HMIL Lab (CSL801)")
                self.lbim308.setText("DCL Lab (CSL802)")
                self.lbim309.setText("CCL Lab (CSL803)")
                self.lbim310.setText("CL-II Lab(CSL804)")
                self.lbim311.setText("MP-II (CSP805)")
                self.lbim312.setVisible(False)
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf312.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            # aids
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 3"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM3 (CSC301)")
                self.lbim304.setText("DSACT (CSC302)")
                self.lbim305.setText("DS (CSC303)")
                self.lbim306.setText("DLACA (CSC304)")
                self.lbim307.setText("CG (CSC305)")
                self.lbim308.setText("DSL (CSL301)")
                self.lbim309.setText("DLACAL (CSL302)")
                self.lbim310.setText("CGL (CSL303)")
                self.lbim311.setText("PWJ (CSL304)")
                self.lbim312.setText("MP1A (CSM301)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Artificial intelligence and data science" and semester == "Semester 4"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM4 (CSC401)")
                self.lbim304.setText("AOA (CSC402)")
                self.lbim305.setText("DBMS (CSC403)")
                self.lbim306.setText("OS (CSC404)")
                self.lbim307.setText("MP (CSC405)")
                self.lbim308.setText("AOAL (CSL401)")
                self.lbim309.setText("DBMSL (CSL402)")
                self.lbim310.setText("OSL (CSL403)")
                self.lbim311.setText("MPL (CSL404)")
                self.lbim312.setText("PP (CSL405)")
                self.lbim313.setText("MP1B (CSM401)")
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Artificial intelligence and data science" and semester == "Semester 5"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("CN (CSC501)")
                self.lbim304.setText("WBC (CSC502)")
                self.lbim305.setText("AI(CSC503)")
                self.lbim306.setText("DWAM (CSC504)")
                self.lbim307.setText("DLOC1 (CSDLO501X)")
                self.lbim308.setText("WBCANL (CSL501)")
                self.lbim309.setText("AIL (CSL502)")
                self.lbim310.setText("DWAML (CSL503)")
                self.lbim311.setText("BACE2 (CSL504)")
                self.lbim312.setText("MP2A (CSM501)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Artificial intelligence and data science" and semester == "Semester 6"):
                print("hello hi ")
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("DAAV (CSC601)")
                self.lbim304.setText("CASS (CSC602)")
                self.lbim305.setText("SEAPM(CSC603)")
                self.lbim306.setText("ML (CSC604)")
                self.lbim307.setText("DLOC2 (CSDLO601X)")
                self.lbim308.setText("DAAVL (CSL601)")
                self.lbim309.setText("CASSL (CSL602)")
                self.lbim310.setText("SEAPML (CSL603)")
                self.lbim311.setText("MLL (CSL604)")
                self.lbim312.setText("CC (CSM605)")
                self.lbim313.setText("MP2B (CSM601)")
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Artificial intelligence and data science" and semester == "Semester 7"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("ML(CSC701)")
                self.lbim304.setText("BDA(CSC702)")
                self.lbim305.setText("DLOP-3(CSDC701X)")
                self.lbim306.setText("DLOP-4 (CSDC702X)")
                self.lbim307.setText("ILO1 (ILO701X)")
                self.lbim308.setText("ML Lab (CSL701)")
                self.lbim309.setText("BDA Lab (CSL702)")
                self.lbim310.setText("DLOP-3 lab(CSL703)")
                self.lbim311.setText("DLOP-4 (CSL704)")
                self.lbim312.setText("MP1 (CSP701)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)


            elif (branch == "Artificial intelligence and data science" and semester == "Semester 8"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("HMI (CSC801)")
                self.lbim304.setText("DC (CSC802)")
                self.lbim305.setText("DLO-4(CSDC801X)")
                self.lbim306.setText("IL0-2(ILO801X)")
                self.lbim307.setText("HMIL Lab (CSL801)")
                self.lbim308.setText("DCL Lab (CSL802)")
                self.lbim309.setText("CCL Lab (CSL802)")
                self.lbim310.setText("CL-II Lab(CSL803)++")
                self.lbim311.setText("MP-II (CSL804)")
                self.lbim312.setText("MP-2 (CSP801)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            #extc

            elif (branch == "Electronics and telecommunication" and semester == "Semester 3"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM3 (ECC301)")
                self.lbim304.setText("EDAC (ECC302)")
                self.lbim305.setText("DSD (ECC303)")
                self.lbim306.setText("NT (ECC304)")
                self.lbim307.setText("EIACS (ECC305)")
                self.lbim308.setText("EDACL (ECL301)")
                self.lbim309.setText("DSDL (ECL302)")
                self.lbim310.setText("EIACSL (ECL303)")
                self.lbim311.setText("C++JV (ECL304)")
                self.lbim312.setText("MP1A (ECM301)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)


            elif (branch == "Electronics and telecommunication" and semester == "Semester 4"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EM4 (ECC401)")
                self.lbim304.setText("MC (ECC402)")
                self.lbim305.setText("LIC (ECC403)")
                self.lbim306.setText("SAS (ECC404)")
                self.lbim307.setText("POCE (ECC405)")
                self.lbim308.setText("MCL (ECL401)")
                self.lbim309.setText("LICL (ECL402)")
                self.lbim310.setText("POCEL (ECL403)")
                self.lbim311.setText("PP (ECL404)")
                self.lbim312.setText("MP1B (ECM401)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Electronics and telecommunication" and semester == "Semester 5"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("DC (ECC501)")
                self.lbim304.setText("DTSP (ECC502)")
                self.lbim305.setText("DVLSI (ECC503)")
                self.lbim306.setText("RSA (ECC504)")
                self.lbim307.setText("DLOC1 (ECCDLO501X)")
                self.lbim308.setText("DCL (ECL501)")
                self.lbim309.setText("DTSPL (ECL502)")
                self.lbim310.setText("DVLSIL (ECL503)")
                self.lbim311.setText("PCE2 (ECL504)")
                self.lbim312.setText("MP2A (ECM501)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Electronics and telecommunication" and semester == "Semester 6"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("EMAA (ECC601)")
                self.lbim304.setText("CCN (ECC602)")
                self.lbim305.setText("IPAMV (ECC603)")
                self.lbim306.setText("ANNAFL (ECC604)")
                self.lbim307.setText("DLOC2 (ECCDLO601X)")
                self.lbim308.setText("EMAAL (ECL601)")
                self.lbim309.setText("CCNL (ECL602)")
                self.lbim310.setText("IPAMVL (ECL603)")
                self.lbim311.setText("LANASC (ECL604)")
                self.lbim312.setText("MP2B (ECM601)")
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Electronics and telecommunication" and semester == "Semester 7"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("MWE (ECC701)")
                self.lbim304.setText("MCS (ECC702)")
                self.lbim305.setText("DLOC3 (ECCDLO701X)")
                self.lbim306.setText("DLOC4 (ECCDLO702X)")
                self.lbim307.setText("ILOC1 (ILO701X)")
                self.lbim308.setText("MWEL (ECL701)")
                self.lbim309.setText("MCSL (ECL702)")
                self.lbim310.setText("MP1 (ECM701)")
                self.lbim311.setVisible(False)
                self.lbim312.setVisible(False)
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf311.setVisible(False)
                self.tf312.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)

            elif (branch == "Electronics and telecommunication" and semester == "Semester 8"):
                self.lbim301.setText("Student no.")
                self.lbim302.setText("Student name")
                self.lbim303.setText("RFD (ECC801)")
                self.lbim304.setText("WRLSN (ECC802)")
                self.lbim305.setText("DLOC4 (ECCDLO804X)")
                self.lbim306.setText("ILOC2 (ILO802X)")
                self.lbim307.setText("RFDL (ECL801)")
                self.lbim308.setText("WRLSNL (ECL802)")
                self.lbim309.setText("DLOCL (ECLDLO804X)")
                self.lbim310.setText("P2 (ECM801)")
                self.lbim311.setVisible(False)
                self.lbim312.setVisible(False)
                self.lbim313.setVisible(False)
                self.lbim314.setVisible(False)
                self.lbim315.setVisible(False)
                self.tf311.setVisible(False)
                self.tf312.setVisible(False)
                self.tf313.setVisible(False)
                self.tf314.setVisible(False)
                self.tf315.setVisible(False)


    def insertmarks3(self):
        branch = self.cb31.currentText()
        semester = self.cb32.currentText()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abesaale123",
            database="college_result_management_sys"
        )

        # Define a cursor object to interact with the database
        my = mydb.cursor()
        # Get the selected value from cb301
        selected_roll_no = self.tf301.currentText()

        # Get the corresponding data from the database using the selected roll no
        # Replace the placeholders in the query with the actual table and column names
        my.execute("SELECT Name FROM  studdetails WHERE Roll_no = %s AND Semester=%s AND Branch=%s", (selected_roll_no,semester,branch))
        result = my.fetchall()
        print (result)

        # Clear any existing items from cb302
        self.tf302.clear()

        # Populate cb302 with the results of the query
        for item in result:
            self.tf302.addItem(str(item[0]))



    def insertmarkssem1it(self):
        branch = self.cb31.currentText()
        semester = self.cb32.currentText()



        if(self.b32.clicked):
         if (semester == "Semester 1"):

            Student_no = int(self.tf301.currentText())
            Student_name = (self.tf302.currentText())
            FEC101 = int(self.tf303.text())
            FEC102 = int(self.tf304.text())
            FEC103 = int(self.tf305.text())
            FEC104 = int(self.tf306.text())
            FEC105 = int(self.tf307.text())
            FEL101 = int(self.tf308.text())
            FEL102 = int(self.tf309.text())
            FEL103 = int(self.tf310.text())
            FEL104 = int(self.tf311.text())
            FEL105 = int(self.tf312.text())




            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="abesaale123",
                    database="college_result_management_sys"
                )
                cursor = conn.cursor()
                cgpa = ((((FEC101 + FEC102 + FEC103+ FEC104+ FEC105 + FEL101 + FEL102+ FEL103 +FEL104 + FEL105) * 100) / 1000) / 9.0)
                if (0 < cgpa < 3.9):
                    GRADE = "F"
                elif (4 < cgpa < 4.49):
                    GRADE = "P"
                elif (4.5 < cgpa < 4.99):
                    GRADE = "E"
                elif (5 < cgpa < 5.99):
                    GRADE = "D"
                elif (6 < cgpa < 6.99):
                    GRADE = "C"
                elif (7 < cgpa < 7.49):
                    GRADE = "B"
                elif (7.5 < cgpa < 7.99):
                    GRADE = "A"
                elif (8 < cgpa < 10):
                    GRADE = "O"
                v = (Student_no, Student_name,FEC101, FEC102, FEC103, FEC104, FEC105, FEL101,FEL102, FEL103,FEL104,FEL105, cgpa,GRADE)

                querry = "" "Insert into " \
                         "college_result_management_sys.IT_SEM1_2(ID,NAME,FEC101," \
                         "FEC102," \
                         "FEC103,FEC104,FEC105," \
                         "FEL101,FEL102,FEL103," \
                         "FEL104,FEL105,CGPA,grade)" \
                         "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(querry, v)
                conn.commit()
                QMessageBox.information(self,"Message", "{}".format(cgpa))
                conn.close()
            except Exception as e:
                QMessageBox.information(self,"Error", "Error in database connection or query execution: {}".format(e))

            finally:
                cursor.close()
                conn.close()
        #computer
         elif (branch == "Computer" and semester == "Semester 3"):

             Student_no = int(self.tf301.currentText())
             Student_name = self.tf302.currentText()
             CSC301 = int(self.tf303.text())
             CSC302 = int(self.tf304.text())
             CSC303 = int(self.tf305.text())
             CSC304 = int(self.tf306.text())
             CSC305 = int(self.tf307.text())

             CSL301 = int(self.tf308.text())
             CSL302 = int(self.tf309.text())
             CSL303 = int(self.tf310.text())
             CSL304 = int(self.tf311.text())
             CSM301 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((CSC301 + CSC302 + CSC303 + CSC304 + CSC305 + CSL301 + CSL302 + CSL303 + CSL304 + CSM301) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (Student_no, Student_name, CSC301, CSC302, CSC303, CSC304, CSC305, CSL301, CSL302, CSL303, CSL304, CSM301, cgpa, GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.COMPS_SEM_3(ID,NAME,CSC301," \
                          "CSC302," \
                          "CSC303,CSC304,CSC305," \
                          "CSL301,CSL302,CSL303," \
                          "CSL304,CSM301,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Computer" and semester == "Semester 4"):

             Student_no = int(self.tf301.currentText())
             Student_name = self.tf302.currentText()
             CSC401 = int(self.tf303.text())
             CSC402 = int(self.tf304.text())
             CSC403 = int(self.tf305.text())
             CSC404 = int(self.tf306.text())
             CSC405 = int(self.tf307.text())
             CSL401 = int(self.tf308.text())
             CSL402 = int(self.tf309.text())
             CSL403 = int(self.tf310.text())
             CSL404 = int(self.tf311.text())
             CSM401 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   CSC401 + CSC402 + CSC403 + CSC404 + CSC405 + CSL401 + CSL402 + CSL403 + CSL404 + CSM401) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                     Student_no, Student_name, CSC401, CSC402, CSC403, CSC404, CSC405, CSL401, CSL402, CSL403, CSL404,
                     CSM401, cgpa,
                     GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.COMPS_SEM4(ID,NAME,CSC401," \
                          "CSC402," \
                          "CSC403,CSC404,CSC405," \
                          "CSL401,CSL402,CSL403," \
                          "CSL404,CSM401,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()
         elif (branch == "Computer" and semester == "Semester 5"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             CSC501 = int(self.tf303.text())
             CSC502 = int(self.tf304.text())
             CSC503 = int(self.tf305.text())
             CSC504 = int(self.tf306.text())
             CSC505 = int(self.tf307.text())
             CSL501 = int(self.tf308.text())
             CSL502 = int(self.tf309.text())
             CSL503 = int(self.tf310.text())
             CSL504 = int(self.tf311.text())
             CSM501 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   CSC501 + CSC502 + CSC503 + CSC504 + CSC505 + CSL501 + CSL502 + CSL503 + CSL504 + CSM501) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                     Student_no, Student_name, CSC501, CSC502, CSC503, CSC504, CSC505, CSL501, CSL502, CSL503, CSL504,
                     CSM501, cgpa,
                     GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.COMPS_SEM5(ID,NAME,CSC501," \
                          "CSC502," \
                          "CSC503,CSC504,CSC505," \
                          "CSL501,CSL502,CSL503," \
                          "CSL504,CSM501,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()
         elif (branch == "Computer" and semester == "Semester 6"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             CSC601 = int(self.tf303.text())
             CSC602 = int(self.tf304.text())
             CSC603 = int(self.tf305.text())
             CSC604 = int(self.tf306.text())
             CSDL0601X = int(self.tf307.text())
             CSL601 = int(self.tf308.text())
             CSL602 = int(self.tf309.text())
             CSL603 = int(self.tf310.text())
             CSL604 = int(self.tf311.text())
             CSL605 = int(self.tf312.text())
             CSM601 = int(self.tf313.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   CSC601 + CSC602 + CSC603 + CSC604 + CSDL0601X + CSL601 + CSL602 + CSL603 + CSL604 + CSL605 + CSM601) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (Student_no, Student_name, CSC601, CSC602, CSC603, CSC604, CSDL0601X, CSL601, CSL602, CSL603, CSL604,
                      CSL605, CSM601, cgpa,
                      GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.COMPS_SEM6(ID,NAME,CSC601," \
                          "CSC602," \
                          "CSC603,CSC604,CSDL0601X," \
                          "CSL601,CSL602,CSL603," \
                          "CSL604,CSL605,CSM601,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Comnputer" and semester == "Semester 7"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             CSC701 = int(self.tf303.text())
             CSC702 = int(self.tf304.text())
             CDSC701X = int(self.tf305.text())
             CDSC702X = int(self.tf306.text())
             ILO701X = int(self.tf307.text())
             CSL701 = int(self.tf308.text())
             CSL702 = int(self.tf309.text())
             CSDL701X = int(self.tf310.text())
             CSDL702X = int(self.tf311.text())
             CSP701 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   CSC701 + CSC702 + CDSC701X + CDSC702X + ILO701X + CSL701 + CSL702 + CSDL701X + CSDL702X + CSP701) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, CSC701, CSC702, CDSC701X, CDSC702X, ILO701X, CSL701, CSL702, CSDL701X, CSDL702X,
                 CSP701, cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.COMPS_SEM7(ID,NAME,CSC701," \
                          "CSC702," \
                          "CDSC701X,CDSC702X,ILO701X," \
                          "CSL701,CSL702,CSDL701X," \
                          "CSDL702X,CSP701,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Computer" and semester == "Semester 8"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             CSC801 = int(self.tf303.text())
             CSC802 = int(self.tf304.text())
             CSDL0801X = int(self.tf305.text())
             ILO801X = int(self.tf306.text())
             CSL801 = int(self.tf307.text())
             CSL802 = int(self.tf308.text())
             CSL803 = int(self.tf309.text())
             CSL804 = int(self.tf310.text())
             CSP805 = int(self.tf311.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   CSC801 + CSC802 + CSDL0801X + ILO801X + CSL801 + CSL802 + CSL803 + CSL804 + CSP805) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, CSC801, CSC802, CSDL0801X, ILO801X, CSL801, CSL802, CSL803, CSL804, CSP805, cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.COMPS_SEM8(ID,NAME,CSC801," \
                          "CSC802," \
                          "CSDL0801X,ILO801X" \
                          "CSL801,CSL802,CSL803," \
                          "CSL804,CSP805,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()
         elif (branch == "Information technology" and semester == "Semester 3"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             ITC301 = int(self.tf303.text())
             ITC302 = int(self.tf304.text())
             ITC303 = int(self.tf305.text())
             ITC304 = int(self.tf306.text())
             ITC305 = int(self.tf307.text())
             ITL301 = int(self.tf308.text())
             ITL302 = int(self.tf309.text())
             ITL303 = int(self.tf310.text())
             ITL304 = int(self.tf311.text())
             ITM301 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   ITC301 + ITC302 + ITC303 + ITC304 + ITC305 + ITL301 + ITL302 + ITL303 + ITL304 + ITM301) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, ITC301, ITC302, ITC303, ITC304, ITC305, ITL301, ITL302, ITL303, ITL304, ITM301, cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.IT_SEM3(ID,NAME,ITC301," \
                          "ITC302," \
                          "ITC303,ITC304,ITC305,ITL301," \
                          "ITL302,ITL303,ITL304," \
                          "ITM301,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()
         elif (branch == "Information technology" and semester == "Semester 4"):

             '''Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             ITC401 = int(self.tf303.text())
             ITC402 = int(self.tf304.text())
             ITC403 = int(self.tf305.text())
             ITC404 = int(self.tf306.text())
             ITC405 = int(self.tf307.text())
             ITL401 = int(self.tf308.text())
             ITL402 = int(self.tf309.text())
             ITL403 = int(self.tf310.text())
             ITL404 = int(self.tf311.text())
             ITM401 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   ITC401 + ITC402 + ITC403 + ITC404 + ITC405 + ITL401 + ITL402 + ITL403 + ITL404 + ITM401) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"

                 if (ITC401 < 32):

                     subject_variable = "F"
                     pass_fail_variable = "Fail"
                 else:
                     subject_variable = ""
                     pass_fail_variable = "Pass"

                 print("pass or fail=", pass_fail_variable)
                 print("subject variable=", subject_variable)

                 hello_subject = str(ITC401)

                 test_variable = hello_subject + subject_variable
                 print("test variable=", test_variable)

                 v = (
                 Student_no, Student_name, ITC401, ITC402, ITC403, ITC404, ITC405, ITL401, ITL402, ITL403, ITL404, ITM401,
                 cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.IT_SEM4(ID,NAME,ITC401," \
                          "ITC402," \
                          "ITC403,ITC404,ITC405," \
                          "ITL401,ITL402,ITL403," \
                          "ITL404,ITM401,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()'''
             Student_no = int(self.tf301.currentText())
             Student_name = self.tf302.currentText()
             subject_scores = {
                 'ITC401': int(self.tf303.text()),
                 'ITC402': int(self.tf304.text()),
                 'ITC403': int(self.tf305.text()),
                 'ITC404': int(self.tf306.text()),
                 'ITC405': int(self.tf307.text()),
                 'ITL401': int(self.tf308.text()),
                 'ITL402': int(self.tf309.text()),
                 'ITL403': int(self.tf310.text()),
                 'ITL404': int(self.tf311.text()),
                 'ITM401': int(self.tf312.text())
             }
             pass_fail_variable = "Pass"

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 total_score = sum(subject_scores.values())
                 cgpa = total_score / 900 * 10

                 if 0 <= cgpa < 3.9:
                     grade = "F"
                 elif 3.9 <= cgpa < 4.5:
                     grade = "P"
                 elif 4.5 <= cgpa < 5:
                     grade = "E"
                 elif 5 <= cgpa < 6:
                     grade = "D"
                 elif 6 <= cgpa < 7:
                     grade = "C"
                 elif 7 <= cgpa < 7.5:
                     grade = "B"
                 elif 7.5 <= cgpa < 8:
                     grade = "A"
                 else:
                     grade = "O"

                 for subject, score in subject_scores.items():
                     if score < 32:
                         subject_variable = "F"
                         pass_fail_variable = "Fail"
                         grade = "--"
                         cgpa = "--"
                     else:
                         subject_variable = ""


                     score_with_variable = str(score) + subject_variable

                     subject_scores[subject] = score_with_variable

                     # print("test variable=", test_variable)
                 cgpa = '%.6s' % cgpa
                 v = (
                     Student_no, Student_name,
                     subject_scores['ITC401'], subject_scores['ITC402'], subject_scores['ITC403'],
                     subject_scores['ITC404'], subject_scores['ITC405'], subject_scores['ITL401'],
                     subject_scores['ITL402'], subject_scores['ITL403'], subject_scores['ITL404'],
                     subject_scores['ITM401'], cgpa, grade, pass_fail_variable
                 )

                 query = """INSERT INTO college_result_management_sys.IT_SEM4(ID, NAME, ITC401, ITC402, ITC403, ITC404,
                             ITC405, ITL401, ITL402, ITL403, ITL404, ITM401, CGPA, grade , RESULT)
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                 cursor.execute(query, v)
                 conn.commit()

                 QMessageBox.information(self, "Message", "Data Inserted")
                 # QMessageBox.information(self, "Message", f"CGPA: {cgpa}")
             except Exception as e:
                 QMessageBox.information(self, "Error", f"Error in database connection or query execution: {e}")
             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Information technology" and semester == "Semester 5"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             ITC501 = int(self.tf303.text())
             ITC502 = int(self.tf304.text())
             ITC503 = int(self.tf305.text())
             ITC504 = int(self.tf306.text())
             ITD0501X = int(self.tf307.text())
             ITL501 = int(self.tf308.text())
             ITL502 = int(self.tf309.text())
             ITL503 = int(self.tf310.text())
             ITL504 = int(self.tf311.text())
             ITL505 = int(self.tf312.text())
             ITM501 = int(self.tf313.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   ITC501 + ITC502 + ITC503 + ITC504 + ITD0501X + ITL501 + ITL502 + ITL503 + ITL504 + ITL505 + ITM501) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, ITC501, ITC502, ITC503, ITC504, ITD0501X, ITL501, ITL502, ITL503, ITL504, ITL505,
                 ITM501, cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.IT_SEM5(ID,NAME,ITC501," \
                          "ITC502," \
                          "ITC503,ITC504,ITD0501X," \
                          "ITL501,ITL502,ITL503," \
                          "ITL504,ITL505,ITM501,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Information technology" and semester == "Semester 6"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             ITC601 = int(self.tf303.text())
             ITC602 = int(self.tf304.text())
             ITC603 = int(self.tf305.text())
             ITC604 = int(self.tf306.text())
             ITD0601X = int(self.tf307.text())
             ITL601 = int(self.tf308.text())
             ITL602 = int(self.tf309.text())
             ITL603 = int(self.tf310.text())
             ITL604 = int(self.tf311.text())
             ITL605 = int(self.tf312.text())
             ITM601 = int(self.tf313.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   ITC601 + ITC602 + ITC603 + ITC604 + ITD0601X + ITL601 + ITL602 + ITL603 + ITL604 + ITL605 + ITM601) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, ITC601, ITC602, ITC603, ITC604, ITD0601X, ITL601, ITL602, ITL603, ITL604, ITL605,
                 ITM601, cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.IT_SEM6(ID,NAME,ITC601," \
                          "ITC602," \
                          "ITC603,ITC604,ITD0601X," \
                          "ITL601,ITL602,ITL603," \
                          "ITL604,ITL605,ITM601,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()


         elif (branch == "Information technology" and semester == "Semester 7"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             ITC701 = int(self.tf303.text())
             ITC702 = int(self.tf304.text())
             ITDO701X = int(self.tf305.text())
             ITD0702X = int(self.tf306.text())
             ITIO701X = int(self.tf307.text())
             ITL701 = int(self.tf308.text())
             ITL702 = int(self.tf309.text())
             ITL703 = int(self.tf310.text())
             ITL704 = int(self.tf311.text())
             ITP701 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   ITC701 + ITC702 + ITDO701X + ITD0702X + ITIO701X + ITL701 + ITL702 + ITL703 + ITL704 + ITP701) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (Student_no, Student_name, ITC701, ITC702, ITDO701X, ITD0702X, ITIO701X, ITL701, ITL702, ITL703, ITL704,
                      ITP701, cgpa,
                      GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.IT_SEM7(ID,NAME,ITC701," \
                          "ITC702," \
                          "ITDO701X,ITD0702X,ITIO701X," \
                          "ITL701,ITL702,ITL703," \
                          "ITL704,ITP701,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Information technology" and semester == "Semester 8"):

            Student_no = int(self.tf301.currentText())
            Student_name = (self.tf302.currentText())
            ITC801 = int(self.tf303.text())
            ITDO801X = int(self.tf304.text())
            ITDO802X = int(self.tf305.text())
            ITIO801X = int(self.tf306.text())
            ITL801 = int(self.tf307.text())
            ITL802 = int(self.tf308.text())
            ITP801 = int(self.tf309.text())

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="abesaale123",
                    database="college_result_management_sys"
                )
                cursor = conn.cursor()
                cgpa = ((((
                                  ITC801 + ITDO801X + ITDO802X + ITIO801X + ITL801 + ITL802 + ITP801) * 100) / 1000) / 9.0)
                if (0 < cgpa < 3.9):
                    GRADE = "F"
                elif (4 < cgpa < 4.49):
                    GRADE = "P"
                elif (4.5 < cgpa < 4.99):
                    GRADE = "E"
                elif (5 < cgpa < 5.99):
                    GRADE = "D"
                elif (6 < cgpa < 6.99):
                    GRADE = "C"
                elif (7 < cgpa < 7.49):
                    GRADE = "B"
                elif (7.5 < cgpa < 7.99):
                    GRADE = "A"
                elif (8 < cgpa < 10):
                    GRADE = "O"
                v = (Student_no, Student_name, ITC801, ITDO801X, ITDO802X, ITIO801X, ITL801, ITL802, ITP801, cgpa,
                     GRADE)

                querry = "" "Insert into " \
                         "college_result_management_sys.IT_SEM8(ID,NAME,ITC801," \
                         "ITDO801X," \
                         "ITDO802X,ITIO801X,ITL801,ITL802," \
                         "ITP801," \
                         "FEL104,FEL105,CGPA,grade)" \
                         "values(%s,%s,%s,%s,%s,%s,%s,%s,,%s,%s)"""
                cursor.execute(querry, v)
                conn.commit()
                QMessageBox.information(self, "Message", "{}".format(cgpa))
                conn.close()
            except Exception as e:
                QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

            finally:
                cursor.close()
                conn.close()

         elif (branch == "Mechanical" and semester == "Semester 3"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             MEC301 = int(self.tf303.text())
             MEC302 = int(self.tf304.text())
             MEC303 = int(self.tf305.text())
             MEC304 = int(self.tf306.text())
             MEC305 = int(self.tf307.text())
             MEL301 = int(self.tf308.text())
             MEL302 = int(self.tf309.text())
             MEL303 = int(self.tf310.text())
             MEL304 = int(self.tf311.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   MEC301 + MEC302 + MEC303 + MEC304 + MEC305 + MEL301 + MEL302 + MEL303 + MEL304) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, MEC301, MEC302, MEC303, MEC304, MEC305, MEL301, MEL302, MEL303, MEL304, cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.MECH_SEM_3(ID,NAME,MEC301," \
                          "MEC302," \
                          "MEC303,MEC304,MEC305," \
                          "MEL301,MEL302,MEL303," \
                          "MEL304,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Mechanical" and semester == "Semester 4"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             MEC401 = int(self.tf303.text())
             MEC402 = int(self.tf304.text())
             MEC403 = int(self.tf305.text())
             MEC404 = int(self.tf306.text())
             MEC405 = int(self.tf307.text())
             MEL401 = int(self.tf308.text())
             MEL402 = int(self.tf309.text())
             MEL403 = int(self.tf310.text())
             MEL404 = int(self.tf311.text())
             MEL405 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   MEC401 + MEC402 + MEC403 + MEC404 + MEC405 + MEL401 + MEL402 + MEL403 + MEL404 + MEL405) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, MEC401, MEC402, MEC403, MEC404, MEC405, MEL401, MEL402, MEL403, MEL404, MEL405,
                 cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.MECH_SEM_4(ID,NAME,MEC401," \
                          "MEC402," \
                          "MEC403,MEC404,MEC405," \
                          "MEL401,MEL402,MEL403," \
                          "MEL404,MEL405,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Mechanical" and semester == "Semester 5"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             MEC501 = int(self.tf303.text())
             MEC502 = int(self.tf304.text())
             MEC503 = int(self.tf305.text())
             MEC504 = int(self.tf306.text())
             MEDLO501X = int(self.tf307.text())
             MEL501 = int(self.tf308.text())
             MEL502 = int(self.tf309.text())
             MEL503 = int(self.tf310.text())
             MEL504 = int(self.tf311.text())
             MEL505 = int(self.tf312.text())
             MEL506 = int(self.tf313.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   MEC501 + MEC502 + MEC503 + MEC504 + MEDLO501X + MEL501 + MEL502 + MEL503 + MEL504 + MEL505 + MEL506) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (Student_no, Student_name, MEC501, MEC502, MEC503, MEC504, MEDLO501X, MEL501, MEL502, MEL503, MEL504,
                      MEL505, MEL506, cgpa,
                      GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.MECH_SEM_5(ID,NAME,MEC501," \
                          "MEC502," \
                          "MEC503,MEC504,MEDLO501X," \
                          "MEL501,MEL502,MEL503," \
                          "MEL504,MEL505,MEL506,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%S)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Mechanical" and semester == "Semester 6"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             MEC601 = int(self.tf303.text())
             MEC602 = int(self.tf304.text())
             MEC603 = int(self.tf305.text())
             MEC604 = int(self.tf306.text())
             MEDL0602X = int(self.tf307.text())
             MEL601 = int(self.tf308.text())
             MEL602 = int(self.tf309.text())
             MEL603 = int(self.tf310.text())
             MEL604 = int(self.tf311.text())
             MEL605 = int(self.tf312.text())
             MEL606 = int(self.tf313.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   MEC601 + MEC602 + MEC603 + MEC604 + MEDL0602X + MEL601 + MEL602 + MEL603 + MEL604 + MEL605 + MEL606) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (Student_no, Student_name, MEC601, MEC602, MEC603, MEC604, MEDL0602X, MEL601, MEL602, MEL603, MEL604,
                      MEL605, MEL606, cgpa,
                      GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.MECH_SEM_6(ID,NAME,MEC601," \
                          "MEC602," \
                          "MEC603,MEC604,MEDL0602X," \
                          "MEL601,MEL602,MEL603," \
                          "MEL604,MEL605,MEL606,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%S)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Mechanical" and semester == "Semester 7"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             MEC701 = int(self.tf303.text())
             MEC702 = int(self.tf304.text())
             MEC703 = int(self.tf305.text())
             MEDLO703X = int(self.tf306.text())
             IL0701X = int(self.tf307.text())
             MEL701 = int(self.tf308.text())
             MEL702 = int(self.tf309.text())
             MEL703 = int(self.tf310.text())
             MEP704 = int(self.tf311.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   MEC701 + MEC702 + MEC703 + MEDLO703X + IL0701X + MEL701 + MEL702 + MEL703 + MEP704) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, MEC701, MEC702, MEC703, MEDLO703X, IL0701X, MEL701, MEL702, MEL703, MEP704, cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.MECH_SEM_7(ID,NAME,MEC701," \
                          "MEC702," \
                          "MEC703,MEDLO703X,IL0701X," \
                          "MEL701,MEL702,MEL703," \
                          "MEP704,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Mechanical" and semester == "Semester 8"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             MEC801 = int(self.tf303.text())
             MEC802 = int(self.tf304.text())
             MEC803 = int(self.tf305.text())
             MEDLO804X = int(self.tf306.text())
             ILO802X = int(self.tf307.text())
             MEL801 = int(self.tf308.text())
             MEL802 = int(self.tf309.text())
             MEP803 = int(self.tf310.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   MEC801 + MEC802 + MEC803 + MEDLO804X + ILO802X + MEL801 + MEL802 + MEP803) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (Student_no, Student_name, MEC801, MEC802, MEC803, MEDLO804X, ILO802X, MEL801, MEL802, MEP803, cgpa,
                      GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.MECH_SEM_8(ID,NAME,MEC801," \
                          "MEC802," \
                          "MEC803,MEDLO804X,ILO802X," \
                          "MEL801,MEL802,MEP803," \
                          "CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()



         elif (branch == "Electronics and telecommunication" and semester == "Semester 3"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             ECC301 = int(self.tf303.text())
             ECC302 = int(self.tf304.text())
             ECC303 = int(self.tf305.text())
             ECC304 = int(self.tf306.text())
             ECC305 = int(self.tf307.text())
             ECL301 = int(self.tf308.text())
             ECL302 = int(self.tf309.text())
             ECL303 = int(self.tf310.text())
             ECL304 = int(self.tf311.text())
             ECM301 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   ECC301 + ECC302 + ECC303 + ECC304 + ECC305 + ECL301 + ECL302 + ECL303 + ECL304 + ECM301) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, ECC301, ECC302, ECC303, ECC304, ECC305, ECL301, ECL302, ECL303, ECL304, ECM301,
                 cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.EXTC_SEM3(ID,NAME,ECC301," \
                          "ECC302," \
                          "ECC303,ECC304,ECC305," \
                          "ECL301,ECL302,ECL303," \
                          "ECL304,ECM301,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Electronics and telecommunication" and semester == "Semester 4"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             ECC401 = int(self.tf303.text())
             ECC402 = int(self.tf304.text())
             ECC403 = int(self.tf305.text())
             ECC404 = int(self.tf306.text())
             ECC405 = int(self.tf307.text())
             ECL401 = int(self.tf308.text())
             ECL402 = int(self.tf309.text())
             ECL403 = int(self.tf310.text())
             ECL404 = int(self.tf311.text())
             ECM401 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   ECC401 + ECC402 + ECC403 + ECC404 + ECC405 + ECL401 + ECL402 + ECL403 + ECL404 + ECM401) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, ECC401, ECC402, ECC403, ECC404, ECC405, ECL401, ECL402, ECL403, ECL404, ECM401,
                 cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.EXTC_SEM4(ID,NAME,ECC401," \
                          "ECC402," \
                          "ECC403,ECC404,ECC405," \
                          "ECL401,ECL402,ECL403," \
                          "ECL404,ECM401,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Electronics and telecommunication" and semester == "Semester 5"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             ECC501 = int(self.tf303.text())
             ECC502 = int(self.tf304.text())
             ECC503 = int(self.tf305.text())
             ECC504 = int(self.tf306.text())
             ECCDLO501X = int(self.tf307.text())
             ECL501 = int(self.tf308.text())
             ECL502 = int(self.tf309.text())
             ECL503 = int(self.tf310.text())
             ECL504 = int(self.tf311.text())
             ECM501 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   ECC501 + ECC502 + ECC503 + ECC504 + ECCDLO501X + ECL501 + ECL502 + ECL503 + ECL504 + ECM501) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (Student_no, Student_name, ECC501, ECC502, ECC503, ECC504, ECCDLO501X, ECL501, ECL502, ECL503, ECL504,
                      ECM501, cgpa,
                      GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.EXTC_SEM5(ID,NAME,ECC501," \
                          "ECC502," \
                          "ECC503,ECC504,ECCDLO501X," \
                          "ECL501,ECL502,ECL503," \
                          "ECL504,ECM501,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Electronics and telecommunication" and semester == "Semester 6"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             ECC601 = int(self.tf303.text())
             ECC602 = int(self.tf304.text())
             ECC603 = int(self.tf305.text())
             ECC604 = int(self.tf306.text())
             ECCDLO601X = int(self.tf307.text())
             ECL601 = int(self.tf308.text())
             ECL602 = int(self.tf309.text())
             ECL603 = int(self.tf310.text())
             ECL604 = int(self.tf311.text())
             ECM601 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   ECC601 + ECC602 + ECC603 + ECC604 + ECCDLO601X + ECL601 + ECL602 + ECL603 + ECL604 + ECM601) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (Student_no, Student_name, ECC601, ECC602, ECC603, ECC604, ECCDLO601X, ECL601, ECL602, ECL603, ECL604,
                      ECM601, cgpa,
                      GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.MECH_SEM6(ID,NAME,ECC601," \
                          "ECC602," \
                          "ECC603,ECC604,ECCDLO601X," \
                          "ECL601,ECL602,ECL603," \
                          "ECL604,ECM601,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Electronics and telecommunication" and semester == "Semester 7"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             ECC701 = int(self.tf303.text())
             ECC702 = int(self.tf304.text())
             ECCDLO701X = int(self.tf305.text())
             ECCDLO702X = int(self.tf306.text())
             ECCILO701X = int(self.tf307.text())
             ECL701 = int(self.tf308.text())
             ECL702 = int(self.tf309.text())
             ECP701 = int(self.tf310.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   ECC701 + ECC702 + ECCDLO701X + ECCDLO702X + ECCILO701X + ECL701 + ECL702 + ECP701) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, ECC701, ECC702, ECCDLO701X, ECCDLO702X, ECCILO701X, ECL701, ECL702, ECP701, cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.EXTC_SEM7(ID,NAME,ECC701," \
                          "ECC702," \
                          "ECCDLO701X,ECCDLO702X,ECCILO701X," \
                          "ECL701,ECL702,ECP701," \
                          "CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Electronics and telecommunication" and semester == "Semester 8"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             ECC801 = int(self.tf303.text())
             ECC802 = int(self.tf304.text())
             ECCDLO804X = int(self.tf305.text())
             IL0802X = int(self.tf306.text())
             ECL801 = int(self.tf307.text())
             ECL802 = int(self.tf308.text())
             ECLDLO804X = int(self.tf309.text())
             ECL803 = int(self.tf310.text())
             FEL104 = int(self.tf311.text())
             FEL105 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   ECC801 + ECC802 + ECCDLO804X + IL0802X + ECL801 + ECL802 + ECLDLO804X + ECL803) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, ECC801, ECC802, ECCDLO804X, IL0802X, ECL801, ECL802, ECLDLO804X, ECL803, cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.EXTC_SEM8(ID,NAME,ECC801," \
                          "ECC802," \
                          "ECCDLO804X,IL0802X,ECL801," \
                          "ECL802,ECLDLO804X,ECL803," \
                          "CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Artificial intelligence and data science" and semester == "Semester 3"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             CSC301 = int(self.tf303.text())
             CSC302 = int(self.tf304.text())
             CSC303 = int(self.tf305.text())
             CSC304 = int(self.tf306.text())
             CSC305 = int(self.tf307.text())
             CSL301 = int(self.tf308.text())
             CSL302 = int(self.tf309.text())
             CSL303 = int(self.tf310.text())
             CSL304 = int(self.tf311.text())
             CSM301 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   CSC301 + CSC302 + CSC303 + CSC304 + CSC305 + CSL301 + CSL302 + CSL303 + CSL304 + CSM301) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, CSC301, CSC302, CSC303, CSC304, CSC305, CSL301, CSL302, CSL303, CSL304, CSM301,
                 cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.AIDS_SEM3(ID,NAME,CSC301," \
                          "CSC302," \
                          "CSC303,CSC304,CSC305," \
                          "CSL301,CSL302,CSL303," \
                          "CSL304,CSM301,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Artificial intelligence and data science" and semester == "Semester 4"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             CSC401 = int(self.tf303.text())
             CSC402 = int(self.tf304.text())
             CSC403 = int(self.tf305.text())
             CSC404 = int(self.tf306.text())
             CSC405 = int(self.tf307.text())
             CSL401 = int(self.tf308.text())
             CSL402 = int(self.tf309.text())
             CSL403 = int(self.tf310.text())
             CSL404 = int(self.tf311.text())
             CSM401 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   CSC401 + CSC402 + CSC403 + CSC404 + CSC405 + CSL401 + CSL402 + CSL403 + CSL404 + CSM401) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, CSC401, CSC402, CSC403, CSC404, CSC405, CSL401, CSL402, CSL403, CSL404, CSM401,
                 cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.AIDS_SEM4(ID,NAME,CSC401," \
                          "CSC402," \
                          "CSC403,CSC404,CSC405," \
                          "CSL401,CSL402,CSL403," \
                          "CSL404,CSM401,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Artificial intelligence and data science" and semester == "Semester 5"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             CSC501 = int(self.tf303.text())
             CSC502 = int(self.tf304.text())
             CSC503 = int(self.tf305.text())
             CSC504 = int(self.tf306.text())
             CSCDLO501X = int(self.tf307.text())
             CSL501 = int(self.tf308.text())
             CSL502 = int(self.tf309.text())
             CSL503 = int(self.tf310.text())
             CSL504 = int(self.tf311.text())
             CSM501 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   CSC501 + CSC502 + CSC503 + CSC504 + CSCDLO501X + CSL501 + CSL502 + CSL503 + CSL504 + CSM501) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (Student_no, Student_name, CSC501, CSC502, CSC503, CSC504, CSCDLO501X, CSL501, CSL502, CSL503, CSL504,
                      CSM501, cgpa,
                      GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.AIDS_SEM5(ID,NAME,CSC501," \
                          "CSC502," \
                          "CSC503,CSC504,CSCDLO501X," \
                          "CSL501,CSL502,CSL503," \
                          "CSL504,CSM501,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Artificial intelligence and data science" and semester == "Semester 6"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             CSC601 = int(self.tf303.text())
             CSC602 = int(self.tf304.text())
             CSC603 = int(self.tf305.text())
             CSC604 = int(self.tf306.text())
             CSCDLO601X = int(self.tf307.text())
             CSL601 = int(self.tf308.text())
             CSL602 = int(self.tf309.text())
             CSL603 = int(self.tf310.text())
             CSL604 = int(self.tf311.text())
             CSL605 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   CSC601 + CSC602 + CSC603 + CSC604 + CSCDLO601X + CSL601 + CSL602 + CSL603 + CSL604 + CSL605) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (Student_no, Student_name, CSC601, CSC602, CSC603, CSC604, CSCDLO601X, CSL601, CSL602, CSL603, CSL604,
                      CSL605, cgpa,
                      GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.AIDS_SEM6(ID,NAME,CSC601," \
                          "CSC602," \
                          "CSC603,CSC604,CSCDLO601X," \
                          "CSL601,CSL602,CSL603," \
                          "CSL604,CSL605,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Artificial intelligence and data science" and semester == "Semester 7"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             CSC701 = int(self.tf303.text())
             CSC702 = int(self.tf304.text())
             CDSC701X = int(self.tf305.text())
             CDSC702X = int(self.tf306.text())
             IL0701X = int(self.tf307.text())
             CSL701 = int(self.tf308.text())
             CSL702 = int(self.tf309.text())
             CSDL701X = int(self.tf310.text())
             CSDL702X = int(self.tf311.text())
             CSP701 = int(self.tf312.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   CSC701 + CSC702 + CDSC701X + CDSC702X + IL0701X + CSL701 + CSL702 + CSDL701X + CSDL702X + CSP701) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, CSC701, CSC702, CDSC701X, CDSC702X, IL0701X, CSL701, CSL702, CSDL701X, CSDL702X,
                 CSP701, cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.AIDS_SEM7(ID,NAME,CSC701," \
                          "CSC702," \
                          "CDSC701X,CDSC702X,IL0701X," \
                          "CSL701,CSL702,CSDL701X," \
                          "CSDL702X,CSP701,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

         elif (branch == "Artificial intelligence and data science" and semester == "Semester 8"):

             Student_no = int(self.tf301.currentText())
             Student_name = (self.tf302.currentText())
             CSC801 = int(self.tf303.text())
             CSC802 = int(self.tf304.text())
             CSDL0801X = int(self.tf305.text())
             IL0801X = int(self.tf306.text())
             CSL801 = int(self.tf307.text())
             CSL802 = int(self.tf308.text())
             CSL803 = int(self.tf309.text())
             CSL804 = int(self.tf310.text())
             CSP805 = int(self.tf311.text())

             try:
                 conn = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="abesaale123",
                     database="college_result_management_sys"
                 )
                 cursor = conn.cursor()
                 cgpa = ((((
                                   CSC801 + CSC802 + CSDL0801X + IL0801X + CSL801 + CSL802 + CSL803 + CSL804 + CSP805) * 100) / 1000) / 9.0)
                 if (0 < cgpa < 3.9):
                     GRADE = "F"
                 elif (4 < cgpa < 4.49):
                     GRADE = "P"
                 elif (4.5 < cgpa < 4.99):
                     GRADE = "E"
                 elif (5 < cgpa < 5.99):
                     GRADE = "D"
                 elif (6 < cgpa < 6.99):
                     GRADE = "C"
                 elif (7 < cgpa < 7.49):
                     GRADE = "B"
                 elif (7.5 < cgpa < 7.99):
                     GRADE = "A"
                 elif (8 < cgpa < 10):
                     GRADE = "O"
                 v = (
                 Student_no, Student_name, CSC801, CSC802, CSDL0801X, IL0801X, CSL801, CSL802, CSL803, CSL804, CSP805, cgpa,
                 GRADE)

                 querry = "" "Insert into " \
                          "college_result_management_sys.AIDS_SEM8(ID,NAME,CSC801," \
                          "CSC802," \
                          "CSDL0801X,IL0801X,CSL801," \
                          "CSL802,CSL803,CSL804," \
                          "CSP805,CGPA,grade)" \
                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                 cursor.execute(querry, v)
                 conn.commit()
                 QMessageBox.information(self, "Message", "{}".format(cgpa))
                 conn.close()
             except Exception as e:
                 QMessageBox.information(self, "Error", "Error in database connection or query execution: {}".format(e))

             finally:
                 cursor.close()
                 conn.close()

    def uploadmarks(self):
        branch = self.cb31.currentText()
        semester = self.cb32.currentText()
        if (self.b33.clicked.connect):

            if (semester == "Semester 1"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['FEC101'] + row['FEC102'] +
                                          row['FEC103'] + row['FEC104'] +
                                          row['FEC105'] + row['FEL101'] +
                                          row['FEL102'] + row['FEL103'] +
                                          row['FEL104'] + row['FEL105']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"



                        sql = """Insert into college_result_management_sys.IT_SEM1_2(ID,NAME,FEC101,
                                      FEC102,FEC103,FEC104,FEC105,
                                      FEL101,FEL102,FEL103,
                                      FEL104,FEL105,CGPA,grade)
                                      values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['FEC101'],
                                  row['FEC102'], row['FEC103'],
                                  row['FEC104'], row['FEC105'],
                                  row['FEL101'], row['FEL102'],
                                  row['FEL103'], row['FEL104'],
                                  row['FEL105'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error", str(e))
            elif (semester == "Semester 2"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['FEC201'] + row['FEL201'] +
                                          row['FEC202'] + row['FEL202'] +
                                          row['FEC203'] + row['FEL203'] +
                                          row['FEC204'] + row['FEL204'] +
                                          row['FEC205'] + row['FEL205'] +
                                          row['FEC206'] + row['FEL206']) * 100) / 1000) / 9.0)

                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.AIDS_SEM2(ID,NAME,FEC201,
                                                  FEC202,FEC203,FEC204,FEC205,
                                                  FEC206,FEL201, FEL202,
                                                  FEL203,FEL204,FEL205,FEL206,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['FEC201'],
                                  row['FEC202'], row['FEC203'],
                                  row['FEC204'], row['FEC205'],
                                  row['FEC206'], row['FEL201'],
                                  row['FEL202'], row['FEL203'],
                                  row['FEL204'], row['FEL205'],
                                  row['FEL206'], row['CGPA'],
                                  row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Mechanical" and semester == "Semester 3"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['MEC301'] + row['MEL301'] +
                                          row['MEC302'] + row['MEL302'] +
                                          row['MEC303'] + row['MEL303'] +
                                          row['MEC304'] + row['MEL304'] +
                                          row['MEC305']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.MECH_SEM3(ID,NAME,MEC301,
                                                      MEC302,MEC303,MEC304,MEC305,
                                                      MEL301,MEL302,MEL303,
                                                      MEL304,CGPA,GRADE)
                                                      values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['MEC301'],
                                  row['MEC302'], row['MEC303'],
                                  row['MEC304'], row['MEC305'],
                                  row['MEL301'], row['MEL302'],
                                  row['MEL303'], row['MEL304'],
                                  row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))
                    QMessageBox.critical(self, "Error", str(e))
            elif (branch == "Mechanical" and semester == "Semester 4"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['MEC401'] + row['MEL401'] +
                                          row['MEC402'] + row['MEL402'] +
                                          row['MEC403'] + row['MEL403'] +
                                          row['MEC404'] + row['MEL404'] +
                                          row['MEC405'] + row['MEL405']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.MECH_SEM4(ID,NAME,MEC401,
                                                      MEC402,MEC403,MEC404,MEC405,
                                                      MEL401,MEL402,MEL403,
                                                      MEL404,MEL405,CGPA,GRADE)
                                                      values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['MEC401'],
                                  row['MEC402'], row['MEC403'],
                                  row['MEC404'], row['MEC405'],
                                  row['MEL401'], row['MEL402'],
                                  row['MEL403'], row['MEL404'],
                                  row['MEL405'], row['CGPA'],
                                  row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")

                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error", str(e))
            elif (branch == "Mechanical" and semester == "Semester 5"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['MEC501'] + row['MEL501'] +
                                          row['MEC502'] + row['MEL502'] +
                                          row['MEC503'] + row['MEL503'] +
                                          row['MEC504'] + row['MEL504'] +
                                          row['MEDLO501X'] + row['MEL505'] +
                                          row['MEL506']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.MECH_SEM5(ID,NAME,MEC501,
                                                       MEC502,MEC503,MEC504,MEDLO501X,
                                                       MEL501,MEL502,MEL503,
                                                       MEL504,MEL505,MEL506,CGPA,GRADE)
                                                       values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['MEC501'],
                                  row['MEC502'], row['MEC503'],
                                  row['MEC504'], row['MEDLO501X'],
                                  row['MEL501'], row['MEL502'],
                                  row['MEL503'], row['MEL504'],
                                  row['MEL505'], row['MEL506'],
                                  row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error", str(e))
            elif (branch == "Mechanical" and semester == "Semester 6"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['MEC601'] + row['MEL601'] +
                                          row['MEC602'] + row['MEL602'] +
                                          row['MEC603'] + row['MEL603'] +
                                          row['MEC604'] + row['MEL604'] +
                                          row['MEDLO602X'] + row['MEL605'] +
                                          row['MEL606']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.MECH_SEM6(ID,NAME,MEC601,
                                                      MEC602,MEC603,MEC604,MEDLO602X,
                                                      MEL601,MEL602,MEL603,
                                                      MEL604,MEL605,MEL606,CGPA,GRADE)
                                                      values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['MEC601'],
                                  row['MEC602'], row['MEC603'],
                                  row['MEC604'], row['MEDLO602X'],
                                  row['MEL601'], row['MEL602'],
                                  row['MEL603'], row['MEL604'],
                                  row['MEL605'], row['MEL606'],
                                  row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error", str(e))
            elif (branch == "Mechanical" and semester == "Semester 7"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['MEC701'] + row['MEL701'] +
                                          row['MEC702'] + row['MEL702'] +
                                          row['MEC703'] + row['MEL703'] +
                                          row['MEDLO703X'] + row['MEP704'] +
                                          row['ILO701X']) * 100) / 1000) / 9.0)

                    if (0 < row['CGPA'] < 3.9):
                        row['GRADE'] = "F"
                    elif (row['CGPA'] < 4.5):
                        row['GRADE'] = "P"
                    elif (row['CGPA'] < 5):
                        row['GRADE'] = "E"
                    elif (row['CGPA'] < 6):
                        row['GRADE'] = "D"
                    elif (row['CGPA'] < 7):
                        row['GRADE'] = "C"
                    elif (row['CGPA'] < 7.5):
                        row['GRADE'] = "B"
                    elif (row['CGPA'] < 8):
                        row['GRADE'] = "A"
                    else:
                        row['GRADE'] = "O"

                    sql = """Insert into college_result_management_sys.MECH_SEM7(ID,NAME,MEC701,
                                                          MEC702,MEC703,MEDLO703X,ILO701X,
                                                          MEL701,MEL702,MEL703,
                                                          MEP704,CGPA,GRADE)
                                                          values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                    values = (row['ID'], row['NAME'], row['MEC701'],
                              row['MEC702'], row['MEC703'],
                              row['MEDLO703X'], row['ILO701X'],
                              row['MEL701'], row['MEL702'],
                              row['MEL703'], row['MEP704'],
                              row['CGPA'], row['GRADE'])

                    cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error", str(e))
            elif (branch == "Mechanical" and semester == "Semester 8"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['MEC801'] + row['ILO802X'] +
                                          row['MEC802'] + row['MEL801'] +
                                          row['MEC803'] + row['MEL802'] +
                                          row['MEDLO804X'] + row['MEP803']) * 100) / 1000) / 9.0)

                    if (0 < row['CGPA'] < 3.9):
                        row['GRADE'] = "F"
                    elif (row['CGPA'] < 4.5):
                        row['GRADE'] = "P"
                    elif (row['CGPA'] < 5):
                        row['GRADE'] = "E"
                    elif (row['CGPA'] < 6):
                        row['GRADE'] = "D"
                    elif (row['CGPA'] < 7):
                        row['GRADE'] = "C"
                    elif (row['CGPA'] < 7.5):
                        row['GRADE'] = "B"
                    elif (row['CGPA'] < 8):
                        row['GRADE'] = "A"
                    else:
                        row['GRADE'] = "O"

                    sql = """Insert into college_result_management_sys.MECH_SEM8(ID,NAME,MEC801,
                                                          MEC802,MEC803,MEDLO804X,ILO802X,
                                                          MEL801,MEL802,MEP803,
                                                          CGPA,GRADE)
                                                          values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                    values = (row['ID'], row['NAME'], row['MEC801'],
                              row['MEC802'], row['MEC803'],
                              row['MEDLO804X'], row['ILO802X'],
                              row['MEL801'], row['MEL802'],
                              row['MEP803'], row['CGPA'],
                              row['GRADE'])

                    cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error", str(e))
            elif (branch == "Information technology" and semester == "Semester 3"):
                print("hello it")

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ITC301'] + row['ITL301'] +
                                          row['ITC302'] + row['ITL302'] +
                                          row['ITC303'] + row['ITL303'] +
                                          row['ITC304'] + row['ITL304'] +
                                          row['ITC305'] + row['ITM301']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.IT_SEM3(ID,NAME,ITC301,
                                                      ITC302,ITC303,ITC304,ITC305,
                                                      ITL301,ITL302,ITL303,
                                                      ITL304,ITM301,CGPA,grade)
                                                      values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['ITC301'],
                                  row['ITC302'], row['ITC303'],
                                  row['ITC304'], row['ITC305'],
                                  row['ITL301'], row['ITL302'],
                                  row['ITL303'], row['ITL304'],
                                  row['ITM301'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Information technology" and semester == "Semester 4"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ITC401'] + row['ITL401'] +
                                          row['ITC402'] + row['ITL402'] +
                                          row['ITC403'] + row['ITL403'] +
                                          row['ITC404'] + row['ITL404'] +
                                          row['ITC405'] + row['ITM401']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.IT_SEM4(ID,NAME,ITC401,
                                                  ITC402,ITC403,ITC504,ITC405,
                                                  ITL401,ITL402,ITL403,
                                                  ITL404,ITM401,CGPA,grade)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['ITC401'],
                                  row['ITC402'], row['ITC403'],
                                  row['ITC404'], row['ITC405'],
                                  row['ITL401'], row['ITL402'],
                                  row['ITL403'], row['ITL404'],
                                  row['ITM401'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Information technology" and semester == "Semester 5"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ITC501'] + row['ITL501'] +
                                          row['ITC502'] + row['ITL502'] +
                                          row['ITC503'] + row['ITL503'] +
                                          row['ITC504'] + row['ITL504'] +
                                          row['ITDO501X'] + row['ITL505'] +
                                          row['ITM501']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.IT_SEM5(ID,NAME,ITC501,
                                                  ITC502,ITC503,ITC504,ITDO501X,
                                                  ITL501,ITL502,ITL503,
                                                  ITL504,ITM505,ITM501,CGPA,grade)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['ITC501'],
                                  row['ITC502'], row['ITC503'],
                                  row['ITC504'], row['ITDO501X'],
                                  row['ITL501'], row['ITL502'],
                                  row['ITL503'], row['ITL504'],
                                  row['ITL505'], row['ITM501'],
                                  row['CGPA'], row['GRADE'])
                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Information technology" and semester == "Semester 6"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ITC601'] + row['ITL601'] +
                                          row['ITC602'] + row['ITL602'] +
                                          row['ITC603'] + row['ITL603'] +
                                          row['ITC604'] + row['ITL604'] +
                                          row['ITDO601X'] + row['ITL605'] +
                                          row['ITM601']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.IT_SEM6(ID,NAME,ITC601,
                                                  ITC602,ITC603,ITC604,ITDO601X,
                                                  ITL601,ITL602,ITL603,
                                                  ITL604,ITM605,ITM601,CGPA,grade)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['ITC601'],
                                  row['ITC602'], row['ITC603'],
                                  row['ITC604'], row['ITDO601X'],
                                  row['ITL601'], row['ITL602'],
                                  row['ITL603'], row['ITL604'],
                                  row['ITL605'], row['ITM601'],
                                  row['CGPA'], row['GRADE'])
                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Information technology" and semester == "Semester 7"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ITC701'] + row['ITL701'] +
                                          row['ITC702'] + row['ITL702'] +
                                          row['ITDO701X'] + row['ITL703'] +
                                          row['ITDO702X'] + row['ITL704'] +
                                          row['ITIO701X'] + row['ITP701']) * 100) / 1000) / 9.0)

                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.IT_SEM7(ID,NAME,ITC701,
                                                  ITC702,ITDO701X,ITDO702X,ITIO701X,
                                                  ITL701,ITL702,ITL703,
                                                  ITL704,ITP701,CGPA,grade)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)"""

                        values = (row['ID'], row['NAME'], row['ITC701'],
                                  row['ITC702'], row['ITDO701X'],
                                  row['ITDO702X'], row['ITIO701X'],
                                  row['ITL701'], row['ITL702'],
                                  row['ITL703'], row['ITL704'],
                                  row['ITP701'], row['CGPA'],
                                  row['GRADE'])
                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Information technology" and semester == "Semester 8"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ITC801'] + row['ITL801'] +
                                          row['ITDO801X'] + row['ITL802'] +
                                          row['ITDO802X'] + row['ITP801'] +
                                          row['ITIO801X']) * 100) / 1000) / 9.0)

                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.IT_SEM8(ID,NAME,ITC801,
                                                 ITDO801X,ITDO802X,ITIO801X,
                                                  ITL801,ITL802,ITP801,CGPA,grade)
    
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['ITC801'],
                                  row['ITDO801X'], row['ITDO802X'],
                                  row['ITIO801X'], row['ITL801'],
                                  row['ITL802'], row['ITP801'],
                                  row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 3"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ECC301'] + row['ECL301'] +
                                          row['ECC302'] + row['ECL302'] +
                                          row['ECC303'] + row['ECL303'] +
                                          row['ECC304'] + row['ECL304'] +
                                          row['ECC305'] + row['ECM301']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.EXTC_SEM3(ID,NAME,ECC301,
                                                  ECC302,ECC303,ECC304,ECC305,
                                                  ECL301,ECL302,ECL303,
                                                  ECL304,ECM301,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['ECC301'],
                                  row['ECC302'], row['ECC303'],
                                  row['ECC304'], row['ECC305'],
                                  row['ECL301'], row['ECL302'],
                                  row['ECL303'], row['ECL304'],
                                  row['ECM301'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 4"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ECC401'] + row['ECL401'] +
                                          row['ECC402'] + row['ECL402'] +
                                          row['ECC403'] + row['ECL403'] +
                                          row['ECC404'] + row['ECL404'] +
                                          row['ECC405'] + row['ECM401']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.EXTC_SEM4(ID,NAME,ECC401,
                                                  ECC402,ECC403,ECC404,ECC405,
                                                  ECL401,ECL402,ECL403,
                                                  ECL404,ECM401,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['ECC401'],
                                  row['ECC402'], row['ECC403'],
                                  row['ECC404'], row['ECC405'],
                                  row['ECL401'], row['ECL402'],
                                  row['ECL403'], row['EC404'],
                                  row['ECM401'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 5"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ECC501'] + row['ECL501'] +
                                          row['ECC502'] + row['ECL502'] +
                                          row['ECC503'] + row['ECL503'] +
                                          row['ECC504'] + row['ECL504'] +
                                          row['ECCDLO501X'] + row['ECM501']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.EXTC_SEM5(ID,NAME,ECC501,
                                                  ECC502,ECC503,ECC504,ECCDLO501X,
                                                  ECL501,ECL502,ECL503,
                                                  ECL504,ECM501,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['ECC501'],
                                  row['ECC502'], row['ECC503'],
                                  row['ECC504'], row['ECCDLO501X'],
                                  row['ECL501'], row['ECL502'],
                                  row['ECL503'], row['ECL504'],
                                  row['ECM501'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 6"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ECC601'] + row['ECL601'] +
                                          row['ECC602'] + row['ECL602'] +
                                          row['ECC603'] + row['ECL603'] +
                                          row['ECC604'] + row['ECL604'] +
                                          row['ECCDLO601X'] + row['ECM601']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.EXTC_SEM6(ID,NAME,ECC601,
                                                  ECC602,ECC603,ECC504,ECCDLO601X,
                                                  ECL601,ECL602,ECL603,
                                                  ECL604,ECM601,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['ECC601'],
                                  row['ECC602'], row['ECC603'],
                                  row['ECC604'], row['ECCDLO601X'],
                                  row['ECL601'], row['ECL602'],
                                  row['ECL603'], row['ECL604'],
                                  row['ECM601'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 7"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ECC701'] + row['ECCILO701X'] +
                                          row['ECC702'] + row['ECL701'] +
                                          row['ECCDLO701X'] + row['ECL702'] +
                                          row['ECCDLO702X'] + row['ECP701']) * 100) / 1000) / 9.0)

                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.EXTC_SEM7(ID,NAME,ECC701,
                                                  ECC702,ECCDLO701X,ECCDLO702X,ECCILO701X,
                                                  ECL701,ECL702,ECP701,
                                                  CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['ECC701'],
                                  row['ECC702'], row['ECCDLO701X'],
                                  row['ECCDLO702X'], row['ECCILO701X'],
                                  row['ECL701'], row['ECL702'],
                                  row['ECP701'], row['CGPA'],
                                  row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 8"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['ECC801'] + row['ECL801'] +
                                          row['ECC802'] + row['ECL802'] +
                                          row['ECCDLO804X'] + row['ECLDLO804X'] +
                                          row['ECCILO802X'] + row['ECL803']) * 100) / 1000) / 9.0)

                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.EXTC_SEM8(ID,NAME,ECC801,
                                                  ECC802,ECCDLO804X,ECCILO802X,ECL801,
                                                  ECL802,ECLDLO804X,ECL803
                                                  CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['ECC801'],
                                  row['ECC802'], row['ECCDLO804X'],
                                  row['ECCILO802X'], row['ECL801'],
                                  row['ECL802'], row['ECLDLO804X'],
                                  row['ECL803'], row['CGPA'],
                                  row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Computer" and semester == "Semester 3"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC301'] + row['CSL301'] +
                                          row['CSC302'] + row['CSL302'] +
                                          row['CSC303'] + row['CSL303'] +
                                          row['CSC304'] + row['CSL304'] +
                                          row['CSC305'] + row['CSM301']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.COMPS_SEM_3(ID,NAME,CSC301,
                                                  CSC302,CSC303,CSC304,CSC305,
                                                  CSL301,CSL302,CSL303,
                                                  CSL304,CSM301,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC301'],
                                  row['CSC302'], row['CSC303'],
                                  row['CSC304'], row['CSC305'],
                                  row['CSL301'], row['CSL302'],
                                  row['CSL303'], row['CSL304'],
                                  row['CSM301'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Computer" and semester == "Semester 4"):
                print("hello comps")

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC401'] + row['CSL401'] +
                                          row['CSC402'] + row['CSL402'] +
                                          row['CSC403'] + row['CSL403'] +
                                          row['CSC404'] + row['CSL404'] +
                                          row['CSC405'] + row['CSM401']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.COMPS_SEM4(ID,NAME,CSC401,
                                                  CSC402,CSC403,CSC404,CSC405,
                                                  CSL401,CSL402,CSL403,
                                                  CSL404,CSM401,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC401'],
                                  row['CSC402'], row['CSC403'],
                                  row['CSC404'], row['CSC405'],
                                  row['CSL401'], row['CSL402'],
                                  row['CSL403'], row['CSL404'],
                                  row['CSM401'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Computer" and semester == "Semester 5"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC501'] + row['CSL501'] +
                                          row['CSC502'] + row['CSL502'] +
                                          row['CSC503'] + row['CSL503'] +
                                          row['CSC504'] + row['CSL504'] +
                                          row['CSCDLO501X'] + row['CSM501']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.COMPS_SEM5(ID,NAME,CSC501,
                                                  CSC502,CSC503,CSC504,CSDLO501X,
                                                  CSL501,CSL502,CSL503,
                                                  CSL504,CSM501,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC501'],
                                  row['CSC502'], row['CSC503'],
                                  row['CSC504'], row['CSDLO501X'],
                                  row['CSL501'], row['CSL502'],
                                  row['CSL503'], row['CSL504'],
                                  row['CSM501'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Computer" and semester == "Semester 6"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC601'] + row['CSL601'] +
                                          row['CSC602'] + row['CSL602'] +
                                          row['CSC603'] + row['CSL603'] +
                                          row['CSC604'] + row['CSL604'] +
                                          row['CSCDLO601X'] + row['CSL605'] +
                                          row['CSM601']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.COMPS_SEM6(ID,NAME,CSC601,
                                                  CSC602,CSC603,CSC604,CSDLO601X,
                                                  CSL601,CSL602,CSL603,
                                                  CSL604,CSM605,CSM601,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC601'],
                                  row['CSC602'], row['CSC603'],
                                  row['CSC604'], row['CSDLO601X'],
                                  row['CSL601'], row['CSL602'],
                                  row['CSL603'], row['CSL604'],
                                  row['CSL605'], row['CSM601'],
                                  row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Computer" and semester == "Semester 7"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC701'] + row['CSL701'] +
                                          row['CSC702'] + row['CSL702'] +
                                          row['CDSC701X'] + row['CSDL701X'] +
                                          row['CDSC702X'] + row['CSDL702X'] +
                                          row['ILO701X'] + row['CSP701']) * 100) / 1000) / 9.0)

                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.COMPS_SEM7(ID,NAME,CSC701,
                                                  CSC702,CDSC701X,CDSC702X,ILO701X,CSL701,
                                                  CSL702,CSDL701X,CSDL702X,
                                                  CSP701,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC701'],
                                  row['CSC702'], row['CDSC701X'],
                                  row['CDSC702X'], row['ILO701X'],
                                  row['CSL701'], row['CSL702'],
                                  row['CSDL701X'], row['CSDL702X'],
                                  row['CSP701'], row['CGPA'],
                                  row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Computer" and semester == "Semester 8"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC801'] + row['CSL801'] +
                                          row['CSC802'] + row['CSL802'] +
                                          row['CSDLO801X'] + row['CSL803'] +
                                          row['ILO801X'] + row['CSL804'] +
                                          row['CSP805']) * 100) / 1000) / 9.0)

                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.COMPS_SEM8(ID,NAME,CSC801,
                                                  CSC802,CSDLO801X,ILO801X,CSL801,
                                                  CSL802,CSL803,CSL804,
                                                  CSP805,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC801'],
                                  row['CSC802'], row['CSDLO801X'],
                                  row['IL0801X'], row['CSL801'],
                                  row['CSL802'], row['CSL803'],
                                  row['CSL804'], row['CSP805'],
                                  row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 3"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC301'] + row['CSL301'] +
                                          row['CSC302'] + row['CSL302'] +
                                          row['CSC303'] + row['CSL303'] +
                                          row['CSC304'] + row['CSL304'] +
                                          row['CSC305'] + row['CSM301']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.AIDS_SEM3(ID,NAME,CSC301,
                                                  CSC302,CSC303,CSC304,CSC305,
                                                  CSL301,CSL302,CSL303,
                                                  CSL304,CSM301,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC301'],
                                  row['CSC302'], row['CSC303'],
                                  row['CSC304'], row['CSC305'],
                                  row['CSL301'], row['CSL302'],
                                  row['CSL303'], row['CSL304'],
                                  row['CSM301'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 4"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC401'] + row['CSL401'] +
                                          row['CSC402'] + row['CSL402'] +
                                          row['CSC403'] + row['CSL403'] +
                                          row['CSC404'] + row['CSL404'] +
                                          row['CSC405'] + row['CSM401']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.AIDS_SEM4(ID,NAME,CSC401,
                                                  CSC402,CSC403,CSC404,CSC405,
                                                  CSL401,CSL402,CSL403,
                                                  CSL404,CSM401,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC401'],
                                  row['CSC402'], row['CSC403'],
                                  row['CSC404'], row['CSC405'],
                                  row['CSL401'], row['CSL402'],
                                  row['CSL403'], row['CSL404'],
                                  row['CSM401'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 5"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC501'] + row['CSL501'] +
                                          row['CSC502'] + row['CSL502'] +
                                          row['CSC503'] + row['CSL503'] +
                                          row['CSC504'] + row['CSL504'] +
                                          row['CSCDLO501X'] + row['CSM501']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.AIDS_SEM5(ID,NAME,CSC501,
                                                  CSC502,CSC503,CSC504,CSDLO501X,
                                                  CSL501,CSL502,CSL503,
                                                  CSL504,CSM501,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC501'],
                                  row['CSC502'], row['CSC503'],
                                  row['CSC504'], row['CSDLO501X'],
                                  row['CSL501'], row['CSL502'],
                                  row['CSL503'], row['CSL504'],
                                  row['CSM501'], row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 6"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC601'] + row['CSL601'] +
                                          row['CSC602'] + row['CSL602'] +
                                          row['CSC603'] + row['CSL603'] +
                                          row['CSC604'] + row['CSL604'] +
                                          row['CSCDLO601X'] + row['CSL605'] +
                                          row['CSM601']) * 100) / 1000) / 9.0)
                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.AIDS_SEM6(ID,NAME,CSC601,
                                                  CSC602,CSC603,CSC604,CSDLO601X,
                                                  CSL601,CSL602,CSL603,
                                                  CSL604,CSM605,CSM601,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC601'],
                                  row['CSC602'], row['CSC603'],
                                  row['CSC604'], row['CSDLO601X'],
                                  row['CSL601'], row['CSL602'],
                                  row['CSL603'], row['CSL604'],
                                  row['CSL605'], row['CSM601'],
                                  row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 7"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC701'] + row['CSL701'] +
                                          row['CSC702'] + row['CSL702'] +
                                          row['CDSC701X'] + row['CSDL701X'] +
                                          row['CDSC702X'] + row['CSDL702X'] +
                                          row['ILO701X'] + row['CSP701']) * 100) / 1000) / 9.0)

                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.AIDS_SEM7(ID,NAME,CSC701,
                                                  CSC702,CDSC701X,CDSC702X,ILO701X,CSL701,
                                                  CSL702,CSDL701X,CSDL702X,
                                                  CSP701,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC701'],
                                  row['CSC702'], row['CDSC701X'],
                                  row['CDSC702X'], row['ILO701X'],
                                  row['CSL701'], row['CSL702'],
                                  row['CSDL701X'], row['CSDL702X'],
                                  row['CSP701'], row['CGPA'],
                                  row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 8"):

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="abesaale123",
                        database="college_result_management_sys"
                    )
                    file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                    df = pd.read_excel(file_path)

                    cursor = conn.cursor()

                    for index, row in df.iterrows():
                        row['CGPA'] = ((((row['CSC801'] + row['CSL801'] +
                                          row['CSC802'] + row['CSL802'] +
                                          row['CSDLO801X'] + row['CSL803'] +
                                          row['ILO801X'] + row['CSL804'] +
                                          row['CSP805']) * 100) / 1000) / 9.0)

                        if (0 < row['CGPA'] < 3.9):
                            row['GRADE'] = "F"
                        elif (row['CGPA'] < 4.5):
                            row['GRADE'] = "P"
                        elif (row['CGPA'] < 5):
                            row['GRADE'] = "E"
                        elif (row['CGPA'] < 6):
                            row['GRADE'] = "D"
                        elif (row['CGPA'] < 7):
                            row['GRADE'] = "C"
                        elif (row['CGPA'] < 7.5):
                            row['GRADE'] = "B"
                        elif (row['CGPA'] < 8):
                            row['GRADE'] = "A"
                        else:
                            row['GRADE'] = "O"

                        sql = """Insert into college_result_management_sys.AIDS_SEM8(ID,NAME,CSC801,
                                                  CSC802,CSDLO801X,ILO801X,CSL801,
                                                  CSL802,CSL803,CSL804,
                                                  CSP805,CGPA,GRADE)
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                        values = (row['ID'], row['NAME'], row['CSC801'],
                                  row['CSC802'], row['CSDLO801X'],
                                  row['IL0801X'], row['CSL801'],
                                  row['CSL802'], row['CSL803'],
                                  row['CSL804'], row['CSP805'],
                                  row['CGPA'], row['GRADE'])

                        cursor.execute(sql, values)

                    conn.commit()
                    cursor.close()
                    conn.close()

                    self.statusBar().showMessage("Data uploaded successfully")
                    QMessageBox.information(self, "Success", "Data uploaded successfully")


                except Exception as e:

                    self.statusBar().showMessage("Error: " + str(e))

                    QMessageBox.critical(self, "Error",str(e))




    def viewmarks1(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        branch = self.cb41.currentText()
        semester = self.cb42.currentText()
        basedon = self.cb43.currentText()
        self.label_44.setVisible(False)
        self.b43.setVisible(False)
        self.tf41.setVisible(False)

        if (self.b41.clicked):
          self.gb42.setVisible(True)
          if (basedon == "Based on individual"):
           self.label_44.setVisible(True)
           self.b43.setVisible(True)
           self.tf41.setVisible(True)

          if (basedon == "Based on whole class"):

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abesaale123",
                database="college_result_management_sys"
            )

            # Create cursor object
            mycursor = mydb.cursor()

            # Execute SQL query
            if (semester == "Semester 1"):
                    mycursor.execute("SELECT * FROM IT_SEM1_2 order by ID")
            elif (semester == "Semester 2"):
                    mycursor.execute("SELECT * FROM IT_SEM_2 order by ID")
            elif (branch == "Computer" and semester == "Semester 3"):
                    print("hii hello 123")
                    mycursor.execute("SELECT * FROM COMPS_SEM_3 order by ID")
            elif (branch == "Computer" and semester == "Semester 4"):
                    mycursor.execute("SELECT * FROM COMPS_SEM4 order by ID")
            elif (branch == "Computer" and semester == "Semester 5"):
                    mycursor.execute("SELECT * FROM COMPS_SEM5 order by ID")
            elif (branch == "Computer" and semester == "Semester 6"):
                    mycursor.execute("SELECT * FROM COMPS_SEM6 order by ID")
            elif (branch == "Computer" and semester == "Semester 7"):
                    mycursor.execute("SELECT * FROM COMPS_SEM7 order by ID")
            elif (branch == "Computer" and semester == "Semester 8"):
                    mycursor.execute("SELECT * FROM COMPS_SEM8 order by ID")
            elif (branch == "Information technology" and semester == "Semester 3"):
                    mycursor.execute("SELECT * FROM IT_SEM3 order by ID")
            elif (branch == "Information technology" and semester == "Semester 4"):
                    mycursor.execute("SELECT * FROM IT_SEM4 order by ID")
            elif (branch == "Information technology" and semester == "Semester 5"):
                    mycursor.execute("SELECT * FROM IT_SEM5 order by ID")
            elif (branch == "Information technology" and semester == "Semester 6"):
                    mycursor.execute("SELECT * FROM IT_SEM6 order by ID")
            elif (branch == "Information technology" and semester == "Semester 7"):
                    mycursor.execute("SELECT * FROM IT_SEM7 order by ID")
            elif (branch == "Information technology" and semester == "Semester 8"):
                    mycursor.execute("SELECT * FROM IT_SEM8 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 3"):
                    mycursor.execute("SELECT * FROM MECH_SEM_3 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 4"):
                    mycursor.execute("SELECT * FROM MECH_SEM_4 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 5"):
                    mycursor.execute("SELECT * FROM MECH_SEM_5 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 6"):
                    mycursor.execute("SELECT * FROM MECH_SEM_6 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 7"):
                    mycursor.execute("SELECT * FROM MECH_SEM_7 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 8"):
                    mycursor.execute("SELECT * FROM MECH_SEM_8 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 3"):
                    mycursor.execute("SELECT * FROM EXTC_SEM3 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 4"):
                    mycursor.execute("SELECT * FROM EXTC_SEM4 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 5"):
                    mycursor.execute("SELECT * FROM EXTC_SEM5 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 6"):
                    mycursor.execute("SELECT * FROM EXTC_SEM6 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 7"):
                    mycursor.execute("SELECT * FROM EXTC_SEM7 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 8"):
                    mycursor.execute("SELECT * FROM EXTC_SEM8 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 3"):
                    mycursor.execute("SELECT * FROM AIDS_SEM3 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 4"):
                    mycursor.execute("SELECT * FROM AIDS_SEM4 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 5"):
                    mycursor.execute("SELECT * FROM AIDS_SEM5 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 6"):
                    mycursor.execute("SELECT * FROM AIDS_SEM6 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 7"):
                    mycursor.execute("SELECT * FROM AIDS_SEM7 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 8"):
                    mycursor.execute("SELECT * FROM AIDS_SEM8 order by ID")

            # Fetch all data from query
            data = mycursor.fetchall()

            # Create QTableWidget object
            # table = QTableWidget()

            # Set number of rows and columns
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]))

            # Set column headers
            if (semester == "Semester 1"):
                columnheaders = ["ID", "NAME", "FEC101", "FEC102", "FEC103", "FEC104", "FEC105", "FEL101", "FEL102",
                             "FEL103", "FEL104", "FEL105", "CGPA", "GRADE"]
            elif (branch == "Computer" and semester == "Semester 3"):
                columnheaders = [ "ID", "NAME", "CSC301", "CSC302", "CSC303", "CSC304", "CSC305", "CSL301", "CSL302", "CSL303", "CSL304", "CSM301", "CGPA", "GRADE",]
            elif (branch == "Computer" and semester == "Semester 4"):
                columnheaders = ["ID", "NAME","CSC401 "," CSC402 "," CSC403 "," CSC404 "," CSC405 "," CSL401 "," CSL402 "," CSL403 "," CSL404 "," CSM401", "CGPA", "GRADE"]
            elif (branch == "Computer" and semester == "Semester 5"):
                columnheaders = ["ID", "NAME","CSC501 "," CSC502 "," CSC503 "," CSC504 "," CSC505 "," CSL501 "," CSL502 "," CSL503 "," CSL504 "," CSM501", "CGPA", "GRADE"]
            elif (branch == "Computer" and semester == "Semester 6"):
                columnheaders = ["ID", "NAME","CSC601 "," CSC602 "," CSC603 "," CSC604 "," CSDL0601X "," CSL601 "," CSL602 "," CSL603 "," CSL604 "," CSL605 "," CSM601", "CGPA", "GRADE"]
            elif (branch == "Computer" and semester == "Semester 7"):
                columnheaders = ["ID", "NAME","CSC701 "," CSC702 "," CDSC701X "," CDSC702X "," ILO701X "," CSL701 "," CSL702 "," CSDL701X "," CSDL702X "," CSP701", "CGPA", "GRADE"]
            elif (branch == "Computer" and semester == "Semester 8"):
                columnheaders = ["ID", "NAME","CSC801 "," CSC802 "," CSDL0801X "," ILO801X "," CSL801 "," CSL802 "," CSL803 "," CSL804 "," CSP805", "CGPA", "GRADE"]
            elif (branch == "Information technology" and semester == "Semester 3"):
                columnheaders = ["ID", "NAME","ITC301 "," ITC302 "," ITC303 "," ITC304 "," ITC305 "," ITL301 "," ITL302 "," ITL303 "," ITL304 "," ITM301", "CGPA", "GRADE"]
            elif (branch == "Information technology" and semester == "Semester 4"):
                columnheaders = ["ID", "NAME","ITC401 "," ITC402 "," ITC403 "," ITC404 "," ITC405 "," ITL401 "," ITL402 "," ITL403 "," ITL404 "," ITM401", "CGPA", "GRADE","RESULT"]
            elif (branch == "Information technology" and semester == "Semester 5"):
                columnheaders = ["ID", "NAME","ITC501 "," ITC502 "," ITC503 "," ITC504 "," ITD0501X "," ITL501 "," ITL502 "," ITL503 "," ITL504 "," ITL505 "," ITM501", "CGPA", "GRADE"]
            elif (branch == "Information technology" and semester == "Semester 6"):
                columnheaders = ["ID", "NAME","ITC601 "," ITC602 "," ITC603 "," ITC604 "," ITD0601X "," ITL601 "," ITL602 "," ITL603 "," ITL604 "," ITL605 "," ITM601", "CGPA", "GRADE"]
            elif (branch == "Information technology" and semester == "Semester 7"):
                columnheaders = ["ID", "NAME","ITC701 "," ITC702 "," ITDO701X "," ITD0702X "," ITIO701X "," ITL701 "," ITL702 "," ITL703 "," ITL704 "," ITP701", "CGPA", "GRADE"]
            elif (branch == "Information technology" and semester == "Semester 8"):
                columnheaders = ["ID", "NAME","ITC801 "," ITDO801X "," ITDO802X "," ITIO801X "," ITL801 "," ITL802 "," ITP801", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 3"):
                columnheaders = ["ID", "NAME","MEC301 "," MEC302 "," MEC303 "," MEC304 "," MEC305 "," MEL301 "," MEL302 "," MEL303 "," MEL304", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 4"):
                columnheaders = ["ID", "NAME","MEC401 "," MEC402 "," MEC403 "," MEC404 "," MEC405 "," MEL401 "," MEL402 "," MEL403 "," MEL404 "," MEL405", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 5"):
                columnheaders = ["ID", "NAME","MEC501 "," MEC502 "," MEC503 "," MEC504 "," MEDLO501X "," MEL501 "," MEL502 "," MEL503 "," MEL504 "," MEL505 "," MEL506", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 6"):
                columnheaders = ["ID", "NAME","MEC601 "," MEC602 "," MEC603 "," MEC604 "," MEDL0602X "," MEL601 "," MEL602 "," MEL603 "," MEL604 "," MEL605 "," MEL606", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 7"):
                columnheaders = ["ID", "NAME","MEC701 "," MEC702 "," MEC703 "," MEDLO703X "," IL0701X "," MEL701 "," MEL702 "," MEL703 "," MEP704", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 8"):
                columnheaders = ["ID", "NAME","MEC801 "," MEC802 "," MEC803 "," MEDLO804X "," ILO802X "," MEL801 "," MEL802 "," MEP803", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 3"):
                columnheaders = ["ID", "NAME","ECC301 "," ECC302 "," ECC303 "," ECC304 "," ECC305 "," ECL301 "," ECL302 "," ECL303 "," ECL304 "," ECM301", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 4"):
                columnheaders = ["ID", "NAME","ECC401 "," ECC402 "," ECC403 "," ECC404 "," ECC405 "," ECL401 "," ECL402 "," ECL403 "," ECL404 "," ECM401", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 5"):
                columnheaders = ["ID", "NAME","ECC501 "," ECC502 "," ECC503 "," ECC504 "," ECCDLO501X "," ECL501 "," ECL502 "," ECL503 "," ECL504 "," ECM501", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 6"):
                columnheaders = ["ID", "NAME","ECC601 "," ECC602 "," ECC603 "," ECC604 "," ECCDLO601X "," ECL601 "," ECL602 "," ECL603 "," ECL604 "," ECM601", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 7"):
                columnheaders = ["ID", "NAME","ECC701 "," ECC702 "," ECCDLO701X "," ECCDLO702X "," ECCILO701X "," ECL701 "," ECL702 "," ECP701", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 8"):
                columnheaders = ["ID", "NAME","ECC801 "," ECC802 "," ECCDLO804X "," IL0802X "," ECL801 "," ECL802 "," ECLDLO804X "," ECL803", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 3"):
                columnheaders = ["ID", "NAME","CSC301 "," CSC302 "," CSC303 "," CSC304 "," CSC305 "," CSL301 "," CSL302 "," CSL303 "," CSL304 "," CSM301", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 4"):
                columnheaders = ["ID", "NAME","CSC401 "," CSC402 "," CSC403 "," CSC404 "," CSC405 "," CSL401 "," CSL402 "," CSL403 "," CSL404 "," CSM401", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 5"):
                columnheaders = ["ID", "NAME","CSC501 "," CSC502 "," CSC503 "," CSC504 "," CSCDLO501X "," CSL501 "," CSL502 "," CSL503 "," CSL504 "," CSM501", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 6"):
                columnheaders = ["ID", "NAME","CSC601 "," CSC602 "," CSC603 "," CSC604 "," CSCDLO601X "," CSL601 "," CSL602 "," CSL603 "," CSL604 "," CSL605", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 7"):
                columnheaders = ["ID", "NAME","CSC701 "," CSC702 "," CDSC701X "," CDSC702X "," IL0701X "," CSL701 "," CSL702 "," CSDL701X "," CSDL702X "," CSP701", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 8"):
                columnheaders = ["ID", "NAME","CSC801 "," CSC802 "," CSDL0801X "," IL0801X "," CSL801 "," CSL802 "," CSL803 "," CSL804 "," CSP805", "CGPA", "GRADE"]


            self.tableWidget.setHorizontalHeaderLabels(columnheaders)

            # Iterate over data and insert into table
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.tableWidget.setItem(i, j, item)


    def viewmarks_basedonindividaul(self):
        branch = self.cb41.currentText()
        semester = self.cb42.currentText()
        basedon = self.cb43.currentText()
        roll_no = self.tf41.text()

        try:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abesaale123",
                database="college_result_management_sys"
            )

            # Create cursor object
            mycursor = mydb.cursor()

            # Execute SQL query
            if (basedon == "Based on individual"):
                if (semester == "Semester 1"):
                        mycursor.execute("SELECT * FROM IT_SEM1_2 where ID = %s", (roll_no,))
                elif (semester == "Semester 2"):
                        mycursor.execute("SELECT * FROM IT_SEM_2 where ID = %s", (roll_no,))
                elif (branch == "Computer" and semester == "Semester 3"):
                        mycursor.execute("SELECT * FROM COMPS_SEM_3 where ID = %s", (roll_no,))
                elif (branch == "Computer" and semester == "Semester 4"):
                        mycursor.execute("SELECT * FROM COMPS_SEM4 where ID = %s", (roll_no,))
                elif (branch == "Computer" and semester == "Semester 5"):
                        mycursor.execute("SELECT * FROM COMPS_SEM5 where ID = %s", (roll_no,))
                elif (branch == "Computer" and semester == "Semester 6"):
                        mycursor.execute("SELECT * FROM COMPS_SEM6 where ID = %s", (roll_no,))
                elif (branch == "Computer" and semester == "Semester 7"):
                        mycursor.execute("SELECT * FROM COMPS_SEM7 where ID = %s", (roll_no,))
                elif (branch == "Computer" and semester == "Semester 8"):
                        mycursor.execute("SELECT * FROM COMPS_SEM8 where ID = %s", (roll_no,))
                elif (branch == "Information technology" and semester == "Semester 3"):
                        mycursor.execute("SELECT * FROM IT_SEM3 where ID = %s", (roll_no,))
                elif (branch == "Information technology" and semester == "Semester 4"):
                        mycursor.execute("SELECT * FROM IT_SEM4 where ID = %s", (roll_no,))
                elif (branch == "Information technology" and semester == "Semester 5"):
                        mycursor.execute("SELECT * FROM IT_SEM5 where ID = %s", (roll_no,))
                elif (branch == "Information technology" and semester == "Semester 6"):
                        mycursor.execute("SELECT * FROM IT_SEM6 where ID = %s", (roll_no,))
                elif (branch == "Information technology" and semester == "Semester 7"):
                        mycursor.execute("SELECT * FROM IT_SEM7 where ID = %s", (roll_no,))
                elif (branch == "Information technology" and semester == "Semester 8"):
                        mycursor.execute("SELECT * FROM IT_SEM8 where ID = %s", (roll_no,))
                elif (branch == "Mechanical" and semester == "Semester 3"):
                        mycursor.execute("SELECT * FROM MECH_SEM_3 where ID = %s", (roll_no,))
                elif (branch == "Mechanical" and semester == "Semester 4"):
                        mycursor.execute("SELECT * FROM MECH_SEM_4 where ID = %s", (roll_no,))
                elif (branch == "Mechanical" and semester == "Semester 5"):
                        mycursor.execute("SELECT * FROM MECH_SEM_5 where ID = %s", (roll_no,))
                elif (branch == "Mechanical" and semester == "Semester 6"):
                        mycursor.execute("SELECT * FROM MECH_SEM_6 where ID = %s", (roll_no,))
                elif (branch == "Mechanical" and semester == "Semester 7"):
                        mycursor.execute("SELECT * FROM MECH_SEM_7 where ID = %s", (roll_no,))
                elif (branch == "Mechanical" and semester == "Semester 8"):
                        mycursor.execute("SELECT * FROM MECH_SEM_8 where ID = %s", (roll_no,))
                elif (branch == "Electronics and telecommunication" and semester == "Semester 3"):
                        mycursor.execute("SELECT * FROM EXTC_SEM3 where ID = %s", (roll_no,))
                elif (branch == "Electronics and telecommunication" and semester == "Semester 4"):
                        mycursor.execute("SELECT * FROM EXTC_SEM4 where ID = %s", (roll_no,))
                elif (branch == "Electronics and telecommunication" and semester == "Semester 5"):
                        mycursor.execute("SELECT * FROM EXTC_SEM5 where ID = %s", (roll_no,))
                elif (branch == "Electronics and telecommunication" and semester == "Semester 6"):
                        mycursor.execute("SELECT * FROM EXTC_SEM6 where ID = %s", (roll_no,))
                elif (branch == "Electronics and telecommunication" and semester == "Semester 7"):
                        mycursor.execute("SELECT * FROM EXTC_SEM7 where ID = %s", (roll_no,))
                elif (branch == "Electronics and telecommunication" and semester == "Semester 8"):
                        mycursor.execute("SELECT * FROM EXTC_SEM8 where ID = %s", (roll_no,))
                elif (branch == "Artificial intelligence and data science" and semester == "Semester 3"):
                        mycursor.execute("SELECT * FROM AIDS_SEM3 where ID = %s", (roll_no,))
                elif (branch == "Artificial intelligence and data science" and semester == "Semester 4"):
                        mycursor.execute("SELECT * FROM AIDS_SEM4 where ID = %s", (roll_no,))
                elif (branch == "Artificial intelligence and data science" and semester == "Semester 5"):
                        mycursor.execute("SELECT * FROM AIDS_SEM5 where ID = %s", (roll_no,))
                elif (branch == "Artificial intelligence and data science" and semester == "Semester 6"):
                        mycursor.execute("SELECT * FROM AIDS_SEM6 where ID = %s", (roll_no,))
                elif (branch == "Artificial intelligence and data science" and semester == "Semester 7"):
                        mycursor.execute("SELECT * FROM AIDS_SEM7 where ID = %s", (roll_no,))
                elif (branch == "Artificial intelligence and data science" and semester == "Semester 8"):
                        mycursor.execute("SELECT * FROM AIDS_SEM8 where ID = %s", (roll_no,))


            # Fetch all data from query
            data = mycursor.fetchall()

            # Create QTableWidget object
            # table = QTableWidget()

            # Set number of rows and columns
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]))

            # Set column headers
            if (semester == "Semester 1"):
                columnheaders = ["ID", "NAME", "FEC101", "FEC102", "FEC103", "FEC104", "FEC105", "FEL101", "FEL102",
                                 "FEL103", "FEL104", "FEL105", "CGPA", "GRADE"]
            elif (branch == "Computer" and semester == "Semester 3"):
                columnheaders = ["ID", "NAME", "CSC301", "CSC302", "CSC303", "CSC304", "CSC305", "CSL301", "CSL302",
                                 "CSL303", "CSL304", "CSM301", "CGPA", "GRADE", ]
            elif (branch == "Computer" and semester == "Semester 4"):
                columnheaders = ["ID", "NAME", "CSC401 ", " CSC402 ", " CSC403 ", " CSC404 ", " CSC405 ", " CSL401 ",
                                 " CSL402 ", " CSL403 ", " CSL404 ", " CSM401", "CGPA", "GRADE"]
            elif (branch == "Computer" and semester == "Semester 5"):
                columnheaders = ["ID", "NAME", "CSC501 ", " CSC502 ", " CSC503 ", " CSC504 ", " CSC505 ", " CSL501 ",
                                 " CSL502 ", " CSL503 ", " CSL504 ", " CSM501", "CGPA", "GRADE"]
            elif (branch == "Computer" and semester == "Semester 6"):
                columnheaders = ["ID", "NAME", "CSC601 ", " CSC602 ", " CSC603 ", " CSC604 ", " CSDL0601X ", " CSL601 ",
                                 " CSL602 ", " CSL603 ", " CSL604 ", " CSL605 ", " CSM601", "CGPA", "GRADE"]
            elif (branch == "Computer" and semester == "Semester 7"):
                columnheaders = ["ID", "NAME", "CSC701 ", " CSC702 ", " CDSC701X ", " CDSC702X ", " ILO701X ",
                                 " CSL701 ", " CSL702 ", " CSDL701X ", " CSDL702X ", " CSP701", "CGPA", "GRADE"]
            elif (branch == "Computer" and semester == "Semester 8"):
                columnheaders = ["ID", "NAME", "CSC801 ", " CSC802 ", " CSDL0801X ", " ILO801X ", " CSL801 ",
                                 " CSL802 ", " CSL803 ", " CSL804 ", " CSP805", "CGPA", "GRADE"]
            elif (branch == "Information technology" and semester == "Semester 3"):
                columnheaders = ["ID", "NAME", "ITC301 ", " ITC302 ", " ITC303 ", " ITC304 ", " ITC305 ", " ITL301 ",
                                 " ITL302 ", " ITL303 ", " ITL304 ", " ITM301", "CGPA", "GRADE"]
            elif (branch == "Information technology" and semester == "Semester 4"):
                columnheaders = ["ID", "NAME", "ITC401 ", " ITC402 ", " ITC403 ", " ITC404 ", " ITC405 ", " ITL401 ",
                                 " ITL402 ", " ITL403 ", " ITL404 ", " ITM401", "CGPA", "GRADE","RESULT"]
            elif (branch == "Information technology" and semester == "Semester 5"):
                columnheaders = ["ID", "NAME", "ITC501 ", " ITC502 ", " ITC503 ", " ITC504 ", " ITD0501X ", " ITL501 ",
                                 " ITL502 ", " ITL503 ", " ITL504 ", " ITL505 ", " ITM501", "CGPA", "GRADE"]
            elif (branch == "Information technology" and semester == "Semester 6"):
                columnheaders = ["ID", "NAME", "ITC601 ", " ITC602 ", " ITC603 ", " ITC604 ", " ITD0601X ", " ITL601 ",
                                 " ITL602 ", " ITL603 ", " ITL604 ", " ITL605 ", " ITM601", "CGPA", "GRADE"]
            elif (branch == "Information technology" and semester == "Semester 7"):
                columnheaders = ["ID", "NAME", "ITC701 ", " ITC702 ", " ITDO701X ", " ITD0702X ", " ITIO701X ",
                                 " ITL701 ", " ITL702 ", " ITL703 ", " ITL704 ", " ITP701", "CGPA", "GRADE"]
            elif (branch == "Information technology" and semester == "Semester 8"):
                columnheaders = ["ID", "NAME", "ITC801 ", " ITDO801X ", " ITDO802X ", " ITIO801X ", " ITL801 ",
                                 " ITL802 ", " ITP801", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 3"):
                columnheaders = ["ID", "NAME", "MEC301 ", " MEC302 ", " MEC303 ", " MEC304 ", " MEC305 ", " MEL301 ",
                                 " MEL302 ", " MEL303 ", " MEL304", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 4"):
                columnheaders = ["ID", "NAME", "MEC401 ", " MEC402 ", " MEC403 ", " MEC404 ", " MEC405 ", " MEL401 ",
                                 " MEL402 ", " MEL403 ", " MEL404 ", " MEL405", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 5"):
                columnheaders = ["ID", "NAME", "MEC501 ", " MEC502 ", " MEC503 ", " MEC504 ", " MEDLO501X ", " MEL501 ",
                                 " MEL502 ", " MEL503 ", " MEL504 ", " MEL505 ", " MEL506", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 6"):
                columnheaders = ["ID", "NAME", "MEC601 ", " MEC602 ", " MEC603 ", " MEC604 ", " MEDL0602X ", " MEL601 ",
                                 " MEL602 ", " MEL603 ", " MEL604 ", " MEL605 ", " MEL606", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 7"):
                columnheaders = ["ID", "NAME", "MEC701 ", " MEC702 ", " MEC703 ", " MEDLO703X ", " IL0701X ",
                                 " MEL701 ", " MEL702 ", " MEL703 ", " MEP704", "CGPA", "GRADE"]
            elif (branch == "Mechanical" and semester == "Semester 8"):
                columnheaders = ["ID", "NAME", "MEC801 ", " MEC802 ", " MEC803 ", " MEDLO804X ", " ILO802X ",
                                 " MEL801 ", " MEL802 ", " MEP803", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 3"):
                columnheaders = ["ID", "NAME", "ECC301 ", " ECC302 ", " ECC303 ", " ECC304 ", " ECC305 ", " ECL301 ",
                                 " ECL302 ", " ECL303 ", " ECL304 ", " ECM301", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 4"):
                columnheaders = ["ID", "NAME", "ECC401 ", " ECC402 ", " ECC403 ", " ECC404 ", " ECC405 ", " ECL401 ",
                                 " ECL402 ", " ECL403 ", " ECL404 ", " ECM401", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 5"):
                columnheaders = ["ID", "NAME", "ECC501 ", " ECC502 ", " ECC503 ", " ECC504 ", " ECCDLO501X ",
                                 " ECL501 ", " ECL502 ", " ECL503 ", " ECL504 ", " ECM501", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 6"):
                columnheaders = ["ID", "NAME", "ECC601 ", " ECC602 ", " ECC603 ", " ECC604 ", " ECCDLO601X ",
                                 " ECL601 ", " ECL602 ", " ECL603 ", " ECL604 ", " ECM601", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 7"):
                columnheaders = ["ID", "NAME", "ECC701 ", " ECC702 ", " ECCDLO701X ", " ECCDLO702X ", " ECCILO701X ",
                                 " ECL701 ", " ECL702 ", " ECP701", "CGPA", "GRADE"]
            elif (branch == "Electronics and telecommunication" and semester == "Semester 8"):
                columnheaders = ["ID", "NAME", "ECC801 ", " ECC802 ", " ECCDLO804X ", " IL0802X ", " ECL801 ",
                                 " ECL802 ", " ECLDLO804X ", " ECL803", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 3"):
                columnheaders = ["ID", "NAME", "CSC301 ", " CSC302 ", " CSC303 ", " CSC304 ", " CSC305 ", " CSL301 ",
                                 " CSL302 ", " CSL303 ", " CSL304 ", " CSM301", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 4"):
                columnheaders = ["ID", "NAME", "CSC401 ", " CSC402 ", " CSC403 ", " CSC404 ", " CSC405 ", " CSL401 ",
                                 " CSL402 ", " CSL403 ", " CSL404 ", " CSM401", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 5"):
                columnheaders = ["ID", "NAME", "CSC501 ", " CSC502 ", " CSC503 ", " CSC504 ", " CSCDLO501X ",
                                 " CSL501 ", " CSL502 ", " CSL503 ", " CSL504 ", " CSM501", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 6"):
                columnheaders = ["ID", "NAME", "CSC601 ", " CSC602 ", " CSC603 ", " CSC604 ", " CSCDLO601X ",
                                 " CSL601 ", " CSL602 ", " CSL603 ", " CSL604 ", " CSL605", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 7"):
                columnheaders = ["ID", "NAME", "CSC701 ", " CSC702 ", " CDSC701X ", " CDSC702X ", " IL0701X ",
                                 " CSL701 ", " CSL702 ", " CSDL701X ", " CSDL702X ", " CSP701", "CGPA", "GRADE"]
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 8"):
                columnheaders = ["ID", "NAME", "CSC801 ", " CSC802 ", " CSDL0801X ", " IL0801X ", " CSL801 ",
                                 " CSL802 ", " CSL803 ", " CSL804 ", " CSP805", "CGPA", "GRADE"]
            self.tableWidget.setHorizontalHeaderLabels(columnheaders)

            # Iterate over data and insert into table
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.tableWidget.setItem(i, j, item)

        except Exception as e:

            self.statusBar().showMessage("Error: " + str(e))

            QMessageBox.critical(self, "Error", str(e))


    def print_table_to_pdf(self):
        branch = self.cb41.currentText()
        semester = self.cb42.currentText()
        basedon = self.cb43.currentText()
        roll_no = self.tf41.text()
        # Get the file name to save the PDF as
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abesaale123",
            database="college_result_management_sys"
        )

        mycursor = mydb.cursor()

        if (basedon == "Based on whole class"):
            print("1234")
            if (semester == "Semester 1"):
                mycursor.execute("SELECT * FROM IT_SEM1_2 order by ID")
            elif (semester == "Semester 2"):
                mycursor.execute("SELECT * FROM IT_SEM_2 order by ID")
            elif (branch == "Computer" and semester == "Semester 3"):
                mycursor.execute("SELECT * FROM COMPS_SEM_3 order by ID")
            elif (branch == "Computer" and semester == "Semester 4"):
                mycursor.execute("SELECT * FROM COMPS_SEM4 order by ID")
            elif (branch == "Computer" and semester == "Semester 5"):
                mycursor.execute("SELECT * FROM COMPS_SEM5 order by ID")
            elif (branch == "Computer" and semester == "Semester 6"):
                mycursor.execute("SELECT * FROM COMPS_SEM6 order by ID")
            elif (branch == "Computer" and semester == "Semester 7"):
                mycursor.execute("SELECT * FROM COMPS_SEM7 order by ID")
            elif (branch == "Computer" and semester == "Semester 8"):
                mycursor.execute("SELECT * FROM COMPS_SEM8 order by ID")
            elif (branch == "Information technology" and semester == "Semester 3"):
                mycursor.execute("SELECT * FROM IT_SEM3 order by ID")
            elif (branch == "Information technology" and semester == "Semester 4"):
                mycursor.execute("SELECT * FROM IT_SEM4 order by ID")
            elif (branch == "Information technology" and semester == "Semester 5"):
                mycursor.execute("SELECT * FROM IT_SEM5 order by ID")
            elif (branch == "Information technology" and semester == "Semester 6"):
                mycursor.execute("SELECT * FROM IT_SEM6 order by ID")
            elif (branch == "Information technology" and semester == "Semester 7"):
                mycursor.execute("SELECT * FROM IT_SEM7 order by ID")
            elif (branch == "Information technology" and semester == "Semester 8"):
                mycursor.execute("SELECT * FROM IT_SEM8 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 3"):
                mycursor.execute("SELECT * FROM MECH_SEM_3 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 4"):
                mycursor.execute("SELECT * FROM MECH_SEM_4 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 5"):
                mycursor.execute("SELECT * FROM MECH_SEM_5 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 6"):
                mycursor.execute("SELECT * FROM MECH_SEM_6 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 7"):
                mycursor.execute("SELECT * FROM MECH_SEM_7 order by ID")
            elif (branch == "Mechanical" and semester == "Semester 8"):
                mycursor.execute("SELECT * FROM MECH_SEM_8 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 3"):
                mycursor.execute("SELECT * FROM EXTC_SEM3 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 4"):
                mycursor.execute("SELECT * FROM EXTC_SEM4 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 5"):
                mycursor.execute("SELECT * FROM EXTC_SEM5 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 6"):
                mycursor.execute("SELECT * FROM EXTC_SEM6 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 7"):
                mycursor.execute("SELECT * FROM EXTC_SEM7 order by ID")
            elif (branch == "Electronics and telecommunication" and semester == "Semester 8"):
                mycursor.execute("SELECT * FROM EXTC_SEM8 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 3"):
                    mycursor.execute("SELECT * FROM AIDS_SEM3 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 4"):
                    mycursor.execute("SELECT * FROM AIDS_SEM4 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 5"):
                    mycursor.execute("SELECT * FROM AIDS_SEM5 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 6"):
                    mycursor.execute("SELECT * FROM AIDS_SEM6 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 7"):
                    mycursor.execute("SELECT * FROM AIDS_SEM7 order by ID")
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 8"):
                    mycursor.execute("SELECT * FROM AIDS_SEM8 order by ID")

        elif (basedon == "Based on individual"):
            if (semester == "Semester 1"):
                mycursor.execute("SELECT * FROM IT_SEM1_2 where ID = %s", (roll_no,))
            elif (semester == "Semester 2"):
                mycursor.execute("SELECT * FROM IT_SEM_2 where ID = %s", (roll_no,))
            elif (branch == "Computer" and semester == "Semester 3"):
                mycursor.execute("SELECT * FROM COMPS_SEM_3 where ID = %s", (roll_no,))
            elif (branch == "Computer" and semester == "Semester 4"):
                mycursor.execute("SELECT * FROM COMPS_SEM4 where ID = %s", (roll_no,))
            elif (branch == "Computer" and semester == "Semester 5"):
                mycursor.execute("SELECT * FROM COMPS_SEM5 where ID = %s", (roll_no,))
            elif (branch == "Computer" and semester == "Semester 6"):
                mycursor.execute("SELECT * FROM COMPS_SEM6 where ID = %s", (roll_no,))
            elif (branch == "Computer" and semester == "Semester 7"):
                mycursor.execute("SELECT * FROM COMPS_SEM7 where ID = %s", (roll_no,))
            elif (branch == "Computer" and semester == "Semester 8"):
                mycursor.execute("SELECT * FROM COMPS_SEM8 where ID = %s", (roll_no,))
            elif (branch == "Information technology" and semester == "Semester 3"):
                mycursor.execute("SELECT * FROM IT_SEM3 where ID = %s", (roll_no,))
            elif (branch == "Information technology" and semester == "Semester 4"):
                mycursor.execute("SELECT * FROM IT_SEM4 where ID = %s", (roll_no,))
            elif (branch == "Information technology" and semester == "Semester 5"):
                mycursor.execute("SELECT * FROM IT_SEM5 where ID = %s", (roll_no,))
            elif (branch == "Information technology" and semester == "Semester 6"):
                mycursor.execute("SELECT * FROM IT_SEM6 where ID = %s", (roll_no,))
            elif (branch == "Information technology" and semester == "Semester 7"):
                mycursor.execute("SELECT * FROM IT_SEM7 where ID = %s", (roll_no,))
            elif (branch == "Information technology" and semester == "Semester 8"):
                mycursor.execute("SELECT * FROM IT_SEM8 where ID = %s", (roll_no,))
            elif (branch == "Mechanical" and semester == "Semester 3"):
                mycursor.execute("SELECT * FROM MECH_SEM_3 where ID = %s", (roll_no,))
            elif (branch == "Mechanical" and semester == "Semester 4"):
                mycursor.execute("SELECT * FROM MECH_SEM_4 where ID = %s", (roll_no,))
            elif (branch == "Mechanical" and semester == "Semester 5"):
                mycursor.execute("SELECT * FROM MECH_SEM_5 where ID = %s", (roll_no,))
            elif (branch == "Mechanical" and semester == "Semester 6"):
                mycursor.execute("SELECT * FROM MECH_SEM_6 where ID = %s", (roll_no,))
            elif (branch == "Mechanical" and semester == "Semester 7"):
                mycursor.execute("SELECT * FROM MECH_SEM_7 where ID = %s", (roll_no,))
            elif (branch == "Mechanical" and semester == "Semester 8"):
                mycursor.execute("SELECT * FROM MECH_SEM_8 where ID = %s", (roll_no,))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 3"):
                mycursor.execute("SELECT * FROM EXTC_SEM3 where ID = %s", (roll_no,))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 4"):
                mycursor.execute("SELECT * FROM EXTC_SEM4 where ID = %s", (roll_no,))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 5"):
                mycursor.execute("SELECT * FROM EXTC_SEM5 where ID = %s", (roll_no,))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 6"):
                mycursor.execute("SELECT * FROM EXTC_SEM6 where ID = %s", (roll_no,))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 7"):
                mycursor.execute("SELECT * FROM EXTC_SEM7 where ID = %s", (roll_no,))
            elif (branch == "Electronics and telecommunication" and semester == "Semester 8"):
                mycursor.execute("SELECT * FROM EXTC_SEM8 where ID = %s", (roll_no,))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 3"):
                mycursor.execute("SELECT * FROM AIDS_SEM3 where ID = %s", (roll_no,))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 4"):
                mycursor.execute("SELECT * FROM AIDS_SEM4 where ID = %s", (roll_no,))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 5"):
                mycursor.execute("SELECT * FROM AIDS_SEM5 where ID = %s", (roll_no,))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 6"):
                mycursor.execute("SELECT * FROM AIDS_SEM6 where ID = %s", (roll_no,))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 7"):
                mycursor.execute("SELECT * FROM AIDS_SEM7 where ID = %s", (roll_no,))
            elif (branch == "Artificial intelligence and data science" and semester == "Semester 8"):
                mycursor.execute("SELECT * FROM AIDS_SEM8 where ID = %s", (roll_no,))

        result = mycursor.fetchall()

        pdf = FPDF(orientation='L')  # Set orientation to landscape
        pdf.set_display_mode('fullwidth')  # Set display mode to full width

        # Set font and column widths
        pdf.set_font("Arial", size=8)
        col_width = pdf.w / 17
        row_height = pdf.font_size + 4  # Decrease row height to avoid text splitting

        # Add a new page
        pdf.add_page()

        # Add column names
        for column in mycursor.description:
            pdf.cell(col_width, row_height, str(column[0]), border=1)

        pdf.ln()

        # Add rows
        pdf.set_font("Arial", size=7)

        for row in result:
            for item in row:
                # Truncate long text and add ellipsis
                text = str(item)[:9] + '...' if len(str(item)) > 9 else str(item)
                pdf.cell(col_width, row_height, text, border=1)
            pdf.ln()

        # Choose a file name and location for the PDF file to be saved
        file_path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "PDF (*.pdf)")

        # Save the PDF file
        pdf.output(file_path)

    def viewmarks(self):

        if (self.b23.clicked):
            self.tabWidget.setCurrentIndex(4)

    def delete_user(self):

        if (self.b26.clicked):
            self.menuBar().setVisible(True)
            self.tabWidget.setCurrentIndex(5)
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abesaale123",
                database="college_result_management_sys"
            )

            # Create cursor object
            mycursor = mydb.cursor()

            # Execute SQL query

            mycursor.execute("SELECT * FROM register order by id")

            # Fetch all data from query
            data = mycursor.fetchall()

            # Create QTableWidget object
            # table = QTableWidget()

            # Set number of rows and columns
            self.tableWidget_3.setRowCount(len(data))
            self.tableWidget_3.setColumnCount(len(data[0]))

            # Iterate over data and insert into table
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.tableWidget_3.setItem(i, j, item)

            columnheaders = ["Name","Username","Password","Branch"]
            self.tableWidget_3.setHorizontalHeaderLabels(columnheaders)

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abesaale123",
                database="college_result_management_sys"
            )

            # Define a cursor object to interact with the database
            my = mydb.cursor()

            # Write a SQL query to select the data you want to display in the combobox
            my.execute("SELECT id FROM register")

            # Fetch the results of the query and store them in a variable
            result = my.fetchall()

            # Print the results to the console
            print(result)

            # Clear any existing items from the combobox
            self.cb501.clear()

            # Populate the combobox with the results of the query
            for item in result:
                self.cb501.addItem(str(item[0]))
            delete = self.cb501.currentText()



    def delete_user1(self):
        sid = self.cb501.currentText()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abesaale123",
            database="college_result_management_sys"
        )
        my = mydb.cursor()
        my.execute("DELETE FROM REGISTER WHERE ID = %s", (sid,))
        mydb.commit()
        mydb.close()

        self.delete_user()



    def studentdetails(self):
        self.tabWidget.setCurrentIndex(6)

    def insertstudentdetails(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="abesaale123",
            database="college_result_management_sys"
        )
        name = self.tf61.text()
        un1 = self.tf62.text()
        pw1 = self.cb61.currentText()
        branch_teachers = self.cb62.currentText()
        cursor = conn.cursor()
        querry = "Insert into   studdetails(Name,Roll_no,Branch,Semester)values(%s,%s,%s,%s)"
        cursor.execute(querry, (name, un1, pw1, branch_teachers))
        conn.commit()
        QMessageBox.information(self, "Message", "Done Registeration")
        cursor.close()
        conn.close()

    def insertstudentdetails1(self):


            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="abesaale123",
                    database="college_result_management_sys"
                )
                file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx)")

                df = pd.read_excel(file_path)

                cursor = conn.cursor()

                for index, row in df.iterrows():
                    sql = """Insert into college_result_management_sys.STUDDETAILS(Name ,Roll_no ,Branch ,
                                             Semester )
                                             values(%s,%s,%s,%s)"""

                    values = (row['Name'], row['Roll_no'], row['Branch'],
                              row['Semester'])

                    cursor.execute(sql, values)

                conn.commit()
                cursor.close()
                conn.close()

                self.statusBar().showMessage("Data uploaded successfully")
                QMessageBox.information(self, "Success", "Data uploaded successfully")


            except Exception as e:

                self.statusBar().showMessage("Error: " + str(e))

                QMessageBox.critical(self, "Error", str(e))


def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()