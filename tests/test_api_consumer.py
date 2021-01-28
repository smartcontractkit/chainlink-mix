import pytest
import time
from brownie import APIConsumer, network


@pytest.fixture
def deploy_api_contract(get_account, get_oracle, get_job_id, chainlink_fee, get_link_token):
    # Arrange / Act
    api_consumer = APIConsumer.deploy(get_oracle.address,
                                      get_job_id,
                                      chainlink_fee,
                                      get_link_token.address,
                                      {'from': get_account})
    # Assert
    assert api_consumer is not None
    return api_consumer


def test_send_api_request_local(deploy_api_contract, get_account, get_link_token,
                                chainlink_fee, get_oracle, get_data):

    # Arrange
    if network.show_active() not in ['development'] or 'fork' in network.show_active():
        pytest.skip('Only for local testing')
    api_contract = deploy_api_contract
    get_link_token.transfer(api_contract.address,
                            chainlink_fee * 2, {'from': get_account})
    # Act
    transaction_receipt = api_contract.requestVolumeData({'from': get_account})
    requestId = transaction_receipt.events['ChainlinkRequested']['id']
    # Assert
    get_oracle.fulfillOracleRequest(requestId, get_data)
    assert isinstance(api_contract.volume(), int)
    assert api_contract.volume() > 0


def test_send_api_request_testnet(deploy_api_contract, get_account, get_link_token, chainlink_fee):
    # Arrange
    if network.show_active() not in ['kovan', 'rinkeby']:
        pytest.skip('Only for local testing')
    api_contract = deploy_api_contract
    get_link_token.transfer(api_contract.address,
                            chainlink_fee * 2, {'from': get_account})
    # Act
    requestId = api_contract.requestVolumeData({'from': get_account})
    # Assert
    assert requestId is not None
    time.sleep(20)
    assert isinstance(api_contract.volume(), int)
    assert api_contract.volume() > 0
