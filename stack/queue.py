
class Queue:
    '''队列'''
    def __init__(self, max_size):
        self.MAX_SIZE = max_size
        self.stack_1 = ['\0' for i in range(self.MAX_SIZE)]
        self.stack_2 = ['\0' for i in range(self.MAX_SIZE)]
        self.top_1 = -1
        self.top_2 = -1

    def is_empty(self, stack):
        if stack is self.stack_1:
            return self.top_1 == -1
        else :
            return self.top_2 == -1

    def is_full(self, stack):
        if stack is self.stack_1:
            return self.top_1 == self.MAX_SIZE - 1
        else :
            return self.top_2 == self.MAX_SIZE - 1

    def push_in(self, stack, ele):
        '''入栈'''
        if stack is self.stack_1:
            if self.is_full(self.stack_1):
                print('栈1已满')
                return
            self.top_1 += 1
            self.stack_1[self.top_1] = ele
        else :
            if self.is_full(self.stack_2):
                print(self.stack_2)
                print('栈2已满')
                return
            self.top_2 += 1
            self.stack_2[self.top_2] = ele

    def pop_out(self, stack):
        '''出栈'''
        if stack is self.stack_1:
            if self.is_empty(self.stack_1):
                print('栈1已空')
                return
            self.top_1 -= 1
            return self.stack_1[self.top_1 + 1]

        else :
            if self.is_empty(self.stack_2):
                print('栈2已空')
                return
            self.top_2 -= 1
            return self.stack_2[self.top_2 + 1]



    def append_tail(self, ele):
        self.push_in(self.stack_1, ele)

    def delete_head(self):
        if self.is_empty(self.stack_2):#栈2为空
            if not self.is_empty(self.stack_1):#栈1不为空
                while(not self.is_empty(self.stack_1)):#将栈1元素全弹到栈2
                    ele = self.pop_out(self.stack_1)
                    self.push_in(self.stack_2, ele)
            else:
                print('队列为空')
                return
        return self.pop_out(self.stack_2)


queue = Queue(100)
for i in range(3):
    queue.append_tail(i)
    print(str(i) + '已加入队列')
for i in range(4):
    ele = queue.delete_head()
    if ele is not None:
        print(str(ele) + '已移出队列')
for i in range(3, 5):
    queue.append_tail(i)
    print(str(i) + '已加入队列')
for i in range(4):
    ele = queue.delete_head()
    if ele is not None:
        print(str(ele) + '已移出队列')


