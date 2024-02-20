"""
This view will create endpoints only for calculating
the stats of assets, groups, and portfolio. These
endpoints will not be used for calculating investments
or calculating portfolio template stats during portfolio
template creation.
"""

from flask import Blueprint, request, jsonify, current_app as app, abort
from functools import wraps
import os
from app.algos.calc_portfolio_stats import (
    calculate_portfolio_equity,
    calculate_portfolio_weighting,
    calculate_group_equity,
    calculate_group_weighting,
    calculate_group_portfolio_weighting,
)

# Assuming your secret token is stored in an environment variable named SECRET_TOKEN
SECRET_TOKEN = os.environ.get('SECRET_TOKEN', 'default_secret_token')

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get token from request headers
        token = request.headers.get('Authorization')
        
        # Check if token is valid
        if not token or token != SECRET_TOKEN:
            app.logger.error('Unauthorized access attempt.')
            abort(401, description="Unauthorized: Invalid or missing token.")
        
        return f(*args, **kwargs)
    return decorated_function

# Create a Blueprint for the "Stats" API
stats_blueprint = Blueprint("stats", __name__)

@stats_blueprint.route("/portfolio_stats", methods=["POST"])
@token_required
def portfolio_stats():
    app.logger.info(f'Received request for /portfolio_stats')

    try:
        # Directly use the JSON data from the request as the list of assets
        assets = request.json  # This is now a list of assets directly

        # Call the functions from algos to calculate portfolio stats
        portfolio_equity = calculate_portfolio_equity(assets)
        portfolio_weighting_result = calculate_portfolio_weighting(assets, portfolio_equity)
        group_equity_result = calculate_group_equity(assets)
        group_weighting_result = calculate_group_weighting(assets, group_equity_result)
        group_portfolio_weighting_result = calculate_group_portfolio_weighting(
            portfolio_equity, group_equity_result
        )

        # Construct the formatted response JSON object
        response = {
            "portfolio": [{"portfolio_equity": portfolio_equity}],
            "asset": [
                {
                    "symbol": asset["symbol"],
                    "equity": asset["equity"],
                    "group_assignment": asset["group_assignment"],
                    "portfolio_weighting": next(
                        (
                            weight
                            for symbol, weight in portfolio_weighting_result
                            if symbol == asset["symbol"]
                        ),
                        None,
                    ),
                    "group_weighting": group_weighting_result.get(
                        asset["group_assignment"], {}
                    ).get(asset["symbol"], 0),
                }
                for asset in assets  # Iterate directly over the provided list
            ],
            "asset_group": [
                {
                    "group_name": group,
                    "group_equity": equity,
                    "group_portfolio_weighting": group_portfolio_weighting_result[group],
                }
                for group, equity in group_equity_result.items()
            ],
        }

        app.logger.info(f'Successfully processed /portfolio_stats request')
        return jsonify(response)

    except Exception as e:
        app.logger.error(f'Failed to process /portfolio_stats request: {str(e)}', exc_info=True)
        return jsonify({'error': 'An error occurred processing the portfolio stats'}), 500
