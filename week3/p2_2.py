def calculate_average_length(graph, start, end, tolerance=1e-6):
    # Initialize expected lengths for all nodes to 0
    expected_length = {node: 0 for node in graph}
    expected_length[end] = 0  # End node has zero length

    while True:
        max_change = 0
        for node in graph:
            if node == end:
                continue

            # Compute the new expected length for this node
            new_length = sum(
                prob * (1 + expected_length[neighbor])
                for neighbor, prob in graph[node].items()
            )

            # Update the change and the expected length
            max_change = max(max_change, abs(new_length - expected_length[node]))
            expected_length[node] = new_length

        # Check for convergence
        if max_change < tolerance:
            break

    return expected_length[start]

# Example usage
def main():
    graph = {
        "START": {"hooray": 0.6, "yay": 0.4},
        "hooray": {"for": 1.0},
        "for": {"AI": 0.5, "puzzles": 0.5},
        "yay": {"for": 1.0},
        "AI": {"and": 1.0},
        "and": {"ML": 1.0},
        "ML": {"END": 1.0},
        "puzzles": {"END": 1.0},
    }

    avg_length = calculate_average_length(graph, "START", "END")
    print(f"The average sentence length is: {avg_length:.2f}")

if __name__ == "__main__":
    main()