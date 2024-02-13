"""
This view will create endpoints only for calculating
the stats of assets, groups, and portfolio. These
endpoints will not be used for calculating investments
or calculating portfolio template stats during
template creation.
"""

from flask import Blueprint, request, jsonify
from app.algos.calc_portfolio_stats import calculate_portfolio_stats

# Create a Blueprint for the "Stats" API
stats_blueprint = Blueprint('stats', __name__)

# Endpoint to calculate portfolio stats
@stats_blueprint.route('/portfolio_stats', methods=['POST'])
def portfolio_stats():
    # Get the JSON data from the request body
    data = request.json
    
    # Call the function to calculate portfolio stats
    stats_result = calculate_portfolio_stats(data)
    
    # Return the calculated stats as a JSON response
    return jsonify(stats_result)
