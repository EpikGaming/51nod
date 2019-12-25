def solveMeFirst(a,b):
  return a+b

nums = input().split();
print(nums)
num1 = int(nums[0])
num2 = int(nums[1])
res = solveMeFirst(num1,num2)
print (res)

'''
给出2个整数A和B，计算两个数的和。

基础题，input.split()拆分输入数据并使其成为一个数组
Input：
1 2
Output：
3
'''