#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(t, k):
    stack = [t]
    res = []
    while stack:
        cur = stack.pop()
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
        res.append(cur.value)
    return res