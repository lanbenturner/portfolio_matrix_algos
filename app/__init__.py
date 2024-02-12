"""
This module is where you can reference all url prefixes
"""

from flask import Flask
from .api.views.views_stats import stats_blueprint
from .api.views.views_invest import invest_blueprint

def create_app():
    app = Flask(__name__)

    # Register the "Stats" blueprint
    app.register_blueprint(stats_blueprint, url_prefix='/stats')

    # Register the "Invest" blueprint
    app.register_blueprint(invest_blueprint, url_prefix='/invest')

    return app
