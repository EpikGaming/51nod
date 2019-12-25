'''def LDR(str1,str2):
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    elif str1 == str2:
        return 0


    if str1[len(str1) - 1] == str2[len(str2) - 1]:
        d = 0
    else:
        d = 1

    return min(LDR(str1,str2[:-1]) + 1,
               LDR(str1[:-1],str2) + 1,
               LDR(str1[:-1],str2[:-1]) + d)

str1 = input()
str2 = input()
print(LDR(str1,str2))
'''

import time
def LDR(str1,str2):
    matrix = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1,len(str1) +1):
        for j in range(1,len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                d = 0
            else:
                d = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1,matrix[i][j - 1] + 1,matrix[i - 1][j - 1] + d)
    return matrix[len(str1)][len(str2)]


time_begin = time.time()
str1 = input()
str2 = input()
print(LDR(str1,str2))
time_end = time.time()
print('time:',time_end - time_begin)