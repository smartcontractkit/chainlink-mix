#!/usr/bin/python3
from brownie import PriceFeed, accounts, config, network
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_verify_status,
    get_account,
)

# mainnet_eth_usd_address = '0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419'
# kovan_eth_usd_address = '0x9326BFA02ADD2366b30bacB125260Af641031331'


def main():
    account = get_account()
    price_feed = PriceFeed.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
        publish_source=get_verify_status(),
    )
    print(
        "The current price of ETH is "
        + str(price_feed.getLatestPrice({"from": accounts[0]}))
    )
    return price_feed
