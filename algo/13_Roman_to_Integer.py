def romanToInt(s: str) -> int:
    # count=0
    # s = 'o'+s
    # for idx,symbol in enumerate(s):
    #     if symbol == 'o':
    #         continue
    #     elif symbol == 'I':
    #         count += 1
    #     elif symbol == 'V' and s[idx-1] == 'I':
    #         count += 3
    #     elif symbol == 'X' and s[idx-1] == 'I':
    #         count += 8
    #     elif symbol == 'V':
    #         count += 5
    #     elif symbol == 'X':
    #         count += 10
    #     elif symbol == 'L' and s[idx-1] == 'X':
    #         count += 30
    #     elif symbol == 'C' and s[idx-1] == 'X':
    #         count += 80
    #     elif symbol == 'L':
    #         count += 50
    #     elif symbol == 'C':
    #         count += 100
    #     elif symbol == 'D' and s[idx-1] == 'C':
    #         count += 300
    #     elif symbol == 'M' and s[idx-1] == 'C':
    #         count += 800
    #     elif symbol == 'D':
    #         count += 500
    #     elif symbol == "M":
    #         count += 1000
    d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    res, p = 0, 'I'
    for c in s[::-1]:
        if d[c] < d[p]:
            res, p = res - d[c], c
        else:
            res, p = res + d[c], c

    return res

print(romanToInt('IX'))
