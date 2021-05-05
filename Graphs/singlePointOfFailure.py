from collections import defaultdict
import copy
def singlePointOfFailure(connections):
    graph = defaultdict(set)
    for i in range(len(connections)):
        for j in range(len(connections[i])):
            if connections[i][j] == 1:
                graph[i].add(j)
    queue, seen = [0], set({0})
    cnt = 0
    while queue:
        node = queue.pop(0)
        for e in graph[node]:
            graphCopy = copy.deepcopy(graph)
            graphCopy[node] -= {e}
            graphCopy[e] -= {node}
            if not e in seen:
                queue.append(e)
                seen.add(e)
            if findFailure(graphCopy, len(graph)):
                cnt += 1
    return cnt / 2
def findFailure(graph, numNode):
    queue, seen = [0], set({0})
    while queue:
        node = queue.pop(0)
        for e in graph[node]:
            if not e in seen:
                queue.append(e)
                seen.add(e)
    return numNode != len(seen)