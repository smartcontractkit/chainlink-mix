#!/usr/bin/python3
import os
from brownie import APIConsumer, accounts, network, interface, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    # Get the most recent PriceFeed Object
    api_contract = APIConsumer[len(APIConsumer) - 1]
    interface.LinkTokenInterface(config['networks'][network.show_active()]['link_token']).transfer(
        api_contract, 1000000000000000000, {'from': dev})
    print("Funded {}".format(api_contract.address))
