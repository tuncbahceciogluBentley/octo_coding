import json

# def find_all_paths(graph, start, end, current_prob=1, current_length=0):
#     # If reached the end node, return the weighted sum (length * probability)
#     if start == end:
#         return (current_length - 1) * current_prob

#     # Explore all neighbors
#     total_weighted_sum = 0
#     for neighbor, prob in graph.get(start, {}).items():
#         weighted_sum = find_all_paths(
#             graph, neighbor, end, current_prob * prob, current_length + 1
#         )
#         total_weighted_sum += weighted_sum

#     return total_weighted_sum

def find_all_paths(graph, start, end):
    # Stack entries: (node, current_prob, current_length, visited_set)
    stack = [(start, 1, 0, set())]
    total_weighted_sum = 0

    while stack:
        node, current_prob, current_length, visited = stack.pop()

        # If this node is already in the current path, skip to avoid cycles
        if node in visited:
            continue

        # Add this node to the visited set for the current path
        visited = visited | {node}

        # If reached the end node, calculate the weighted sum and add it
        if node == end:
            total_weighted_sum += (current_length - 1) * current_prob
            continue

        # Push neighbors to the stack with updated probability, length, and visited set
        for neighbor, prob in graph.get(node, {}).items():
            stack.append((neighbor, current_prob * prob, current_length + 1, visited))

    return total_weighted_sum

# Main function
def main():
    #file_path = "D:\\tb\\octo_coding\\week3\\OCTO-Coding-Challenge-2024-Week-3-Part-2-test-input.txt"  # Replace with your file path
    file_path = "D:\\tb\\octo_coding\\week3\\OCTO-Coding-Challenge-2024-Week-3-Part-2-input.txt"  # Replace with your file path
    with open(file_path, "r") as file:
        graph = json.load(file)

    print(f"The average weighted product of length and probability is: {find_all_paths(graph, 'START', 'END')}")

if __name__ == "__main__":
    main()
