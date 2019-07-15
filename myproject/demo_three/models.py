from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(11), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    password = db.Column(db.String(125), nullable=False)

    def __init__(self, *args, **kwargs):
        username = kwargs.get('username')
        phone = kwargs.get('phone')
        password = kwargs.get('password')

        self.username = username
        self.password = generate_password_hash(password)
        self.phone = phone

    # 密码加salt
    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(11), nullable=False)
    content = db.Column(db.Text, nullable=False)

    create_time = db.Column(db.DateTime, default=datetime.now)
    # table的名字
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    author = db.relationship('User', backref=db.backref('questions'))


class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    text_content = db.Column(db.Text, nullable=False)

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    create_time = db.Column(db.DateTime, default=datetime.now)

    question = db.relationship('Question', backref=db.backref('answers'), order_by=create_time.desc())
    author = db.relationship('User', backref=db.backref('answers'))
