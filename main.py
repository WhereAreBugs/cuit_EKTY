import requests
import qrcode
import time

# 登陆地址: http://ekty.cuit.edu.cn/#/pages/home/login
# 登录API: http://ekty.cuit.edu.cn/api/login?sf_request_type=ajax

# head: 请求头
# OPTIONS /api/login?sf_request_type=ajax HTTP/1.1
# Accept: */*
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
# Access-Control-Request-Headers: content-type,sdp-app-session
# Access-Control-Request-Method: POST
# Host: ekt-cuit-edu-cn.webvpn.cuit.edu.cn:8118
# Origin: http://ekty-cuit-edu-cn.webvpn.cuit.edu.cn:8118
# Proxy-Connection: keep-alive
# Referer: http://ekty-cuit-edu-cn.webvpn.cuit.edu.cn:8118/
# Sec-Fetch-Mode: cors
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54

# playload: 请求体
# {
#   "account": "",
#   "password": ""
# }

# 当前暂未实现自动化获取二维码,先完成一个手动的版本

prefix = "http://ekty-cuit-edu-cn.webvpn.cuit.edu.cn:8118/#/pages/activity/studentQdqt?id="
id = input("请输入活动ID: ")
now_time = int(round(time.time() * 1000))
now_time += 14400000  # 获取两小时之后的时间
url = prefix + id + "&timestamp=" + str(now_time)
print("签到链接: " + url)
print("有效期" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time/1000)))
img = qrcode.make(url)
print("二维码已生成,请在当前目录下查看(qrcode.png)")
img.save("qrcode.png")
