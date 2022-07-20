# -*- coding:utf-8 -*-
# @FileName  :3_案例2.py
# @Time      :2022/7/20 23:02
# @Author    :shengdao

# 1.定位2022必须看的片
# 2.从2022中提取到子页面的链接
# 3.请求子页面的链接地址，拿到下载地址

import re
import requests


def main():
    url = "https://www.dy2018.com/"
    resp = requests.get(url)  # verify=False
    resp.encoding = 'gb2312'

    obj1 = re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
    result1=obj1.finditer(resp.text)
    str=""
    for it in result1:
        str+=it.group("ul")
    print(str)
    obj2=re.compile(r"<li><a href='(?P<urls>.*?).*?《(>P<name>.*?)》",re.S)
    result2=obj2.finditer(str)
    for it in result2:
        print(it.group("urls")+"  "+it.group("name"))
    resp.close()
    return None


if __name__ == "__main__":
    main()
