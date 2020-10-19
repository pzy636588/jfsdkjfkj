# _*_coding: UTF-8_*_
# 开发团队: 彭大工程师
# 开发人员: penghong
# 开发时间: 2020/10/19 21:30
# 文件名称: 格式化字符串
# 开发工具: PyCharm

#格式化输出
template='编号：%09d\t公司名称： %s \t官网：http://www.%s.com'        #定义模板
context1=(7,'百度','baidu')                                        #定义转换的内容1
context2=(8,'明日学院','mingrisoft')                                #定义转换的内容2
print(template%context1)                                           #格式化输出1
print(template%context2)                                           #格式化输出2


#使用字符串对象的format()方法
template='编号：%09d\t公司名称： %s \t官网：http://www.%s.com'        #定义模板
context1=template.format(7,'百度','baidu')                                #定义转换的内容1
context2=template.format(8,'明日学院','mingrsoft')                             #定义转换的内容2
print(context1)                                           #格式化输出1
print(context2)                                           #格式化输出2

