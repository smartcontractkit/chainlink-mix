#!/usr/bin/python3
from brownie import APIConsumer, LinkToken, MockOracle, config, network
from scripts.helpful_scripts import (
    get_account,
    get_verify_status,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.deploy_mocks import deploy_mocks


def deploy_api_consumer():
    jobId = config["networks"][network.show_active()]["jobId"]
    fee = config["networks"][network.show_active()]["fee"]
    account = get_account()
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(MockOracle) <= 0:
            deploy_mocks()
        oracle = MockOracle[-1].address
        link_token = LinkToken[-1].address
    else:
        oracle = config["networks"][network.show_active()]["oracle"]
        link_token = config["networks"][network.show_active()]["link_token"]
    api_consumer = APIConsumer.deploy(
        oracle,
        jobId,
        fee,
        link_token,
        {"from": account},
        publish_source=get_verify_status(),
    )
    print(f"API Consumer deployed to {api_consumer.address}")
    return api_consumer


def main():
    deploy_api_consumer()
