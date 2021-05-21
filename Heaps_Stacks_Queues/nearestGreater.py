def nearestGreater(a):
    s1 = []
    s2 = []
    ans = [[] for _ in a]
    for i in range(len(a)):
        while s1 and a[s1[-1]] < a[i]:
            ans[s1[-1]].append(i)
            s1.pop()
        s1.append(i)
    for i in reversed(range(len(a))):
        while s2 and a[s2[-1]] < a[i]:
            ans[s2[-1]].append(i)
            s2.pop()
        s2.append(i)
    res = [-1 for _ in a]
    for i, n in enumerate(ans):
        if len(n) > 0: 
            if len(n) > 1:
                a = n[0] - i
                b = i - n[1]
                if a == b: res[i] = n[1]
                else:
                    if a > b:
                        res[i] = n[1]
                    else:
                        res[i] = n[0]
            else:
                res[i] = n[0]
    return res
