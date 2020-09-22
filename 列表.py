# _*_coding: UTF-8_*_
# 开发团队: 彭大工程师
# 开发人员: penghong
# 开发时间: 2020/9/22 21:33
# 文件名称: 列表
# 开发工具: PyCharm

num=[4,6,7,8,9,34,65,7]
print(list(range(10,50,2)))
del num                      #删除列表常用操作用del

#遍历列表
team=['英国','法国','俄罗斯','日本']
for item in team:
    print(item)

for index,item in enumerate(team):    #使用for循环和enmerate()函数可以输出索引值和元素内容
    print(index+1,item)

team2=[1,3,5,6,7,8,0]
team.append('韩国')
print(team)
team2.extend(team)       #添加一个元素到另外一个列表中用extend()
print(team2)
del team2[0]              #删掉列表或元素用del
print(team2)
team2.remove('俄罗斯')            #删掉不知道的内容用remove
print(team2)