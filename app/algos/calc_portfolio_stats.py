def calculate_portfolio_stats(data):
    """
    This function takes the input data and returns a modified version of it.
    For testing purposes, let's just add 10 to each equity value.
    """
    modified_data = []

    for asset in data:
        # Assuming each asset is represented as a dictionary with 'equity' key
        asset['equity'] += 10
        modified_data.append(asset)

    return modified_data
