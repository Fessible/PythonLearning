from flask import Blueprint

# 蓝图
web = Blueprint('web', __name__)

from app.web import book, auth, drift, gift, main, wish


@web.context_processor
def context_processor():
    return {'current_user': 'zhangsan'}
