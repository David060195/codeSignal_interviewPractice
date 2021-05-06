def climbingStaircase(n, k):
    ans = []
    dfs(ans, [], n, k)
    return ans
    
def dfs(ans, temp, n, k):
    if n == 0: ans.append(temp.copy())
    for i in range(1, k + 1):
        if i <= n:
            temp.append(i)
            dfs(ans, temp, n - i, k)
            temp.pop()