
import pytest
from brownie import config, network, accounts
import os


@pytest.fixture
def kovan_eth_usd_address():
    return '0x9326BFA02ADD2366b30bacB125260Af641031331'


@pytest.fixture
def mainnet_eth_usd_address():
    return '0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419'


@pytest.fixture
def get_testnet_account():
    if network.show_active() != 'kovan' and network.show_active() != 'rinkeby':
        pytest.skip('Only works for testnets network')
    testnet_account = accounts.add(
        os.getenv(config['wallets']['from_key']))
    return testnet_account
