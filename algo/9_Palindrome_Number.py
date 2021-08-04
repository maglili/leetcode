def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x >= 0 and str(x) == str(x)[::-1]:
        return True
    else:
        return False
    # if x < 0:
    #     return False
    #
    # ranger = 1
    # while x / ranger >= 10:
    #     ranger *= 10
    #
    # while x:
    #     left = x // ranger
    #     print(left)
    #     right = x % 10
    #     print(right)
    #     if left != right:
    #         return False
    #
    #     x = (x % ranger) // 10
    #     ranger /= 100
    #
    # return True
print(isPalindrome(123454321))
