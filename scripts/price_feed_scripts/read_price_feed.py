#!/usr/bin/python3
from brownie import PriceFeed


def main():
    price_feed_contract = PriceFeed[len(PriceFeed) - 1]
    print("Reading data from {}".format(price_feed_contract.address))
    print(price_feed_contract.getLatestPrice())
