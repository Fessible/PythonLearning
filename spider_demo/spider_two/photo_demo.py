# 使用多线程获取图片

import requests
from lxml import etree
import os
import re
from urllib import request
from queue import Queue
import threading

# 一个用来解析页面，一个用来下载图片

base_url = 'https://www.doutula.com/article/list/?page=%d'


class Producer(threading.Thread):
    headers = {
        'User_agent': 'Mozilla/5.0 '
                      '(Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.img_queue = img_queue
        self.page_queue = page_queue

    def parse_page(self, url, directory):
        response = requests.get(url)
        text = response.text
        element = etree.HTML(text)
        images = element.xpath("//div[@class='col-sm-9 center-wrap']//img[@class!='gif']")
        for img in images:
            # print(etree.tostring(img,encoding='utf-8').decode('utf-8'))
            image_url = img.get('data-original')

            # 过滤掉特殊字符串
            name = img.get('alt')
            regex = "[`~!@#$%^&*()+=|{}':;',\\[\\].<>/?~！@#￥%……&*（）——+|{}【】‘；：”“’。，、？\\s]"
            name = re.sub(regex, '', name)

            # 获取后缀名
            suffix = os.path.splitext(image_url)[1]
            file_name = directory + name + suffix

            self.img_queue.put((image_url, file_name))

    def run(self):
        while True:
            if self.page_queue.empty():
                break

            url, directory = self.page_queue.get()
            self.parse_page(url, directory)


class Consumer(threading.Thread):

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    # 下载图片
    def run(self):
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                break
            image_url, file_name = self.img_queue.get()
            request.urlretrieve(image_url, file_name, )
            print(image_url, file_name)


def main():
    page_queue = Queue(1000)
    img_queue = Queue(1000)

    for i in range(1, 101):
        url = base_url % i
        directory = 'images/page%d/' % i
        if not os.path.exists(directory):
            os.makedirs(directory)
        page_queue.put((url, directory))

    for i in range(5):
        t1 = Producer(page_queue, img_queue)
        t1.start()
        t2 = Consumer(page_queue, img_queue)
        t2.start()


if __name__ == '__main__':
    main()
