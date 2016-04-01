class Solution(object):
    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     ls = len(nums)
    #     start = [0] * ls
    #     all = [0] * ls
    #     start[-1], all[-1] = nums[-1], nums[-1]
    #     for i in reversed(range(ls - 1)):
    #         start[i] = max(nums[i], nums[i] + start[i + 1])
    #         all[i] = max(start[i], all[i + 1])
    #     return all[0]

    def maxSubArray(self, nums):
        ls = len(nums)
        start, all = nums[-1], nums[-1]
        for i in reversed(range(ls - 1)):
            start = max(nums[i], nums[i] + start)
            all = max(start, all)
        return all