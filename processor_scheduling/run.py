import sys
from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from SchedulingAlgorithm import Schedule


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.process_name_text = None   # 进程名称
        self.arrive_time_text = None    # 到达时间
        self.service_time_text = None   # 服务时间

        self.dict = []
        self.order = 0
        self.rowNum = 0

    def row_add(self):
        """
        将所添加的进程信息显示出来
        :return:
        """
        self.process_name_text = self.process_name.text()  # 获取进程名称
        self.arrive_time_text = self.arrive_time.text()     # 获取进程的到达时间
        self.service_time_text = self.service_time.text()     # 获取进程的服务时间

        # 删除linetxt中的信息
        self.process_name.clear()
        self.arrive_time.clear()
        self.service_time.clear()

        if (self.process_name_text is not None) and (self.arrive_time_text is not None ) and (self.service_time_text is not None) :
            self.dict.append((self.order, self.process_name_text, int(self.arrive_time_text), int(self.service_time_text)))
            # print(self.dict)

            self.tableWidget.setItem(self.rowNum, 0, QTableWidgetItem(str(self.order)))
            self.tableWidget.setItem(self.rowNum, 1, QTableWidgetItem(self.process_name_text))
            self.tableWidget.setItem(self.rowNum, 2, QTableWidgetItem(self.arrive_time_text))
            self.tableWidget.setItem(self.rowNum, 3, QTableWidgetItem(self.service_time_text))
            self.rowNum += 1
            self.order += 1
        else:
            print("error")

    def FCFS_msg(self):
        """
        先来先服务算法
        :return:
        """
        print("this is fcfs")
        state = Schedule(self.dict)
        message = state.FCFS_schedule()
        self.output_res(message)

    def SJF_msg(self):
        """
        短作业优先算法
        :return:
        """
        print('this is sjf')
        state = Schedule(self.dict)
        message = state.SJF_schedule()
        self.output_res(message)

    def output_res(self, message):
        """
        显示算法调度之后各进程的运行结果
        :param message: 装有运行结果的信息
        :return:
        """
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(len(message))
        for i in range(len(message)):
            self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(message[i][0])))
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(message[i][1])))
            self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(message[i][2])))
            self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(message[i][3])))
            self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(message[i][4])))
            self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(message[i][5])))

    def RR_msg(self):
        """
        时间片轮转算法，时间片的大小为 1
        :return:
        """
        print("this is rr")
        state = Schedule(self.dict)
        message = state.RR_schedule()
        self.output_res(message)

    def HRN_msg(self):
        """
        高响应比优先算法
        :return:
        """
        print("this is hrn")
        state = Schedule(self.dict)
        message = state.HRN_schedule()
        self.output_res(message)

# 程序运行
app = QApplication(sys.argv)
mainwindow = QMainWindow()
myDlg = MainWindow()
myDlg.setupUi(mainwindow)
mainwindow.show()
sys.exit(app.exec_())
