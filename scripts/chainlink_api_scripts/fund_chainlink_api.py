#!/usr/bin/python3
from brownie import APIConsumer, accounts, config, interface, network


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    # Get the most recent PriceFeed Object
    api_contract = APIConsumer[len(APIConsumer) - 1]
    interface.LinkTokenInterface(
        config["networks"][network.show_active()]["link_token"]
    ).transfer(api_contract, 1000000000000000000, {"from": dev})
    print("Funded {}".format(api_contract.address))
