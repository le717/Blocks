# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\about.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutDiag(object):
    def setupUi(self, aboutDiag):
        aboutDiag.setObjectName("aboutDiag")
        aboutDiag.resize(368, 320)
        aboutDiag.setMinimumSize(QtCore.QSize(368, 320))
        aboutDiag.setWindowTitle("About - app-name")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/images/Blocks.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutDiag.setWindowIcon(icon)
        aboutDiag.setStyleSheet("QTableWidget { font-size: 9pt; }\n"
"QLabel { qproperty-alignment: AlignCenter; }")
        self.lbCreated = QtWidgets.QLabel(aboutDiag)
        self.lbCreated.setGeometry(QtCore.QRect(120, 50, 131, 41))
        self.lbCreated.setMinimumSize(QtCore.QSize(0, 0))
        self.lbCreated.setStyleSheet("font-size: 10pt;")
        self.lbCreated.setText("<p>Created 2013-2015 app-creator</p>")
        self.lbCreated.setWordWrap(True)
        self.lbCreated.setObjectName("lbCreated")
        self.lbHeader = QtWidgets.QLabel(aboutDiag)
        self.lbHeader.setGeometry(QtCore.QRect(110, 20, 151, 21))
        self.lbHeader.setStyleSheet("font-size: 15pt;")
        self.lbHeader.setText("app-name vapp-version")
        self.lbHeader.setObjectName("lbHeader")
        self.btnClose = QtWidgets.QPushButton(aboutDiag)
        self.btnClose.setGeometry(QtCore.QRect(150, 280, 75, 23))
        self.btnClose.setText("Close")
        self.btnClose.setObjectName("btnClose")
        self.appLogo = QtWidgets.QFrame(aboutDiag)
        self.appLogo.setGeometry(QtCore.QRect(110, 100, 151, 101))
        self.appLogo.setStyleSheet("image: url(:/ui/images/Blocks.png);")
        self.appLogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.appLogo.setObjectName("appLogo")
        self.btnGitHub = QtWidgets.QPushButton(aboutDiag)
        self.btnGitHub.setGeometry(QtCore.QRect(60, 280, 75, 23))
        self.btnGitHub.setText("GitHub")
        self.btnGitHub.setObjectName("btnGitHub")
        self.btnLicense = QtWidgets.QPushButton(aboutDiag)
        self.btnLicense.setGeometry(QtCore.QRect(240, 280, 75, 23))
        self.btnLicense.setText("License")
        self.btnLicense.setObjectName("btnLicense")
        self.label = QtWidgets.QLabel(aboutDiag)
        self.label.setGeometry(QtCore.QRect(0, 200, 371, 61))
        self.label.setStyleSheet("font-size: 13pt;\n"
"qproperty-wordWrap: true;")
        self.label.setText("An Island Xtreme Stunts Trouble in Store minigame level editor.")
        self.label.setObjectName("label")

        self.retranslateUi(aboutDiag)
        self.btnClose.clicked.connect(aboutDiag.close)
        QtCore.QMetaObject.connectSlotsByName(aboutDiag)
        aboutDiag.setTabOrder(self.btnGitHub, self.btnClose)
        aboutDiag.setTabOrder(self.btnClose, self.btnLicense)

    def retranslateUi(self, aboutDiag):
        pass

import graphics_rc
