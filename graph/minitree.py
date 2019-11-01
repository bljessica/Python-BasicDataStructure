from unionfind import UnionFind

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
        for u, values in self.graph.items():
            for v in values:
                if v != 0:
                    edge = Edge(u, v)
                    edges.append(edge)
        return edges


    def kruskal(self):
        '''不断选择权最小的边，通过并查集实现'''
        sets = UnionFind(len(self.graph)) #初始化并查集


    def prim(self):
        '''不断增加节点，通过优先队列实现'''


graph = {0: [0, 5, 0, 6, 0, 0, 0, 0, 0], 1: [5, 0, 0, 0, 9, 0, 0, 0, 0], 2: [0, 0, 0, 7, 0, 0, 3, 0, 0],
         3: [6, 0, 7, 0, 1, 0, 0, 0, 0], 4: [0, 9, 0, 1, 0, 0, 0, 0, 0], 5: [0, 0, 0, 0, 0, 0, 8, 0, 0],
         6: [0, 0, 3, 0, 0, 8, 0, 0, 0], 7: [0, 0, 0, 0, 0, 0, 0, 0, 2], 8: [0, 0, 0, 0, 0, 0, 0, 2, 0]}
            #有权图，九个节点，每个节点自己不与自己相连