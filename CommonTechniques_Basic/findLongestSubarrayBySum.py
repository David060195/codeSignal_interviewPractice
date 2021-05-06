def findLongestSubarrayBySum(s, arr):
    l, start, ans, m = 0, 0, [-1], float('-inf')
    for end, e in enumerate(arr):
        l += e
        while l > s:
            l -= arr[start]
            start += 1
        if l == s and end - start > m:
            ans = [0, 0]
            m = end - start
            ans[0], ans[1] = start + 1, end + 1
    return ans