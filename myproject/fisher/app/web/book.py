"""
 Created by 七月 on 2018-2-1.
"""
from flask import request, current_app, render_template, flash

from app.forms.book import SearchForm

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection, BookViewModel
from . import web

__author__ = '七月'


@web.route('/book/search')
def search():
    """
        q :普通关键字 isbn
        page
        ?q=金庸&page=1
    """

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


# 书籍信息
@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    # 使用isbn进行搜索，然后将数据显示到详情页面
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    # book = BookViewModel(yushu_book.first())
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


@web.route('/test')
def test():
    r = {
        'name': None,
        'age': 18
    }
    # data['age']
    r1 = {

    }
    flash('hello,qiyue', category='error')
    flash('hello, jiuyue', category='warning')
    # 模板 html
    return render_template('test.html', data=r, data1=r1)


@web.route('/test1')
def test1():
    print(id(current_app))
    from flask import request
    # from app.libs.none_local import n
    # print(n.v)
    # n.v = 2
    # print('-----------------')
    # print(getattr(request, 'v', None))
    # setattr(request, 'v', 2)
    # print('-----------------')
    return ''
