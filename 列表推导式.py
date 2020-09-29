# _*_coding: UTF-8_*_
# 开发团队: 彭大工程师
# 开发人员: penghong
# 开发时间: 2020/9/29 21:36
# 文件名称: 列表推导式
# 开发工具: PyCharm
import random
randomnumber=[random.randint(12,1000)for i in range(20)]
print('生成的随机数',randomnumber)


#价格打折
price=[789,346,568,33456,66789,3456,5678]
sale=[int(c*0.6)for c in price]
print('打折后的价格',sale)

