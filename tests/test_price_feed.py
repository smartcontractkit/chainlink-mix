import pytest
from brownie import PriceFeed


def test_transfer(accounts):
    price_feed = PriceFeed.deploy({'from': accounts[0]})
    value = price_feed.getLatestPrice({'from': accounts[0]})
    assert isinstance(value, int)
