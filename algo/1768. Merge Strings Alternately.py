class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        p1, p2 = 0, 0
        len_1, len_2 = len(word1), len(word2)
        res = ''

        while (p1 != len_1 or p2 != len_2):
            if (p1 < len_1):
                res += word1[p1]
                p1 += 1
            if (p2 < len_2):
                res += word2[p2]
                p2 += 1

        return res