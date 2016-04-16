# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        ld = self.minDepth(root.left)
        rd = self.minDepth(root.right)
        if ld != 0 and rd != 0:
            # handle 0 case!
            return 1 + min(ld, rd)
        return 1 + ld +rd