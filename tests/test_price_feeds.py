import pytest
from brownie import PriceFeed, accounts, network


def test_can_get_latest_price(get_eth_usd_price_feed_address, get_account):
    # Arrange
    address = get_eth_usd_price_feed_address
    # Act
    price_feed = PriceFeed.deploy(address, {'from': get_account})
    # Assert
    value = price_feed.getLatestPrice({'from': get_account})
    assert isinstance(value, int)
    assert value > 0
