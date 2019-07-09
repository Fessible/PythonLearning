from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

# 关闭自动跟踪修改
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flask_books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '6868767dhjhj'

# 创建数据库连接
db = SQLAlchemy(app)

'''
1.配置数据库
    创建数据库表对象
    创建数据库 create database flask_books;

'''


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # 关联关系
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return 'Author {} {} '.format(self.name, self.id)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(16), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return 'Book {} {} {}'.format(self.id, self.name, self.author_id)


db.drop_all()
db.create_all()

# 生成数据
au1 = Author(name='老王')
au2 = Author(name='老惠')
au3 = Author(name='老刘')

# 把数据库提交给用户会话
db.session.add_all([au1, au2, au3])
# 提交会话
db.session.commit()
bk1 = Book(name='老王回忆录', author_id=au1.id)
bk2 = Book(name='我读书少别嘌我', author_id=au1.id)
bk3 = Book(name='如何此按钮变强', author_id=au2.id)
bk4 = Book(name='怎要更优秀', author_id=au3.id)
bk5 = Book(name='如何睡觉', author_id=au3.id)
db.session.add_all([bk1, bk2, bk3, bk4, bk5])
# 提交会话
db.session.commit()


# 自定义表单类
class AuthorForm(FlaskForm):
    author = StringField('作者', validators=[DataRequired()])
    book = StringField('书籍', validators=[DataRequired()])
    submit = SubmitField('提交')


@app.route('/', methods=['POST', 'GET'])
def index():
    # 自定义表单类
    author_form = AuthorForm()
    authors = Author.query.all()

    '''
    验证逻辑
        1.调用wtf的函数验证实现
        2.验证通过，获取数据源
        3.判断作者是否存在
        4.如果作者存在，判断书籍是否存在，没有重复书籍就添加，如果重复就提示错误
        5.如果作者不存在就添加书籍
        6.验证不通过就提示错误    
    '''

    if request.method == 'POST':
        #  判断参数是否为空
        if author_form.validate_on_submit():

            # 获取数据
            author_name = author_form.author.data
            book_name = author_form.book.data

            # 从数据库中获取数据
            author = Author.query.filter_by(name=author_name).first()

            # 如果作者存在
            if author:
                # 判断书籍是否存在
                book = Book.query.filter_by(name=book_name).first()
                if book:
                    flash('已存在同名书籍')
                else:
                    try:
                        new_book = Book(name=book_name, author_id=author.id)
                        db.session.add(new_book)
                        db.session.commit()

                        return redirect(url_for('index'))

                    except Exception as e:
                        print(e)
                        flash('添加书籍失败')
                        db.session.rollback()

            else:
                try:
                    # 添加作者，然后添加书籍
                    new_author = Author(name=author_name)
                    db.session.add(new_author)
                    db.session.commit()
                    # 添加书籍
                    new_book = Book(name=book_name, author_id=new_author.id)
                    db.session.add(new_book)
                    db.session.commit()
                    return redirect(url_for('index'))
                except Exception as e:
                    print(e)
                    flash('添加作者和书籍失败')
                    db.session.rollback()
        else:
            flash('参数为空')

    return render_template('books.html', authors=authors, form=author_form)


# 删除书籍——》网页中删除-》点击需要发送书籍的id给删除数据的路由-》路由接收参数
@app.route('/delete_book/<book_id>')
def delete(book_id):
    # 查询数据库中是否有该书
    book = Book.query.get(book_id)

    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除数据出错')
            db.session.rollback()

    else:
        flash('书籍找不到')

    # 返回到当前网址-》重定向
    return redirect(url_for('index'))


@app.route('/delete_author/<author_id>')
# 删除作者,需要删除书和作者
def delete_author(author_id):
    author = Author.query.get(author_id)
    if author:
        try:
            # 直接把书删除
            Book.query.filter_by(author_id=author_id).delete()
            # 删除作者
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除作者失败')
            db.session.rollback()
    else:
        flash('作者不存在')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
