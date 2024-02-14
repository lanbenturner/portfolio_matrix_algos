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

    # Initialize dictionary to store asset weightings
    asset_weightings = {}

    # Calculate Portfolio Weighting for each asset
    for asset in assets:
        equity = asset.get('equity', 0)
        symbol = asset.get('symbol')
        
        if portfolio_equity_rounded != 0:  # Avoid division by zero
            asset_weighting = round((equity / portfolio_equity_rounded) * 100, 2)
        else:
            asset_weighting = 0  # Set weighting to 0 if portfolio equity is 0
        
        # Store asset weighting in the dictionary
        asset_weightings[symbol] = asset_weighting

    return asset_weightings









"""
Test JSON:
<COPY STARTING AT BRACKET BELOW>
{
    "assets": [
        {
            "symbol": "AAPL",
            "equity": 5000,
            "group_assignment": "Group1"
        },
        {
            "symbol": "GOOGL",
            "equity": 3000,
            "group_assignment": "Group1"
        },
        {
            "symbol": "MSFT",
            "equity": 4000,
            "group_assignment": "Group2"
        },
        {
            "symbol": "AMZN",
            "equity": 6000,
            "group_assignment": "Group2"
        },
        {
            "symbol": "FB",
            "equity": 3500,
            "group_assignment": "Group3"
        },
        {
            "symbol": "TSLA",
            "equity": 4500,
            "group_assignment": "Group3"
        },
        {
            "symbol": "NVDA",
            "equity": 2000,
            "group_assignment": "Group1"
        },
        {
            "symbol": "JPM",
            "equity": 3800,
            "group_assignment": "Group2"
        },
        {
            "symbol": "NFLX",
            "equity": 4200,
            "group_assignment": "Group3"
        },
        {
            "symbol": "V",
            "equity": 3500,
            "group_assignment": "Group1"
        }
    ]
}
<COPY UNTIL BRACKET ABOVE>
"""