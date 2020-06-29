# Uses python3

import sys

from loguru import logger


def dijkstra(graph, cost, s):
    logger.info("Start dijkstra algorithm")
    dist = []
    prev = []
    H = {}
    for i in range(len(graph)):
        dist.append(len(graph) + 10000)
        H[i] = len(graph) + 10000
        prev.append(0)
    logger.info("H {}; dist {}; prev {}", H, dist, prev)
    dist[s] = 0
    H[s] = 0
    while H:
        u = min(H, key=H.get)
        logger.info("Minimum u {}", u)
        del H[u]
        logger.info("H after remove {}", H)
        for node in graph[u]:
            logger.info("For node {} in graph", node)
            w = cost[u][graph[u].index(node)]
            if dist[node] > dist[u] + w:
                logger.info("Cost {}", cost)
                logger.info("* Node {}; dist node {}, w {}", node, dist[node], w)
                dist[node] = dist[u] + w
                prev[node] = u
                logger.info("Dist {}", dist[node])
                logger.info("H {}", H)
                logger.info("{}", H[node])
                H[node] = dist[node]
    return dist


def distance(adj, cost, s, t):
    dist2t = dijkstra(adj, cost, s)[t]
    if dist2t == len(adj) + 1000:
        return -1
    return dist2t


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0 : (3 * m) : 3], data[1 : (3 * m) : 3]), data[2 : (3 * m) : 3]))
    data = data[3 * m :]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
