# _*_coding: UTF-8_*_
# 开发团队: 彭大工程师
# 开发人员: penghong
# 开发时间: 2020/10/8 21:17
# 文件名称: 元组推导式
# 开发工具: PyCharm


import random
randomnumber=(random.randint(10,100)for i in range(10))
randomnumber=tuple(randomnumber)
print('生成的元组为',randomnumber)

number=(i for i in range(10))
print(number.__next__())
print(number.__next__())
print(number.__next__())
print('转换前',number)
number=tuple(number)
print('转换后',number)


number=(i for i in range(7))
for i in number:
    print(i,end='')
print(tuple(number))

