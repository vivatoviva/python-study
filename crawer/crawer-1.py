# 北京小猪房
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq


import requests

# 构造请求头部
headers = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}

urls = []

# 获取子页面url
def getUrl():
    index = 0 # 当前页数
    response = requests.get('http://www.jy510.com/index.php?m=esf&c=info&same=2&etype=1&page={}'.format(index), headers = headers)
    # 处理最大页数
    soup = BeautifulSoup(response.text, 'lxml')
    maxPage = soup.select('.pages > span')
    maxIndex = int(maxPage[0].get_text()[1:-3])
    while index < 10:
        response = requests.get('http://www.jy510.com/index.php?m=esf&c=info&same=2&etype=1&page={}'.format(index), headers = headers)
        soup = BeautifulSoup(response.text, 'lxml')
        index = index + 1
        # 处理跳转链接
        links = soup.select('div.houseItem a')
        for link in links:
            urls.append(link.get('href'))

# 处理一个页面
def getData(url):
    response = requests.get('http://www.jy510.com/' + url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        price = soup.select('.house-tit span em')[0].get_text()
        pay = soup.select('.detail-pay span em')[0].get_text()
    except BaseException as e:
        return  '价格：' + '未知' + "万元 单价：" + '未知' + "\n"
    else: 
        return '价格：' + price + "万元 单价：" + price + "\n"


if __name__ == '__main__':
    getUrl()
    str = ''
    for url in urls:
        str = str + getData(url)
        print(str)
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write(str)
