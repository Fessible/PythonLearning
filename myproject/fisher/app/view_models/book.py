# api视图
class BookViewModel:

    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages'] or ''
        self.price = book['price'] or ''
        self.author = '、'.join(book['author'])
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.isbn = book['isbn']

    # 用属性访问的方式来调用函数
    @property
    def intro(self):
        # 希望输出 author/publisher/price 或者 author/price的格式
        # if self.publisher:
        #     pass
        # if self.price:
        #     pass
        intros = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return '/'.join(intros)



class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


