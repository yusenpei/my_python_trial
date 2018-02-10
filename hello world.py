# D:\python
# encoding=utf-8

import time
import re

# print("hello world")
# print("hello worldp")
# name = 'jack'
# age = 30
# print("{0} is {1} years old ".format(name, age))
# print("{0} is not old".format(age))
# score = 0
# print("你的分数是：%d" % score)
# 从键盘获取用户的输入
# passwd=input("请输入密码:")
# print("您的密码是%s"%passwd)

# name1 = input("请输入您的姓名：")
# QQ1 = input("请输入您的QQ号码：")
# phone1 = input("请输入您的手机：")
# addr1 = input("请输入您的公司地址：")
#
# print("系统正在生成您的名片，请稍候")
# time.sleep(3)
# print("==========================",
#       "姓名：%s" % name1,
#       "Q Q：%s" % QQ1,
#       "手机：%s" % phone1,
#       "地址：%s" % addr1,
#       "==========================", sep="\n")
#
# files = open('D:\my_python_trial\myfile.txt', "w")  # "w"
# files.write("lets do this")
# files.close()

# with open('D:\my_python_trial\myfile.txt', 'r') as f:
#     files_context = f.read()

# files1 = open('D:\my_python_trial\myfile1.txt', "w")  # "w"
# files1.write("data from the other file = %s"%files_context)
# files1.close()
# my_type = type('this type')
# print("type is %s"% my_type)
# b=100
# b += 1
# print("%d"%b)
key_word_entity = 'entity'
key_word_end_entity = 'end entity'
files = open('D:\my_python_trial\myfile.txt', "r")  # "r"
all_content = files.read()
entity_header_pattern = re.compile(key_word_entity+'(.*?)'+key_word_end_entity,re.S)
# entity_header = entity_header_pattern.findall(all_content,text)
print("entity_header")
files1 = open('D:\my_python_trial\myfile1.txt', "w")  # "w"
files1.write('\n'.join(entity_header_pattern.findall(all_content)))
files1.write()

files.close()
files1.close()


