from flask import Blueprint

# 蓝图
web = Blueprint('web', __name__)

from app.web import book
