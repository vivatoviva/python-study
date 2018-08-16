# 【煎蛋网】美女图片
# 【网址】http://jandan.net/ooxx/page-1

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
import os
from hashlib import md5
from pyquery import PyQuery as pq
from urllib.parse import quote
from multiprocessing.pool import Pool


MAX_PAGE = 46 # 总共46页数据

# 初始化浏览器对象
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 10)

# 页面跳转
def index_page(page):
    url = 'http://jandan.net/ooxx/page-' + str(page)
    print('爬取第' + str(page) + "页")

    try:
        browser.get(url)
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".comment-like"))
        )
        get_img()
    except TimeoutError as e:
        index_page(page)
    pass

def get_img():
    html = browser.page_source
    doc = pq("<html>" + html + "</html>")
    items = doc('#wrapper #body #content #comments .commentlist .row img').items()
    for item in items:
        img_url = item.attr('src')
        print('图片url：', img_url)
        save_img(img_url)
    print('当前页面抓取完毕')
    pass


def save_img(url):
    if not os.path.exists('meizi'):
        os.mkdir('meizi')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_path = 'meizi/' + (md5(response.content).hexdigest() + '.jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to save image')

def main(index):
    index_page(index)
    pass

if __name__ == '__main__':
    pool = Pool() # 进程池
    groups = [x for x in range(1, MAX_PAGE)]
    pool.map(main, groups)
    pool.close()
    pool.join()
# 多线程、多进程、异步进行抓取
