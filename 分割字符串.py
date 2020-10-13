# _*_coding: UTF-8_*_
# 开发团队: 彭大工程师
# 开发人员: penghong
# 开发时间: 2020/10/12 21:37
# 文件名称: 分割字符串
# 开发工具: PyCharm


str1='明 日 学 院 官 网  >>> www.mingrisoft.com'
print('原字符串',str1)
list1=str1.split()
list2=str1.split('>>>')
list3=str1.split('.')
list4=str1.split(' ',4)
print(str(list1)+'\n'+str(list2)+'\n'+str(list3)+'\n'+str(list4)+'\n')
list5=str1.split('>')
print(list5)


