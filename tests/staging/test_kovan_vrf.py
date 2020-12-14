import pytest
import time
from brownie import VRFConsumer, network, config, interface
from flaky import flaky

STATIC_RANDOM_SEED = 123


@pytest.fixture
def deploy_vrf_contract(get_testnet_account):
    # Arrange
    if network.show_active() != 'kovan':
        pytest.skip('Only works for kovan network')
    # Act
    vrf_consumer = VRFConsumer.deploy(config['networks']['kovan']['keyhash'],
                                      config['networks']['kovan']['vrf_coordinator'],
                                      config['networks']['kovan']['link_token'],
                                      {'from': get_testnet_account})
    # Assert
    assert vrf_consumer is not None
    return vrf_consumer


@flaky
def test_send_random_number_request(deploy_vrf_contract, get_testnet_account):
    # Arrange
    vrf_contract = deploy_vrf_contract
    if network.show_active() != 'kovan':
        pytest.skip('Only works for kovan network')
    interface.LinkTokenInterface(config['networks']['kovan']['link_token']).transfer(
        vrf_contract, 1000000000000000000, {'from': get_testnet_account})
    # Act
    requestId = vrf_contract.getRandomNumber(
        STATIC_RANDOM_SEED, {'from': get_testnet_account})
    # Assert
    assert requestId is not None
    time.sleep(20)
    assert isinstance(vrf_contract.randomResult(), int)
