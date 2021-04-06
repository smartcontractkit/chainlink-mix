#!/usr/bin/python3
from brownie import APIConsumer, accounts, config, network


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    return APIConsumer.deploy(
        config["networks"][network.show_active()]["oracle"],
        config["networks"][network.show_active()]["jobId"],
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["link_token"],
        {"from": dev},
        publish_source=config["verify"],
    )
