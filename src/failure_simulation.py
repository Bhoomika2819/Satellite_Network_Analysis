import networkx as nx

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

print("===================================")
print("   SATELLITE NETWORK RESILIENCE")
print("===================================")

# Original network
print("\nORIGINAL NETWORK")
print("----------------")

components_before = list(nx.connected_components(G))

print("Number of connected components:",
      len(components_before))

print("Number of satellites:",
      G.number_of_nodes())

# Simulate SAT-02 failure
failed_satellite = "SAT-02"

G.remove_node(failed_satellite)

print("\n❌ SAT-02 FAILURE SIMULATED")
print("---------------------------")

# Network after failure
components_after = list(nx.connected_components(G))

print("Number of connected components:",
      len(components_after))

print("Remaining satellites:",
      G.number_of_nodes())

# Display components
print("\nRemaining network groups:")

for i, component in enumerate(components_after, 1):
    print("Group", i, ":", list(component))

# Check unreachable satellites
print("\nNetwork status:")

if nx.is_connected(G):
    print("All remaining satellites are connected.")
else:
    print("Some satellites are now separated.")