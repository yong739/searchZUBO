
import time

import concurrent.futures

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import requests

import re

import os

import threading

from queue import Queue

from datetime import datetime

import replace

import fileinput

# 合并自定义频道文件#################################################################################################

file_contents = []

file_paths = ["天津联通.txt", "山西联通.txt","安徽电信.txt", "河南联通.txt", "河南电信.txt", "四川联通.txt", "重庆联通.txt", "重庆电信.txt","山东电信.txt","广东电信.txt","广西电信.txt","江西电信.txt","河北电信.txt","浙江电信.txt","湖南电信.txt","辽宁联通.txt","陕西电信.txt","JIEXI.txt"]  # 替换为实际的文件路径列表

for file_path in file_paths:

    with open(file_path, 'r', encoding="utf-8") as file:

        content = file.read()

        file_contents.append(content)


# 写入合并后的文件

with open("合并.txt", "w", encoding="utf-8") as output:

    output.write('\n'.join(file_contents))


#替换多余的关键字词###################################################################################################

for line in fileinput.input("合并.txt", inplace=True):  #打开文件，并对其进行原地替换

    line = line.replace("CCTV10", "CCTW10")

    line = line.replace("CCTV11", "CCTW11")

    line = line.replace("CCTV12", "CCTW12")

    line = line.replace("CCTV13", "CCTW13")

    line = line.replace("CCTV14", "CCTW14")

    line = line.replace("CCTV15", "CCTW15")

    line = line.replace("CCTV16", "CCTW16")

    line = line.replace("CCTV17", "CCTW17")

    #需要排在前面的频道

    line = line.replace("CCTV1综合", "CCTV1")

    line = line.replace("CCTV2财经", "CCTV2")

    line = line.replace("CCTV3综艺", "CCTV3")

    line = line.replace("CCTV4国际", "CCTV4")

    line = line.replace("CCTV4中文国际", "CCTV4")

    line = line.replace("CCTV4欧洲", "CCTV4")

    line = line.replace("CCTV5体育", "CCTV5")

    line = line.replace("CCTV5+体育", "CCTV5+")

    line = line.replace("CCTV6电影", "CCTV6")

    line = line.replace("CCTV7军事", "CCTV7")

    line = line.replace("CCTV7军农", "CCTV7")

    line = line.replace("CCTV7农业", "CCTV7")

    line = line.replace("CCTV7国防军事", "CCTV7")

    line = line.replace("CCTV8电视剧", "CCTV8")

    line = line.replace("CCTV8纪录", "CCTV9")

    line = line.replace("CCTV9记录", "CCTV9")

    line = line.replace("CCTV9纪录", "CCTV9")

    line = line.replace("CCTV10科教", "CCTV10")

    line = line.replace("CCTV11戏曲", "CCTV11")

    line = line.replace("CCTV12社会与法", "CCTV12")

    line = line.replace("CCTV13新闻", "CCTV13")

    line = line.replace("CCTV新闻", "CCTV13")

    line = line.replace("CCTV14少儿", "CCTV14")

    line = line.replace("央视14少儿", "CCTV14")

    line = line.replace("CCTV少儿超", "CCTV14")

    line = line.replace("CCTV15音乐", "CCTV15")

    line = line.replace("CCTV音乐", "CCTV15")

    line = line.replace("CCTV16奥林匹克", "CCTV16")

    line = line.replace("CCTV17农业农村", "CCTV17")

    line = line.replace("CCTV17军农", "CCTV17")

    line = line.replace("CCTV17农业", "CCTV17")

    line = line.replace("CCTV5+体育赛视", "CCTV5+")

    line = line.replace("CCTV5+赛视", "CCTV5+")

    line = line.replace("CCTV5+体育赛事", "CCTV5+")

    line = line.replace("CCTV5+赛事", "CCTV5+")

    line = line.replace("CCTV5+体育", "CCTV5+")

    line = line.replace("CCTV5赛事", "CCTV5+")



    print(line, end="")  #设置end=""，避免输出多余的换行符



