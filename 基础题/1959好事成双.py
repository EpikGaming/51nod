a = input().split()
b = [int(i) for i in a]
del b[-1]
#c = [i * 2 for i in b]
d = [i / 2 for i in b]
x = 0
for i in d:
    if i in b:
        #print(i)
        x += 1
print(x)

'''
中国人办喜事讲究好事成双，现在定义“好事成双”对：如果两个数字a,b，只要a=2b或者b=2a成立，那么就说这两个数字是“好事成双”对。
现在给出一个数组，请计算一下里面有多少“好事成双”对。
样例解释：
1 4 3 2 9 7 18 22
这儿总共有3对：2和1，4和2，18和9。

暴力题，算基础题，直接将数值存入列表A
复制列表并把列表中的值除2得列表B
看列表B中有多少个元素与列表A内元素相等
注意题目中最后一个数值为0表示结束，需要将0删去
Input：
1 4 3 2 9 7 18 22
Output：
3
'''