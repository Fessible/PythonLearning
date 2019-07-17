from app.libs.httper import HTTP
# 通过这个获取到当前的app
from flask import current_app


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__file_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.get_start_page(page))
        result = HTTP.get(url)
        self.__file_collection(result)

    def get_start_page(self, page):
        # page从0开始
        return (page - 1) * current_app.config['PER_PAGE']

    def __file_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __file_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']
