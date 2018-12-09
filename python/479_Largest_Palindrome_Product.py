class Solution(object):
    # def largestPalindrome(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 1:
    #         return 9
    #     # https://leetcode.com/problems/largest-palindrome-product/discuss/96297/Java-Solution-using-assumed-max-palindrom
    #     upperBound = 10 ** n - 1
    #     lowerBound = upperBound / 10
    #     maxNum = upperBound * upperBound
    #     firstHalf = maxNum / (10 ** n)
    #     palindromFound = False
    #     palindrom = 0
    #     while not palindromFound:
    #         palindrom = int(str(firstHalf) + str(firstHalf)[::-1])
    #         for i in xrange(upperBound, lowerBound, -1):
    #             if i * i < palindrom:
    #                 break
    #             if palindrom % i == 0:
    #                 palindromFound = True
    #                 break
    #         firstHalf -= 1
    #     return palindrom % 1337

    def largestPalindrome(self, n):
        if n == 1:
            return 9
        if n == 2:
            return 987
        for a in xrange(2, 9 * 10 ** (n - 1)):
            hi = (10 ** n) - a
            lo = int(str(hi)[::-1])
            if a ** 2 - 4 * lo < 0:
                continue
            if (a ** 2 - 4 * lo) ** .5 == int((a ** 2 - 4 * lo) ** .5):
                return (lo + 10 ** n * (10 ** n - a)) % 1337
