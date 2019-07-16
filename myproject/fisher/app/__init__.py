# 初始化数据


from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    # import config
    # 也可以使用from_object(config)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    # 注册蓝图
    register_blueprint(app)

    # 数据库初始化
    db.init_app(app)
    db.create_all(app=app)

    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
