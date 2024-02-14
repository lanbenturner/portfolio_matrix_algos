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





