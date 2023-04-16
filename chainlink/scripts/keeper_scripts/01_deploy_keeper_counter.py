#!/usr/bin/python3
from scripts.helpful_scripts import get_account, is_verifiable_contract
from brownie import Counter, config, network


def deploy_keeper_counter():
    account = get_account()
    return Counter.deploy(
        config["networks"][network.show_active()]["update_interval"],
        {"from": account},
        publish_source=is_verifiable_contract(),
    )


def main():
    deploy_keeper_counter()
