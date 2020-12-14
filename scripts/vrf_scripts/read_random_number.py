#!/usr/bin/python3
from brownie import VRFConsumer

STATIC_SEED = 123


def main():
    vrf_contract = VRFConsumer[len(VRFConsumer) - 1]
    print(vrf_contract.randomResult())
