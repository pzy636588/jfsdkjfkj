# _*_coding: UTF-8_*_
# 开发团队: 彭大工程师
# 开发人员: penghong
# 开发时间: 2020/10/12 21:29
# 文件名称: 截取字符串
# 开发工具: PyCharm

str2='人生苦短，我用python!'
sub1=str2[1]
sub2=str2[2:5]
sub3=str2[:5]                   #从左边开始截取5个字符
sub4=str2[5:]                   #从第6个字符截取
print('原字符串',str2)
print(sub1+'\n'+sub2+'\n'+sub3+'\n'+sub4+'\n')

try:
    sub1=str2[15]
except IndexError:
    print('指定的索引不存在')