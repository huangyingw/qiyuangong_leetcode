# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """

class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        last = s[-1]
        for t in reversed(s):
            if t == 'C' and last in ['D', 'M']:
                result -= roman[t]
            elif t == 'X' and last in ['L', 'C']:
                result -= roman[t]
            elif t == 'I' and last in ['V', 'X']:
                result -= roman[t]
            else:
                result += roman[t]
            last = t
        return result

