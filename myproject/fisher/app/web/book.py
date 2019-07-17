import json

from flask import jsonify, request

from app.spider.yushu_book import YuShuBook
from app.libs.helper import is_isbn_or_key
# 这里导入的app，执行if __name__时==fisher，所以没有执行run
# from fisher import app

from . import web
from app.web.forms.book import SearchForm
from app.view_models.book import BookCollection


# http://127.0.0.1:5000/book/search/9787501524044/1
@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        is_isbn_or_key(q)
        yushu_book = YuShuBook()

        isb_or_key = 'isbn'
        if isb_or_key == 'isbn':
            yushu_book.search_by_isbn(q)

        else:

            yushu_book.search_by_keyword(q, page)
            # 原来返回的数据是 book:{'total':1,}的json数据格式
            # result = YuShuBook.search_by_keyword(q, page=page)
            # result = BookViewModel.package_collection(result, q)

        # dict 序列化
        # return json.dumps(result), 200, {'content-type': 'application/json'}
        # return jsonify(result)
        books.fill(yushu_book, q)
        # books是一个对象，所以要讲books转化成dict
        return json.dumps(books, default=lambda o: o.__dict__)
    return jsonify(form.errors)
