# Uses python3

import sys


class GraphSearch:
    def __init__(self, graph, visited):
        self.graph = graph
        self.visited = visited
        self.connected_compounds = 0

    def explore(self, node):
        self.visited[node] = True
        for node_child in self.graph[node]:
            if not self.visited[node_child]:
                self.explore(node_child)

    def dfs(self):
        for node in range(len(self.graph)):
            if not self.visited[node]:
                self.explore(node)
                self.connected_compounds += 1
        return self.connected_compounds


def number_of_components(adj):
    visited = [False] * len(adj)
    graph_search = GraphSearch(adj, visited)
    return graph_search.dfs()


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
