class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        r_color = image[sr][sc]
        y_len = len(image)
        x_len = len(image[0])
        if r_color != color:
            self.helper(image, sr, sc, color, r_color, y_len, x_len)
        return image

    def helper(self, image, sr, sc, color, r_color, y_len, x_len):
        if (0 <= sr < y_len and 0 <= sc < x_len and image[sr][sc] != color):
            if (image[sr][sc] == r_color):
                image[sr][sc] = color
                self.helper(image, sr-1, sc, color, r_color, y_len, x_len)
                self.helper(image, sr+1, sc, color, r_color, y_len, x_len)
                self.helper(image, sr, sc-1, color, r_color, y_len, x_len)
                self.helper(image, sr, sc+1, color, r_color, y_len, x_len)
        return