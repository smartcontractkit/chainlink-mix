import time
import pytest
from brownie import VRFConsumer, convert, network
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def test_can_request_random_number(get_keyhash, chainlink_fee):
    # Arrange
    vrf_consumer = VRFConsumer.deploy(
        get_keyhash,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        chainlink_fee,
        {"from": get_account()},
    )
    get_contract("link_token").transfer(
        vrf_consumer.address, chainlink_fee * 3, {"from": get_account()}
    )
    # Act
    requestId = vrf_consumer.getRandomNumber.call({"from": get_account()})
    assert isinstance(requestId, convert.datatypes.HexString)


def test_returns_random_number_local(get_keyhash, chainlink_fee):
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    vrf_consumer = VRFConsumer.deploy(
        get_keyhash,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        chainlink_fee,
        {"from": get_account()},
    )
    get_contract("link_token").transfer(
        vrf_consumer.address, chainlink_fee * 3, {"from": get_account()}
    )
    # Act
    transaction_receipt = vrf_consumer.getRandomNumber({"from": get_account()})
    requestId = vrf_consumer.getRandomNumber.call({"from": get_account()})
    assert isinstance(transaction_receipt.txid, str)
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, 777, vrf_consumer.address, {"from": get_account()}
    )
    # Assert
    assert vrf_consumer.randomResult() > 0
    assert isinstance(vrf_consumer.randomResult(), int)


def test_returns_random_number_testnet(
    get_keyhash,
    chainlink_fee,
):
    # Arrange
    if network.show_active() not in ["kovan", "rinkeby", "ropsten"]:
        pytest.skip("Only for testnet testing")
    vrf_consumer = VRFConsumer.deploy(
        get_keyhash,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        chainlink_fee,
        {"from": get_account()},
    )
    get_contract("link_token").transfer(
        vrf_consumer.address, chainlink_fee * 3, {"from": get_account()}
    )
    # Act
    transaction_receipt = vrf_consumer.getRandomNumber({"from": get_account()})
    assert isinstance(transaction_receipt.txid, str)
    transaction_receipt.wait(1)
    time.sleep(35)
    # Assert
    assert vrf_consumer.randomResult() > 0
    assert isinstance(vrf_consumer.randomResult(), int)
