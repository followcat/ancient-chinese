# coding:utf-8
from flask import Flask
from tools.flask_wxapp import WXApp


wxapp = WXApp()

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    wxapp.init_app(app)

    from api.api_1 import blueprint as api_1_blueprint
    app.register_blueprint(api_1_blueprint, url_prefix='/api/v1')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8002)
