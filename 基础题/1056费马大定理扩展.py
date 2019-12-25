import re
N = int(input())
listA = []
listB = []
#listA用来存放给定整数内对应的整数的3次方
for i in range(N+1):
    listA.append(pow(i,3))
#print(listA)
#print(type(listA[2]))
for a in range(2,N-2):
    for b in range(a+1,N-1):
        for c in range(b+1,N):
            for d in range(c+1,N+1):
                if listA[d] == listA[a] + listA[b] + listA[c]:
                    #print(listA[d],listA[a],listA[b],listA[c])
                    #print(d,a,b,c)
                    listB.append([d,a,b,c])
#print(listB)
listB.sort()
#print(listB)
if listB == []:
    print("OMG")
else:
    for listC in listB:
        listC = str(listC)
        message = re.sub("\[","(",listC)
        message = re.sub("\]",")",message)
        message = re.sub(" ","",message)
        #print(listC)
        print(message)

'''
费马大定理：对于 n>2 ,不存在整数 x,y,z>1 使得 x^n=y^n+z^n满足。
但是对于 n=3的时候，是有可能存在 o,r,s,t>1 ,使得 o^3=r^3+s^3+t^3成立的
(比如 12^3=6^3+8^3+10^3)。
现在给定一个整数N，请列出所有满足条件的 {o,r,s,t}组合，
其中 1<o≤N,1<r<s<t 

暴力题，对于给定的数值N，使用4重循环
先把给定的数值N的3次方全存入列表里，再从列表内操作
最后修改格式
Input：
24
Output：
(6,3,4,5)
(12,6,8,10)
(18,2,12,16)
(18,9,12,15)
(19,3,10,18)
(20,7,14,17)
(24,12,16,20)
'''