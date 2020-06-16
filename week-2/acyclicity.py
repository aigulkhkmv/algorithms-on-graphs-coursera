#Uses python3

import sys


class GraphSearch:
    def __init__(self, graph, visited):
        self.graph = graph
        self.visited = visited
        self.cycle = False
        self.reverse_graph = []
        self.post_count = 0
        self.post = [0]*len(self.graph)

    def explore(self, node):
        self.visited[node] = True
        for node_child in self.graph[node]:
            if not self.visited[node_child]:
                self.explore(node_child)

    def dfs(self):
        for node in range(len(self.graph)):
            if not self.visited[node]:
                self.explore(node)

    def reverse(self):
        new_chi = [[] for i in self.graph]
        for parent_num, old_chis_ in enumerate(self.graph, 0):
            for old_chi in old_chis_:
                new_chi[old_chi].append(parent_num)
        self.reverse_graph = new_chi

    def post(self, node):
        pass


def acyclic(adj):
    visited = [False] * len(adj)
    graph_search = GraphSearch(adj, visited)
    graph_search.dfs()
    if graph_search.cycle:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
