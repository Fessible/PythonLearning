import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


# g是一个特殊的对象，独立于每个请求，这样每次调用get_db的时候就不用每次都创建。类似于java中的类变量
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    # 打开文件
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))

# 定义一个init-db命令行，它调用init_db函数
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    # 告诉flask在返回响应后清理的时候调用此函数
    app.teardown_appcontext(close_db)

    # 添加一个新的，能与flask一起工作的命令
    app.cli.add_command(init_db_command)