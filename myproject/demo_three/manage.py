from app import app
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from exts import db

manager = Manager(app)

migrate = Migrate(app, db)

# 添加命令
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()
