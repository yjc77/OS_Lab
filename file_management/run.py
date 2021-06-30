import sys
import random
import math
from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.disk = 500 * [0, ]  # 模拟磁盘的状况，1表示装有数据
        self.capacities = []    # 记录所装入的文件位置信息
        self.free_block = []    # 记录产生的空闲段的信息

    def generate(self):
        num = 1
        self.tableWidget.setRowCount(60)
        # 随机产生50个文件
        for i in range(1, 51):
            filename = str(i) + ".txt"
            filesize = round(random.uniform(2, 10), 1)
            index_block = num
            num += math.ceil(filesize / 2)

            self.capacities.append((filename, filesize, index_block))   # 将文件信息记录
            # 显示文件信息
            self.tableWidget.setItem(i - 1, 0, QTableWidgetItem(filename))
            self.tableWidget.setItem(i - 1, 1, QTableWidgetItem(str(filesize)))
            self.tableWidget.setItem(i - 1, 2, QTableWidgetItem(str([x for x in range(index_block, index_block + math.ceil(filesize / 2))])[1:-1]))
            self.tableWidget.setItem(i - 1, 3, QTableWidgetItem(str(index_block)))
        # 显示空闲段的信息
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setItem(0, 0, QTableWidgetItem(str(num)))
        self.tableWidget_2.setItem(0, 1, QTableWidgetItem(str(num) + " ~ 500"))
        self.tableWidget_2.setItem(0, 2, QTableWidgetItem(str(501 - num)))
        # 将磁盘信息相应地变化
        self.disk = (num - 1) * [1, ] + (501 - num) * [0, ]
        # print(self.disk)

    def delete_files(self):
        """
        执行删除奇数的文件的任务
        :return:
        """
        wait_del = []
        for index in range(len(self.capacities)):
            if self.differ_single(self.capacities[index][0]):
                for x in range(self.capacities[index][2], self.capacities[index][2] + math.ceil(self.capacities[index][1] / 2)):
                    self.disk[x - 1] = 0 # 删除时磁盘相应变化
                self.free_block.append((self.capacities[index][2], math.ceil(self.capacities[index][1] / 2)))
                # del(self.capacities[index])
                wait_del.append(index)
        # print(wait_del)
        self.del_capacity(wait_del)
        self.show_capacity()
        self.show_free()

    def del_capacity(self, li):
        """
        删除文件中所记录的文件信息
        :param li: 奇数文件的索引列表
        :return:
        """
        li = li[::-1]
        for i in li:
            del(self.capacities[i])

    def show_free(self):
        """
        显示空闲区间的信息
        :return:
        """
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(len(self.free_block))
        for i in range(len(self.free_block)):
            self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(self.free_block[i][0])))
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str([x for x in range(self.free_block[i][0], self.free_block[i][0] + self.free_block[i][1])])[1:-1]))
            self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(self.free_block[i][1])))

    def show_capacity(self):
        """
        显示文件的信息
        :return:
        """
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(self.capacities))
        # print(len(self.capacities))
        for i in range(len(self.capacities)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(self.capacities[i][0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.capacities[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str([x for x in range(self.capacities[i][2], self.capacities[i][2] + math.ceil(self.capacities[i][1] / 2))])[1:-1]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.capacities[i][2])))

    def differ_single(self, filename):
        """
        根据文件名称来判断是否属于奇数文件
        :param filename: 文件名称，字符串
        :return:
        """
        filename = filename[:-4]
        num = int(filename)
        if num % 2:
            return 1
        return 0

    def inserts(self):
        """
        将A B C D E五个文件按照首次适应的方法进行插入
        :return:
        """
        files = [("A.txt", 7, 0), ("B.txt", 5, 0), ("C.txt", 2, 0), ("D.txt", 9, 0), ("E.txt", 3.5, 0)]
        for i in range(len(files)):     # 每次空闲表的头部开始寻找，插入一个文件
            needSize = math.ceil(files[i][1] / 2)
            file = list(files[i])
            for index in range(len(self.free_block)):
                # print(index, len(self.free_block))
                if self.free_block[index][1] > needSize:
                    file[2] = self.free_block[index][0]
                    self.free_block[index] = (file[2] + needSize, self.free_block[index][1] - needSize)
                    # self.free_block[index][1] -= needSize
                    self.capacities.append(tuple(file))
                    break
                else:
                    file[2] = self.free_block[index][0]
                    del(self.free_block[index])
                    self.capacities.append(tuple(file))
                    break
        self.show_capacity()
        self.show_free()

    def reset_all(self):
        """
        重置所有信息
        :return:
        """
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.clearContents()

        self.capacities = []
        self.free_block = []
        self.disk = 500 * [0, ]


# 运行程序
app = QApplication(sys.argv)
mainwindow = QMainWindow()
myDlg = MainWindow()
myDlg.setupUi(mainwindow)
mainwindow.show()
sys.exit(app.exec_())
