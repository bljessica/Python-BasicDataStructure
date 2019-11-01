class UnionFind:
    '''实现并查集'''
    def __init__(self, size):
        self.parent = [i for i in range(size)] #存储节点的根节点，一开始互不相交，根节点为自己
        self.rank = [0 for i in range(size)] #存储节点的高度（秩）信息

    # 简单实现并查集的操作
    def find_root_simple(self, i):
        '''求一个元素的父节点'''
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def merge_simple(self, i, j):
        '''求并集'''
        i_root = self.find_root(i)
        j_root = self.find_root(j)
        self.parent[i_root] = j_root

    # 并查集的优化，按秩合并，路径压缩
    def merge(self, i, j):
        '''按秩合并，将秩小的子树的根指向秩大的子树的根(秩为每个节点高度的上界,因为路径压缩会改变树的高度)'''
        i_root = self.find_root(i)
        j_root = self.find_root(j)
        if i_root == j_root: # 两树已连通
            return
        if self.rank[i_root] < self.rank[j_root]:
            self.parent[i_root] = j_root
        else:
            self.parent[j_root] = i_root
            if self.rank(i_root) == self.rank(j_root):
                self.rank[i_root] += 1

    def find_root(self, i):
        '''路径压缩,使查找路径中的所有父节点都直接指向树根'''
        parents = []
        while self.parent[i] != i:
            parents.append(self.parent[i])
            i = self.parent[i]
        while parents:
            p = parents.pop()
            self.parent[p] = i
            self.rank[p] = self.parent[i] + 1
        return i




