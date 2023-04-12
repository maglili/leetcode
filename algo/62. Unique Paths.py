class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m == 1) or (n == 1):
            return 1
            
        dp_top_row = [1] * n
        for i in range(m):
            dp_v = 1
            for j in range(n):
                if (i == 0) or (j == 0):
                    continue
                dp_v = dp_v + dp_top_row[j]
                dp_top_row[j] = dp_v

        return dp_top_row[-1]