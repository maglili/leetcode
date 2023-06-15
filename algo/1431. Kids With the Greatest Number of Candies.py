class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        std = max(candies) - extraCandies
        return [True if x >= std else False for x in candies]
