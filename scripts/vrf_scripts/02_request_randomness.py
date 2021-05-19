#!/usr/bin/python3
from brownie import VRFConsumer, accounts, config, network
from scripts.helpful_scripts import fund_with_link

STATIC_SEED = 123


def main():
    account = accounts.add(config["wallets"]["from_key"])
    # Get the most recent PriceFeed Object
    vrf_contract = VRFConsumer[len(VRFConsumer) - 1]
    tx = fund_with_link(
        vrf_contract, amount=config["networks"][network.show_active()]["fee"]
    )
    tx.wait(1)
    vrf_contract.getRandomNumber(STATIC_SEED, {"from": account})
    print("Requested!")
