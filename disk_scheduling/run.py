import sys
import numpy as np
from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.locate = 0  # 磁臂当前所在位置
        self.sequence_ = []  # 随机产生的请求序列
        self.se_step = self.sequence_   # 复制序列用于步进
        self.se = self.sequence_    # 复制序列用于全部执行

    def product(self):
        """
        根据所获得到的信息，产生符合要求的随机序列以及当前磁臂所在位置
        :return:
        """
        se_num = int(self.sequence_num.text())  # 产生随机数序列的个数
        se_range = int(self.sequence_range.text())  # 随机数的产生范围

        self.sequence_ = np.random.randint(0, se_range, se_num)
        self.se_step = self.sequence_   # 复制序列用于步进执行
        self.se = self.sequence_    # 复制序列用于全部执行

        sequence_str = str(self.sequence_)[1:-1]
        self.sequences.setText(sequence_str)    # 显示信息

        self.locate = np.random.randint(0, se_range, 1)[0]   # 产生初始时磁臂的位置
        self.location.setText(str(self.locate))     # 显示磁臂位置

    def single_step(self):
        """
        步进执行
        :return:
        """
        res = self.differ_radio()
        if res == 'SSTF':   # 步进执行， 按SSTF算法策略
            # self.se_step = self.sequence_
            self.sstf_step()
        elif res == 'SCAN':     # 步进执行， 按SCAN算法策略
            self.scan_step()

    def action(self):
        """
        全部执行
        :return:
        """
        res = self.differ_radio()
        self.execute_detail.clear()
        if res == "SSTF":
            self.se_step = self.sequence_
            while len(self.se_step):
                self.sstf_step()
        elif res == "SCAN":
            self.se = self.sequence_
            while len(self.se):
                self.scan_step()

    def differ_radio(self):
        """
        区分所选择的算法
        :return:
        """
        if self.radioButton_1.isChecked():
            return 'SSTF'
        if self.radioButton_2.isChecked():
            return 'SCAN'

    def sstf_step(self):
        """
        SSTF算法的步进执行
        :return:
        """
        # 未编写错误处理
        varS = abs(self.se_step - self.locate)
        if len(varS):
            num = np.argmin(varS)
            message1 = "由" + str(self.locate)
            self.locate = self.se_step[num]
            message2 = "到" + str(self.locate)
            self.se_step = np.delete(self.se_step, num)
            self.execute_detail.append(message1 + message2)     # 显示步进执行的信息
        else:
            self.execute_detail.append("执行完毕")

    def scan_step(self):
        """
        SCAN算法的步进执行
        :return:
        """
        self.se = np.sort(self.se)
        var = abs(self.se - self.locate)
        if len(var):
            num = np.argmin(var)
            num = (num + 1) % len(var) if self.locate > self.se[num] else num
            mes1 = "由" + str(self.locate)
            self.locate = self.se[num]
            mes2 = "到" + str(self.locate)
            self.se = np.delete(self.se, num)
            self.execute_detail.append(mes1 + mes2)     # 显示步进执行的信息
        else:
            self.execute_detail.append("执行完毕")

# 运行程序
app = QApplication(sys.argv)
mainwindow = QMainWindow()
myDlg = MainWindow()
myDlg.setupUi(mainwindow)
mainwindow.show()
sys.exit(app.exec_())