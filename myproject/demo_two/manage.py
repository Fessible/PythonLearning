from flask_script import Manager
from script_demo import app
from db_manage import dbManager
from exts import db
import config
from models import Article

from flask_migrate import MigrateCommand, Migrate

manager = Manager(app)

# 数据库
app.config.from_object(config)
db.init_app(app)

# 要使用flask-migrate 就要绑定app和db
migrate = Migrate(app, db)

# 把migrate的命令添加到manage中
manager.add_command('db', MigrateCommand)


# init 初始化环境
# migrate  模型-—>迁移文件
# upgrade  表


@manager.command
def runserver():
    print('服务器跑起来了！！！')


# 取别名
# manager.add_command('db', dbManager)

if __name__ == '__main__':
    manager.run()
