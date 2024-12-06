# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)
import Imgs_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 800)
        MainWindow.setMinimumSize(QSize(1120, 800))
        MainWindow.setMaximumSize(QSize(1120, 800))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"\n"
"QLabel{\n"
"	color: rgb(48, 48, 48);\n"
"}")
        self.Table_Frame = QFrame(self.centralwidget)
        self.Table_Frame.setObjectName(u"Table_Frame")
        self.Table_Frame.setGeometry(QRect(10, 0, 381, 781))
        self.Table_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 241, 233);\n"
"	background-color: rgb(240, 232, 225);\n"
"}\n"
"QLabel{\n"
"	color: rgb(45, 45, 45);\n"
"	font-size: 20px;\n"
"	background-color: rgb(255, 251, 229);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"	background-color: rgb(255, 254, 242);\n"
"	border: 1px solid black;\n"
"	border-radius: 10px;\n"
"	font-size: 30px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(240, 240, 240); /* Cor de fundo padr\u00e3o */\n"
"}\n"
"\n"
"/* Estado quando o bot\u00e3o \u00e9 pressionado */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 200, 200); /* Cor de fundo ao pressionar */\n"
"}\n"
"\n"
"/* Estado quando o mouse est\u00e1 sobre o bot\u00e3o */\n"
"QPushButton:hover {\n"
"    background-color: rgb(220, 220, 220); /* Cor de fundo ao passar o mouse */\n"
"}\n"
"")
        self.Table_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Table_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.Table_Frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 10, 231, 40))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Player_1_label = QLabel(self.layoutWidget)
        self.Player_1_label.setObjectName(u"Player_1_label")
        font = QFont()
        self.Player_1_label.setFont(font)

        self.horizontalLayout.addWidget(self.Player_1_label)

        self.Player_2_label = QLabel(self.layoutWidget)
        self.Player_2_label.setObjectName(u"Player_2_label")
        self.Player_2_label.setFont(font)

        self.horizontalLayout.addWidget(self.Player_2_label)

        self.layoutWidget1 = QWidget(self.Table_Frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 60, 381, 721))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Ones_Widget = QWidget(self.layoutWidget1)
        self.Ones_Widget.setObjectName(u"Ones_Widget")
        self.Ones = QLabel(self.Ones_Widget)
        self.Ones.setObjectName(u"Ones")
        self.Ones.setGeometry(QRect(10, 0, 101, 51))
        self.Ones_value_1 = QTextBrowser(self.Ones_Widget)
        self.Ones_value_1.setObjectName(u"Ones_value_1")
        self.Ones_value_1.setGeometry(QRect(140, 0, 111, 51))
        self.Ones_value_2 = QTextBrowser(self.Ones_Widget)
        self.Ones_value_2.setObjectName(u"Ones_value_2")
        self.Ones_value_2.setGeometry(QRect(260, 0, 111, 51))
        self.Ones_btn_1 = QPushButton(self.Ones_Widget)
        self.Ones_btn_1.setObjectName(u"Ones_btn_1")
        self.Ones_btn_1.setGeometry(QRect(140, 0, 111, 51))
        self.Ones_btn_2 = QPushButton(self.Ones_Widget)
        self.Ones_btn_2.setObjectName(u"Ones_btn_2")
        self.Ones_btn_2.setGeometry(QRect(260, 0, 111, 51))

        self.verticalLayout.addWidget(self.Ones_Widget)

        self.Twos_Widget = QWidget(self.layoutWidget1)
        self.Twos_Widget.setObjectName(u"Twos_Widget")
        self.Twos = QLabel(self.Twos_Widget)
        self.Twos.setObjectName(u"Twos")
        self.Twos.setGeometry(QRect(10, 0, 101, 51))
        self.Twos_value_1 = QTextBrowser(self.Twos_Widget)
        self.Twos_value_1.setObjectName(u"Twos_value_1")
        self.Twos_value_1.setGeometry(QRect(140, 0, 111, 51))
        self.Twos_value_2 = QTextBrowser(self.Twos_Widget)
        self.Twos_value_2.setObjectName(u"Twos_value_2")
        self.Twos_value_2.setGeometry(QRect(260, 0, 111, 51))
        self.Twos_btn_1 = QPushButton(self.Twos_Widget)
        self.Twos_btn_1.setObjectName(u"Twos_btn_1")
        self.Twos_btn_1.setGeometry(QRect(140, 0, 111, 51))
        self.Twos_btn_2 = QPushButton(self.Twos_Widget)
        self.Twos_btn_2.setObjectName(u"Twos_btn_2")
        self.Twos_btn_2.setGeometry(QRect(260, 0, 111, 51))

        self.verticalLayout.addWidget(self.Twos_Widget)

        self.Threes_Widget = QWidget(self.layoutWidget1)
        self.Threes_Widget.setObjectName(u"Threes_Widget")
        self.Threes = QLabel(self.Threes_Widget)
        self.Threes.setObjectName(u"Threes")
        self.Threes.setGeometry(QRect(10, 0, 101, 51))
        self.Threes_value_1 = QTextBrowser(self.Threes_Widget)
        self.Threes_value_1.setObjectName(u"Threes_value_1")
        self.Threes_value_1.setGeometry(QRect(140, 0, 111, 51))
        self.Threes_value_2 = QTextBrowser(self.Threes_Widget)
        self.Threes_value_2.setObjectName(u"Threes_value_2")
        self.Threes_value_2.setGeometry(QRect(260, 0, 111, 51))
        self.Threes_btn_1 = QPushButton(self.Threes_Widget)
        self.Threes_btn_1.setObjectName(u"Threes_btn_1")
        self.Threes_btn_1.setGeometry(QRect(140, 0, 111, 51))
        self.Threes_btn_2 = QPushButton(self.Threes_Widget)
        self.Threes_btn_2.setObjectName(u"Threes_btn_2")
        self.Threes_btn_2.setGeometry(QRect(260, 0, 111, 51))

        self.verticalLayout.addWidget(self.Threes_Widget)

        self.Fours_Widget = QWidget(self.layoutWidget1)
        self.Fours_Widget.setObjectName(u"Fours_Widget")
        self.Fours = QLabel(self.Fours_Widget)
        self.Fours.setObjectName(u"Fours")
        self.Fours.setGeometry(QRect(10, 0, 101, 51))
        self.Fours_value_1 = QTextBrowser(self.Fours_Widget)
        self.Fours_value_1.setObjectName(u"Fours_value_1")
        self.Fours_value_1.setGeometry(QRect(140, 0, 111, 51))
        self.Fours_value_2 = QTextBrowser(self.Fours_Widget)
        self.Fours_value_2.setObjectName(u"Fours_value_2")
        self.Fours_value_2.setGeometry(QRect(260, 0, 111, 51))
        self.Fours_btn_1 = QPushButton(self.Fours_Widget)
        self.Fours_btn_1.setObjectName(u"Fours_btn_1")
        self.Fours_btn_1.setGeometry(QRect(140, 0, 111, 51))
        self.Fours_btn_2 = QPushButton(self.Fours_Widget)
        self.Fours_btn_2.setObjectName(u"Fours_btn_2")
        self.Fours_btn_2.setGeometry(QRect(260, 0, 111, 51))

        self.verticalLayout.addWidget(self.Fours_Widget)

        self.Fives_Widget = QWidget(self.layoutWidget1)
        self.Fives_Widget.setObjectName(u"Fives_Widget")
        self.Fives = QLabel(self.Fives_Widget)
        self.Fives.setObjectName(u"Fives")
        self.Fives.setGeometry(QRect(10, 0, 101, 51))
        self.Fives_value_1 = QTextBrowser(self.Fives_Widget)
        self.Fives_value_1.setObjectName(u"Fives_value_1")
        self.Fives_value_1.setGeometry(QRect(140, 0, 111, 51))
        self.Fives_value_2 = QTextBrowser(self.Fives_Widget)
        self.Fives_value_2.setObjectName(u"Fives_value_2")
        self.Fives_value_2.setGeometry(QRect(260, 0, 111, 51))
        self.Fives_btn_1 = QPushButton(self.Fives_Widget)
        self.Fives_btn_1.setObjectName(u"Fives_btn_1")
        self.Fives_btn_1.setGeometry(QRect(140, 0, 111, 51))
        self.Fives_btn_2 = QPushButton(self.Fives_Widget)
        self.Fives_btn_2.setObjectName(u"Fives_btn_2")
        self.Fives_btn_2.setGeometry(QRect(260, 0, 111, 51))

        self.verticalLayout.addWidget(self.Fives_Widget)

        self.Sixes_Widget = QWidget(self.layoutWidget1)
        self.Sixes_Widget.setObjectName(u"Sixes_Widget")
        self.Sixes = QLabel(self.Sixes_Widget)
        self.Sixes.setObjectName(u"Sixes")
        self.Sixes.setGeometry(QRect(10, 0, 101, 51))
        self.Sixes_value_1 = QTextBrowser(self.Sixes_Widget)
        self.Sixes_value_1.setObjectName(u"Sixes_value_1")
        self.Sixes_value_1.setGeometry(QRect(140, 0, 111, 51))
        self.Sixes_value_2 = QTextBrowser(self.Sixes_Widget)
        self.Sixes_value_2.setObjectName(u"Sixes_value_2")
        self.Sixes_value_2.setGeometry(QRect(260, 0, 111, 51))
        self.Sixes_btn_1 = QPushButton(self.Sixes_Widget)
        self.Sixes_btn_1.setObjectName(u"Sixes_btn_1")
        self.Sixes_btn_1.setGeometry(QRect(140, 0, 111, 51))
        self.Sixes_btn_2 = QPushButton(self.Sixes_Widget)
        self.Sixes_btn_2.setObjectName(u"Sixes_btn_2")
        self.Sixes_btn_2.setGeometry(QRect(260, 0, 111, 51))

        self.verticalLayout.addWidget(self.Sixes_Widget)

        self.Four_of_Widget = QWidget(self.layoutWidget1)
        self.Four_of_Widget.setObjectName(u"Four_of_Widget")
        self.Four_Of = QLabel(self.Four_of_Widget)
        self.Four_Of.setObjectName(u"Four_Of")
        self.Four_Of.setGeometry(QRect(10, 0, 111, 51))
        self.Four_Of_value_1 = QTextBrowser(self.Four_of_Widget)
        self.Four_Of_value_1.setObjectName(u"Four_Of_value_1")
        self.Four_Of_value_1.setGeometry(QRect(140, 0, 111, 51))
        self.Four_Of_value_2 = QTextBrowser(self.Four_of_Widget)
        self.Four_Of_value_2.setObjectName(u"Four_Of_value_2")
        self.Four_Of_value_2.setGeometry(QRect(260, 0, 111, 51))
        self.Four_Of_btn_1 = QPushButton(self.Four_of_Widget)
        self.Four_Of_btn_1.setObjectName(u"Four_Of_btn_1")
        self.Four_Of_btn_1.setGeometry(QRect(140, 0, 111, 51))
        self.Four_Of_btn_2 = QPushButton(self.Four_of_Widget)
        self.Four_Of_btn_2.setObjectName(u"Four_Of_btn_2")
        self.Four_Of_btn_2.setGeometry(QRect(260, 0, 111, 51))

        self.verticalLayout.addWidget(self.Four_of_Widget)

        self.Full_House_Widget = QWidget(self.layoutWidget1)
        self.Full_House_Widget.setObjectName(u"Full_House_Widget")
        self.Full_House = QLabel(self.Full_House_Widget)
        self.Full_House.setObjectName(u"Full_House")
        self.Full_House.setGeometry(QRect(10, 0, 111, 51))
        self.Full_House_value_1 = QTextBrowser(self.Full_House_Widget)
        self.Full_House_value_1.setObjectName(u"Full_House_value_1")
        self.Full_House_value_1.setGeometry(QRect(140, 0, 111, 51))
        self.Full_House_value_2 = QTextBrowser(self.Full_House_Widget)
        self.Full_House_value_2.setObjectName(u"Full_House_value_2")
        self.Full_House_value_2.setGeometry(QRect(260, 0, 111, 51))
        self.Full_House_btn_1 = QPushButton(self.Full_House_Widget)
        self.Full_House_btn_1.setObjectName(u"Full_House_btn_1")
        self.Full_House_btn_1.setGeometry(QRect(140, 0, 111, 51))
        self.Full_House_btn_2 = QPushButton(self.Full_House_Widget)
        self.Full_House_btn_2.setObjectName(u"Full_House_btn_2")
        self.Full_House_btn_2.setGeometry(QRect(260, 0, 111, 51))

        self.verticalLayout.addWidget(self.Full_House_Widget)

        self.S_Straight_Widget = QWidget(self.layoutWidget1)
        self.S_Straight_Widget.setObjectName(u"S_Straight_Widget")
        self.S_Straight = QLabel(self.S_Straight_Widget)
        self.S_Straight.setObjectName(u"S_Straight")
        self.S_Straight.setGeometry(QRect(10, 0, 111, 51))
        self.S_Straight_value_1 = QTextBrowser(self.S_Straight_Widget)
        self.S_Straight_value_1.setObjectName(u"S_Straight_value_1")
        self.S_Straight_value_1.setGeometry(QRect(140, 0, 111, 51))
        self.S_Straight_value_2 = QTextBrowser(self.S_Straight_Widget)
        self.S_Straight_value_2.setObjectName(u"S_Straight_value_2")
        self.S_Straight_value_2.setGeometry(QRect(260, 0, 111, 51))
        self.S_Straight_btn_1 = QPushButton(self.S_Straight_Widget)
        self.S_Straight_btn_1.setObjectName(u"S_Straight_btn_1")
        self.S_Straight_btn_1.setGeometry(QRect(140, 0, 111, 51))
        self.S_Straight_btn_2 = QPushButton(self.S_Straight_Widget)
        self.S_Straight_btn_2.setObjectName(u"S_Straight_btn_2")
        self.S_Straight_btn_2.setGeometry(QRect(260, 0, 111, 51))

        self.verticalLayout.addWidget(self.S_Straight_Widget)

        self.B_Straight_Widget = QWidget(self.layoutWidget1)
        self.B_Straight_Widget.setObjectName(u"B_Straight_Widget")
        self.B_Straight = QLabel(self.B_Straight_Widget)
        self.B_Straight.setObjectName(u"B_Straight")
        self.B_Straight.setGeometry(QRect(10, 0, 111, 51))
        self.B_Straight_value_1 = QTextBrowser(self.B_Straight_Widget)
        self.B_Straight_value_1.setObjectName(u"B_Straight_value_1")
        self.B_Straight_value_1.setGeometry(QRect(140, 0, 111, 51))
        self.B_Straight_value_2 = QTextBrowser(self.B_Straight_Widget)
        self.B_Straight_value_2.setObjectName(u"B_Straight_value_2")
        self.B_Straight_value_2.setGeometry(QRect(260, 0, 111, 51))
        self.B_Straight_btn_1 = QPushButton(self.B_Straight_Widget)
        self.B_Straight_btn_1.setObjectName(u"B_Straight_btn_1")
        self.B_Straight_btn_1.setGeometry(QRect(140, 0, 111, 51))
        self.B_Straight_btn_2 = QPushButton(self.B_Straight_Widget)
        self.B_Straight_btn_2.setObjectName(u"B_Straight_btn_2")
        self.B_Straight_btn_2.setGeometry(QRect(260, 0, 111, 51))

        self.verticalLayout.addWidget(self.B_Straight_Widget)

        self.Yatch_Widget = QWidget(self.layoutWidget1)
        self.Yatch_Widget.setObjectName(u"Yatch_Widget")
        self.Yatch = QLabel(self.Yatch_Widget)
        self.Yatch.setObjectName(u"Yatch")
        self.Yatch.setGeometry(QRect(10, 0, 101, 51))
        self.Yatch_value_1 = QTextBrowser(self.Yatch_Widget)
        self.Yatch_value_1.setObjectName(u"Yatch_value_1")
        self.Yatch_value_1.setGeometry(QRect(140, 0, 111, 51))
        self.Yatch_value_2 = QTextBrowser(self.Yatch_Widget)
        self.Yatch_value_2.setObjectName(u"Yatch_value_2")
        self.Yatch_value_2.setGeometry(QRect(260, 0, 111, 51))
        self.Yatch_btn_1 = QPushButton(self.Yatch_Widget)
        self.Yatch_btn_1.setObjectName(u"Yatch_btn_1")
        self.Yatch_btn_1.setGeometry(QRect(140, 0, 111, 51))
        self.Yatch_btn_2 = QPushButton(self.Yatch_Widget)
        self.Yatch_btn_2.setObjectName(u"Yatch_btn_2")
        self.Yatch_btn_2.setGeometry(QRect(260, 0, 111, 51))

        self.verticalLayout.addWidget(self.Yatch_Widget)

        self.Mesa_Frame = QFrame(self.centralwidget)
        self.Mesa_Frame.setObjectName(u"Mesa_Frame")
        self.Mesa_Frame.setGeometry(QRect(390, 0, 731, 781))
        self.Mesa_Frame.setStyleSheet(u"QFrame{\n"
"	background-image: url(:/Imgs/background.png);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(183, 158, 139);\n"
"	color: rgb(40, 40, 40);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* Estado quando o bot\u00e3o \u00e9 pressionado */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 200, 200); /* Cor de fundo ao pressionar */\n"
"}\n"
"\n"
"/* Estado quando o mouse est\u00e1 sobre o bot\u00e3o */\n"
"QPushButton:hover {\n"
"    background-color: rgb(124, 106, 94);/* Cor de fundo ao passar o mouse */\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.Mesa_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Mesa_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Mesa_img = QLabel(self.Mesa_Frame)
        self.Mesa_img.setObjectName(u"Mesa_img")
        self.Mesa_img.setGeometry(QRect(40, 120, 661, 461))
        self.layoutWidget2 = QWidget(self.Mesa_Frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(110, 590, 521, 121))
        # Criar o QLabel para o status
        self.status_label = QLabel("Bem-vindo ao jogo!", self.layoutWidget2)
        self.status_label.setStyleSheet("color: black; font-size: 16px;")
        self.status_label.setMinimumWidth(521)
        self.status_label.setAlignment(Qt.AlignCenter)
        #
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Jogar_dados = QPushButton(self.layoutWidget2)
        self.Jogar_dados.setObjectName(u"Jogar_dados")
        font1 = QFont()
        font1.setPointSize(20)
        self.Jogar_dados.setFont(font1)
        self.Jogar_dados.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.Jogar_dados)

        self.dado_1 = QLabel(self.Mesa_Frame)
        self.dado_1.setObjectName(u"dado_1")
        self.dado_1.setGeometry(QRect(70, 300, 101, 101))
        self.dado_1.setMaximumSize(QSize(16777215, 16777213))
        self.dado_1.setAutoFillBackground(False)
        self.dado_1.setStyleSheet(u"background-color: white;")
        self.dado_2 = QLabel(self.Mesa_Frame)
        self.dado_2.setObjectName(u"dado_2")
        self.dado_2.setGeometry(QRect(190, 300, 101, 101))
        self.dado_2.setMaximumSize(QSize(16777215, 16777213))
        self.dado_2.setAutoFillBackground(False)
        self.dado_2.setStyleSheet(u"background-color: white;")
        self.dado_3 = QLabel(self.Mesa_Frame)
        self.dado_3.setObjectName(u"dado_3")
        self.dado_3.setGeometry(QRect(310, 300, 101, 101))
        self.dado_3.setMaximumSize(QSize(16777215, 16777213))
        self.dado_3.setAutoFillBackground(False)
        self.dado_3.setStyleSheet(u"background-color: white;")
        self.dado_4 = QLabel(self.Mesa_Frame)
        self.dado_4.setObjectName(u"dado_4")
        self.dado_4.setGeometry(QRect(440, 300, 101, 101))
        self.dado_4.setMaximumSize(QSize(16777215, 16777213))
        self.dado_4.setAutoFillBackground(False)
        self.dado_4.setStyleSheet(u"background-color: white;")
        self.dado_5 = QLabel(self.Mesa_Frame)
        self.dado_5.setObjectName(u"dado_5")
        self.dado_5.setGeometry(QRect(570, 300, 101, 101))
        self.dado_5.setMaximumSize(QSize(16777215, 16777213))
        self.dado_5.setAutoFillBackground(False)
        self.dado_5.setStyleSheet(u"background-color: white;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Player_1_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:15pt;\">Player_1: </span></p></body></html>", None))
        self.Player_2_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:15pt;\">Player_2:</span></p></body></html>", None))
        self.Ones.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Ones</span></p></body></html>", None))
        self.Ones_btn_1.setText("")
        self.Ones_btn_2.setText("")
        self.Twos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Twos</span></p></body></html>", None))
        self.Twos_btn_1.setText("")
        self.Twos_btn_2.setText("")
        self.Threes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Threes</span></p></body></html>", None))
        self.Threes_btn_1.setText("")
        self.Threes_btn_2.setText("")
        self.Fours.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Fours</span></p></body></html>", None))
        self.Fours_btn_1.setText("")
        self.Fours_btn_2.setText("")
        self.Fives.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Fives</span></p></body></html>", None))
        self.Fives_btn_1.setText("")
        self.Fives_btn_2.setText("")
        self.Sixes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Sixes</span></p></body></html>", None))
        self.Sixes_btn_1.setText("")
        self.Sixes_btn_2.setText("")
        self.Four_Of.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">4 Of a Kind</span></p></body></html>", None))
        self.Four_Of_btn_1.setText("")
        self.Four_Of_btn_2.setText("")
        self.Full_House.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Full House</span></p></body></html>", None))
        self.Full_House_btn_1.setText("")
        self.Full_House_btn_2.setText("")
        self.S_Straight.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">S. Straight</span></p></body></html>", None))
        self.S_Straight_value_1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:30px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.S_Straight_value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:30px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.S_Straight_btn_1.setText("")
        self.S_Straight_btn_2.setText("")
        self.B_Straight.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">B. Straight</span></p></body></html>", None))
        self.B_Straight_btn_1.setText("")
        self.B_Straight_btn_2.setText("")
        self.Yatch.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Yatch</span></p></body></html>", None))
        self.Yatch_value_1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:30px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Yatch_value_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:30px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Yatch_btn_1.setText("")
        self.Yatch_btn_2.setText("")
        self.Mesa_img.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Imgs/mesa.png\"/></p></body></html>", None))
        self.Jogar_dados.setText(QCoreApplication.translate("MainWindow", u"Jogar Dados", None))
        self.dado_1.setText("")
        self.dado_2.setText("")
        self.dado_3.setText("")
        self.dado_4.setText("")
        self.dado_5.setText("")
    # retranslateUi

