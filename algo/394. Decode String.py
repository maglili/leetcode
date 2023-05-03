class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        ans = ''
        part_str = ''
        times = ''
        for idx, char in enumerate(s):
            if char.isnumeric():
                times += char
                continue
            elif char == '[':
                stack.append((times, part_str))
                part_str = ''
            elif char == ']':
                times, last_park = stack.pop()
                part_str = last_park + int(times) * part_str
                if len(stack) == 0:
                    ans += part_str
                    part_str = ''
            else:
                part_str += char
            times = ''

        ans += part_str
        return ans