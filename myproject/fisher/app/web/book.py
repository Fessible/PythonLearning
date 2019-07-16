from flask import jsonify, request

from app.spider.yushu_book import YuShuBook
from app.libs.helper import is_isbn_or_key
# 这里导入的app，执行if __name__时==fisher，所以没有执行run
# from fisher import app

from . import web
from app.web.forms.book import SearchForm


# http://127.0.0.1:5000/book/search/9787501524044/1
@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        is_isbn_or_key(q)
        isb_or_key = 'isbn'
        if isb_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page=page)
        # dict 序列化
        # return json.dumps(result), 200, {'content-type': 'application/json'}
        return jsonify(result)
    return jsonify(form.errors)
