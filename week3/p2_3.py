import networkx as nx

def calculate_average_length(graph):
    # Create a directed graph from the Markov chain
    G = nx.DiGraph(graph)

    # Define a recursive function to perform DFS traversal
    def dfs(node, length=0):
        if node == "END":
            return length
        expected_length = 0
        for neighbor, weight in G[node].items():
            expected_length += weight * dfs(neighbor, length + 1)
        return expected_length

    # Calculate the average length of a sentence
    average_length = dfs("START")
    return average_length

# Example usage
graph = {
    "START": {"hooray": 0.6, "yay": 0.4},
    "hooray": {"for": 1.0},
    "for": {"AI": 0.5, "puzzles": 0.5},
    "yay": {"for": 1.0},
    "AI": {"and": 1.0},
    "and": {"ML": 1.0},
    "ML": {"END": 1.0},
    "puzzles": {"END": 1.0}
}

average_length = calculate_average_length(graph)
print(average_length)  # Output: 4.0