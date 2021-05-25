def longestIncreasingSubsequence(sequence)
    def findLongestIncreasing(index, sequence, memo)
        return memo[index] if memo.key?(index)
        maxLocal = 1
        (index...sequence.length).each do |i|
            if sequence[i] > sequence[index]
                maxLocal = [maxLocal, findLongestIncreasing(i, sequence, memo) + 1].max
            end
        end
        memo[index] = maxLocal
        maxLocal
    end
    maxGlobal = 0; memo = Hash.new
    (0...sequence.size).each do |i|
        maxGlobal = [maxGlobal, findLongestIncreasing(i, sequence, memo)].max
    end
    maxGlobal
end