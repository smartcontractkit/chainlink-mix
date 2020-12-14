#!/usr/bin/python3
from brownie import APIConsumer


def main():
    api_contract = APIConsumer[len(APIConsumer) - 1]
    print("Reading data from {}".format(api_contract.address))
    print(api_contract.volume())
