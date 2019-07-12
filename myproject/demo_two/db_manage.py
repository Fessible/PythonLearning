from flask_script import Manager

dbManager = Manager()


@dbManager.command
def init():
    print("数据库初始化成功！！")


@dbManager.command
def migrate():
    print("数据库迁移成功！！！")
