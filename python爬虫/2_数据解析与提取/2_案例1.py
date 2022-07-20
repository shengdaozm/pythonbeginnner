# -*- coding:utf-8 -*-
# @FileName  :2_案例1.py
# @Time      :2022/7/9 16:19
# @Author    :shengdao

# 首先拿到页面的源代码
# 通过re提取到有效的信息
import re
import requests
import csv


# 出现打印源码为空的时候，就要考虑是不是headers的问题
def main(a):
    url = "https://movie.douban.com/top250?start=" + ('%d' % a) + "&filter="
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    page_content = resp.text  # 拿到页面的源代码

    # 解析数据
    # 正则式的书写
    obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>'
                     r'(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">'
                     r'(?P<num>.*?)</span>.*?<span>(?P<people>.*?)</span>', re.S)
    # 开始匹配
    result = obj.finditer(page_content)
    # for it in result:
    #     print(it.group("name") + " " + it.group("year").strip() + " " + it.group("num") + " " + it.group("people"))
    # # 写入文件
    f = open("data.csv", 'a+', newline='', encoding='utf-8')
    csvwriter = csv.writer(f)
    for it in result:
        dic = it.groupdict()  # 处理成字典的格式
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
        print(dic.values())
    f.close()
    resp.close()
    return None


if __name__ == "__main__":
    num = 0
    while num <= 225:
        main(num)
        num += 25
