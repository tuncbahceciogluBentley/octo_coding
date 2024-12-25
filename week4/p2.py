import json
from collections import deque, defaultdict
import argparse

def read_graph(file_path):
    with open(file_path, 'r') as file:
        graph = json.load(file)
    return graph

def bfs(capacity, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()

        for v in capacity[u]:
            if v not in visited and capacity[u][v] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(graph, source, sink):
    capacity = defaultdict(lambda: defaultdict(int))
    for u in graph:
        for v in graph[u]:
            capacity[u][v] = graph[u][v]

    parent = {}
    max_flow = 0

    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

def main():
    parser = argparse.ArgumentParser(description='Process a graph JSON file.')
    parser.add_argument('file_path', type=str, help='Path to the graph JSON file')
    source = 'A'
    sink = 'Z'
    args = parser.parse_args()

    graph = read_graph(args.file_path)
    max_traffic_capacity = edmonds_karp(graph, source, sink)
    print(f"The maximum traffic capacity between {source} and {sink} is: {max_traffic_capacity}")

if __name__ == "__main__":
    main()