# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(777, 565)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(777, 565))
        MainWindow.setMaximumSize(QtCore.QSize(777, 565))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 761, 528))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.executeStep = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.executeStep.setObjectName("executeStep")
        self.gridLayout.addWidget(self.executeStep, 6, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 2, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.tableWidget_1 = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget_1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_1.setShowGrid(False)
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(3)
        self.tableWidget_1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(2, item)
        self.tableWidget_1.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget_1.verticalHeader().setVisible(False)
        self.tableWidget_1.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_1.verticalHeader().setMinimumSectionSize(25)
        self.gridLayout.addWidget(self.tableWidget_1, 5, 0, 1, 2)
        self.workNum = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.workNum.setObjectName("workNum")
        self.gridLayout.addWidget(self.workNum, 1, 1, 1, 1)
        self.generate = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.generate.setObjectName("generate")
        self.gridLayout.addWidget(self.generate, 1, 3, 1, 1)
        self.executeAll = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.executeAll.setObjectName("executeAll")
        self.gridLayout.addWidget(self.executeAll, 6, 2, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 3)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(113)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(25)
        self.gridLayout.addWidget(self.tableWidget_2, 5, 2, 1, 2)
        self.workMaxNum = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.workMaxNum.setObjectName("workMaxNum")
        self.gridLayout.addWidget(self.workMaxNum, 0, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 2)
        self.workMem = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.workMem.setReadOnly(True)
        self.workMem.setObjectName("workMem")
        self.gridLayout.addWidget(self.workMem, 3, 1, 1, 3)
        self.memorySize = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.memorySize.setObjectName("memorySize")
        self.gridLayout.addWidget(self.memorySize, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 4, 6, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.generate.clicked.connect(self.product_order)
        self.executeStep.clicked.connect(self.distribute)
        self.executeAll.clicked.connect(self.recycle)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def product_order(self):
        pass

    def distribute(self):
        pass

    def recycle(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "存储管理模拟"))
        self.label_8.setText(_translate("MainWindow", "内存大小(K)"))
        self.executeStep.setText(_translate("MainWindow", "分配"))
        self.label_12.setText(_translate("MainWindow", "内存中作业"))
        self.label_9.setText(_translate("MainWindow", "作业大小:1~"))
        self.label_14.setText(_translate("MainWindow", "空闲分区表"))
        self.label_10.setText(_translate("MainWindow", "作业数量"))
        item = self.tableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "作业名"))
        item = self.tableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "大小(K)"))
        item = self.tableWidget_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "区间"))
        self.generate.setText(_translate("MainWindow", "生成序列"))
        self.executeAll.setText(_translate("MainWindow", "回收"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "大小(K)"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "区间"))
        self.label_11.setText(_translate("MainWindow", "作业序列"))
        self.label_13.setText(_translate("MainWindow", "已分区表"))
        self.label.setText(_translate("MainWindow", "操作信息"))