"""
This view will create endpoints only for calculating
the stats of assets, groups, and portfolio. These
endpoints will not be used for calculating investments
or calculating portfolio template stats during
template creation.
"""

from flask import Blueprint, request, jsonify


# Create a Blueprint for the "Stats" API
stats_blueprint = Blueprint('stats', __name__)

# Endpoint to calculate stats
@stats_blueprint.route('/calculate_stats', methods=['GET'])
def calculate_stats():
    # Implement your logic here to calculate portfolio stats
    # For example:
    stats_data = {'return': 0.05, 'risk': 0.03}
    return jsonify(stats_data)


# Endpoint to calculate stats
@stats_blueprint.route('/portfolio_stats', methods=['POST'])
def portfolio_stats():
    #Get the JSON data from the request body
    data = request.json
    return jsonify(data)