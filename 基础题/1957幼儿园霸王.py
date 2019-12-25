n = int(input())
lista = []
for a in range(n):
    dataname = input().split()
    data = int(dataname[0]) * int(dataname[1]) * int(dataname[2])
    name = dataname[3]
    lista.append([data,name])
#print(lista)
lista.sort()
#print(lista)
print(lista[-1][-1] + " " + lista[0][-1])

'''
幼儿园里面的小朋友在玩橡皮泥，每一个小朋友都有一块橡皮泥。每一块橡皮泥都是一个长方体块。
从橡皮泥的大小可以看出哪一个小朋友是老大，哪一个小朋友是小弟。
拥有橡皮泥体积最大的小朋友总喜欢欺负拥有橡皮泥体积最小的小朋友。
现在给出n个小朋友的橡皮泥，请输出谁欺负了谁。

暴力题，用个二维列表直接存储对应的名字和体积，最后排序直接选择第一个和最后一个的名字即可
Input：
3
10 10 2 J
5 3 10 W
5 5 10 B
Output：
B W
'''