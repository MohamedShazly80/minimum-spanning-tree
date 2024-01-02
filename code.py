def kruskal(graph):
    A = []  # Set of edges in the MST
    forest = {v: {v} for v in graph[0]}

    # Sort edges by weight in ascending order
    graph.sort(key=lambda edge: edge[2])

    for u, v, weight in graph:
        if find_set(forest, u) != find_set(forest, v):
            A.append((u, v))  # Add edge to MST
            union(forest, u, v)  # Merge trees containing u and v
    return A

def find_set(forest, vertex):
    if vertex != forest[vertex]:
        forest[vertex] = find_set(forest, forest[vertex])
    return forest[vertex]

def union(forest, u, v):
    """Combines the sets containing u and v into a single set."""
    forest[find_set(forest, u)] = find_set(forest, v)
