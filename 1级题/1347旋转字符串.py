def Judge(S):
    if len(S) % 2 == 1:
        return False
    else:
        lengh = len(S)
        half = lengh // 2
        if S[:half] == S[half:]:
            return True
    return False
s = str(input())
if Judge(s):
    print("YES")
else:
    print("NO")