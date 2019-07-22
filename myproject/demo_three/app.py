from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from sqlalchemy import or_

import config
from exts import db
from models import User, Question, Answer
from decorator import login_request

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    context = {
        'questions': Question.query.all()
    }
    return render_template('index.html', **context)


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        phone = request.form.get('phone')
        password = request.form.get('password')
        user = User.query.filter(User.phone == phone).first()
        if user and user.check_password(raw_password=password):
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            flash('用户名或密码错误')

    return render_template('login.html')


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        phone = request.form.get('phone')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        user = User.query.filter(User.phone == phone).first()
        if user:
            flash('该手机号码已经被注册')
        else:
            if password != password2:
                flash("两次密码不相等，请重新输入")
            else:
                user = User(phone=phone, username=username, password=password)
                print(phone, password, username)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/question', methods=['POST', 'GET'])
@login_request
def question():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content, author_id=g.user_id)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('question.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/detail/<question_id>')
def detail(question_id):
    question = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question)


@app.route('/add_answer', methods=['POST'])
@login_request
def add_answer():
    content = request.form.get('answer_content')
    question_id = request.form.get('question_id')

    # user_id = session['user_id']

    answer = Answer(text_content=content)
    answer.author_id = g.user_id
    answer.question_id = question_id

    # answer.author = User.query.filter(User.id == user_id).first()
    # answer.question = Question.query.filter(Question.id == question_id).first()

    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


@app.route('/search')
def search():
    q = request.args.get('q')
    # title或content中包含
    questions = Question.query.filter(or_(Question.title.contains(q), Question.content.contains(q)))
    return render_template('index.html', questions=questions)


# 执行在请求之前
@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        g.user_id = user_id


# before_request --》视图函数-》context_processor(),所以我们使用全局g
@app.context_processor
def context_processor():
    # user_id = session.get('user_id')
    if hasattr(g, 'user_id'):
        user_id = g.user_id
        if user_id:
            user = User.query.filter(User.id == user_id).first()
            if user:
                return {'user': user}
    return {}

if __name__ == '__main__':
    app.run()
