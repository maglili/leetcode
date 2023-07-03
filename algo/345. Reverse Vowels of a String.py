class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        target = {
            'a':True, 'A':True, 'e':True, 'E':True, 'i':True, 'I':True, 'o':True, 'O':True,'u':True, 'U':True
        }

        ans = list(s)
        p1 = 0
        p2 = len(s) - 1
        temp = None

        while (p1 < p2):
            if (s[p1] in target) and (s[p2] in target):
                temp = ans[p1]
                ans[p1] = ans[p2]
                ans[p2] = temp
                p1 += 1
                p2 -= 1
            if (s[p1] not in target):
                p1 += 1
            if (s[p2] not in target):
                p2 -= 1
        
        return''.join(ans)