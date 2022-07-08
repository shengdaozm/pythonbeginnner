# 爬虫：通过编写程序来获取互联网的资源
# 需求：用程序模拟浏览器，输入一个网址，从网址后的资源

from urllib.request import urlopen


def test():
    url = "http://www.baidu.com"
    resp = urlopen(url)

    # print(resp.read().decode("utf-8"))
    with open("mybaidu.html", mode="w", encoding="utf-8") as f:
        f.write(resp.read().decode("utf-8"))  #读取到页面的源代码
    print("over!")
    return None


if __name__ == "__main__":
    test()
