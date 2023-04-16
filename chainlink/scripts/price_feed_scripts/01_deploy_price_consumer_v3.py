#!/usr/bin/python3
from brownie import PriceFeedConsumer
from scripts.helpful_scripts import (
    BLOCK_CONFIRMATIONS_FOR_VERIFICATION,
    get_account,
    get_contract,
    is_verifiable_contract,
)


def deploy_price_feed_consumer():
    account = get_account()
    eth_usd_price_feed_address = get_contract("eth_usd_price_feed").address
    price_feed = PriceFeedConsumer.deploy(
        eth_usd_price_feed_address,
        {"from": account},
    )

    if is_verifiable_contract():
        price_feed.tx.wait(BLOCK_CONFIRMATIONS_FOR_VERIFICATION)
        PriceFeedConsumer.publish_source(price_feed)

    print(f"The current price of ETH is {price_feed.getLatestPrice()}")
    return price_feed


def main():
    deploy_price_feed_consumer()
