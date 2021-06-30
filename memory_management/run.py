import sys
import random
from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.mem_size = None
        self.work_size_range = None
        self.num_work = None

        self.order_list = []       # 产生的作业序列   （名称str， 大小int）
        self.distributed_list = []      # 已分配列表 （名称str， 大小int， 初始位置int）
        self.free_list = []     # 空闲列表 （大小int， 初始位置int）

    def product_order(self):
        str_mem_size = self.memorySize.text()
        str_work_size_range = self.workMaxNum.text()
        str_num_work = self.workNum.text()
        if str_mem_size and str_work_size_range and str_num_work:
            self.mem_size = int(str_mem_size)    # 获取内存大小
            self.work_size_range = int(str_work_size_range)     # 获取作业大小的范围，最小为 1
            self.num_work = int(str_num_work)   # 获取产生的作业数量
            self.free_list.append((self.mem_size, 0))    # 初始化空闲列表
            for i in range(self.num_work):
                size = round(random.uniform(1, self.work_size_range), 1)
                name = "W" + str(i + 1)
                self.order_list.append((name, size))
            self.lineEdit.setText(str(self.order_list)[1:-2].replace(" ", ""))   # 显示作业序列
        else:
            pass

    def distribute(self):
        signal = 0  # 获取的作业索引
        while len(self.order_list):
            print('------')
            # 获取待分配的作业信息
            semaphore = 0   # 设置信号量标注是否分配成功
            wait_dis = self.order_list[signal]
            self.textBrowser.append("作业" + wait_dis[0] + "开始分配")
            # 从空闲列表中寻找合适位置插入
            for index in range(len(self.free_list)):
                 if self.free_list[index][0] >= wait_dis[1]:
                    semaphore = 1
                    now_size = self.free_list[index][0] - wait_dis[1]
                    now_local = self.free_list[index][1] + wait_dis[1]
                    self.distributed_list.append(wait_dis + (self.free_list[index][1],))    # 更新已分配表
                    if self.free_list[index][0] > wait_dis[1]:
                        self.free_list[index] = (now_size, now_local)   # 更新空闲表 1
                        print(self.free_list[0])
                    else:
                        del(self.free_list[index])  # 更新空闲表  2
                        print('over')
                    del(self.order_list[signal])
                    break
            if semaphore:
                self.show_distribute_table()    # 只有作业添加成功才会更新 tableWidget_1
                self.show_free_table()
                self.textBrowser.append("作业" + wait_dis[0] + "分配成功")
                break
            else:
                self.textBrowser.append("作业" + wait_dis[0] + "分配失败，自动分配下一个")
                signal += 1
            if signal == len(self.order_list):
                self.textBrowser.append("所有作业都不能分配，请先回收")
                break
        if len(self.order_list) == 0:
            self.textBrowser.append("所有作业已分配完毕，请回收")

    def show_distribute_table(self):
        self.tableWidget_1.setRowCount(0)
        self.tableWidget_1.clearContents()
        self.tableWidget_1.setRowCount(len(self.distributed_list))
        for i in range(len(self.distributed_list)):
            self.tableWidget_1.setItem(i, 0, QTableWidgetItem(self.distributed_list[i][0]))
            self.tableWidget_1.setItem(i, 1, QTableWidgetItem(str(self.distributed_list[i][1])))
            up_to = self.distributed_list[i][2] + self.distributed_list[i][1]
            interval = "[{},{})".format(self.distributed_list[i][2], up_to)
            self.tableWidget_1.setItem(i, 2, QTableWidgetItem(interval))

    def show_free_table(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(len(self.free_list))
        for i in range(len(self.free_list)):
            self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(round(self.free_list[i][0], 1))))
            up_to = self.free_list[i][0] + self.free_list[i][1]
            interval = "[{},{})".format(self.free_list[i][1], up_to)
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(interval))

    def recycle(self):
        # 对于分配表中的作业按照进入顺序开始回收
        if len(self.distributed_list) == 0:
            self.textBrowser.appedn("所有作业已经回收，请先分配")
        else:
            for_free = self.distributed_list[0]
            del(self.distributed_list[0])
            start_local = for_free[2]   # 回收区间的起始位置
            end_local = for_free[1] + for_free[2]   # 分配区间的终止位置
            # 遍历空闲列表，寻找符合要求的区间合并
            index_list = []
            for i in range(len(self.free_list)):
                start_free = self.free_list[i][1]
                end_free = self.free_list[i][0] + self.free_list[i][1]
                if start_local == end_free:     # 待回收区间的前面已有空闲区间
                    start_local = start_free
                    index_list.append(i)
                elif end_local == start_free:   # 待回收的区间的后面已有空闲区间
                    end_local = end_free
                    index_list.append(i)
            # 删除空闲列表中的多余项
            index_list = index_list[::-1]
            if len(index_list):
                for i in range(len(index_list)):
                    del(self.free_list[index_list[i]])
            # 将已回收块加入到空闲表中
            self.free_list.append((end_local - start_local, start_local))
            # 显示相关信息
            self.textBrowser.append("成功回收作业{}".format(for_free[0]))
            self.show_distribute_table()
            self.show_free_table()


# 程序运行
app = QApplication(sys.argv)
mainwindow = QMainWindow()
myDlg = MainWindow()
myDlg.setupUi(mainwindow)
mainwindow.show()
sys.exit(app.exec_())