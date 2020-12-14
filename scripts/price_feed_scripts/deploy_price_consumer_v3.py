#!/usr/bin/python3
import os
from brownie import PriceFeed, accounts, network

mainnet_eth_usd_address = '0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419'
kovan_eth_usd_address = '0x9326BFA02ADD2366b30bacB125260Af641031331'


def main():
    if network.show_active() == 'mainnet-fork' or network.show_active() == 'development':
        return PriceFeed.deploy(mainnet_eth_usd_address, {'from': accounts[0]})
    elif network.show_active() == 'kovan':
        dev = accounts.add(os.getenv('PRIVATE_KEY'))
        return PriceFeed.deploy(kovan_eth_usd_address, {'from': dev})
    else:
        print('Please pick a supported network, or add the rinkeby config')
