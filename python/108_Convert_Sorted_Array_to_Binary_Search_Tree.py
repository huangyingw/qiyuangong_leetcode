# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def sortedArrayToBST(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: TreeNode
    #     """
    #     length = len(nums)
    #     if length == 0:
    #         return None
    #     mid = length / 2
    #     current = TreeNode(nums[mid])
    #     left = self.sortedArrayToBST(nums[mid])
    #     try:
    #         right = self.sortedArrayToBST(nums[mid + 1:])
    #     except:
    #         right = None
    #     current.left = left
    #     current.right = right
    #     return current

    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root