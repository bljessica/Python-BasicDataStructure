import sys
from minitree import Edge
from priority_queue import *

class Dijkstra:
    '''基于优先队列实现单源最短路径算法'''
    def __init__(self, graph):
        self.graph = graph

    def initial_graph(self):
        '''更新图'''
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] == 0:
                    self.graph[i][j] = sys.maxsize

    def dijkstra(self, start):
        self.initial_graph()
        distance = [sys.maxsize for i in range(len(self.graph))]#源节点到各节点的最短距离
        nodes = [i for i in range(len(self.graph))]
        visited = [start] #已确定最短距离的结点
        nodes.remove(start)
        for i in range(len(self.graph)):
            distance[i] = self.graph[start][i]
        distance[start] = 0
        # prio_queue = MinPriorityqueue([])
        # for i in range(len(distance)):
        #     e = Edge(start, i, distance[i])
        #     prio_queue.insert(e)
        # prio_queue.delete_min()#去掉初始点
        while nodes:
            # index_edge = prio_queue.delete_min()
            # index_min = index_edge.v
            min = sys.maxsize
            index_min = 0
            for node in nodes:#选出距离最小的点
                if distance[node] < min and distance[node] > 0:
                    index_min = node
                    min = distance[node]
            visited.append(index_min)
            nodes.remove(index_min)
            for node in nodes:
                if distance[index_min] + self.graph[index_min][node] < distance[node]:
                    distance[node] = distance[index_min] + self.graph[index_min][node]
                    # prio_queue.decrease_key(node, distance[node])
                    # print(node)
        return distance


graph = [[0, 5, 0, 6, 0, 0, 0, 0, 0], [5, 0, 0, 0, 9, 0, 0, 0, 0], [0, 0, 0, 7, 0, 0, 3, 0, 15],
         [6, 0, 7, 0, 1, 0, 0, 0, 0], [0, 9, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 8, 0, 0],
         [0, 0, 3, 0, 0, 8, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 15, 0, 0, 0, 0, 2, 0]]
            #有权图，九个节点，每个节点自己不与自己相连

d = Dijkstra(graph)
print(d.dijkstra(2))