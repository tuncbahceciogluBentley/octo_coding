import csv
import heapq
import argparse

def read_distance_matrix(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        matrix = [list(map(int, row)) for row in reader]
    return matrix

def prim_mst(matrix):
    num_cities = len(matrix)
    visited = [False] * num_cities
    min_heap = [(0, 0)]  # (cost, city)
    total_cost = 0

    while min_heap:
        cost, city = heapq.heappop(min_heap)
        if visited[city]:
            continue
        visited[city] = True
        total_cost += cost

        for next_city in range(num_cities):
            if not visited[next_city] and matrix[city][next_city] != 0:
                heapq.heappush(min_heap, (matrix[city][next_city], next_city))

    return total_cost

def main():
    parser = argparse.ArgumentParser(description='Process a distance matrix CSV file.')
    parser.add_argument('file_path', type=str, help='Path to the distance matrix CSV file')
    args = parser.parse_args()

    distance_matrix = read_distance_matrix(args.file_path)
    min_total_distance = prim_mst(distance_matrix)
    print(f"The minimum total distance of the network is: {min_total_distance}")

if __name__ == "__main__":
    main()