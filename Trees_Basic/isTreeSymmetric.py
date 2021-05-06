#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
    if not t: return True
    return findMirror(t, t)
def findMirror(t1, t2):
    stack1, stack2 = [(t1, 'c')], [(t2, 'c')]
    while stack1 and stack2:
        node1, d1 = stack1.pop()
        node2, d2 = stack2.pop()
        if d1 != 'c' and d2 != 'c':
            if (node1.value != node2.value) or (d1 == d2): return False
        if node1.right:
            stack1.append((node1.right, 'r'))
        if node1.left:
            stack1.append((node1.left, 'l'))
        if node2.left:
            stack2.append((node2.left, 'l'))
        if node2.right:
            stack2.append((node2.right, 'r'))
    return True