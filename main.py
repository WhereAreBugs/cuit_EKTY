import requests
import qrcode
import time

# 登陆地址: http://ekty.cuit.edu.cn/#/pages/home/login
# 登录API: http://ekty.cuit.edu.cn/api/login?sf_request_type=ajax

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
