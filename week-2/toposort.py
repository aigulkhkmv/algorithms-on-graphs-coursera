# Uses python3
import operator
import sys


class GraphSearch:
    def __init__(self, graph, visited):
        self.clock = 0
        self.post_list = {}
        self.pre_list = {}
        self.graph = graph
        self.visited = visited

    def explore(self, node):
        self.visited[node] = True
        self.pre(node)
        for node_child in self.graph[node]:
            if not self.visited[node_child]:
                self.explore(node_child)
        self.post(node)

    def dfs(self):
        for node in range(len(self.graph)):
            if not self.visited[node]:
                self.explore(node)

    def pre(self, node):
        self.clock += 1
        self.pre_list[node] = self.clock

    def post(self, node):
        self.clock += 1
        self.post_list[node] = self.clock


def toposort(adj):
    graph = GraphSearch(adj, [False] * len(adj))
    graph.dfs()
    sorted_post = dict(sorted(graph.post_list.items(), key=operator.itemgetter(1), reverse=True))
    order = [i for i in sorted_post.keys()]
    return order


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=" ")
