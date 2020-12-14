#!/usr/bin/python3
import os
from brownie import VRFConsumer, accounts, network, interface, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    # Get the most recent PriceFeed Object
    vrf_contract = VRFConsumer[len(VRFConsumer) - 1]
    interface.LinkTokenInterface(config['networks'][network.show_active()]['link_token']).transfer(
        vrf_contract, 1000000000000000000, {'from': dev})
