from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS here
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
    CORS(app)  # Enable CORS for the app, add this line

    if config_name is None:
        config_name = os.getenv("FLASK_CONFIG", "DevelopmentConfig")

    if config_name == "ProductionConfig":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    # Register the blueprints
    app.register_blueprint(stats_blueprint, url_prefix="/stats")
    app.register_blueprint(invest_blueprint, url_prefix="/invest")

    # Health check endpoint
    @app.route("/health", methods=["GET"])
    def health_check():
        # Simply return a 200 OK response indicating the app is online
        return jsonify(message="Portfolio Matrix python back-end is online and functioning correctly"), 200

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
        app.logger.info('Portfolio Matrix API startup')

    # Generic error handler
    @app.errorhandler(Exception)
    def handle_exception(e):
        # Log the error details
        app.logger.error(f'An error occurred: {str(e)}', exc_info=True)

        # Return a generic error response
        return jsonify({'error': 'An internal server error occurred'}), 500
    
    # Security headers
    @app.after_request
    def add_security_headers(response):
        response.headers["Content-Security-Policy"] = "default-src 'self';"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response

    return app
