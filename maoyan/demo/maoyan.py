import requests
from lxml import etree


def getOnePage(page):
    url = f'https://maoyan.com/board/4?offset={page}'

    # 告诉服务器我们是浏览器
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

    r = requests.get(url, headers=header)

    return r.text


# 提取数据

def parse(text):
    html = etree.HTML(text)

    title = html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
    release_time = html.xpath('//p[@class="releasetime"]/text()')

    for name, time in zip(title, release_time):
        print(name, time)



text = getOnePage(10)
# print(text)
parse(text)


# # 保存数据
# def saveFile():
