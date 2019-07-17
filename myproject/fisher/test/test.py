from flask import Flask, current_app

app = Flask(__name__)

# 应用上下文 对象Flask
# 请求上下文 对象Request
# Flask AppContext
# Request RequestContext
# 离线应用，单元测试需要我们自己去创建上下文。而在实际场景中，Flask会自动创建上下文


# ctx = app.app_context()
# ctx.push()
#
# a = current_app
# d = current_app.config['DEBUG']
#
# ctx.pop()

# with app.app_context():
#     a = current_app
#     d = current_app.config['DEBUG']


class MyResource:
    def __enter__(self):
        print('connect to resource ')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('close resource')

    def query_resource(self):
        print('resource query')


with MyResource() as resource:
    resource.query_resource()
