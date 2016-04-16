class Solution:
    # import itertools
    # def permute(self, num):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     result = itertools.permutations(num)
    #     result = [list(t) for t in result]
    #     return result

    def permute(self, num):
        res = []
        if len(num) == 0:
            return res
        self.get_permute(res, num, 0)
        return res

    def get_permute(self, res, num, index):
        if index == len(num):
            res.append(list(num))
            return
        for i in range(index, len(num)):
            num[i], num[index] = num[index], num[i]
            # s(n) = 1 + s(n-1)
            self.get_permute(res, num, index + 1)
            num[i], num[index] = num[index], num[i]