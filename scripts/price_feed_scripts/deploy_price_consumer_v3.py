#!/usr/bin/python3
import os
from brownie import PriceFeed, accounts, network, config

# mainnet_eth_usd_address = '0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419'
# kovan_eth_usd_address = '0x9326BFA02ADD2366b30bacB125260Af641031331'


def main():
    if network.show_active() in ['mainnet-fork', 'binance-fork', 'matic-fork']:
        price_feed = PriceFeed.deploy(config['networks'][network.show_active(
        )]['eth_usd_price_feed'], {'from': accounts[0]})
        print("The current price of ETH is " +
              str(price_feed.getLatestPrice({'from': accounts[0]})))
        return price_feed
    elif network.show_active() in ['kovan', 'rinkeby', 'mainnet']:
        dev = accounts.add(os.getenv(config['wallets']['from_key']))
        return PriceFeed.deploy(config['networks'][network.show_active()]['eth_usd_price_feed'], {'from': dev})
    else:
        print('Please pick a supported network, or fork a chain')
