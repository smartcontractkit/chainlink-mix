#!/usr/bin/python3
from brownie import APIConsumer, accounts, config
from scripts.helpful_scripts import fund_with_link


def main():
    account = accounts.add(config["wallets"]["from_key"])
    api_contract = APIConsumer[len(APIConsumer) - 1]
    tx = fund_with_link(
        api_contract, amount=config["networks"][network.show_active()]["fee"]
    )
    tx.wait(1)
    api_contract.requestVolumeData({"from": account})
