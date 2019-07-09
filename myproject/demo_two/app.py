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

    # 在一对多中，一的地方写上关联
    # relationship Users表示与Users模型发生关联
    # backref='role'表示role是User要用的属性
    users = db.relationship('Users', backref='role')

    # 显示一个可读的字符串
    def __repr__(self):
        return '<Role %s  %s>' % (self.name, self.id)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<Users> %s %s' % (self.name, self.role_id)


db.drop_all()
db.create_all()
role = Role(name='Admin')
db.session.add(role)
db.session.commit()

user1 = Users(name='xiaohong', role_id=role.id)
user2 = Users(name='wangxiao', role_id=role.id)
db.session.add(user1)
db.session.add(user2)
db.session.commit()

if __name__ == '__main__':
    # db.drop_all()
    app.run()
