import json
from collections import defaultdict, deque

def load_graph_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def topological_sort(graph, vertices):
    in_degree = {v: 0 for v in vertices}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([v for v in vertices if in_degree[v] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph.get(u, {}):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return topo_order

def longest_path_dag(graph, vertices, start, end):
    # Topological Sort
    topo_order = topological_sort(graph, vertices)

    # Initialize distances
    distance = {v: -float('inf') for v in vertices}
    distance[start] = 0

    # Process vertices in topological order
    for u in topo_order:
        if distance[u] != -float('inf'):  # Only consider reachable nodes
            for v, weight in graph.get(u, {}).items():
                distance[v] = max(distance[v], distance[u] + 1)

    return distance[end]

# Main function
def main():
    #file_path = "D:\\tb\\octo_coding\\week3\\OCTO-Coding-Challenge-2024-Week-3-Part-1-test-input.json"  # Replace with your file path
    file_path = "D:\\tb\\octo_coding\\week3\\OCTO-Coding-Challenge-2024-Week-3-Part-1-input.json"  # Replace with your file path
    graph_data = load_graph_from_json(file_path)

    # Get all vertices
    vertices = set(graph_data.keys())
    for edges in graph_data.values():
        vertices.update(edges.keys())

    # Define start and end nodes
    start = "START"
    end = "END"

    # Find the longest path
    longest_path_weight = longest_path_dag(graph_data, vertices, start, end) - 1
    print(f"The weight of the longest path from {start} to {end} is: {longest_path_weight}")

if __name__ == "__main__":
    main()
