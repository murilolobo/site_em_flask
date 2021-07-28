from flask import Flask
from site_em_flask.ext import configuration


def create_app():
    app = Flask(__name__)
    app.run(debug=True)
    configuration.init_app(app)
    configuration.load_extensions(app)
    return app

