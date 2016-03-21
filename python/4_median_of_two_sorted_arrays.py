class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p1 = p2 = 0
        ls1 = len(nums1)
        ls2 = len(nums2)
        all_nums = []
        median = 0.0
        while p1 < ls1 and p2 < ls2:
            if nums1[p1] < nums2[p2]:
                all_nums.append(nums1[p1])
                p1 += 1
            else:
                all_nums.append(nums2[p2])
                p2 += 1
        if p1 < ls1:
            while p1 < ls1:
                all_nums.append(nums1[p1])
                p1 += 1
        if p2 < ls2:
            while p2 < ls2:
                all_nums.append(nums2[p2])
                p2 += 1
        print all_nums
        if (ls1 + ls2) % 2 == 1:
            median = all_nums[(ls1 + ls2) / 2]
        else:
            median = 1.0 * (all_nums[(ls1 + ls2) / 2] + all_nums[(ls1 + ls2) / 2 - 1]) / 2
        return median


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.findMedianSortedArrays([1, 1], [1, 2])