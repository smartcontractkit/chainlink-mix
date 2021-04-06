#!/usr/bin/python3
from brownie import VRFConsumer, accounts, config, network


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    return VRFConsumer.deploy(
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link_token"],
        {"from": dev},
        publish_source=config["verify"],
    )
