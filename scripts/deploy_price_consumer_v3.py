#!/usr/bin/python3

from brownie import PriceFeed, accounts


def main():
    return PriceFeed.deploy({'from': accounts[0]})
