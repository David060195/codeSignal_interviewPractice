def nextLarger(a):
    stack = []
    ans = [-1 for _ in range(len(a))]
    for i, n in enumerate(a):
        while stack and n > a[stack[-1]]:
            ans[stack[-1]] = a[i]
            stack.pop()
        stack.append(i)
    return ans

    