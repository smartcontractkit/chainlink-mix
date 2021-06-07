#!/usr/bin/python3
from brownie import VRFConsumer, VRFCoordinatorMock, LinkToken, config, network
from scripts.helpful_scripts import (
    get_account,
    get_verify_status,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.deploy_mocks import deploy_mocks


def depoly_vrf():
    account = get_account()
    print(f"On network {network.show_active()}")
    keyhash = config["networks"][network.show_active()]["keyhash"]
    fee = config["networks"][network.show_active()]["fee"]
    account = get_account()
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(VRFCoordinatorMock) <= 0:
            deploy_mocks()
        vrf_coordinator = VRFCoordinatorMock[-1].address
        link_token = LinkToken[-1].address
    else:
        vrf_coordinator = config["networks"][network.show_active()]["vrf_coordinator"]
        link_token = config["networks"][network.show_active()]["link_token"]

    return VRFConsumer.deploy(
        keyhash,
        vrf_coordinator,
        link_token,
        fee,
        {"from": account},
        publish_source=get_verify_status(),
    )


def main():
    depoly_vrf()
