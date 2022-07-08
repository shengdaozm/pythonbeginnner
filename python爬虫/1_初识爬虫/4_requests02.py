# 百度翻译反爬好像加强了。。
import requests

def main():
    url="http://fanyi.baidu.com/sug"

    s=input("输入你要翻译的英语单词:\n")
    print(s)
    dat={
        "kw":s,
    }
    #发送post请求
    resp=requests.post(url,data=dat)
    print(resp.text)
    print(resp.json)
if __name__=="__main__":
    main()