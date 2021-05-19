#!/usr/bin/python3
from brownie import VRFConsumer, accounts, config, network


def main():
    account = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    return VRFConsumer.deploy(
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link_token"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=config["verify"],
    )
