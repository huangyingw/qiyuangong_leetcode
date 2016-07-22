class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        max_here_pre = min_here_pre = max_so_far = nums[0]
        for i in range(1, len(nums)):
            max_here = max(max(max_here_pre * nums[i], min_here_pre * nums[i]), nums[i])
            min_here = min(min(max_here_pre * nums[i], min_here_pre * nums[i]), nums[i])
            max_so_far = max(max_here, max_so_far)
            max_here_pre = max_here
            min_here_pre = min_here
        return max_so_far