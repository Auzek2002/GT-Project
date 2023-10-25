import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes with positions
G.add_node('A', pos=(0, 0))
G.add_node('B', pos=(2, 2))
G.add_node('C', pos=(2, -2))
G.add_node('D', pos=(4, 0))

# Add edges with weights
G.add_edge('A', 'B', weight=4, capacity=10)
G.add_edge('A', 'C', weight=2, capacity=5)
G.add_edge('B', 'C', weight=5, capacity=15)
G.add_edge('B', 'D', weight=10, capacity=10)
G.add_edge('C', 'D', weight=3, capacity=10)

# Set node positions
pos = nx.get_node_attributes(G, 'pos')

# Source and target nodes
source_node = 'A'
target_node = 'D'

# Function to find the shortest path using Dijkstra's algorithm
def shortest_path(graph, source, target):
    shortest_path = nx.shortest_path(graph, source=source, target=target, weight='weight')
    shortest_distance = nx.shortest_path_length(graph, source=source, target=target, weight='weight')
    return shortest_path, shortest_distance

# Function to find the maximum flow using Ford-Fulkerson algorithm
def maximum_flow(graph, source, target):
    flow_value, flow_dict = nx.maximum_flow(graph, source, target)
    return flow_value, flow_dict

# Find the shortest path
shortest_path, shortest_distance = shortest_path(G, source_node, target_node)
print(f"Shortest Path: {shortest_path}")
print(f"Shortest Distance: {shortest_distance}")

# Find the maximum flow
flow_value, flow_dict = maximum_flow(G, source_node, target_node)
print(f"Maximum Flow Value: {flow_value}")
print("Flow Dictionary:")
for u, flows in flow_dict.items():
    for v, flow in flows.items():
        print(f"Flow from {u} to {v}: {flow}")

# Plot the graph with coordinates
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Graph with Coordinates')
plt.show()
