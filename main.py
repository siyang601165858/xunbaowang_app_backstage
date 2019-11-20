from flask import jsonify, current_app
from init import create_app, Redis
from plugins.public.error import ViewException


app = create_app()


@app.route('/')
def hello_world():
    return 'Hello World!!!'


@app.route('/500/')
def hello_world_500():
    pass


@app.before_first_request
def before_first_request():
    """应用初始化"""


@app.errorhandler(ViewException)
def view_error(error):
    """视图错误"""
    return jsonify(error.info)


if __name__ == '__main__':
    app.run(port=9003, debug=True)