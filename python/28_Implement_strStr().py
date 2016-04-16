class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lsh, lsn = len(haystack), len(needle)
        if lsn == 0:
            return 0
        pos, index = 0, 0
        while index <= lsh - lsn:
            if haystack[index] == needle[pos]:
                backup = index
                while index < lsh and pos < lsn and haystack[index] == needle[pos]:
                    pos += 1
                    index += 1
                if pos == len(needle):
                    return index - pos
                index = backup
            index += 1
            pos = 0
        return -1

    # def strStr(self, haystack, needle):
    #     lsh, lsn = len(haystack), len(needle)
    #     if lsn == 0:
    #         return 0
    #     pos, index = 0, 0
    #     while index <= lsh - lsn:
    #         if haystack[index] == needle[0]:
    #             # slice index:index + lsn
    #             if haystack[index:index + lsn] == needle:
    #                 return index
    #         index += 1
    #     return -1
