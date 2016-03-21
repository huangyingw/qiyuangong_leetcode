class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = len(s)
        if ls <= 1 or len(set(s)) == 1:
            return s
        # create a new list like this: "abc"->"a#b#c"
        temp_s = '#'.join('{}'.format(s))
        # print temp_s
        tls = len(temp_s)
        seed = range(1, tls - 1)
        # this table stores the max length palindrome
        len_table = [0] * tls
        for step in range(1, tls / 2 + 1):
            final = []
            for pos in seed:
                if pos - step < 0 or pos + step >= tls:
                    continue
                if temp_s[pos - step] != temp_s[pos + step]:
                    continue
                final.append(pos)
                if temp_s[pos - step] == '#':
                    continue
                len_table[pos] = step
            seed = final
        max_pos, max_step = 0, 0
        for i, s in enumerate(len_table):
            if s >= max_step:
                max_step = s
                max_pos = i
        return temp_s[max_pos - max_step:max_pos + max_step + 1].translate(None, '#')
        # return s[(final[0] - step) / 2: (final[0] + step + 2) / 2]

                # def longestPalindrome(self, s):
                #     #Manacher algorithm
                #     #http://en.wikipedia.org/wiki/Longest_palindromic_substring
                #     # Transform S into T.
                #     # For example, S = "abba", T = "^#a#b#b#a#$".
                #     # ^ and $ signs are sentinels appended to each end to avoid bounds checking
                #     T = '#'.join('^{}$'.format(s))
                #     n = len(T)
                #     P = [0] * n
                #     C = R = 0
                #     for i in range (1, n-1):
                #         P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
                #         # Attempt to expand palindrome centered at i
                #         while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                #             P[i] += 1
                #
                #         # If palindrome centered at i expand past R,
                #         # adjust center based on expanded palindrome.
                #         if i + P[i] > R:
                #             C, R = i, i + P[i]
                #
                #     # Find the maximum element in P.
                #     maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
                #     return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.longestPalindrome("abcbe")