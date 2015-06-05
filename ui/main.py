# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 274)
        MainWindow.setWindowTitle("app-name app-ver")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/images/Blocks.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QLabel {\n"
"font-family: \"Open Sans\";\n"
"font-size: 9pt;\n"
"qproperty-alignment: AlignCenter\n"
"}")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.appLogo = QtWidgets.QFrame(self.centralwidget)
        self.appLogo.setGeometry(QtCore.QRect(430, 150, 120, 80))
        self.appLogo.setStyleSheet("image: url(:/Logo/images/Blocks.png);\n"
"border: none;")
        self.appLogo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.appLogo.setObjectName("appLogo")
        self.btnNew = QtWidgets.QPushButton(self.centralwidget)
        self.btnNew.setGeometry(QtCore.QRect(450, 60, 75, 23))
        self.btnNew.setText("New")
        self.btnNew.setObjectName("btnNew")
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setGeometry(QtCore.QRect(450, 90, 75, 23))
        self.btnOpen.setText("Open")
        self.btnOpen.setObjectName("btnOpen")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(450, 120, 75, 23))
        self.btnSave.setText("Save")
        self.btnSave.setObjectName("btnSave")
        self.pteLevelArea = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pteLevelArea.setGeometry(QtCore.QRect(60, 60, 321, 141))
        self.pteLevelArea.setStyleSheet("font-size: 10pt;\n"
"font-family: \"Source Code Pro\", \"Consolas\";")
        self.pteLevelArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pteLevelArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pteLevelArea.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.pteLevelArea.setPlainText("")
        self.pteLevelArea.setPlaceholderText("Minigame layout will be displayed here.")
        self.pteLevelArea.setObjectName("pteLevelArea")
        self.appDetails = QtWidgets.QLabel(self.centralwidget)
        self.appDetails.setGeometry(QtCore.QRect(430, 0, 111, 20))
        self.appDetails.setText("app-name app-ver")
        self.appDetails.setObjectName("appDetails")
        self.appYear = QtWidgets.QLabel(self.centralwidget)
        self.appYear.setGeometry(QtCore.QRect(430, 16, 111, 20))
        self.appYear.setText("Created 2013-2015")
        self.appYear.setObjectName("appYear")
        self.appCreator = QtWidgets.QLabel(self.centralwidget)
        self.appCreator.setGeometry(QtCore.QRect(450, 30, 71, 20))
        self.appCreator.setStyleSheet("")
        self.appCreator.setText("app-creator")
        self.appCreator.setObjectName("appCreator")
        self.lbLevelName = QtWidgets.QLabel(self.centralwidget)
        self.lbLevelName.setGeometry(QtCore.QRect(180, 30, 71, 16))
        self.lbLevelName.setStyleSheet("font-size: 10pt;")
        self.lbLevelName.setText("")
        self.lbLevelName.setObjectName("lbLevelName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setTearOffEnabled(False)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setEnabled(True)
        self.menuHelp.setObjectName("menuHelp")
        self.menuLegend = QtWidgets.QMenu(self.menuHelp)
        self.menuLegend.setObjectName("menuLegend")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionLegendWater = QtWidgets.QAction(MainWindow)
        self.actionLegendWater.setObjectName("actionLegendWater")
        self.actionLegendMain = QtWidgets.QAction(MainWindow)
        self.actionLegendMain.setObjectName("actionLegendMain")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setEnabled(False)
        self.actionAbout.setText("&About")
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuLegend.addAction(self.actionLegendMain)
        self.menuLegend.addAction(self.actionLegendWater)
        self.menuHelp.addAction(self.menuLegend.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.menuLegend.setTitle(_translate("MainWindow", "&Legend"))
        self.actionNew.setText(_translate("MainWindow", "&New"))
        self.actionNew.setIconText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "&Open..."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionLegendWater.setText(_translate("MainWindow", "&Water Blocks"))
        self.actionLegendMain.setText(_translate("MainWindow", "&Main Blocks"))

import graphics_rc
