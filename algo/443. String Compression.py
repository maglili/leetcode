class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        w_ptr = 0
        r_ptr = 0
        count = None

        while (r_ptr < len(chars)):
            chars[w_ptr] = chars[r_ptr]
            count = 1

            while (r_ptr + 1 < len(chars) and chars[r_ptr] == chars[r_ptr+1]):
                r_ptr += 1
                count += 1

            if count != 1:
                for char in str(count):
                    chars[w_ptr+1] = char
                    w_ptr += 1

            # update ptr
            w_ptr += 1
            r_ptr += 1

        return w_ptr
