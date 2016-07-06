class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.get_min(nums, 0, len(nums) - 1)

    def get_min(self, nums, start, end):
        mid = (start + end) / 2
        if start == end:
            # one element
            return nums[start]
        if mid == start or mid == end:
            # two element
            return min(nums[start], nums[end])
        if nums[mid] < nums[end]:
            # right side sorted
            if nums[mid] > nums[start]:
                # not rotated
                return nums[start]
            return self.get_min(nums, start, mid)
        elif nums[mid] > nums[end]:
            # left side sorted
            return self.get_min(nums, mid, end)

