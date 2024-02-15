"""
This view will create endpoints only for calculating
the stats of assets, groups, and portfolio. These
endpoints will not be used for calculating investments
or calculating portfolio template stats during portfolio
template creation.
"""

from flask import Blueprint, request, jsonify
from app.algos.calc_portfolio_stats import (
    calculate_portfolio_equity,
    calculate_portfolio_weighting,
    calculate_group_equity,
    calculate_group_weighting,
    calculate_group_portfolio_weighting
)

# Create a Blueprint for the "Stats" API
stats_blueprint = Blueprint('stats', __name__)

# Endpoint to calculate portfolio stats
@stats_blueprint.route('/portfolio_stats', methods=['POST'])
def portfolio_stats():
    # Get the JSON data from the request body
    data = request.json
    
    # Call the functions from algos to calculate portfolio stats
    portfolio_equity = calculate_portfolio_equity(data)
    portfolio_weighting_result = calculate_portfolio_weighting(data, portfolio_equity)
    group_equity_result = calculate_group_equity(data)
    group_weighting_result = calculate_group_weighting(data, group_equity_result)
    group_portfolio_weighting_result = calculate_group_portfolio_weighting(portfolio_equity, group_equity_result)
    
    # Construct the formatted response JSON object
    response = {
        "portfolio": [
            {"portfolio_equity": portfolio_equity}
        ],
        "asset": [
            {
                "symbol": asset['symbol'],
                "equity": asset['equity'],
                "group_assignment": asset['group_assignment'],
                "portfolio_weighting": next((weight for symbol, weight in portfolio_weighting_result if symbol == asset['symbol']), None),
                "group_weighting": group_weighting_result.get(asset['group_assignment'], {}).get(asset['symbol'], 0),
            } for asset in data.get('assets', [])
        ],
        "asset_group": [
            {
                "group_name": group,
                "group_equity": equity,
                "group_portfolio_weighting": group_portfolio_weighting_result[group],
            } for group, equity in group_equity_result.items()
        ]
    }
    
    # Return the formatted stats as a JSON response
    return jsonify(response)
