def houseRobber(nums)
    def findLongestPath(index, nums, memo)
        return 0 if index >= nums.size
        return memo[index] if memo.key?index
        memo[index] = [nums[index] + findLongestPath(index + 2, nums, memo), findLongestPath(index + 1, nums, memo)].max
        memo[index]
    end
    findLongestPath(0, nums, memo = {})
end