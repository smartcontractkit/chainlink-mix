from brownie import PriceFeedConsumer
from scripts.helpful_scripts import get_account


def test_can_get_latest_price(get_eth_usd_price_feed_address):
    # Arrange
    address = get_eth_usd_price_feed_address
    # Act
    price_feed = PriceFeedConsumer.deploy(address, {"from": get_account()})
    # Assert
    value = price_feed.getLatestPrice({"from": get_account()})
    assert isinstance(value, int)
    assert value > 0
