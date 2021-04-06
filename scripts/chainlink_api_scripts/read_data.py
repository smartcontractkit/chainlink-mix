#!/usr/bin/python3
from brownie import APIConsumer


def main():
    api_contract = APIConsumer[len(APIConsumer) - 1]
    print("Reading data from {}".format(api_contract.address))
    if api_contract.volume() == 0:
        print("You may have to wait a minute and then call this again!")
    print(api_contract.volume())
