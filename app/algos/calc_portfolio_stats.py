"""
This module calculates all of the portfolio stats. It is called
in the app/api/views/views_stats.py module at this endpoing:
http://127.0.0.1:5000/stats/portfolio_stats
"""


def calculate_portfolio_equity(data):
    # Extract asset data from the input JSON
    assets = data.get('assets', [])

    # Calculate Portfolio Equity
    portfolio_equity = sum(asset.get('equity', 0) for asset in assets)

    # Round the Portfolio Equity to the nearest dollar
    portfolio_equity_rounded = round(portfolio_equity)

    # Return the calculated Portfolio Equity
    return {'portfolio_equity': portfolio_equity_rounded}


def calculate_group_equity(data):
    # Initialize a dictionary to store group equity
    group_equity = {}

    # Iterate through the list of assets
    for asset in data.get('assets', []):
        # Get the group assignment of the current asset
        group_assignment = asset.get('group_assignment')

        # Get the equity of the current asset
        equity = asset.get('equity')

        # Check if the group assignment already exists in the group_equity dictionary
        if group_assignment in group_equity:
            # If the group assignment exists, add the equity of the current asset to the existing sum
            group_equity[group_assignment] += equity
        else:
            # If the group assignment doesn't exist, initialize it with the equity of the current asset
            group_equity[group_assignment] = equity

    return group_equity


def calculate_portfolio_weighting(data, portfolio_equity_rounded):
    # Extract asset data from the input JSON
    assets = data.get('assets', [])

    # Initialize list to store asset weightings as tuples
    asset_weightings = []

    # Calculate Portfolio Weighting for each asset
    for asset in assets:
        equity = asset.get('equity', 0)
        symbol = asset.get('symbol')
        
        if portfolio_equity_rounded != 0:  # Avoid division by zero
            asset_weighting = round((equity / portfolio_equity_rounded) * 100, 2)
        else:
            asset_weighting = 0  # Set weighting to 0 if portfolio equity is 0
        
        # Store asset weighting as a tuple (symbol, weighting)
        asset_weightings.append((symbol, asset_weighting))

    return asset_weightings


def calculate_group_weighting(data, group_equity):
    # Initialize a dictionary to store group weightings
    group_weighting = {}

    # Iterate through the list of assets
    for asset in data.get('assets', []):
        # Get the group assignment of the current asset
        group_assignment = asset.get('group_assignment')

        # Get the equity of the current asset
        equity = asset.get('equity')

        # Calculate the group weighting for the current asset
        if group_assignment in group_equity:
            group_equity_for_group = group_equity[group_assignment]
            if group_equity_for_group != 0:
                asset_weighting = round((equity / group_equity_for_group) * 100, 2)
            else:
                asset_weighting = 0  # Set weighting to 0 if group equity is 0
        else:
            asset_weighting = 0  # Set weighting to 0 if group assignment not found

        # Update the group_weighting dictionary with the asset's weighting
        if group_assignment in group_weighting:
            group_weighting[group_assignment].append(asset_weighting)
        else:
            group_weighting[group_assignment] = [asset_weighting]

    return group_weighting


