import time

import pytest
from brownie import Multiword, network, config
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    listen_for_event,
    get_contract,
    fund_with_link,
)


@pytest.fixture
def deploy_multiword_contract(get_multiword_job_id, chainlink_fee):
    # Arrange / Act
    multiword_contract = Multiword.deploy(
        get_contract("link_token").address,
        get_contract("multiword_oracle").address,
        get_multiword_job_id,
        {"from": get_account()},
    )
    block_confirmations = 6
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        block_confirmations = 1
    multiword_contract.tx.wait(block_confirmations)
    # Assert
    assert multiword_contract is not None
    return multiword_contract


def test_send_multiword_request_local(
    deploy_multiword_contract,
    chainlink_fee,
    get_data,
):
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    multiword_contract = deploy_multiword_contract
    get_contract("link_token").transfer(
        multiword_contract.address, chainlink_fee * 2, {"from": get_account()}
    )
    # Act
    transaction_receipt = multiword_contract.requestMultipleParameters(
        {"from": get_account()}
    )
    requestId = transaction_receipt.events["ChainlinkRequested"]["id"]
    # Assert
    get_contract("oracle").fulfillMultipleParameters(
        requestId, 7, 7, 7, {"from": get_account()}
    )
    assert multiword_contract.btc() > 0
    assert multiword_contract.usd() > 0
    assert multiword_contract.eur() > 0


def test_send_multiword_request_testnet(deploy_multiword_contract, chainlink_fee):
    # Arrange
    if network.show_active() not in ["kovan", "rinkeby", "mainnet"]:
        pytest.skip("Only for testnet testing")
    multiword_contract = deploy_multiword_contract

    if config["networks"][network.show_active()].get("verify", False):
        Multiword.publish_source(multiword_contract)

    tx = fund_with_link(multiword_contract.address, amount=chainlink_fee)
    tx.wait(1)
    # Act
    transaction = multiword_contract.requestMultipleParameters({"from": get_account()})
    transaction.wait(1)

    # Assert
    event_response = listen_for_event(multiword_contract, "RequestMultipleFulfilled")
    assert event_response.event is not None
    assert multiword_contract.btc() > 0
    assert multiword_contract.usd() > 0
    assert multiword_contract.eur() > 0
