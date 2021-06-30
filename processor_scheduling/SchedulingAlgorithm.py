import numpy as np
from queue import Queue

class Schedule(object):
    def __init__(self, process_msg):
        dt = np.dtype([('order', np.int), ('name', 'U10'), ('arrive', np.int), ('service', np.int)])
        self.data = np.array(process_msg, dtype=dt)  # 获取到的进程的相关信息

    def FCFS_schedule(self):
        # print("this is self.data")
        # print(self.data)
        msg = []
        dataOrder = np.sort(self.data, order='arrive')
        nowTime = 0
        for i in range(len(self.data)):
            # print(dataOrder)
            finishTime = max(nowTime, dataOrder[i][2]) + dataOrder[i][3]    # 完成时间
            cycleTime = finishTime - dataOrder[i][2]    # 周转时间
            weightedTime = round(cycleTime / dataOrder[i][3], 3)    # 带权周转时间
            nowTime = finishTime    # 当前时间
            msg.append((dataOrder[i][0], dataOrder[i][1], dataOrder[i][2], dataOrder[i][3], finishTime, cycleTime,
                             weightedTime))
        return msg

    def SJF_schedule(self):
        mes = []
        x = np.sort(self.data, order='arrive')
        nowTime = x[0][2]
        # print(x[0][2])
        nowList = [x[0], ]      # 当前时间，所有已到达但未运行的进程信息
        flag = 1
        # print(nowList)
        while flag < len(x):
            while nowTime >= x[flag][2]:
                nowList.append(x[flag])
                flag += 1
                if flag == len(x):
                    break
            nowList.sort(key=lambda x: x[3])
            finishTime = nowTime + nowList[0][3]
            nowTime = finishTime
            cycleTime = finishTime - nowList[0][2]
            weightedTime = round(cycleTime / nowList[0][3], 3)
            mes.append(
                (nowList[0][0], nowList[0][1], nowList[0][2], nowList[0][3], finishTime, cycleTime, weightedTime))
            del (nowList[0])

        while len(nowList):
            # sorted(nowList, key=lambda x: x[3])
            nowList.sort(key=lambda x: x[3])
            # print(nowList)
            finishTime = nowTime + nowList[0][3]
            nowTime = finishTime
            cycleTime = finishTime - nowList[0][2]
            weightedTime = round(cycleTime / nowList[0][3], 3)
            mes.append(
                (nowList[0][0], nowList[0][1], nowList[0][2], nowList[0][3], finishTime, cycleTime, weightedTime))
            del (nowList[0])
        return mes

    def RR_schedule(self):
        msg = []
        processTable = np.sort(self.data, order='arrive')
        que = Queue(maxsize=len(self.data))
        nowTime = processTable[0][2]
        que.put(list(processTable[0]) + [0, ])
        # np.delete(processTable[0])
        flag = 1
        # del(processTable[0])
        while not que.empty():
            # print(nowTime)
            nowTime += 1
            if flag < len(processTable):
                if processTable[flag][2] == nowTime:
                    que.put(list(processTable[flag]) + [0, ])
                    flag += 1
                    # np.delete(processTable[0])
                    # del(processTable[0])
            first = que.get()
            first[3] -= 1
            if first[3] == 0:
                first[4] = nowTime  # finish time
                cycleTime = first[4] - first[2]
                tu = tuple(self.data[first[0]])
                weightedTime = round(cycleTime / tu[3], 3)
                # da = tuple(self.data[0])[1:]
                # print(self.data, da)

                msg.append(tu[1:] + (first[4], cycleTime, weightedTime))
                # print(self.data[first[0]])
            else:
                que.put(first)
        return msg

    def HRN_schedule(self):
        dataOrder = np.sort(self.data, order='arrive')
        index = 0
        nowTime = dataOrder[0][2]
        msg = []
        dt = np.dtype([('order', np.int), ('name', 'U10'), ('arrive', np.int), ('service', np.int), ('finish', np.int), ('priority', np.int)])
        nowList = np.array([(-1, 'invaild', -1, -1, -1, -1)], dtype=dt)
        while index < len(self.data) or (len(nowList) - 1):
            # 将已到达的进程入内存
            print(len(nowList))
            if index < len(dataOrder):
                while dataOrder[index][2] <= nowTime:
                    # nowList.append(list(dataOrder[index]) + [0, 0])
                    small = np.array([tuple(dataOrder[index]) + (0, 0)], dtype=dt)
                    nowList = np.concatenate([nowList, small])
                    print("------------------", len(nowList))
                    index += 1
                    if index >= len(dataOrder):
                        break
            # 计算各个进程的优先度
            for i in range(len(nowList)):
                nowList[i][5] = (nowTime - nowList[i][2] + nowList[i][3]) / nowList[i][3]
            # 根据优先度选取优先级最高的进程运行
            # nowList = np.array(nowList)
            nowList = np.sort(nowList, order='priority')
            run_pro = nowList[-1]    # 优先级最高的进程
            nowList = np.delete(nowList, -1)  # 将优先级最高的进程从内存中取出并且运行
            # 运行
            nowTime += run_pro[3]
            # 该运行的进程的信息
            finishTime = nowTime
            cycleTime = finishTime - run_pro[2]
            weightedTime = round(cycleTime / run_pro[3], 3)
            msg.append(tuple(self.data[run_pro[0]])[1:] + (finishTime, cycleTime, weightedTime))
        return msg
