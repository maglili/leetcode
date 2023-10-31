class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1 = 0
        p2 = len(height) - 1
        area = 0

        while (p1 != p2):
            d = p2 - p1
            if height[p1] < height[p2]:
                h = height[p1]
                p1 += 1
            else:
                h = height[p2]
                p2 -= 1

            if (d * h > area):
                area = d * h

        return area
