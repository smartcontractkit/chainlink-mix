from brownie import network, accounts, config, interface

NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + [
    "mainnet-fork",
    "binance-fork",
    "matic-fork",
]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if network.show_active() in config["networks"]:
        account = accounts.add(config["wallets"]["from_key"])
        return account
    return None


def fund_with_link(
    contract_address, account=None, link_token=None, amount=1000000000000000000
):
    account = account if account else get_account()
    link_token = (
        link_token
        if link_token
        else config["networks"][network.show_active()]["link_token"]
    )
    tx = interface.LinkTokenInterface(link_token).transfer(
        contract_address, amount, {"from": account}
    )
    print("Funded {}".format(contract_address.address))
    return tx


def get_verify_status():
    verify = (
        config["networks"][network.show_active()]["verify"]
        if config["networks"][network.show_active()].get("verify")
        else False
    )
    return verify
