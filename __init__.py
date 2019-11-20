'''全局对象模块'''
import redis
import config
from flask import Flask
from flask_cors import CORS
from pymysql import install_as_MySQLdb
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


install_as_MySQLdb()
serializer = Serializer(secret_key=config.SECRET_KEY, expires_in=14400 * 2)
pool = redis.ConnectionPool(host=config.redis_host, port=config.redis_port, db=config.redis_db, decode_responses=True)
Redis = redis.StrictRedis(connection_pool=pool)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    CORS(app, resources={r"/interface/*": {"origins": "*"}})
    register_blueprint(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    # app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)
    return app


def register_blueprint(app):
    """注册蓝图"""
    from views.v1 import __all__ as all_api
    for api in all_api:
        app.register_blueprint(api)

