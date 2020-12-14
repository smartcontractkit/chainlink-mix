import pytest
from brownie import PriceFeed, accounts, network


def test_can_deploy_contract(mainnet_eth_usd_address):
    # Arrange
    if network.show_active() != 'mainnet-fork':
        pytest.skip('Only works for mainnet-fork network')
    # Act
    price_feed = PriceFeed.deploy(
        mainnet_eth_usd_address, {'from': accounts[0]})
    # Assert
    assert price_feed is not None


def test_can_get_latest_price(mainnet_eth_usd_address):
    # Arrange
    if network.show_active() != 'mainnet-fork':
        pytest.skip('Only works for mainnet-fork network')
    # Act
    price_feed = PriceFeed.deploy(
        mainnet_eth_usd_address, {'from': accounts[0]})
    # Assert
    value = price_feed.getLatestPrice({'from': accounts[0]})
    assert isinstance(value, int)
