class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # remove lead and tail space
        s.strip()
        try:
            float(s)
            return True
        except:
            if '.' in s or ' ' in s:
                return False
            temp = s.split('e')
            if len(temp) == 2:
                try:
                    int(temp[0])
                    int(temp[1])
                except:
                    return False
                return True
        return False

