import copy, sys

class Sort:
    '''排序'''

    def swap(self, nums, i, j):
        '''交换两个元素'''
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def bubble_sort(self, nums):
        '''冒泡排序'''
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    #交换
                    self.swap(nums, i ,j)
        return nums

    def insert_sort(self, nums, length):
        '''插入排序'''
        for i in range(1, length):
            j = i - 1
            key = nums[i]
            while(j >= 0 and nums[j] > key):
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums

    def partition(self, nums, left, right):
        '''快速排序选基准数'''
        key = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] <= key:
                i += 1
                self.swap(nums, i, j)
        nums[right] = nums[i + 1]
        nums[i + 1] = key
        return i + 1

    def quick_sort(self, nums, left, right):
        '''快速排序'''
        if left < right :
            pivot = self.partition(nums, left, right)
            self.quick_sort(nums, left, pivot - 1)
            self.quick_sort(nums, pivot + 1, right)
        return nums

    def adjust_heap(self, nums, i, length):
        '''调整为最大堆'''
        tmp = nums[i]#先取出当前元素
        k = 2 * i + 1#从节点i的左子节点开始
        while k < length:
            if k + 1 < length and nums[k] < nums[k + 1]:#左子节点小于右子节点
                k += 1 #k指向右子节点
            if nums[k] > tmp: #子节点大于父节点,将子节点复制给父节点，不交换
                nums[i] = nums[k]
                i = k #继续往下
            else:
                break
            k = 2 * k + 1
        nums[i] = tmp #将tmp值放到最终位置

    def heap_sort(self, nums):
        '''堆排序'''
        #构建最大堆，从从下至上、从后往前第一个非叶子节点调整树的结构
        for i in range(int(len(nums)/2) - 1, -1, -1):
            self.adjust_heap(nums, i, len(nums))
        #将最大元素放到最后，然后调整树的结构
        for i in range(len(nums) - 1, 0, -1):
            self.swap(nums, i, 0)
            self.adjust_heap(nums, 0, i)
        return nums

    def merge(self, nums, left, mid, right):
        '''合并'''
        nums_1 = copy.deepcopy(nums[left:mid + 1])
        nums_1.append(sys.maxsize)
        nums_2 = copy.deepcopy(nums[mid + 1:right + 1])
        nums_2.append(sys.maxsize)
        i = 0
        j = 0
        k = left
        while k <= right:
            if(nums_1[i] > nums_2[j]):
                nums[k] = nums_2[j]
                j += 1
            else:
                nums[k] = nums_1[i]
                i += 1
            k += 1
        return nums

    def merge_sort(self, nums, left, right):
        '''归并排序'''
        if left == right:
            return nums
        mid = int((left + right)/2)
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)
        return nums

    def count_sort(self, nums):
        '''计数排序,适用于数的值（非负）都不大的情况'''
        max = 0
        #找出最大元素值
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
        result = [0] * len(nums)
        every_num_count = [0] * (max + 1)
        for i in range(len(nums)):#记录每个值出现的次数
            every_num_count[nums[i]] += 1
        for i in range(1, len(every_num_count)):
            every_num_count[i] += every_num_count[i - 1] #记录小于等于该索引的值出现的次数
        for i in range(len(nums) - 1, -1, -1):
            result[every_num_count[nums[i]] - 1] = nums[i]
            every_num_count[nums[i]] -= 1
        return result

    def bucket_sort(self, nums):
        '''桶排序，元素属于有限区间内'''
        bucket = [[i for i in range(10)] for j in range(len(nums))]#十个桶
        count = [0] * 10 #每个桶中元素个数
        for i in range(len(nums)): #入桶
            j = int(nums[i]/10)
            bucket[j][count[j]] = nums[i]
            count[j] += 1
        for i in range(10):
            self.insert_sort(bucket[i], count[i])
        num = 0
        for i in range(10):
            for j in range(count[i]):
                nums[num] = bucket[i][j]
                num += 1
        return nums



nums = [3, 1, 99, 0, 789, 23, 8, 213, 789, 7896, 4, 66, 6, 6, 7, 8, 2, 1, 0]
# print('Initial array:')
# print(nums)
nums_count = [3, 4, 1, 2, 5, 16, 12, 4, 13, 8, 1, 9, 0, 17, 13, 11]
nums_bucket = [33, 23, 7, 87, 3, 1, 23, 99, 98, 4, 2, 66, 19]

s = Sort()
print("Bubble sorted array:")
print(s.bubble_sort(nums[:]))
print("Insert sorted array:")
print(s.insert_sort(nums[:], len(nums)))
print("Quick sorted array:")
print(s.quick_sort(nums[:], 0, len(nums) - 1))
print("Heap sorted array:")
print(s.heap_sort(nums[:]))
print("Merge sorted array:")
print(s.merge_sort(nums[:], 0, len(nums) - 1))
print("Count sorted array:")
print(s.count_sort(nums_count[:]))
print("Bucket sorted array:")
print(s.bucket_sort(nums_bucket[:]))