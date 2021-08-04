class Solution:
    def calculate(self, s):
        num = 0
        total = 0
        stack = []
        sign = 1
        for char in s:
            if char.isnumeric():
                num = 10 * num + int(char)

            elif char in "+-":
                total += num * sign
                num = 0
                sign = 1 if char == "+" else -1
            elif char in "*/":
                stack.append(num * sign)
                stack.append(char)
                print(stack)
                sign = 1
                num = 0
        return total + num * sign


if __name__ == "__main__":
    # s = "   -20*5+10*5+10*5"
    # s = " 3+5 / 2 "
    # s = "3/4"
    # s = "3+2*2"
    # s = "2*3 - 4/2"
    s = "9/10"
    # s = "1*2-3/4+5*6-7*8+9/10"
    print("output:", Solution().calculate(s))
