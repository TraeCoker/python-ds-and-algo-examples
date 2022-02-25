def dfs(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []
    
    stack.append(root)
    
    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)
    return result