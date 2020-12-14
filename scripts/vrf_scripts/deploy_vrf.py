#!/usr/bin/python3
import os
from brownie import VRFConsumer, accounts, network, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print(network.show_active())
    return VRFConsumer.deploy(config['networks'][network.show_active()]['keyhash'],
                              config['networks'][network.show_active()
                                                 ]['vrf_coordinator'],
                              config['networks'][network.show_active()
                                                 ]['link_token'],
                              {'from': dev})
