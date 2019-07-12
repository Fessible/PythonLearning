# 多对多
from flask import Flask
import config
# from flask_sqlalchemy import SQLAlchemy
from exts import db
from models import Article, Tag

app = Flask(__name__)
app.config.from_object(config)

# db = SQLAlchemy(app)

db.init_app(app)

# db.drop_all()
# with app.app_context():
#     db.drop_all()
#     db.create_all()
#
#     article = Article(title="aaa")
#     article2 = Article(title="bbb")
#
#     tag1 = Tag(name='tag1')
#     tag2 = Tag(name='tag2')
#
#     article.tags.append(tag1)
#     article.tags.append(tag2)
#
#     article2.tags.append(tag2)
#
#     db.session.add(article)
#     db.session.add(article2)
#     db.session.add(tag1)
#     db.session.add(tag2)
#
#     db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
