

class Priorityqueue:
    '''优先队列'''
    def __init__(self, max_size):
        self.MAX_SIZE = 10 #队列最大容量
        self.queue = [0 for i in range(self.MAX_SIZE)]#初始化队列
        self.size_now = 0

    def swap(self, i, j):
        '''交换队列中两个元素'''
        tmp = self.queue[i]
        self.queue[i] = self.queue[j]
        self.queue[j] = tmp

    def parent(self, i):
        '''得到某个节点的父节点的索引'''
        return int((i + 1)/2) - 1

    def increase_key(self, i, key):
        '''增大某个节点的值'''
        if self.queue[i] > key:
            return
        while i > 0 and self.queue[self.parent(i)] < self.queue[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def insert(self, ele):
        '''插入元素'''
        if self.size_now == self.MAX_SIZE:
            print('队列已满')
            return
        self.queue[self.size_now] = ele
        self.size_now += 1
        self.increase_key(self.size_now - 1, ele)

    def get_max(self):
        '''返回集合中最大元素'''
        if self.size_now == 0:
            print('队列为空')
            return
        return self.queue[0]

    def delete_max(self):
        '''返回并删除最大元素'''
        if self.size_now == 0:
            print('队列为空')
            return
        self.swap(0, self.size_now - 1)
        self.size_now -= 1
        self.adjust_heap(0, self.size_now)
        return self.queue[self.size_now + 1]

    def adjust_heap(self, i, length):
        '''调整成为最大堆'''
        tmp = self.queue[i]
        k = 2 * i + 1 #左儿子
        while k < length:
            if k + 1 < length and self.queue[k] < self.queue[k + 1]:
                k += 1 #指向右儿子
            if self.queue[k] > tmp:#子节点大于父节点
                self.queue[i] = self.queue[k]
                i = k  # 继续往下
            else:
                break
            k = 2 * k + 1
        self.queue[i] =tmp #放到最终位置

    def build_max_heap(self):
        '''构造最大堆'''
        for i in range(int(self.size_now/2) - 1, -1, -1):
            self.adjust_heap(i, self.size_now)

q = Priorityqueue(10)
q.insert(5)
q.insert(1)
q.insert(9)
q.insert(7)
q.insert(3)
q.insert(15)
q.build_max_heap()
print(q.queue[:q.size_now])
q.delete_max()
q.delete_max()
print(q.queue[:q.size_now])
