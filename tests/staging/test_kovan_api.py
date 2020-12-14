import pytest
import time
from brownie import APIConsumer, network, config, interface
from flaky import flaky
from web3 import Web3


@pytest.fixture
def deploy_api_contract(get_testnet_account):
    # Arrange
    if network.show_active() != 'kovan':
        pytest.skip('Only works for kovan network')
    # Act
    api_consumer = APIConsumer.deploy(config['networks'][network.show_active()]['oracle'],
                                      config['networks'][network.show_active()
                                                         ]['jobId'],
                                      config['networks'][network.show_active()
                                                         ]['fee'],
                                      {'from': get_testnet_account})
    # Assert
    assert api_consumer is not None
    return api_consumer


@flaky
def test_send_api_request(deploy_api_contract, get_testnet_account):
    # Arrange
    api_contract = deploy_api_contract
    if network.show_active() != 'kovan':
        pytest.skip('Only works for kovan network')
    interface.LinkTokenInterface(config['networks']['kovan']['link_token']).transfer(
        api_contract, 1000000000000000000, {'from': get_testnet_account})
    # Act
    requestId = api_contract.requestVolumeData({'from': get_testnet_account})
    # Assert
    assert requestId is not None
    time.sleep(20)
    assert isinstance(api_contract.volume(), int)
    assert api_contract.volume() > 0
