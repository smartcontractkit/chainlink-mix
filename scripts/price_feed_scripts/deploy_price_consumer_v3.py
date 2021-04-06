#!/usr/bin/python3
from brownie import PriceFeed, accounts, config, network

# mainnet_eth_usd_address = '0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419'
# kovan_eth_usd_address = '0x9326BFA02ADD2366b30bacB125260Af641031331'


def main():
    if network.show_active() in [
        "mainnet-fork",
        "binance-fork",
        "matic-fork",
        "development",
    ]:
        price_feed = PriceFeed.deploy(
            config["networks"][network.show_active()]["eth_usd_price_feed"],
            {"from": accounts[0]},
            publish_source=config["verify"],
        )
        print(
            "The current price of ETH is "
            + str(price_feed.getLatestPrice({"from": accounts[0]}))
        )
        return price_feed
    elif network.show_active() in ["kovan", "rinkeby", "mainnet"]:
        dev = accounts.add(config["wallets"]["from_key"])
        return PriceFeed.deploy(
            config["networks"][network.show_active()]["eth_usd_price_feed"],
            {"from": dev},
            publish_source=config["verify"],
        )
    else:
        print("Please pick a supported network, or fork a chain")
