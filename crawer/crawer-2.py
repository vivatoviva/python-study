# from urllib import request

# Request = request.Request('http://www.baidu.com')

# response = request.urlopen(Request)

# print(response.read().decode('utf-8'))


# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError

# username = 'username'
# password = 'password'
# url = 'http://localhost:5000/'

# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)

# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


# import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

# from urllib import request,error

# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers)


# from urllib.robotparser import RobotFileParser
# from urllib.request import urlopen

# rp = RobotFileParser(url="http://www.jianshu.com/robots.txt")
# # rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
# print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))

# import requests
# import re

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }

# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

# import requests

# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# session 对象

import requests
s  = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)