#二次替换某些关键词为便于排序的自定义词####################################################################################################

for line in fileinput.input("合并.txt", inplace=True):  #打开文件，并对其进行原地替换

    
    line = line.replace("CCTV10", "CCTW10")

    line = line.replace("CCTV11", "CCTW11")

    line = line.replace("CCTV12", "CCTW12")

    line = line.replace("CCTV13", "CCTW13")

    line = line.replace("CCTV14", "CCTW14")

    line = line.replace("CCTV15", "CCTW15")

    line = line.replace("CCTV16", "CCTW16")

    line = line.replace("CCTV17", "CCTW17")

 

    print(line, end="")  #设置end=""，避免输出多余的换行符



#对替换完成的文本进行排序#####################################################################################################################



with open('合并.txt', 'r', encoding='utf-8') as f:

    lines = f.readlines()


lines.sort()


with open('排序.txt', 'w', encoding='UTF-8') as f:

    for line in lines:

        f.write(line)


#再次替换自定义词为常规词##########################################################################################################################

for line in fileinput.input("排序.txt", inplace=True):  #打开文件，并对其进行原地替换

    line = line.replace("CCTW10", "CCTV10")

    line = line.replace("CCTW11", "CCTV11")

    line = line.replace("CCTW12", "CCTV12")

    line = line.replace("CCTW13", "CCTV13")

    line = line.replace("CCTW14", "CCTV14")

    line = line.replace("CCTW15", "CCTV15")

    line = line.replace("CCTW16", "CCTV16")

    line = line.replace("CCTW17", "CCTV17")



    print(line, end="")  #设置end=""，避免输出多余的换行符

 ##################################################################################################################################SPLIT#

#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['CCTV','CETV', 'CF', 'IPT淘', 'CHC', 'IWA', '凤凰卫视', '卫视', '金鹰卡通', '纪实科教', '卡酷少儿', '嘉佳卡通', '哈哈炫动', '乐游频道', '动漫秀场', '新动漫','纪实人文', '金色学堂',  '纪实科教', '金鹰纪实', '求索记录']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

