# -*- coding:utf-8 -*-
# @FileName  :1_re模块.py
# @Time      :2022/7/9 15:55
# @Author    :shengdao

import re


def main():
    # findall ：匹配字符串中所有符合正则的内容
    lst = re.findall(r"\d+", "我的电话号码是：10086,我朋友的电话号码是：10010")
    print(lst)

    # finditer:匹配字符串中所有内容的[返回的是迭代器]
    it = re.finditer(r"\d+", "我的电话号码是：10086,我朋友的电话号码是：10010")
    for i in it:
        print(i.group())

    # search返回的结果是match对象，那数据需要.group()，但是找到了一个结果就会返回值
    s = re.search(r"\d+", "我的电话号码是：10086,我朋友的电话号码是：10010")
    print(s.group())

    # match从头开始匹配，如果从头开始匹配就不匹配的话，就不会在进行匹配了
    s = re.match(r"\d+", "10086,我朋友的电话号码是：10010")
    print(s.group())

    # 预加载正则表达式
    obj=re.compile(r"\d+")
    ret=obj.finditer("我的电话号码是：10086,我朋友的电话号码是：10010")
    print(ret)
    return None

def test():
    #(?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
    # 答应分组的名字即可

    s="""
    <div class='jay'><span id='1'>郭麒麟</span></div>
    <div class='jj'><span id='2'>宋轶</span></div>
    <div class='jolin'><span id='3'>大聪明</span></div>
    <div class='sylar'><span id='4'>范思哲</span></div>
    <div class='tory'><span id='5'>胡说八道</span></div>
    """

    # re.S 使得.能够匹配换行符
    obj=re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<lst>.*?)</span></div>",re.S)
    ret=obj.finditer(s)
    for it in ret:
        print(it.group("lst")+" "+it.group("id"))
    return None

if __name__ == "__main__":
    #main()
    test()
