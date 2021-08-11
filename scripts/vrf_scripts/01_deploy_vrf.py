#!/usr/bin/python3
from brownie import VRFConsumer, config, network
from scripts.helpful_scripts import (
    get_account,
    get_contract,
)


def depoly_vrf():
    account = get_account()
    print(f"On network {network.show_active()}")
    keyhash = config["networks"][network.show_active()]["keyhash"]
    fee = config["networks"][network.show_active()]["fee"]
    vrf_coordinator = get_contract("vrf_coordinator")
    link_token = get_contract("link_token")

    return VRFConsumer.deploy(
        keyhash,
        vrf_coordinator,
        link_token,
        fee,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )


def main():
    depoly_vrf()
