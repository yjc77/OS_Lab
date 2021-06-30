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
        MainWindow.setEnabled(True)
        MainWindow.resize(630, 752)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 610, 711))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.add_process = QtWidgets.QPushButton(self.groupBox)
        self.add_process.setObjectName("add_process")
        self.gridLayout.addWidget(self.add_process, 0, 6, 1, 1)
        self.arrive_time_msg = QtWidgets.QLabel(self.groupBox)
        self.arrive_time_msg.setObjectName("arrive_time_msg")
        self.gridLayout.addWidget(self.arrive_time_msg, 0, 2, 1, 1)
        self.arrive_time = QtWidgets.QLineEdit(self.groupBox)
        self.arrive_time.setObjectName("arrive_time")
        self.gridLayout.addWidget(self.arrive_time, 0, 3, 1, 1)
        self.service_time = QtWidgets.QLineEdit(self.groupBox)
        self.service_time.setObjectName("service_time")
        self.gridLayout.addWidget(self.service_time, 0, 5, 1, 1)
        self.process_name = QtWidgets.QLineEdit(self.groupBox)
        self.process_name.setObjectName("process_name")
        self.gridLayout.addWidget(self.process_name, 0, 1, 1, 1)
        self.service_time_msg = QtWidgets.QLabel(self.groupBox)
        self.service_time_msg.setObjectName("service_time_msg")
        self.gridLayout.addWidget(self.service_time_msg, 0, 4, 1, 1)
        self.process_msg = QtWidgets.QLabel(self.groupBox)
        self.process_msg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.process_msg.setObjectName("process_msg")
        self.gridLayout.addWidget(self.process_msg, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(145)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 7)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.choose_fcfs = QtWidgets.QPushButton(self.groupBox_2)
        self.choose_fcfs.setObjectName("choose_fcfs")
        self.gridLayout_2.addWidget(self.choose_fcfs, 0, 0, 1, 1)
        self.avgrage_time_weight_msg = QtWidgets.QLabel(self.groupBox_2)
        self.avgrage_time_weight_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.avgrage_time_weight_msg.setObjectName("avgrage_time_weight_msg")
        self.gridLayout_2.addWidget(self.avgrage_time_weight_msg, 3, 2, 1, 1)
        self.choose_hrn = QtWidgets.QPushButton(self.groupBox_2)
        self.choose_hrn.setObjectName("choose_hrn")
        self.gridLayout_2.addWidget(self.choose_hrn, 0, 3, 1, 1)
        self.choose_sjf = QtWidgets.QPushButton(self.groupBox_2)
        self.choose_sjf.setObjectName("choose_sjf")
        self.gridLayout_2.addWidget(self.choose_sjf, 0, 1, 1, 1)
        self.avgrage_time = QtWidgets.QLabel(self.groupBox_2)
        self.avgrage_time.setObjectName("avgrage_time")
        self.gridLayout_2.addWidget(self.avgrage_time, 3, 1, 1, 1)
        self.choose_rr = QtWidgets.QPushButton(self.groupBox_2)
        self.choose_rr.setObjectName("choose_rr")
        self.gridLayout_2.addWidget(self.choose_rr, 0, 2, 1, 1)
        self.avgrage_time_msg = QtWidgets.QLabel(self.groupBox_2)
        self.avgrage_time_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.avgrage_time_msg.setObjectName("avgrage_time_msg")
        self.gridLayout_2.addWidget(self.avgrage_time_msg, 3, 0, 1, 1)
        self.avgrage_time_weight = QtWidgets.QLabel(self.groupBox_2)
        self.avgrage_time_weight.setObjectName("avgrage_time_weight")
        self.gridLayout_2.addWidget(self.avgrage_time_weight, 3, 3, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(96)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(25)
        self.gridLayout_2.addWidget(self.tableWidget_2, 1, 0, 1, 4)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.add_process.clicked.connect(self.row_add)
        self.choose_fcfs.clicked.connect(self.FCFS_msg)
        self.choose_sjf.clicked.connect(self.SJF_msg)
        self.choose_rr.clicked.connect(self.RR_msg)
        self.choose_hrn.clicked.connect(self.HRN_msg)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def row_add(self):
        pass

    def FCFS_msg(self):
        pass

    def SJF_msg(self):
        pass

    def RR_msg(self):
        pass

    def HRN_msg(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "处理器调度算法模拟"))
        self.groupBox.setTitle(_translate("MainWindow", "添加进程"))
        self.add_process.setText(_translate("MainWindow", "添加"))
        self.arrive_time_msg.setText(_translate("MainWindow", "到达时间："))
        self.service_time_msg.setText(_translate("MainWindow", "服务时间："))
        self.process_msg.setText(_translate("MainWindow", "进程名："))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "进程名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "到达时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "服务时间"))
        self.groupBox_2.setTitle(_translate("MainWindow", "算法执行"))
        self.choose_fcfs.setText(_translate("MainWindow", "先来先服务FCFS"))
        self.avgrage_time_weight_msg.setText(_translate("MainWindow", "带权周转时间："))
        self.choose_hrn.setText(_translate("MainWindow", "最高响应比优先HRN"))
        self.choose_sjf.setText(_translate("MainWindow", "短作业优先SJF"))
        self.avgrage_time.setText(_translate("MainWindow", "0"))
        self.choose_rr.setText(_translate("MainWindow", "轮转RR"))
        self.avgrage_time_msg.setText(_translate("MainWindow", "平均周转时间："))
        self.avgrage_time_weight.setText(_translate("MainWindow", "0"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "进程名"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "到达时间"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "服务时间"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "完成时间"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "周转时间"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "带权周转时间"))