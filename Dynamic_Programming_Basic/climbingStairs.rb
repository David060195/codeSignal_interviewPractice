def climbingStairs(n)
    def findSteps(n, memo)
        return 0 if n < 0
        return 1 if n == 0
        return memo[n] if memo.key?(n)
        memo[n] = findSteps(n - 1, memo) + findSteps(n - 2, memo)
        return memo[n]
    end
    findSteps(n, memo = Hash.new)
end
