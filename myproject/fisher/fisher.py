from flask import Flask, make_response
from helper import is_isbn_or_key

app = Flask(__name__)
# import config
# 也可以使用from_object(config)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    is_isbn_or_key(q)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0')
