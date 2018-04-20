# coding:utf-8
import datetime
from flask import Flask

from flask_login import LoginManager, UserMixin
from flask_mongoengine import MongoEngine

from tools.flask_wxapp import WXApp


wxapp = WXApp()

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    db = MongoEngine(app)
    wxapp.init_app(app)

    class User(db.Document, UserMixin):
        meta = {'collection': 'user'}
        active = db.BooleanField(default=True)

        # User authentication information
        user_wxid = db.StringField(default='')

        # User information
        play_count = db.IntField(default=0)
        word_count = db.IntField(default=0)
        today_point = db.IntField(default=0)
        total_point = db.IntField(default=0)
        login_time = db.DateTimeField(default=datetime.datetime.utcnow)

    user_manager = LoginManager()
    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(pk=user_id).first()

    from api.api_1 import blueprint as api_1_blueprint
    app.register_blueprint(api_1_blueprint, url_prefix='/api/v1')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8002)
