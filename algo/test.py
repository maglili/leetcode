class Solution:
    def calculate(self, s):
        # Preprocessing: O(n)
        alist = []
        num = ""
        for idx, char in enumerate(s):
            if char.isnumeric():
                num += char
            if (not char.isnumeric()) or ((char.isnumeric()) and (idx == len(s) - 1)):
                if num != "":
                    alist.append(num)
                num = ""
            if (char == "+") or (char == "-") or (char == "(") or (char == ")"):
                alist.append(char)

        # base case
        if "(" not in alist:
            add = True
            val = 0
            last_char = None
            for char in alist:
                if char == "+":
                    add = True
                elif char == "-":
                    add = False
                    if last_char == "-":
                        add = True
                elif char.isnumeric():
                    if add > 0:
                        val += int(char)
                    else:
                        val -= int(char)
                last_char = char
            return val

        # recursive
        else:
            stack = []
            val = 0
            num_list = []
            for idx in range(len(alist[:])):
                if alist[idx] == "(":
                    stack.append(idx)
                elif alist[idx] == ")":
                    start = stack.pop()
                    end = idx
                    val = self.calculate(alist[start + 1 : end])

                    if val < 0:
                        alist[start : end + 1] = ["-", str(val * -1)] + [
                            "" for i in range(len(alist[start : end + 1]) - 2)
                        ]
                    else:
                        alist[start : end + 1] = [str(val)] + [
                            "" for i in range(len(alist[start : end + 1]) - 1)
                        ]

                if stack == [] and ((alist[idx] != "") or (idx + 1 == len(alist))):
                    print("=" * 10)
                    print("alist:", alist)
                    print("idx:", idx)
                    print("alist[idx]:", alist[idx])
                    print("val:", val)
                    print("=" * 10)
                    num_list.append(val)
                    print(num_list)

        return sum(num_list)


if __name__ == "__main__":
    # s = "(6)-(8)-(7)+(1+(6))"
    # s = " 2-1 + 2 "
    s = "2-(5-6)"
    # s = "20+30"
    # s = " 2-1 + 2 "
    # s = "(1+(2+3)+5)"
    # s = " 2-1 + 2 "
    # s = "2147483647"
    # s = "(1+(4+5+2)-3)+(6+8)"

    print("output:", Solution().calculate(s))
