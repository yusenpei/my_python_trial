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
key_word_entity = '   entity'
key_word_end_entity = 'end entity'
key_word_generic = 'generic'
header =("="*15+"\n2018 new year"+"\nCOPYRIGHT@SNAPS\n"+"="*15+'\n')
files = open('D:\my_python_trial\myfile.txt', "r")  # "r"
all_content = files.read()
entity_header_pattern  = re.compile(key_word_entity+'(.*?)'+key_word_end_entity,re.S)
entity_arrow_pattern   = re.compile('=>'+'(.*?)'+';',re.S)
# entity_header = entity_header_pattern.findall(all_content,text)
# print("entity_header")
files1 = open('D:\my_python_trial\myfile1.txt', "w")  # "w"
files1.write(header +key_word_entity+'\n'.join(entity_header_pattern.findall(all_content)) + key_word_end_entity)
files1.close()

with open('D:\my_python_trial\myfile1.txt','r') as new_base:
    new_base_lines = new_base.readlines()
with open('D:\my_python_trial\myfile2.txt','w') as files2:
   for line in new_base_lines:
       line = re.sub(':','=>',line,1)
       if key_word_generic in line:
         line = line.replace(key_word_generic,key_word_generic+'\b'+'map')
       if 'port' in line:
         line = line.replace('port','port'+'\b'+'map')
       if '=>'in line:
         lable = line.split('=>')[0]
         lable1 = lable.strip()
         line  = lable+'=>'+lable1+',\n'
       if key_word_end_entity not in line:
         files2.write(line)
       # files2.write(line)
    line[2] = line[2].replace(',')




# print(try_s)
# list0 = try_s[1]
# list1 = try_s[2]
# list2 = try_s[3]
# list3 = try_s[4]
# print(list0)
# print(list1)
# print(list2)
# print(list3)
# files1.write(header +key_word_entity+'\n'.join(entity_header_pattern.findall(all_content)) + key_word_end_entity)

files.close()
files1.close()
files2.close()

