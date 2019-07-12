from flask import Flask, session
import os
import datetime

app = Flask(__name__)
# 24位字符串
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = datetime.timedelta(days=7)
# app.config['DEBUG'] = True


@app.route('/')
def index():
    session['username'] = 'zhangsan'
    session.permanent = True
    return 'Hello !!!!'


# 获取session
# session['username']/session.get('username')
@app.route('/get')
def get():
    return session.get('username')


# 删除这个字段的session
@app.route('/delete')
def delete():
    session.pop('username')
    print(session.get('username'))
    return 'success'


# 完全清除
@app.route('/clear')
def clear():
    session.clear()
    print(session.get('username'))
    return 'success'


if __name__ == '__main__':
    app.run()
