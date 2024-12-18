const fs = require("fs");

function findAllPaths(graph, start, end, currentProb = 1, currentLength = 0) {
  // If reached the end node, return the weighted sum (length - 1) * probability
  if (start === end) {
    return (currentLength - 1) * currentProb;
  }

  // Explore all neighbors
  let totalWeightedSum = 0;
  if (graph[start]) {
    for (const [neighbor, prob] of Object.entries(graph[start])) {
      const weightedSum = findAllPaths(
        graph,
        neighbor,
        end,
        currentProb * prob,
        currentLength + 1
      );
      totalWeightedSum += weightedSum;
    }
  }

  return totalWeightedSum;
}

// Main function
function main() {
  // Replace with your file path
  //const filePath = "D:\\tb\\octo_coding\\week3\\OCTO-Coding-Challenge-2024-Week-3-Part-2-test-input.txt";
  const filePath = "D:\\tb\\octo_coding\\week3\\OCTO-Coding-Challenge-2024-Week-3-Part-2-input.txt"

  const graph = JSON.parse(fs.readFileSync(filePath, "utf-8"));

  const result = findAllPaths(graph, "START", "END");
  console.log(`The average weighted product of length and probability is: ${result}`);
}

main();