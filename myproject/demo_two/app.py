from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 用户名：密码
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flask_sql_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建1个SQLAlichemy实例
db = SQLAlchemy(app)


#
# 创建数据库表
class Role(db.Model):
    # 表名
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


db.create_all()

if __name__ == '__main__':
    # db.drop_all()
    app.run()
