import json
import sys

THRESHOLD = float(sys.argv[2])

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
        if (node == end) or (current_length > 1) and (current_prob * (current_length - 1)) < THRESHOLD:
            #print(f"Pushing ( {current_prob * (current_length - 1)}, {visited}, {node} )")
            total_weighted_sum += (current_length - 1) * current_prob
            #print (f"Length = {current_length - 1}, Probability: {current_prob}, Total weighted sum: {total_weighted_sum}")
            continue

        # Push neighbors to the stack with updated probability, length, and visited set
        for neighbor, prob in graph.get(node, {}).items():
            stack.append((neighbor, current_prob * prob, current_length + 1, visited))

    return total_weighted_sum

# Main function
def main():
    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        graph = json.load(file)

    print(f"The average weighted product of length and probability is: {find_all_paths(graph, 'START', 'END')}")

if __name__ == "__main__":
    main()
