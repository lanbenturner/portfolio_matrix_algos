"""
This view will create endpoints only for calculating
investments. This will require portfolio stats to
already be calculated and have the user provide
their investment amount.
"""

from flask import Blueprint, request, jsonify

# Create a Blueprint for the "Invest" API
invest_blueprint = Blueprint('invest', __name__)

# Endpoint to calculate investments
@invest_blueprint.route('/calculate_investments', methods=['GET'])
def calculate_investments():
    # Implement your logic here to calculate portfolio investments
    # For example:
    investments_data = {'stocks': 5000, 'bonds': 3000}
    return jsonify(investments_data)
