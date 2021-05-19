#!/usr/bin/python3
from brownie import VRFConsumer

STATIC_SEED = 123


def main():
    vrf_contract = VRFConsumer[len(VRFConsumer) - 1]
    if vrf_contract.randomResult() == 0:
        print("The result is 0, you may have to wait a minute unless on a local chain!")
    print(vrf_contract.randomResult())
