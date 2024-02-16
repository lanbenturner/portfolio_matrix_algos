from flask import Flask
from .api.views.views_stats import stats_blueprint
from .api.views.views_invest import invest_blueprint
import os
import logging
from logging.handlers import RotatingFileHandler

# Assuming config.py is in the root directory, 
# adjust the import path as necessary
from config import DevelopmentConfig, ProductionConfig

def create_app(config_name=None):
    app = Flask(__name__)

    if config_name is None:
        config_name = os.getenv("FLASK_CONFIG", "DevelopmentConfig")

    if config_name == "ProductionConfig":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    # Register the blueprints
    app.register_blueprint(stats_blueprint, url_prefix="/stats")
    app.register_blueprint(invest_blueprint, url_prefix="/invest")

    # Logging setup for production environment
    if not app.debug and not app.testing:
        # Set log level
        log_level = logging.INFO

        # Ensure the directory for log files exists
        if not os.path.exists('logs'):
            os.mkdir('logs')

        # Set up log file rotation
        file_handler = RotatingFileHandler('logs/portfoliomatrixapis.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(log_level)

        # Add the file handler to the app's logger
        app.logger.addHandler(file_handler)
        app.logger.setLevel(log_level)
        app.logger.info('YourApp startup')

    return app
