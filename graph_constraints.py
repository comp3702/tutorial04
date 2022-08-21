import networkx as nx
from networkx.drawing.nx_agraph import write_dot
from matplotlib import pyplot as plt

from CrossWorldEnv import CrossWorldEnv


if __name__ == '__main__':
    env = CrossWorldEnv()

    edge_labels = {(var, constraint[1]): f"{constraint[0]} != {constraint[2]}"
                   for var, constraints in env.intersect_constraints.items()
                   for constraint in constraints}
    edges = [[edge[0], edge[1]] for edge in edge_labels.keys()] \
        + [[key, f"length = {val}"] for key, val in env.length_constraints.items()]

    G = nx.DiGraph()
    G.add_edges_from(edges)
    pos = nx.circular_layout(G)
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1, \
            node_size=500, node_color='pink' ,alpha=0.66, \
            labels={node: node for node in G.nodes()})

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.axis('off')
    plt.show()
    plt.savefig('constraints.png')