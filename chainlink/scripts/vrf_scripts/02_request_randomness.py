#!/usr/bin/python3
from brownie import VRFConsumerV2, config, network
from scripts.helpful_scripts import fund_with_link, get_account


def main():
    account = get_account()
    vrf_contract = VRFConsumerV2[-1]
    try:
        tx = vrf_contract.requestRandomWords({"from": account})
        tx.wait(1)
    except:
        print(
            "Remember to fund your subscription! \n You can do it with the scripts here, or at https://vrf.chain.link/"
        )
    print("Requested!")
