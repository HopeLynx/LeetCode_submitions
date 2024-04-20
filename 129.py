# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def pre_order(node, cntr, s):
    if node:
        s += str(node.val)
        if not node.left and not node.right:
            cntr += int(s)
        else:
            cntr += int(pre_order(node.left, 0, s))
            cntr += int(pre_order(node.right, 0, s))
    return cntr


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return pre_order(root, 0, "")

# Runtime: 37 ms Beats 45.79% of users with Python3
# Memory Usage: 16.48 MB Beats 77.48% of users with Python3
