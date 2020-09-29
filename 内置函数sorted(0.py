# _*_coding: UTF-8_*_
# 开发团队: 彭大工程师
# 开发人员: penghong
# 开发时间: 2020/9/29 21:31
# 文件名称: 内置函数sorted(0
# 开发工具: PyCharm

grade=[98,89,56,78,97,86,96,95,94,93,92,99]
grade_as=sorted(grade)
print('升序',grade_as)
grade_ds=sorted(grade,reverse=True)
print('降序',grade_ds)
print('原序列',grade)