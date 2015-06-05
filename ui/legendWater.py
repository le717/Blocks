# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\legendWater.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_legendDiagWater(object):
    def setupUi(self, legendDiagWater):
        legendDiagWater.setObjectName("legendDiagWater")
        legendDiagWater.resize(445, 410)
        legendDiagWater.setMinimumSize(QtCore.QSize(445, 410))
        legendDiagWater.setWindowTitle("Water Blocks Legend - app-name")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/images/Blocks.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        legendDiagWater.setWindowIcon(icon)
        legendDiagWater.setStyleSheet("QTableWidget {\n"
"    font-size: 9pt;\n"
"    font-family: \"Source Code Pro\", \"Consolas\";\n"
"}\n"
"")
        self.lbHeader = QtWidgets.QLabel(legendDiagWater)
        self.lbHeader.setGeometry(QtCore.QRect(40, 10, 131, 21))
        self.lbHeader.setStyleSheet("font: 75 16pt \"Open Sans\";\n"
"qproperty-alignment: AlignCenter;")
        self.lbHeader.setText("Water Blocks")
        self.lbHeader.setObjectName("lbHeader")
        self.lbDesc = QtWidgets.QLabel(legendDiagWater)
        self.lbDesc.setGeometry(QtCore.QRect(220, 40, 211, 311))
        self.lbDesc.setStyleSheet("font: 75 9pt \"Open Sans\";\n"
"qproperty-alignment: AlignTop;")
        self.lbDesc.setText("<p><span style=\" font-weight:700;\">Water Blocks</span> serve as an obstacle to the player much like Blocked Walls but with a notable exception: cubes will sink when pushed in water, allowing the player to walk and push other cubes over the sunken one.</p><p>Water Blocks are more complicated than ordinary blocks. In addition to their confusing codes, each block can only be placed in their titular positions, e.g., only Top can be placed on the top row, or Top Left in the top left corner of the board.</p><p>Horizontal and Vertical blocks are the only cubes that can in placed in non-bordered areas.</p>")
        self.lbDesc.setWordWrap(True)
        self.lbDesc.setObjectName("lbDesc")
        self.tableCodes = QtWidgets.QTableWidget(legendDiagWater)
        self.tableCodes.setGeometry(QtCore.QRect(10, 40, 201, 291))
        self.tableCodes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableCodes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableCodes.setAutoScroll(False)
        self.tableCodes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableCodes.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableCodes.setObjectName("tableCodes")
        self.tableCodes.setColumnCount(2)
        self.tableCodes.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableCodes.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCodes.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCodes.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCodes.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCodes.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCodes.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCodes.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCodes.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCodes.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Water Type")
        self.tableCodes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Code")
        self.tableCodes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Top")
        self.tableCodes.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("WI")
        self.tableCodes.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Left")
        self.tableCodes.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("WJ")
        self.tableCodes.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Right")
        self.tableCodes.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("WM")
        self.tableCodes.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Top Left")
        self.tableCodes.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("WT")
        self.tableCodes.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Top Right")
        self.tableCodes.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("WL")
        self.tableCodes.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Bottom Left")
        self.tableCodes.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("WR")
        self.tableCodes.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Bottom Right")
        self.tableCodes.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("WB")
        self.tableCodes.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Vertical")
        self.tableCodes.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("WV")
        self.tableCodes.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Horizontal")
        self.tableCodes.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("WH")
        self.tableCodes.setItem(8, 1, item)
        self.tableCodes.verticalHeader().setVisible(False)
        self.btnClose = QtWidgets.QPushButton(legendDiagWater)
        self.btnClose.setGeometry(QtCore.QRect(170, 370, 75, 23))
        self.btnClose.setText("Close")
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(legendDiagWater)
        self.btnClose.clicked.connect(legendDiagWater.close)
        QtCore.QMetaObject.connectSlotsByName(legendDiagWater)

    def retranslateUi(self, legendDiagWater):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.tableCodes.isSortingEnabled()
        self.tableCodes.setSortingEnabled(False)
        self.tableCodes.setSortingEnabled(__sortingEnabled)

import graphics_rc
