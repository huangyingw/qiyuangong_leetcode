class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min, pos = 0, 0
        max = len(nums) - 1
        while min <= max:
            # binary search
            pos = (max + min) / 2
            if nums[pos] == target:
                return pos
            elif nums[pos] > target:
                max = pos - 1
            else:
                min = pos + 1
        if min > pos:
            # this means that target is great than pos, and target
            # is not in nums
            return pos + 1
        return pos


