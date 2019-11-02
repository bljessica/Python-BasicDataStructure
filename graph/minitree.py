from unionfind import *
from priority_queue import *

class Edge:
    '''边'''
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.weight = w

class MinimunSpanningTree:
    '''最小生成树算法'''
    def __init__(self, graph):
        self.graph = graph

    def get_edges(self):
        '''生成边'''
        edges = []
        for i in range(len(self.graph)):
            for j in range(i, len(self.graph)):
                if self.graph[i][j] != 0:
                    edge = Edge(i, j, self.graph[i][j])
                    edges.append(edge)
        return edges

    def get_all_edges(self):
        '''生成边'''
        edges = []
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] != 0:
                    edge = Edge(i, j, self.graph[i][j])
                    edges.append(edge)
        return edges

    def sort_edges(self, edges):
        '''边排序'''
        #冒泡排序
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                if edges[i].weight > edges[j].weight:
                    # 交换
                    tmp = edges[i]
                    edges[i] = edges[j]
                    edges[j] = tmp
        return edges

    def kruskal(self):
        '''不断选择权最小的边，通过并查集实现'''
        edges = m.sort_edges(m.get_edges())#排好序的边
        sets = UnionFind(len(self.graph)) #初始化并查集
        edge_num = 0
        min_weight = 0
        while edge_num < len(self.graph) - 1:#节点未全部加入
            least_edge = edges.pop(0)#权值最小的边
            u = least_edge.u
            v = least_edge.v
            w = least_edge.weight
            if sets.find_root(u) != sets.find_root(v):#未连通
                sets.merge(u, v)
                edge_num += 1
                min_weight += w
        return min_weight

    def prim(self, start):
        '''不断增加节点，通过优先队列实现'''
        edges = m.get_all_edges()
        pri_queue = MinPriorityqueue([])
        nodes = [i for i in range(len(self.graph))]#全部节点
        nodes.remove(start)
        node_set = [start] #已加入的节点
        node_weight = 0
        index = start
        while nodes:#节点未全部加入
            # 加入与该点邻接的边
            tmp = []
            for edge in edges:
                if edge.u == index:
                    tmp.append(edge)
                    pri_queue.insert(edge)
            for e in tmp:
                if e in edges:
                    edges.remove(e)
                for s in edges:
                    if s.u == e.v and s.v == e.u and s.weight ==e.weight:
                        edges.remove(s)
            min_edge = pri_queue.delete_min()#最小边
            if min_edge.u not in node_set:
                node_set.append(min_edge.u)
                index = min_edge.u
                nodes.remove(min_edge.u)
                node_weight += min_edge.weight
            elif min_edge.v not in node_set:
                node_set.append(min_edge.v)
                index = min_edge.v
                nodes.remove(min_edge.v)
                node_weight += min_edge.weight
        return node_weight


graph = [[0, 5, 0, 6, 0, 0, 0, 0, 0], [5, 0, 0, 0, 9, 0, 0, 0, 0], [0, 0, 0, 7, 0, 0, 3, 0, 15],
         [6, 0, 7, 0, 1, 0, 0, 0, 0], [0, 9, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 8, 0, 0],
         [0, 0, 3, 0, 0, 8, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 15, 0, 0, 0, 0, 2, 0]]
            #有权图，九个节点，每个节点自己不与自己相连

m = MinimunSpanningTree(graph)

print(m.kruskal())

print(m.prim(2))




