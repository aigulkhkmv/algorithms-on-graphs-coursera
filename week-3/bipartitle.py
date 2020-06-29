# Uses python3

import sys


def bipartite(adj):
    color = [-1 for i in range(len(adj))]
    color[0] = 1
    Q = [0]
    while Q:
        u = Q.pop(0)
        for node in adj[u]:
            if color[node] == -1:
                Q.append(node)
                color[node] = 1 - color[u]
            if color[node] == color[u]:
                return 0
    return 1


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
    print(bipartite(adj))
