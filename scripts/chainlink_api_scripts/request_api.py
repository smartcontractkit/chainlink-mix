#!/usr/bin/python3
import os
from brownie import APIConsumer, accounts, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    # Get the most recent PriceFeed Object
    api_contract = APIConsumer[len(APIConsumer) - 1]
    api_contract.requestVolumeData({'from': dev})
