"""
The purpose of this module is to list common
variables, functions, and classes that are required
for each individual algorithm.
"""


class Asset:
    def __init__(self, symbol, equity, weighting):
        self.symbol = symbol
        self.equity = equity
        self.weighting = weighting


class AssetGroup:
    def __init__(self, name, equity, weighting, assets):
        self.name = name
        self.equity = equity
        self.weighting = weighting
        self.assets = assets


class Portfolio:
    def __init__(self, equity, weighting, asset_groups):
        self.equity = equity
        self.weighting = weighting
        self.asset_groups = asset_groups
