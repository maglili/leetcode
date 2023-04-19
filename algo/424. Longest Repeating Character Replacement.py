class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # key formula: 
        #   window size - most_freq <=k -> valid window
        #   (r-l+1) - most_freq <= k
        # Goal: find the max window size
        
        l=0
        freq = {}
        max_len = 0

        for r in range(len(s)):
            
            # update freq
            freq[s[r]] = freq.get(s[r], 0)+1

            # check formula
            window_size = r-l+1
            if window_size - max(freq.values()) <= k:
                max_len = window_size
            else:
                freq[s[l]] -= 1
                l+=1
        
        return max_len