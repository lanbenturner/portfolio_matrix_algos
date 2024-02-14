"""
This function takes the input data and returns a modified version of it.
 For testing purposes, let's just add 10 to each equity value.
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
    # Extract equity values from the assets in portfolio_data
    equities = [asset['equity'] for asset in data.get('assets', [])]

    # Calculate Portfolio Weighting
    portfolio_weighting = []
    for equity in equities:
        if portfolio_equity_rounded != 0:  # Avoid division by zero
            asset_weighting = (equity / portfolio_equity_rounded) * 100
        else:
            asset_weighting = 0  # Set weighting to 0 if portfolio equity is 0
        asset_weighting = round(asset_weighting, 2)  # Round to 2 decimal places
        portfolio_weighting.append(asset_weighting)

    return portfolio_weighting








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