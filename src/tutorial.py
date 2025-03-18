import graph

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13)]
G = graph.create_graph(edges)
graph.visualize_graph(G)
print(graph.get_degree(G, 1))
print(graph.dfs_traversal(G, 1))
print(graph.bfs_traversal(G, 1))
print(graph.find_shortest_path(G, 1, 13))
