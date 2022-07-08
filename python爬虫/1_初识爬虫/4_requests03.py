import requests

def main():
    url="https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"

    #重新封装参数
    param={
        "type": "24",
        "interval_id": "100:90",
        "action":"" ,
        "start": "0",
        "limit": "20",
    }

    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    resp=requests.get(url,params=param,headers=headers)
    print(resp.request.url)
    print(resp.json())
    resp.close()


if __name__=="__main__":
    main()

"""
当我们被反爬的时候，第一个考虑的就是User-Agent
"""