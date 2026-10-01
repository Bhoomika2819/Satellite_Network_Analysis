import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Satellite Communication Network",
    page_icon="🛰️",
    layout="wide"
)

st.title("🛰️ Satellite Communication Network")
st.write("Network Analysis and Optimization Using Graph Analytics")

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

# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🛰️ Network Visualization",
    "📊 Centrality Analysis",
    "🛣️ Route Finder",
    "⚠️ Failure Simulation",
    "🤖 ML Prediction"
])

# TAB 1
with tab1:
    st.header("🛰️ Satellite Network")

    fig, ax = plt.subplots(figsize=(8, 5))

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
        ax=ax,
        with_labels=True,
        node_size=2500,
        node_color="skyblue",
        font_size=10,
        font_weight="bold",
        width=2
    )

    ax.set_title("Satellite Communication Network")
    st.pyplot(fig)

    st.write("**Number of Satellites:**", G.number_of_nodes())
    st.write("**Communication Links:**", G.number_of_edges())


# TAB 2
with tab2:
    st.header("📊 Centrality Analysis")

    degree = nx.degree_centrality(G)
    closeness = nx.closeness_centrality(G)
    betweenness = nx.betweenness_centrality(G)

    st.subheader("Degree Centrality")

    for satellite, value in degree.items():
        st.write(f"{satellite}: {value:.3f}")

    st.subheader("Closeness Centrality")

    for satellite, value in closeness.items():
        st.write(f"{satellite}: {value:.3f}")

    st.subheader("Betweenness Centrality")

    for satellite, value in betweenness.items():
        st.write(f"{satellite}: {value:.3f}")


# TAB 3
with tab3:
    st.header("🛣️ Route Finder")

    satellites = list(G.nodes)

    source = st.selectbox(
        "Source Satellite",
        satellites,
        index=0
    )

    destination = st.selectbox(
        "Destination Satellite",
        satellites,
        index=5
    )

    if source == destination:
        st.warning("Source and destination must be different.")

    else:
        route = nx.shortest_path(
            G,
            source=source,
            target=destination
        )

        st.success(
            "Shortest route: " + " → ".join(route)
        )

        st.write(
            "Number of communication links:",
            len(route) - 1
        )


# TAB 4
with tab4:
    st.header("⚠️ Failure Simulation")

    satellites = list(G.nodes)

    failed_satellite = st.selectbox(
        "Select satellite",
        satellites
    )

    if st.button("Simulate Failure"):

        G_failure = G.copy()

        G_failure.remove_node(failed_satellite)

        components_before = nx.number_connected_components(G)
        components_after = nx.number_connected_components(G_failure)

        st.write(
            f"**Failed Satellite:** {failed_satellite}"
        )

        st.write(
            f"**Before:** {components_before} component(s)"
        )

        st.write(
            f"**After:** {components_after} component(s)"
        )

        if nx.is_connected(G_failure):
            st.success("Network remains connected.")

        else:
            st.error("Network has become disconnected.")


# TAB 5
with tab5:
    st.header("🤖 ML Link Quality Prediction")

    distance = st.number_input(
        "Distance (km)",
        min_value=1,
        value=1500
    )

    signal = st.number_input(
        "Signal Strength",
        min_value=-120,
        max_value=0,
        value=-60
    )

    latency = st.number_input(
        "Latency (ms)",
        min_value=1,
        value=45
    )

    packet_loss = st.number_input(
        "Packet Loss (%)",
        min_value=0.0,
        value=2.0
    )

    duration = st.number_input(
        "Connection Duration",
        min_value=1,
        value=80
    )

    if st.button("Predict Link Quality"):

        if packet_loss <= 2 and latency <= 40:
            prediction = "Good Link"

        elif packet_loss <= 5 and latency <= 60:
            prediction = "Moderate Link"

        else:
            prediction = "Poor Link"

        st.success(
            f"Prediction: {prediction}"
        )