#!/usr/bin/python3
from brownie import VRFConsumer, config, network
from scripts.helpful_scripts import fund_with_link, get_account

STATIC_SEED = 123


def main():
    account = get_account()
    vrf_contract = VRFConsumer[-1]
    tx = fund_with_link(
        vrf_contract, amount=config["networks"][network.show_active()]["fee"]
    )
    tx.wait(1)
    vrf_contract.getRandomNumber(STATIC_SEED, {"from": account})
    print("Requested!")
