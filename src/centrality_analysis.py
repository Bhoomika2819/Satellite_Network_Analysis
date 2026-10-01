import networkx as nx
import matplotlib.pyplot as plt

# Create satellite network
G = nx.Graph()

G.add_edges_from([
    ("SAT-01", "SAT-02"),
    ("SAT-01", "SAT-03"),
    ("SAT-02", "SAT-04"),
    ("SAT-03", "SAT-04"),
    ("SAT-03", "SAT-05"),
    ("SAT-04", "SAT-06"),
    ("SAT-05", "SAT-06")
])

# Calculate centrality
degree = nx.degree_centrality(G)
closeness = nx.closeness_centrality(G)
betweenness = nx.betweenness_centrality(G)

# Display all results
print("\n========================================")
print("       SATELLITE NETWORK ANALYSIS")
print("========================================")

print("\n1. DEGREE CENTRALITY")
print("--------------------")
for satellite, value in degree.items():
    print(f"{satellite}: {value:.3f}")

print("\n2. CLOSENESS CENTRALITY")
print("-----------------------")
for satellite, value in closeness.items():
    print(f"{satellite}: {value:.3f}")

print("\n3. BETWEENNESS CENTRALITY")
print("-------------------------")
for satellite, value in betweenness.items():
    print(f"{satellite}: {value:.3f}")

# Draw network
pos = {
    "SAT-01": (0, 2),
    "SAT-02": (2, 2),
    "SAT-03": (0, 1),
    "SAT-04": (2, 1),
    "SAT-05": (0, 0),
    "SAT-06": (2, 0)
}

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500,
    node_color="skyblue",
    font_size=10,
    font_weight="bold",
    width=2
)

plt.title("Satellite Network - Centrality Analysis")
plt.show()