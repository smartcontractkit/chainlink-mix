import time
import pytest
from brownie import VRFConsumerV2, convert, network, config
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    listen_for_event,
)

from scripts.vrf_scripts.create_subscription import (
    create_subscription,
    fund_subscription,
)


def test_can_request_random_number():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    # Arrange
    account = get_account()
    subscription_id = create_subscription()
    fund_subscription(subscription_id=subscription_id)
    gas_lane = config["networks"][network.show_active()][
        "gas_lane"
    ]  # Also known as keyhash
    vrf_coordinator = get_contract("vrf_coordinator")
    link_token = get_contract("link_token")
    vrf_consumer = VRFConsumerV2.deploy(
        subscription_id,
        vrf_coordinator,
        link_token,
        gas_lane,  # Also known as keyhash
        {"from": account},
    )

    # Act
    tx = vrf_consumer.requestRandomWords({"from": account})
    tx.wait(1)
    request_id = tx.events[0]["requestId"]
    assert isinstance(request_id, int)


def test_returns_random_number_local():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    # Arrange
    account = get_account()
    subscription_id = create_subscription()
    fund_subscription(subscription_id=subscription_id)
    gas_lane = config["networks"][network.show_active()]["gas_lane"]
    vrf_coordinator = get_contract("vrf_coordinator")
    link_token = get_contract("link_token")
    vrf_consumer = VRFConsumerV2.deploy(
        subscription_id,
        vrf_coordinator,
        link_token,
        gas_lane,
        {"from": account},
    )

    # Act
    tx = vrf_consumer.requestRandomWords({"from": account})
    tx.wait(1)
    request_id = tx.events[0]["requestId"]
    vrf_coordinator.fulfillRandomWords(
        request_id, vrf_consumer.address, {"from": get_account()}
    )
    # Assert
    assert vrf_consumer.s_randomWords(0) > 0


def test_returns_random_number_testnet():
    # Arrange
    if network.show_active() not in ["rinkeby"]:
        pytest.skip("Only for testnet testing")
    # Arrange
    account = get_account()
    subscription_id = create_subscription()
    fund_subscription(subscription_id=subscription_id)
    gas_lane = config["networks"][network.show_active()]["gas_lane"]
    vrf_coordinator = get_contract("vrf_coordinator")
    link_token = get_contract("link_token")
    vrf_consumer = VRFConsumerV2.deploy(
        subscription_id,
        vrf_coordinator,
        link_token,
        gas_lane,
        {"from": account},
    )
    tx = vrf_coordinator.addConsumer.transact(
        subscription_id, vrf_consumer.address, {"from": account}
    )
    tx.wait(1)

    # Act
    tx = vrf_consumer.requestRandomWords({"from": account})
    tx.wait(1)
    event_response = listen_for_event(vrf_consumer, "ReturnedRandomness")

    # Assert
    assert event_response.event is not None
    assert vrf_consumer.s_randomWords(0) > 0
    assert vrf_consumer.s_randomWords(1) > 0
