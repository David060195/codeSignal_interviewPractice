def bomber(field):
    def findBombs(x, y):
        ans = 0
        for i in xrange(y + 1, len(field[0])):
            if field[x][i] == 'W': break
            if field[x][i] == 'E': ans += 1
        for i in xrange(x + 1, len(field)):
            if field[i][y] == 'W': break
            if field[i][y] == 'E': ans += 1
        for i in xrange(y - 1, -1, -1):
            if field[x][i] == 'W': break
            if field[x][i] == 'E': ans += 1
        for i in xrange(x - 1, -1, -1):
            if field[i][y] == 'W': break
            if field[i][y] == 'E': ans += 1
        return ans
        
    if not field: return 0
    maxGlobal = 0
    for i in xrange(len(field)):
        for j in xrange(len(field[i])):
            if field[i][j] == '0':
                maxGlobal = max(maxGlobal, findBombs(i, j))
    return maxGlobal