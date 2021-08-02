#!/usr/bin/python3
from brownie import APIConsumer, config, network
from scripts.helpful_scripts import (
    get_account,
    get_contract,
)


def deploy_api_consumer():
    jobId = config["networks"][network.show_active()]["jobId"]
    fee = config["networks"][network.show_active()]["fee"]
    account = get_account()
    oracle = get_contract("oracle").address
    link_token = get_contract("link_token").address
    api_consumer = APIConsumer.deploy(
        oracle,
        jobId,
        fee,
        link_token,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"API Consumer deployed to {api_consumer.address}")
    return api_consumer


def main():
    deploy_api_consumer()
