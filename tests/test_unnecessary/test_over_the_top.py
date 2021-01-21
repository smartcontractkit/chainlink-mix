import pytest
import brownie
from brownie import Oracle, APIConsumer, LinkToken


@pytest.mark.skip(reason="overkill testing")
def test_chainlink_api_call_without_link(job_id, dev_account, node_account, chainlink_fee):
    # Arrange
    link_token = LinkToken.deploy({'from': dev_account})
    oracle = Oracle.deploy(link_token.address, {'from': dev_account})
    api_consumer = APIConsumer.deploy(
        oracle.address, job_id, chainlink_fee, link_token.address, {'from': dev_account})
    oracle.setFulfillmentPermission(node_account, True, {'from': dev_account})
    # Act / Assert
    with pytest.raises(brownie.exceptions.VirtualMachineError):
        api_consumer.requestVolumeData({'from': dev_account})


@pytest.mark.skip(reason="overkill testing")
def test_chainlink_api_call_with_link(job_id, dev_account, node_account, chainlink_fee):
    # Arrange
    link_token = LinkToken.deploy({'from': dev_account})
    oracle = Oracle.deploy(link_token.address, {'from': dev_account})
    api_consumer = APIConsumer.deploy(
        oracle.address, job_id, chainlink_fee, link_token.address, {'from': dev_account})
    oracle.setFulfillmentPermission(node_account, True, {'from': dev_account})
    link_token.transfer(api_consumer.address,
                        chainlink_fee, {'from': dev_account})
    # Act
    transaction_data = api_consumer.requestVolumeData({'from': dev_account})
    # Assert
    assert oracle.address == transaction_data.logs[3].address
    # assert request.topic == Web3.utils.keccak256(
    #     'OracleRequest(bytes32,address,bytes32,uint256,address,bytes4,uint256,uint256,bytes)',)


@pytest.mark.skip(reason="overkill testing")
def test_chainlink_api_call_with_link_fulfilled(job_id, dev_account, node_account, chainlink_fee, expiry_time):
    # Arrange
    link_token = LinkToken.deploy({'from': dev_account})
    oracle = Oracle.deploy(link_token.address, {'from': dev_account})
    api_consumer = APIConsumer.deploy(
        oracle.address, '29fa9aa13bf1468788b7cc4a500a45b8', chainlink_fee, link_token.address, {'from': dev_account})
    oracle.setFulfillmentPermission(node_account, True, {'from': dev_account})
    link_token.transfer(api_consumer.address,
                        chainlink_fee * 3, {'from': dev_account})

    transaction_receipt = api_consumer.requestVolumeData({'from': dev_account})
    reqid = transaction_receipt.events['ChainlinkRequested']['id']
    selector = ''
    # Act
    for key, value in api_consumer.__dict__['selectors'].items():
        if value == 'fulfill':
            selector = key
    # We cheated and added `exp_time` to a public variable in the Oracle.sol
    # This is all needed because fulfillOracleRequest hashes all the params and checks to make sure the
    # Hashes all match
    # We are using a modified Oracle.sol
    successful = oracle.fulfillOracleRequest(
        reqid, chainlink_fee, api_consumer.address, selector, oracle.exp_time(), "", {'from': node_account})
    assert successful.status == 1
