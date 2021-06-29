from brownie import Counter
from scripts.helpful_scripts import get_account
import time


def test_can_call_check_upkeep():
    # Arrange
    interval = 2
    account = get_account()
    # Act
    counter = Counter.deploy(interval, {"from": account})
    # Assert
    upkeepNeeded, performData = counter.checkUpkeep.call(
        "",
        {"from": account},
    )
    assert isinstance(upkeepNeeded, bool)
    assert isinstance(performData, bytes)
    assert upkeepNeeded is False
    # Since the interval is 2, after 2 seconds the upkeep should return true
    # We are extra safe and just make it 4
    time.sleep(4)
    upkeepNeeded, performData = counter.checkUpkeep.call(
        "",
        {"from": account},
    )
    assert upkeepNeeded is False
