#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    if not t: return False
    if not t.left or not t.right:
        return s == t.value
    return hasPathWithGivenSum(t.left, s - t.value) or hasPathWithGivenSum(t.right, s - t.value)