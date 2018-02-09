# D:\python
# encoding=utf-8
print("hello world")
print("hello worldp")
name = 'jack'
age = 30
print("{0} is {1} years old ".format(name, age))
print("{0} is not old".format(age))
score = 0
print("你的分数是：%d" % score)
# 从键盘获取用户的输入
# passwd=input("请输入密码:")
# print("您的密码是%s"%passwd)

name1 = input("请输入您的姓名：")
QQ1 = input("请输入您的QQ号码：")
phone1 = input("请输入您的手机：")
addr1 = input("请输入您的公司地址：")

print("系统正在生成您的名片，请稍候")
print("==========================",
      "姓名：%s" % name1,
      "Q Q：%s" % QQ1,
      "手机：%s" % phone1,
      "地址：%s" % addr1,
      "==========================", sep="\n")

files = open('D:\my_python_trial\myfile.txt', "w")  # "w"
files.write("check this out")
files.close()
