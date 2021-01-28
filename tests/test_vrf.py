import pytest
import time
from brownie import network, VRFConsumer, convert


def test_can_request_random_number(get_account, get_vrf_coordinator, get_keyhash,
                                   get_link_token, chainlink_fee, get_seed):
    # Arrange
    vrf_consumer = VRFConsumer.deploy(
        get_keyhash, get_vrf_coordinator.address, get_link_token.address, {'from': get_account})
    get_link_token.transfer(vrf_consumer.address,
                            chainlink_fee * 3, {'from': get_account})
    # Act
    requestId = vrf_consumer.getRandomNumber.call(
        get_seed, {'from': get_account})
    assert isinstance(requestId, convert.datatypes.HexString)


def test_returns_random_number_local(get_account, get_vrf_coordinator, get_keyhash,
                                     get_link_token, chainlink_fee, get_seed):
    # Arrange
    if network.show_active() not in ['development'] or 'fork' in network.show_active():
        pytest.skip('Only for local testing')
    vrf_consumer = VRFConsumer.deploy(
        get_keyhash, get_vrf_coordinator.address, get_link_token.address, {'from': get_account})
    get_link_token.transfer(vrf_consumer.address,
                            chainlink_fee * 3, {'from': get_account})
    # Act
    transaction_receipt = vrf_consumer.getRandomNumber(
        get_seed, {'from': get_account})
    requestId = vrf_consumer.getRandomNumber.call(
        get_seed, {'from': get_account})
    assert isinstance(transaction_receipt.txid, str)
    get_vrf_coordinator.callBackWithRandomness(
        requestId, 777, vrf_consumer.address, {'from': get_account})
    # Assert
    assert vrf_consumer.randomResult() > 0
    assert isinstance(vrf_consumer.randomResult(), int)


def test_returns_random_number_testnet(get_account, get_vrf_coordinator, get_keyhash,
                                       get_link_token, chainlink_fee, get_seed):
    # Arrange
    if network.show_active() not in ['kovan', 'rinkeby']:
        pytest.skip('Only for testnet testing')
    vrf_consumer = VRFConsumer.deploy(
        get_keyhash, get_vrf_coordinator.address, get_link_token.address, {'from': get_account})
    get_link_token.transfer(vrf_consumer.address,
                            chainlink_fee * 3, {'from': get_account})
    # Act
    transaction_receipt = vrf_consumer.getRandomNumber(
        get_seed, {'from': get_account})
    assert isinstance(transaction_receipt.txid, str)
    time.sleep(30)
    # Assert
    assert vrf_consumer.randomResult() > 0
    assert isinstance(vrf_consumer.randomResult(), int)
