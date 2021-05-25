def maximalSquare(matrix)
    return 0 if matrix.empty?
    def findMaxSquare(x, y, matrix, memo)
        return 0 if x >= matrix.size or y >= matrix[0].size
        return memo[[x, y]] if memo.key?([x, y])
        if matrix[x][y] == '0'
            memo[[x, y]] = 0
        else
            memo[[x, y]] = 1 + ([findMaxSquare(x + 1, y, matrix, memo), findMaxSquare(x, y + 1, matrix, memo), findMaxSquare(x + 1, y + 1, matrix, memo)].min)
        end
        memo[[x, y]]
    end
    memo = Hash.new
    maxGlobal = 0
    (0...matrix.size).each do |i|
        (0...matrix[i].size).each do |j|
            maxGlobal = [maxGlobal, findMaxSquare(i, j, matrix, memo)].max
        end
    end
    maxGlobal * maxGlobal
end