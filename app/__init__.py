from flask import Flask
from .api.views.views_stats import stats_blueprint
from .api.views.views_invest import invest_blueprint
import os

# Assuming config.py is in the root directory, adjust the import path as necessary
from config import DevelopmentConfig, ProductionConfig

def create_app(config_name=None):
    app = Flask(__name__)

    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'DevelopmentConfig')

    if config_name == 'ProductionConfig':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    # Register the blueprints
    app.register_blueprint(stats_blueprint, url_prefix='/stats')
    app.register_blueprint(invest_blueprint, url_prefix='/invest')

    return app
