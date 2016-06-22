class Solution(object):
    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # dp
    #     ls = len(nums)
    #     if ls == 0:
    #         return 0
    #     dp = [0] * ls
    #     dp[0] = nums[0]
    #     for i in range(1, ls):
    #         can = [0]
    #         if i >= 2:
    #             can.append(dp[i - 2])
    #         if i >= 3:
    #             can.append(dp[i - 3])
    #         dp[i] = max(can) + nums[i]
    #     return max(dp[ls - 1], dp[ls - 2])

    def rob(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        return nums[-1]