def countClouds(s):
    table = [[False for i in range(len(s[0]))] for _ in range(len(s))]
    
    def check(x, y):
        return x >= 0 and x < len(s) and y >= 0 and y < len(s[0])
    
    def dfs(x, y, s, table):
        table[x][y] = True
        for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x1 = x + a
            y1 = y + b
            if check(x1, y1) and table[x1][y1] == False and s[x][y] == s[x1][y1]:
                dfs(x1, y1, s, table)
    
    ans = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == '1' and table[i][j] == False:
                dfs(i, j, s, table)
                ans += 1
    return ans
    