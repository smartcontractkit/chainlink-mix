#!/usr/bin/python3
from brownie import MockV3Aggregator, PriceFeedConsumer, config, network
from scripts.helpful_scripts import (
    get_verify_status,
    get_account,
    NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.deploy_mocks import deploy_mocks


def deploy_price_feed_consumer():
    account = get_account()
    if network.show_active() in NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(MockV3Aggregator) <= 0:
            deploy_mocks()
        eth_usd_price_feed = MockV3Aggregator[-1].address
    else:
        eth_usd_price_feed = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    price_feed = PriceFeedConsumer.deploy(
        eth_usd_price_feed,
        {"from": account},
        publish_source=get_verify_status(),
    )
    print(f"The current price of ETH is {price_feed.getLatestPrice()}")
    return price_feed


def main():
    deploy_price_feed_consumer()
