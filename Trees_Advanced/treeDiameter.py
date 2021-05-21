def treeDiameter(n, tree):
    if not tree: return 0
    graph = {vertex : set() for vertex in range(n)}
    for x, y in tree:
        graph[x].add(y)
        graph[y].add(x)
    start, _ = maxDiameter(0, graph)
    _, ans = maxDiameter(start, graph)
    return ans
def maxDiameter(node, graph):
    maxDepth, nodeStart = 0, 0
    stack, seen = [(node, maxDepth)], set({node})
    while stack:
        vertex, depth = stack.pop()
        if depth > maxDepth:
            maxDepth = depth
            nodeStart = vertex
        for e in graph[vertex]:
            if not e in seen:
                stack.append((e, depth + 1))
                seen.add(e)
    return nodeStart, maxDepth