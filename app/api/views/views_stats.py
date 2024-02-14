"""
This view will create endpoints only for calculating
the stats of assets, groups, and portfolio. These
endpoints will not be used for calculating investments
or calculating portfolio template stats during
template creation.
"""

from flask import Blueprint, request, jsonify
from app.algos.calc_portfolio_stats import calculate_portfolio_equity, calculate_portfolio_weighting

# Create a Blueprint for the "Stats" API
stats_blueprint = Blueprint('stats', __name__)

# Endpoint to calculate portfolio stats
@stats_blueprint.route('/portfolio_stats', methods=['POST'])
def portfolio_stats():
    # Get the JSON data from the request body
    data = request.json
    
    # Call the functions from algos to calculate portfolio stats
    portfolio_equity_result = calculate_portfolio_equity(data)
    portfolio_weighting_result = calculate_portfolio_weighting(data, portfolio_equity_result['portfolio_equity'])
    
    # Construct the response JSON object
    response = {
        'portfolio_equity': portfolio_equity_result['portfolio_equity'],
        'portfolio_weighting': portfolio_weighting_result
    }
    
    # Return the calculated stats as a JSON response
    return jsonify(response)

