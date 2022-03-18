# Uses python3

import sys


def bfs(graph, start_node):
    dist = []
    for node in graph:
        dist.append(len(graph) + 1000)
    dist[start_node] = 0
    Q = [start_node]
    while Q:
        u = Q.pop(0)
        for node in graph[u]:
            if dist[node] == len(graph) + 1000:
                Q.append(node)
                dist[node] = dist[u] + 1
    return dist


def distance(adj, s, t):
    dist = bfs(adj, s)
    d = dist[t]
    if d == len(adj) + 1000:
        return -1
    return d


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
