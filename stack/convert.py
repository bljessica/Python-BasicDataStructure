class Stack:
    '''堆栈实现中缀表达式转后缀表达式的算法，十进制正整数加减乘除'''
    def __init__(self, max_size):
        self.MAX_SIZE = max_size
        self.top = -1 #记录栈顶指针
        self.stack = ['\0' for i in range(self.MAX_SIZE)]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top ==self.MAX_SIZE - 1

    def push(self, ele):
        if self.is_full():
            print('栈已满')
            return
        self.top += 1
        self.stack[self.top] = ele

    def pop(self):
        if self.is_empty():
            print('栈为空')
            return
        self.top -= 1
        return self.stack[self.top + 1]

    def prority(self, c):
        '''各输入字符的优先级'''
        if c == '(':
            return 0
        elif c == '+' or c == '-':
            return 1
        elif c == '*' or c == '/':
            return 2
        elif c == '+' or c == '-':
            return 3
        else:
            return -1


    def convert(self, str):
        '''中缀表达式转后缀表达式，十进制正整数加减乘除'''
        res = ''
        for i in range(len(str)):
            c = str[i]
            prio = self.prority(c)
            if prio == -1: #数字
                res += c
            elif prio == 0: #左括号
                self.push(c)
            elif prio == 1 or prio == 2: #加减乘除
                if self.is_empty():
                    self.push(c)
                    continue
                while not self.is_empty() and self.prority(self.stack[self.top]) >= prio:
                    res += self.pop()
                self.push(c)
            else: #右括号
                if self.is_empty():
                    print('表达式有误')
                    return
                while not self.is_empty() and self.stack[self.top] != '(':#左括号只弹出不输出
                    res += self.pop()
                self.pop()
        while not self.is_empty():
            res += self.pop()
        return res


s = Stack(20)
str = '1+2*5-4/6+7'
print(s.convert(str))
# for i in range(3):
#     s.push(i)
#     print(str(i) + '已加入堆栈')
# for i in range(4):
#     ele = s.pop()
#     if ele is not None:
#         print(str(ele) + '已移出堆栈')