# D:\python
# encoding=utf-8


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

#定义关键词
key_word_entity = 'entity'
key_word_end_entity = 'end entity'
key_word_generic = 'generic'
header = ("=" * 15 + "\n2018 new year" + "\nCOPYRIGHT@SNAPS\n" + "=" * 15 + '\n')
default_choice = 'def'
#定义寻找模块entity的pattern
entity_header_pattern = re.compile(key_word_entity + '(.*?)' + key_word_end_entity, re.S)

#定义函数
def generate_instance(module_name):
    files = open('D:\my_python_trial\{}.txt'.format(module_name), "r")  # "r"
    all_content = files.read()
    files1 = open('D:\my_python_trial\{}.txt'.format(module_name+'1'),"w")  # "w"
    instance_name = input('例化名称?')#输入准确模块名称
    files1.write(header +instance_name+':'+key_word_entity+'\n'.join(entity_header_pattern.findall(all_content)) + key_word_end_entity)#模块中找出entity并加入header
    files1.close()

    with open('D:\my_python_trial\{}.txt'.format(module_name+'1'),'r') as new_base:
        new_base_lines = new_base.readlines()
        new_base_lines[-2]=new_base_lines[-2].replace(')',')end')#找出entity倒数第二行做标记便于后面处理
    with open('D:\my_python_trial\{}.txt'.format(module_name+'_instance'),'w') as files2:
       for line in new_base_lines:
           if key_word_entity not in line:
             line = re.sub(':','=>',line,1)
           if key_word_generic in line:
             line = line.replace(key_word_generic,key_word_generic+'\b'+'map')
           if 'port' in line:
             line = line.replace('port','port'+'\b'+'map')
           if '=>'in line:
             lable = line.split('=>')[0]
             lable_stripped = lable.strip()
             instant_signal_name=input("例化信号名?({})".format(lable_stripped))#输入例化信号名
             if instant_signal_name == default_choice:#可以选择默认值即被例化的模块信号名
                instant_signal_name = lable_stripped
             else:
                instant_signal_name = instant_signal_name
             if ')end'in line:
                line  = lable+'=>'+instant_signal_name+');\n'#之前的倒数第二行，应是被例化后的最后一行，需要加‘：’
             elif ')'in line:
                line  = lable+'=>'+instant_signal_name+')\n'
             else:
                line  = lable+'=>'+instant_signal_name+',\n'
           if key_word_end_entity not in line:
             files2.write(line)

    files.close()
    files1.close()
    files2.close()
    return files2
module_name1 = input('需要例化的模块名：')
generate_instance(module_name1)