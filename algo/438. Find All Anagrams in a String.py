class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_s, len_p = len(s), len(p)

        if len_p > len_s:
            return []
        
        # build hash_table
        hash_table = {}
        for char in p:
            hash_table[char] = hash_table.get(char, 0) + 1

        # init the window first time
        for i in range(len(p) - 1):
            if s[i] in hash_table:
                hash_table[s[i]] -= 1
        
        ans = []
        for i in range(len_s - len_p + 1):
            if s[i+len_p-1] in hash_table:
                hash_table[s[i+len_p-1]] -= 1

            if all(v==0 for v in hash_table.values()):
                ans.append(i)

            if s[i] in hash_table:
                hash_table[s[i]] += 1
        
        return ans

