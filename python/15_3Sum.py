# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
class Solution(object):
    def threeSum(self, nums):
        # skip duplicate
        if len(nums) < 3:
            return []
        nums.sort()
        ls = len(nums)
        result = []
        for i in range(0, ls - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = ls - 1
            while(j < k):
                temp = [nums[i], nums[j], nums[k]]
                s = sum(temp)
                jtemp = nums[j]
                ktemp = nums[k]
                if s <= 0:
                    j += 1
                    while(j < k and jtemp == nums[j]):
                        j += 1
                    if s == 0:
                        result.append(temp)
                else:
                    k -= 1
                    while(j < k and ktemp == nums[k]):
                        k -= 1
        return result
