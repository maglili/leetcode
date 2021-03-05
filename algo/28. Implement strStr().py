def strStr(haystack: str, needle: str) -> int:
    if needle =='':
        return 0
    for i in range(len(haystack)-len(needle)+1):
        print(haystack[i:len(needle)+i])
        print(needle)
        print('='*20)
        if haystack[i:len(needle)+i] == needle:
            return i
    return -1

print(strStr('hello','ll'))
