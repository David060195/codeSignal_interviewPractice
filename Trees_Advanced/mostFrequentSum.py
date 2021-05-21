#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
from collections import defaultdict
def mostFrequentSum(t):
    if not t: return []
    ans = []
    freq = defaultdict(int)
    helper(t, freq)
    m = max(freq, key = freq.get)
    for key, value in freq.items():
        if value == freq[m]:
            ans.append(key)
    return sorted(ans)
def helper(t, freq):
    if not t.left and not t.right:
        freq[t.value] += 1
        return t.value
    l, r, ans = 0, 0, 0
    if t.left:
        l = helper(t.left, freq)
    if t.right:
        r = helper(t.right, freq)
    ans = l + r + t.value
    freq[ans] += 1
    return ans
