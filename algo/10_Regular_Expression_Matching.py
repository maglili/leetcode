# 把每個 char 字有沒有 match 的旗標做 and
# e.g. T and F and T and T and F and T
def match(text, pattern):
    print("a")
    if not pattern:
        return not text
    first_match = bool(text) and pattern[0] in {text[0], "."}
    return first_match and match(text[1:], pattern[1:])


def isMatch(self, text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], "."}

    if len(pattern) >= 2 and pattern[1] == "*":
        return self.isMatch(text, pattern[2:]) or (  # s='abc', p='d*abc'
            first_match and self.isMatch(text[1:], pattern)  # s='aaaa', p='a*'
        )

    else:
        return first_match and self.isMatch(text[1:], pattern[1:])


if __name__ == "__main__":

    s = "aaabbb"
    p = "aaabbc"
    print(match(s, p))

    # print(Solution().isMatch(s, p))
