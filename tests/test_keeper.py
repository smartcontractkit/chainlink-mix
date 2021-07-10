from brownie import Counter
from scripts.helpful_scripts import get_account
import time


def test_can_call_check_upkeep():
    # Arrange
    interval = 2
    account = get_account()
    counter = Counter.deploy(interval, {"from": account})
    upkeepNeeded, performData = counter.checkUpkeep.call(
        "",
        {"from": account},
    )
    assert isinstance(upkeepNeeded, bool)
    assert isinstance(performData, bytes)
    assert upkeepNeeded is False
    # Since the interval is 2, after 2 seconds the upkeep should return true
    # We are extra safe and just make it 3
    time.sleep(3)
    # We need to make a block happen to get a new timestamp though
    # This is just a dummy transaction to make sure we get a new timestamp
    Counter.deploy(interval, {"from": account})

    # Now we can check
    # Act
    upkeepNeeded, performData = counter.checkUpkeep.call(
        "",
        {"from": account},
    )
    # Assert
    assert upkeepNeeded is True
