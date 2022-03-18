# Uses python3

import sys

def reverse(graph):
    new_chi = [[] for i in graph]
    for parent_num, old_chis_ in enumerate(graph, 0):
        for old_chi in old_chis_:
            new_chi[old_chi].append(parent_num)
    return new_chi


class GraphSearch:
    def __init__(self, graph, visited):
        self.clock = 0
        self.post_list = [0 for i in range(len(graph))]
        self.pre_list = [0 for i in range(len(graph))]
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


def find_scc(graph, post_list):
    for j in range(len(post_list)):
        max_index = post_list.index(max(post_list))
        post_list[max_index] = 0
        if not graph.visited[max_index]:
            graph.visited[max_index] = True
            start_clock = graph.clock
            graph.explore(max_index)
            if start_clock + 2 < graph.clock:
                return 1
    return 0


def magic_check(graph):
    for parent, children in enumerate(graph, 0):
        for child in children:
            if parent > child:
                return False
    return True


def acyclic(adj):
    if magic_check(adj):
        return 0
    visit_list = [False] * len(adj)
    reverse_graph = reverse(adj)

    reverse_graph_search = GraphSearch(reverse_graph, visit_list)
    reverse_graph_search.dfs()
    post_list = reverse_graph_search.post_list

    forvard_graph = GraphSearch(adj, [False] * len(adj))
    return find_scc(forvard_graph, post_list)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
