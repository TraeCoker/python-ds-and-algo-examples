def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    parent = [None] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    queue = []
    
    distance[source] = 0
    queue.append(source)
    idx = 0
    
    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx +=1
        #update the distances of all the neighbors
        update_distances(graph, current, distance, parent)
        
        #find the first unvisited node with the smallest distance
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)
        
    return distance[target], parent


def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current

def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node