import requests

# 在地址栏里面的一定是get的方式
def main():
    #url="https://cn.bing.com/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6"
    query=input("输入一个你喜欢的明星：\n")
    url=f"https://www.sogou.com/web?query={query}"
    dic = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    resp=requests.get(url,headers=dic) #处理一个小小的反爬

    print(resp)
    print(resp.text) #拿到页面的源代码


if __name__=="__main__":
    main()