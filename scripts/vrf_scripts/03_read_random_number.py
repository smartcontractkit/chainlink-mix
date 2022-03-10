#!/usr/bin/python3
from brownie import VRFConsumerV2


def main():
    vrf_contract = VRFConsumerV2[-1]
    try:
        print(f"Random word 0 is {vrf_contract.s_randomWords(0)}")
        print(f"Random word 1 is {vrf_contract.s_randomWords(1)}")
    except:
        print("You may have to wait a minute unless on a local chain!")