if re.search(pattern,line) and line.count(',') == 1: #设置条件为一行只有一个逗号的，排除掉一行中有两个以上逗号的行

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

    with open('排序.txt', 'r', encoding='utf-8') as file, open('T1.txt', 'w', encoding='utf-8') as T1:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T1.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T1.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT1.txt', 'w', encoding='utf-8') as TT1:    #####定义临时文件名

    TT1.write('\n📺中央卫视数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T1.txt', 'r', encoding="utf-8") as input_file, open('TT1.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################

 ##################################################################################################################################SPLIT#

#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['电Y']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T2.txt', 'w', encoding='utf-8') as T2:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T2.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T2.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT2.txt', 'w', encoding='utf-8') as TT2:    #####定义临时文件名

    TT2.write('\n📺电影轮播标清频道,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T2.txt', 'r', encoding="utf-8") as input_file, open('TT2.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################

 ##################################################################################################################################SPLIT#

#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['剧J']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T3.txt', 'w', encoding='utf-8') as T3:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T3.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T3.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT3.txt', 'w', encoding='utf-8') as TT3:    #####定义临时文件名

    TT3.write('\n📺剧集轮播标清频道,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T3.txt', 'r', encoding="utf-8") as input_file, open('TT3.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
    ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['老DY']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T4.txt', 'w', encoding='utf-8') as T4:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T4.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T4.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT4.txt', 'w', encoding='utf-8') as TT4:    #####定义临时文件名

    TT4.write('\n📺老电影黑白频道,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T4.txt', 'r', encoding="utf-8") as input_file, open('TT4.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
    ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['重Q']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T5.txt', 'w', encoding='utf-8') as T5:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T5.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T5.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT5.txt', 'w', encoding='utf-8') as TT5:    #####定义临时文件名

    TT5.write('\n👑重庆数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T5.txt', 'r', encoding="utf-8") as input_file, open('TT5.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
    ##################################################################################################################################SPLIT#
   
   #开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['北J']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T6.txt', 'w', encoding='utf-8') as T6:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T6.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T6.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT6.txt', 'w', encoding='utf-8') as TT6:    #####定义临时文件名

    TT6.write('\n👑北京数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T6.txt', 'r', encoding="utf-8") as input_file, open('TT6.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
    ##################################################################################################################################SPLIT#
   
      #开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['河B']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T7.txt', 'w', encoding='utf-8') as T7:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T7.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T7.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT7.txt', 'w', encoding='utf-8') as TT7:    #####定义临时文件名

    TT7.write('\n👑河北数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T7.txt', 'r', encoding="utf-8") as input_file, open('TT7.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
 ##################################################################################################################################SPLIT#
    
      #开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['河N']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T8.txt', 'w', encoding='utf-8') as T8:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T8.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T8.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT8.txt', 'w', encoding='utf-8') as TT8:    #####定义临时文件名

    TT8.write('\n👑河南数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, int(sort_key))  # 数字从小到大排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T8.txt', 'r', encoding="utf-8") as input_file, open('TT8.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   
 ##################################################################################################################################SPLIT#
      #开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['天J']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T9.txt', 'w', encoding='utf-8') as T9:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T9.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T9.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT9.txt', 'w', encoding='utf-8') as TT9:    #####定义临时文件名

    TT9.write('\n👑天津数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T9.txt', 'r', encoding="utf-8") as input_file, open('TT9.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   
   
 ##################################################################################################################################SPLIT#
      #开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['广D']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T10.txt', 'w', encoding='utf-8') as T10:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T10.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T10.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT10.txt', 'w', encoding='utf-8') as TT10:    #####定义临时文件名

    TT10.write('\n👑广东数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T10.txt', 'r', encoding="utf-8") as input_file, open('TT10.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   
 ##################################################################################################################################SPLIT#
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['广X']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T11.txt', 'w', encoding='utf-8') as T11:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T11.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T11.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT11.txt', 'w', encoding='utf-8') as TT11:    #####定义临时文件名

    TT11.write('\n👑广西数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, int(sort_key))  # 数字从小到大排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T11.txt', 'r', encoding="utf-8") as input_file, open('TT11.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   
 ##################################################################################################################################SPLIT# 
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['湖B']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T12.txt', 'w', encoding='utf-8') as T12:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T12.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T12.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT12.txt', 'w', encoding='utf-8') as TT12:    #####定义临时文件名

    TT12.write('\n👑湖北数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T12.txt', 'r', encoding="utf-8") as input_file, open('TT12.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################

 ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['山D']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T13.txt', 'w', encoding='utf-8') as T13:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T13.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T13.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT13.txt', 'w', encoding='utf-8') as TT13:    #####定义临时文件名

    TT13.write('\n👑山东数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T13.txt', 'r', encoding="utf-8") as input_file, open('TT13.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['安H']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T14.txt', 'w', encoding='utf-8') as T14:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T14.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T14.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT14.txt', 'w', encoding='utf-8') as TT14:    #####定义临时文件名

    TT14.write('\n👑安徽数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, int(sort_key))  # 数字从小到大排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T14.txt', 'r', encoding="utf-8") as input_file, open('TT14.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['江S']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T15.txt', 'w', encoding='utf-8') as T15:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T15.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T15.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT15.txt', 'w', encoding='utf-8') as TT15:    #####定义临时文件名

    TT15.write('\n👑江苏数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T15.txt', 'r', encoding="utf-8") as input_file, open('TT15.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['江X']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T16.txt', 'w', encoding='utf-8') as T16:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T16.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T16.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT16.txt', 'w', encoding='utf-8') as TT16:    #####定义临时文件名

    TT16.write('\n👑江西数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T16.txt', 'r', encoding="utf-8") as input_file, open('TT16.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['山X']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T17.txt', 'w', encoding='utf-8') as T17:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T17.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T17.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT17.txt', 'w', encoding='utf-8') as TT17:    #####定义临时文件名

    TT17.write('\n👑山西数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T17.txt', 'r', encoding="utf-8") as input_file, open('TT17.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
 
 ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['浙J']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T18.txt', 'w', encoding='utf-8') as T18:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T18.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T18.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT18.txt', 'w', encoding='utf-8') as TT18:    #####定义临时文件名

    TT18.write('\n👑浙江数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T18.txt', 'r', encoding="utf-8") as input_file, open('TT18.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['湖N']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T19.txt', 'w', encoding='utf-8') as T19:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T19.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T19.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT19.txt', 'w', encoding='utf-8') as TT19:    #####定义临时文件名

    TT19.write('\n👑湖南数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T19.txt', 'r', encoding="utf-8") as input_file, open('TT19.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['辽L']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T20.txt', 'w', encoding='utf-8') as T20:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T20.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T20.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT20.txt', 'w', encoding='utf-8') as TT20:    #####定义临时文件名

    TT20.write('\n👑辽宁数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, int(sort_key))  # 数字从小到大排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T20.txt', 'r', encoding="utf-8") as input_file, open('TT20.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['吉L']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T21.txt', 'w', encoding='utf-8') as T21:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T21.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T21.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT21.txt', 'w', encoding='utf-8') as TT21:    #####定义临时文件名

    TT21.write('\n👑吉林地方频道,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T21.txt', 'r', encoding="utf-8") as input_file, open('TT21.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['贵Z']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T22.txt', 'w', encoding='utf-8') as T22:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T22.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T22.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT22.txt', 'w', encoding='utf-8') as TT22:    #####定义临时文件名

    TT22.write('\n👑贵州地方频道,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T22.txt', 'r', encoding="utf-8") as input_file, open('TT22.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['陕X']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T23.txt', 'w', encoding='utf-8') as T23:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T23.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T23.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT23.txt', 'w', encoding='utf-8') as TT23:    #####定义临时文件名

    TT23.write('\n👑陕西数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, int(sort_key))  # 数字从小到大排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T23.txt', 'r', encoding="utf-8") as input_file, open('TT23.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
      ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['新J']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T24.txt', 'w', encoding='utf-8') as T24:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T24.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T24.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT24.txt', 'w', encoding='utf-8') as TT24:    #####定义临时文件名

    TT24.write('\n👑新疆数字高清,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T24.txt', 'r', encoding="utf-8") as input_file, open('TT24.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   
         ##################################################################################################################################SPLIT#
   
#开始#########################
#从整理好的文本中按类别进行特定关键词提取#############################################################################################

keywords = ['GAT']  # 需要提取的关键字列表

pattern = '|'.join(keywords)  # 创建正则表达式模式，匹配任意一个关键字

#pattern = r"^(.*?),(?!#genre#)(.*?)$" #以分类直接复制

with open('排序.txt', 'r', encoding='utf-8') as file, open('T25.txt', 'w', encoding='utf-8') as T25:    #####定义临时文件名

    for line in file:

        if re.search(pattern, line):  # 如果行中有任意关键字

         T25.write(line)  # 将该行写入输出文件 #####定义临时文件

for line in fileinput.input("T25.txt", inplace=True):  #打开文件，并对其进行关键词原地替换    

    print(line, end="")  #设置end=""，避免输出多余的换行符          

#新建待合并临时TTxxx.TXT文件并在抬头写入频道编码genre###################
with open('TT25.txt', 'w', encoding='utf-8') as TT25:    #####定义临时文件名

    TT25.write('\n👑中国香港澳门,#genre#\n')        
 
    print(line, end="")  #设置end=""，避免输出多余的换行符 
#写入完成-进入下一步排序######################

#对相同频道IP排序--域名在前###################
import re

# A版本--自定义排序键函数 固定域名--在前
def custom_sort_key(item):
    channel, url = item.split(',')

    channel_letters = ''.join(filter(str.isalpha, channel))
    channel_numbers = ''.join(filter(str.isdigit, channel))

    if channel_numbers.isdigit():
        channel_sort_key = (channel_letters, int(channel_numbers))
    else:
        channel_sort_key = (channel_letters, 0)

    sort_key = re.search(r"http://(.*?)\.", url)
    if sort_key:
        sort_key = sort_key.group(1)
    else:
        sort_key = url

    # 检查sort_key是否为数字
    if sort_key[0].isalpha():
        sort_key = (0, sort_key)  # 字母开头的sort_key排在最前面
    elif sort_key.isdigit():
        sort_key = (1, -int(sort_key))  # 数字从大到小排序
    else:
        sort_key = (2, sort_key)

    return (channel_sort_key, sort_key)

with open('T25.txt', 'r', encoding="utf-8") as input_file, open('TT25.txt', 'a', encoding="utf-8") as output_file:
    # 读取所有行并存储在列表中
    lines = input_file.readlines()

    # 过滤掉空白行
    lines = [line.strip() for line in lines if line.strip()]
    
    sorted_data = sorted(lines, key=custom_sort_key)

    # 将排序后的数据写入输出文件
    for channels in sorted_data: 
        output_file.write(f"{channels}\n")
    sorted_data = sorted(lines, key=custom_sort_key)

   #结束########################################################
   
   ##################################################################################################################################SPLIT#
   
 #合并清理###########

file_contents = []

file_paths = ["TT1.txt", "TT2.txt", "TT3.txt", "TT4.txt", "TT5.txt", "TT6.txt", "TT7.txt", "TT8.txt", "TT9.txt", "TT10.txt", "TT11.txt", "TT12.txt", "TT13.txt", "TT14.txt", "TT15.txt", "TT16.txt", "TT17.txt", "TT18.txt", "TT19.txt", "TT20.txt", "TT21.txt", "TT22.txt", "TT23.txt", "TT24.txt",  "TT25.txt"] 

for file_path in file_paths:

    with open(file_path, 'r', encoding="utf-8") as file:

        content = file.read()

        file_contents.append(content)



# 写入合并后的文件

with open("AMERICAM.txt", "w", encoding="utf-8") as output:

    output.write('\n'.join(file_contents))



os.remove("合并.txt")

os.remove("排序.txt")

os.remove("T1.txt")

os.remove("T2.txt")

os.remove("T3.txt")

os.remove("T4.txt")

os.remove("T5.txt")

os.remove("T6.txt")

os.remove("T7.txt")

os.remove("T8.txt")

os.remove("T9.txt")

os.remove("T10.txt")

os.remove("T11.txt")

os.remove("T12.txt")

os.remove("T13.txt")

os.remove("T14.txt")

os.remove("T15.txt")

os.remove("T16.txt")

os.remove("T17.txt")

os.remove("T18.txt")

os.remove("T19.txt")

os.remove("T20.txt")

os.remove("T21.txt")

os.remove("T22.txt")

os.remove("T23.txt")

os.remove("T24.txt")

os.remove("T25.txt")

os.remove("TT1.txt")

os.remove("TT2.txt")

os.remove("TT3.txt")

os.remove("TT4.txt")

os.remove("TT5.txt")

os.remove("TT6.txt")

os.remove("TT7.txt")

os.remove("TT8.txt")

os.remove("TT9.txt")

os.remove("TT10.txt")

os.remove("TT11.txt")

os.remove("TT12.txt")

os.remove("TT13.txt")

os.remove("TT14.txt")

os.remove("TT15.txt")

os.remove("TT16.txt")

os.remove("TT17.txt")

os.remove("TT18.txt")

os.remove("TT19.txt")

os.remove("TT20.txt")

os.remove("TT21.txt")

os.remove("TT22.txt")

os.remove("TT23.txt")

os.remove("TT24.txt")

os.remove("TT25.txt")

print("任务运行完毕")
