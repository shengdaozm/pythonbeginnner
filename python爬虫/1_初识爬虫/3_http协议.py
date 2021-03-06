# http协议
"""
它将信息分成三部分：
    请求：
    * 请求行——请求方式(get/post),请求url地址，协议
    * 请求头——放一些服务器要使用的附加信息
    * 请求题——一般放一些请求参数

    响应：
    * 状态行——协议，状态码
    * 响应头——放一些客户端要使用的一些附加信息
    * 响应体——服务器返回真正用户客户端用的内容(html,json)等
"""
# 我们需要特别重视请求头和响应头，这两个地方一般蕴含着一些比较重要的信息
"""
请求头中：
    1.User-Agent:请求再提的身份标识（用啥发送的请求）
    2.Referer:防盗链（这次的请求是从哪个页面来的？反怕会从会用到）
    3.cookie:本地的字符串数据信息（用户的登陆信息，反爬虫的token）

响应头中：
    1.cookie：本地的字符串数据信息（用户的登陆信息，反爬虫的token）
    2.各种神奇的莫名其妙的字符串（这个需要经验，一般都是token字样，放置各种攻击和反爬）
"""

# 请求方式
"""
GET：显示提交，查询等


POST：隐式提交，更改页面数据，上传数据等

"""