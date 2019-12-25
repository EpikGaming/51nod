def manacher(str):
    s = '#' + '#'.join(str) + '#'
    mx = 0
    listP = [0] * len(s)
    id = 0
    for i in range(len(s)):
        if mx > i:
            listP[i] = min(mx - i,listP[2 * id - i])
        if mx <= i:
            listP[i] = 1
        while i - listP[i] >= 0 and i + listP[i] < len(s) and s[i - listP[i]] == s[i + listP[i]]:
            listP[i] += 1
        if listP[i] + i - 1 > mx:
            id = i
            mx = listP[i] + i - 1
    return listP[-1] - 1
str = input()
print(manacher(str))

'''
输入一个字符串Str，输出Str里最长回文子串的长度。
回文串：指aba、abba、cccbccc、aaaa这种左右对称的字符串。
串的子串：一个串的子串指此（字符）串中连续的一部分字符构成的子（字符）串
例如 abc 这个串的子串：空串、a、b、c、ab、ac、bc、abc

字符串问题，普通匹配复杂度为o(n^3)，中心扩展复杂度为o(n^2)，manachar算法复杂度为o(n)
'''

def manachar(str):
    s = '#' + '#'.join(str) + '#'
    mx = 0
    listP = [0] * len(s)
    id = 0
    for i in range(len(s)):
        if mx > i:
            listP[i] = listP[2 * id - i]
        if mx <= i:
            listP[i] = 1
        while i - listP[i] >= 0 and i + listP[i] < len(s) and s[i - listP[i]] == s[i + listP[i]]:
            listP[i] += 1
        if listP[i] + i - 1 > mx:
            id = i
            mx = listP[i] + i - 1
    listP.sort()
    return listP[-1] - 1
str = input()
print(manachar(str))