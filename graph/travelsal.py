class Graph:
    '''图的基础遍历算法，最小生成树算法，单源最短路径算法'''
    def __init__(self, g):
        self.graph = g #邻接矩阵表示

    visited = []
    time = 0
    finish_order = []
    def dfs_visit(self, index, start, finish):
        '''DFS，递归'''
        Graph.time += 1
        start[index] = Graph.time
        Graph.visited.append(index)
        for i in self.get_adj(index):
            if i not in Graph.visited:
                self.dfs_visit(i, start, finish)
        Graph.time += 1
        finish[index] = Graph.time
        Graph.finish_order.insert(0, index)

    def dfs_recur(self, index):
        '''DFS，递归实现'''
        start = [-1 for i in range(len(graph))]
        finish = [-1 for i in range(len(self.graph))]
        time = 0
        self.dfs_visit(index, start, finish)
        for i in range(len(self.graph)):
            if i not in Graph.visited:
                self.dfs_visit(i, start, finish)
        return Graph.visited, finish

    def dfs(self, index):
        '''DFS，非递归实现'''
        visited = []
        stack = []
        stack.append(index)
        visited.append(index)
        while len(visited) != len(self.graph): #有节点没有遍历完
            while stack:
                node_index = stack.pop() # 出栈
                for i in self.get_adj(node_index):
                    if i not in visited:
                        stack.append(node_index) #压入节点
                        stack.append(i) #压入邻接节点
                        visited.append(i)
                        break # 退出，保持深度优先
            for i in range(len(self.graph)):
                if i not in visited:
                    stack.append(i)
        return visited

    def dfs_topo(self):
        '''基于DFS的拓扑排序'''
        return Graph.finish_order

    def get_adj(self, index):
        '''得到索引为i的节点的邻接的点的列表'''
        adj = []
        nodes = self.graph.get(index)
        for i in range(len(nodes)):
            if nodes[i] != 0:
                adj.append(i)
        return adj

    def bfs(self, start):
        '''BFS，非递归实现'''
        queue = []
        visited = [] #节点是否被访问完
        queue.append(start) # 第一个节点入队
        visited.append(start)
        while queue:
            node_index = queue.pop(0) # 队列先进先出
            for i in self.get_adj(node_index): #此节点的所有邻接节点
                    if i not in visited: #i未访问到
                        queue.append(i)
                        visited.append(i)
        return visited


# 无向图,以邻接矩阵的方式给出
graph = {0: [0, 1, 0, 1, 0, 0, 0, 0, 0], 1: [1, 0, 0, 0, 1, 0, 0, 0, 0], 2: [0, 0, 0, 1, 0, 0, 1, 0, 0],
         3: [1, 0, 1, 0, 1, 0, 0, 0, 0], 4: [0, 1, 0, 1, 0, 0, 0, 0, 0], 5: [0, 0, 0, 0, 0, 0, 1, 0, 0],
         6: [0, 0, 1, 0, 0, 1, 0, 0, 0], 7: [0, 0, 0, 0, 0, 0, 0, 0, 1], 8: [0, 0, 0, 0, 0, 0, 0, 1, 0]}
            #九个节点，每个节点自己不与自己相连
g = Graph(graph)

# print(g.bfs(0))
# print(g.bfs(6))


print(g.dfs_recur(8)[0])
print("拓扑:", g.dfs_topo())
Graph.visited = []
Graph.time = 0
Graph.finish_order = []
print(g.dfs_recur(2)[0])
print("拓扑:", g.dfs_topo())

# print(g.dfs(8))
# print(g.dfs(2))


