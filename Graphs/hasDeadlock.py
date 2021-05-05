#topological sort
def hasDeadlock(connections):
    countIn = [0] * len(connections)
    graph = {i : a for i, a in enumerate(connections)}
    queue, cnt = [], 0
    for i in range(len(connections)):
        for j in graph[i]:
            countIn[j] += 1
    for i in range(len(countIn)): 
        if countIn[i] == 0: queue.append(i)
    while queue:
        node = queue.pop(0)
        for e in graph[node]:
            countIn[e] -= 1
            if countIn[e] == 0:
                queue.append(e)
        cnt += 1
    return cnt != len(connections)