# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\legend-water.ui'
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
        legendDiagWater.setStyleSheet("QTableWidget {\n"
"    font-size: 9pt;\n"
"    font-family: \"Source Code Pro\", \"Consolas\";\n"
"}\n"
"")
        self.tableWidget_3 = QtWidgets.QTableWidget(legendDiagWater)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 40, 201, 291))
        self.tableWidget_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setAutoScroll(False)
        self.tableWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(8, 1, item)
        self.label = QtWidgets.QLabel(legendDiagWater)
        self.label.setGeometry(QtCore.QRect(40, 10, 131, 21))
        self.label.setStyleSheet("font: 75 16pt \"Open Sans\";\n"
"qproperty-alignment: AlignCenter;")
        self.label.setText("Water Blocks")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(legendDiagWater)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 211, 311))
        self.label_2.setStyleSheet("font: 75 9pt \"Open Sans\";")
        self.label_2.setText("<p><span style=\" font-weight:700;\">Water Blocks</span> serve as an obstacle<br>to the player much like Blocked Walls<br>but with a notable exception:<br>cubes will sink when pushed in water,<br>allowing the player to walk and push<br>other cubesover the suken one.</p><p>Water Blocks are more complicated<br>than ordinary blocks. In addition to<br>their confusing codes,each block<br>can only be placed in their titular<br>positions, e.g., only \"top\" blocks<br>can be placed on the top row,<br>or \"top left\" in the top left corner<br>of the board.</p><p>\"Horizontal\" and \"Vertical\" blocks are<br>the only blocks that can in placed<br>in non-border areas.</p>")
        self.label_2.setObjectName("label_2")
        self.tableWidget_4 = QtWidgets.QTableWidget(legendDiagWater)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 40, 201, 291))
        self.tableWidget_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setAutoScroll(False)
        self.tableWidget_4.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(8, 1, item)
        self.btnClose = QtWidgets.QPushButton(legendDiagWater)
        self.btnClose.setGeometry(QtCore.QRect(170, 370, 75, 23))
        self.btnClose.setText("Close")
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(legendDiagWater)
        self.btnClose.clicked.connect(legendDiagWater.close)
        QtCore.QMetaObject.connectSlotsByName(legendDiagWater)

    def retranslateUi(self, legendDiagWater):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("legendDiagWater", "Water Type"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("legendDiagWater", "Code"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(0, 0)
        item.setText(_translate("legendDiagWater", "Top"))
        item = self.tableWidget_3.item(0, 1)
        item.setText(_translate("legendDiagWater", "WI"))
        item = self.tableWidget_3.item(1, 0)
        item.setText(_translate("legendDiagWater", "Left"))
        item = self.tableWidget_3.item(1, 1)
        item.setText(_translate("legendDiagWater", "WJ"))
        item = self.tableWidget_3.item(2, 0)
        item.setText(_translate("legendDiagWater", "Right"))
        item = self.tableWidget_3.item(2, 1)
        item.setText(_translate("legendDiagWater", "WM"))
        item = self.tableWidget_3.item(3, 0)
        item.setText(_translate("legendDiagWater", "Top Left"))
        item = self.tableWidget_3.item(3, 1)
        item.setText(_translate("legendDiagWater", "WT"))
        item = self.tableWidget_3.item(4, 0)
        item.setText(_translate("legendDiagWater", "Top Right"))
        item = self.tableWidget_3.item(4, 1)
        item.setText(_translate("legendDiagWater", "WL"))
        item = self.tableWidget_3.item(5, 0)
        item.setText(_translate("legendDiagWater", "Bottom Left"))
        item = self.tableWidget_3.item(5, 1)
        item.setText(_translate("legendDiagWater", "WR"))
        item = self.tableWidget_3.item(6, 0)
        item.setText(_translate("legendDiagWater", "Bottom Right"))
        item = self.tableWidget_3.item(6, 1)
        item.setText(_translate("legendDiagWater", "WB"))
        item = self.tableWidget_3.item(7, 0)
        item.setText(_translate("legendDiagWater", "Vertical"))
        item = self.tableWidget_3.item(7, 1)
        item.setText(_translate("legendDiagWater", "WV"))
        item = self.tableWidget_3.item(8, 0)
        item.setText(_translate("legendDiagWater", "Horizontal"))
        item = self.tableWidget_3.item(8, 1)
        item.setText(_translate("legendDiagWater", "WH"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("legendDiagWater", "Water Type"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("legendDiagWater", "Code"))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        item = self.tableWidget_4.item(0, 0)
        item.setText(_translate("legendDiagWater", "Top"))
        item = self.tableWidget_4.item(0, 1)
        item.setText(_translate("legendDiagWater", "WI"))
        item = self.tableWidget_4.item(1, 0)
        item.setText(_translate("legendDiagWater", "Left"))
        item = self.tableWidget_4.item(1, 1)
        item.setText(_translate("legendDiagWater", "WJ"))
        item = self.tableWidget_4.item(2, 0)
        item.setText(_translate("legendDiagWater", "Right"))
        item = self.tableWidget_4.item(2, 1)
        item.setText(_translate("legendDiagWater", "WM"))
        item = self.tableWidget_4.item(3, 0)
        item.setText(_translate("legendDiagWater", "Top Left"))
        item = self.tableWidget_4.item(3, 1)
        item.setText(_translate("legendDiagWater", "WT"))
        item = self.tableWidget_4.item(4, 0)
        item.setText(_translate("legendDiagWater", "Top Right"))
        item = self.tableWidget_4.item(4, 1)
        item.setText(_translate("legendDiagWater", "WL"))
        item = self.tableWidget_4.item(5, 0)
        item.setText(_translate("legendDiagWater", "Bottom Left"))
        item = self.tableWidget_4.item(5, 1)
        item.setText(_translate("legendDiagWater", "WR"))
        item = self.tableWidget_4.item(6, 0)
        item.setText(_translate("legendDiagWater", "Bottom Right"))
        item = self.tableWidget_4.item(6, 1)
        item.setText(_translate("legendDiagWater", "WB"))
        item = self.tableWidget_4.item(7, 0)
        item.setText(_translate("legendDiagWater", "Vertical"))
        item = self.tableWidget_4.item(7, 1)
        item.setText(_translate("legendDiagWater", "WV"))
        item = self.tableWidget_4.item(8, 0)
        item.setText(_translate("legendDiagWater", "Horizontal"))
        item = self.tableWidget_4.item(8, 1)
        item.setText(_translate("legendDiagWater", "WH"))
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)

