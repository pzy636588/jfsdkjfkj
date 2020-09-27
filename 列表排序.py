# _*_coding: UTF-8_*_
# 开发团队: 彭大工程师
# 开发人员: penghong
# 开发时间: 2020/9/27 21:57
# 文件名称: 列表排序
# 开发工具: PyCharm
#1  sort使用列表的对象
grade=[56,45,67,89,67,88.34,57,97]
print('源列表',grade)
grade.sort()
print('升序',grade)
grade.sort(reverse=True)
print('降序',grade)

# 2 对字符串排序
char=['cat','Tom','Angela','pet']
char.sort()
print('区分大小写',char)
char.sort(key=str.lower)
print('不区分大小写',char)

