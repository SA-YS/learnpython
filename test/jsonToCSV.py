# -*- coding:utf-8 -*-
import urllib.request
import csv
import json
import sys
import re


# 所有的url
def get_all_url():
    addr = "http://carprice.58.com/comm/city.json?parentid="
    url_list = ['http://carprice.58.com/comm/province.json']
    # url_list = []
    for i in range(1, 33):
        if i == 26:
            continue
        url_list.append(addr+str(i))
    url_list.append(addr+str(832))
    url_list.append(addr+str(833))
    url_list.append(addr+str(834))
    print(url_list)
    return url_list


# 获取数据
def get_row_data(url):
    if url.__contains__('='):
        id = url.split('=')[1]
    else:
        id = 0
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    data = data[1: -1]
    # print(data, "\n", type(data))
    # print(list, type(list))
    return data, id


# 转换
def trans(data, path):
    p = re.compile(r'{.+?}')
    jsonData = p.findall(data[0])
    csvfile = open(path+'.csv', 'a', newline='')
    writer = csv.writer(csvfile)
    if data[1] == 0:
        for head in jsonData:  # 获取属性列表
            # print(head, type(head))
            dic = json.loads(head)
            keys = dic.keys()
            writer.writerow(keys)  # 将属性列表写入csv中
            break
    for line in jsonData:  # 读取json数据的每一行，将values数据一次一行的写入csv中
        dic = json.loads(line)
        dic['ourparam'] = data[1]  # 将错误的ourparam(parentId)替换
        writer.writerow(dic.values())
    csvfile.close()


if __name__ == '__main__':
    # path=str(sys.argv[1])#获取path参数
    file_path = "d:/csv/city"
    all_url = get_all_url()
    for url in all_url:
        raw_data = get_row_data(url)
        trans(raw_data, file_path)
