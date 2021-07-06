import time

import pytest
from brownie import APIConsumer, network
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from scripts.helpful_scripts import get_contract


@pytest.fixture
def deploy_api_contract(get_job_id, chainlink_fee):
    # Arrange / Act
    api_consumer = APIConsumer.deploy(
        get_contract("oracle").address,
        get_job_id,
        chainlink_fee,
        get_contract("link_token").address,
        {"from": get_account()},
    )
    # Assert
    assert api_consumer is not None
    return api_consumer


def test_send_api_request_local(
    deploy_api_contract,
    chainlink_fee,
    get_data,
):
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    api_contract = deploy_api_contract
    get_contract("link_token").transfer(
        api_contract.address, chainlink_fee * 2, {"from": get_account()}
    )
    # Act
    transaction_receipt = api_contract.requestVolumeData({"from": get_account()})
    requestId = transaction_receipt.events["ChainlinkRequested"]["id"]
    # Assert
    get_contract("oracle").fulfillOracleRequest(
        requestId, get_data, {"from": get_account()}
    )
    assert isinstance(api_contract.volume(), int)
    assert api_contract.volume() > 0


def test_send_api_request_testnet(deploy_api_contract, chainlink_fee):
    # Arrange
    if network.show_active() not in ["kovan", "rinkeby", "mainnet"]:
        pytest.skip("Only for local testing")
    api_contract = deploy_api_contract
    get_contract("link_token").transfer(
        api_contract.address, chainlink_fee * 2, {"from": get_account()}
    )
    # Act
    transaction = api_contract.requestVolumeData({"from": get_account()})
    # Assert
    assert transaction is not None
    transaction.wait(2)
    time.sleep(35)
    assert isinstance(api_contract.volume(), int)
    assert api_contract.volume() > 0
