# _*_coding: UTF-8_*_
# 开发团队: 彭大工程师
# 开发人员: penghong
# 开发时间: 2020/10/9 21:49
# 文件名称: 千年虫
# 开发工具: PyCharm


year=[89,98,00,75,68,37,58,90]                  #原有的年份列表
for index,value in enumerate(year):             #遍历列表元素索引与年份
    if str(value)!='0':                         #判断非0年份
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))       #判断2000年
    year.sort()          #reverse=True 降序排列                      #升序排列年份列表
    print(year)


#本周运动周报
thisweek=[4235,1011,8447,9566,9788,8951,9808]
print('(1)本周运动周报:',thisweek)

#上周运动周报
lastweek=[4235,5612,8447,11250,9211,9985,3782]
print('(1)上周运动周报:',lastweek)

#汇总
sumweek=[]
for i,h in zip(thisweek,lastweek):
    sum=i+h
    sumweek.append(sum)
print('(3)汇总结果：',sumweek)
sumweek.sort()
print('升序',sumweek)
sumweek.sort(reverse=True)
print('降序',sumweek)

day=['周日','周一','周二','周三','周四','周五','周六',]
print('星期统计',day)
x=thisweek.index(max(thisweek))
y=thisweek.index(min(thisweek))
day.insert(x+1,max(thisweek))
day.insert(y+1,min(thisweek))
print('(5)',day)