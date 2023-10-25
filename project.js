const NetworkX = require('networkx-js');
const nx = new NetworkX();

// Function to find the shortest path using Dijkstra's algorithm
function shortestPath(graph, source, target) {
  const shortestPath = nx.shortestPath(graph, source, target, 'weight');
  const shortestDistance = nx.shortestPathLength(graph, source, target, 'weight');
  return [shortestPath, shortestDistance];
}

// Function to find the maximum flow using Ford-Fulkerson algorithm
function maximumFlow(graph, source, target) {
  const flowValue = nx.maximumFlow(graph, source, target);
  return flowValue;
}

// Create a directed graph
const G = new nx.DiGraph();

// Add edges with weights and coordinates
G.addEdge('A', 'B', { weight: 4, capacity: 10, pos: { A: [0, 0], B: [2, 2] } });
G.addEdge('A', 'C', { weight: 2, capacity: 5, pos: { A: [0, 0], C: [2, -2] } });
G.addEdge('B', 'C', { weight: 5, capacity: 15, pos: { B: [2, 2], C: [2, -2] } });
G.addEdge('B', 'D', { weight: 10, capacity: 10, pos: { B: [2, 2], D: [4, 0] } });
G.addEdge('C', 'D', { weight: 3, capacity: 10, pos: { C: [2, -2], D: [4, 0] } });

// Source and target nodes
const sourceNode = 'A';
const targetNode = 'D';

// Find the shortest path
const [shortestPath, shortestDistance] = shortestPath(G, sourceNode, targetNode);
console.log(`Shortest Path: ${shortestPath}`);
console.log(`Shortest Distance: ${shortestDistance}`);

// Find the maximum flow
const flowValue = maximumFlow(G, sourceNode, targetNode);
console.log(`Maximum Flow Value: ${flow
