#!/usr/bin/python3
import os
from brownie import APIConsumer, accounts, network, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    return APIConsumer.deploy(
        config['networks'][network.show_active()]['oracle'],
        config['networks'][network.show_active()]['jobId'],
        config['networks'][network.show_active()]['fee'],
        {'from': dev})
