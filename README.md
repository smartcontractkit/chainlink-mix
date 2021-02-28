# chainlink-mix

<br/>
<p align="center">
<a href="https://chain.link" target="_blank">
<img src="https://raw.githubusercontent.com/smartcontractkit/chainlink-mix/master/img/chainlink-brownie.png" width="225" alt="Chainlink Brownie logo">
</a>
</p>
<br/>

[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/smartcontractkit/chainlink-mix.svg)](http://isitmaintained.com/project/smartcontractkit/chainlink-mix "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/smartcontractkit/chainlink-mix.svg)](http://isitmaintained.com/project/smartcontractkit/chainlink-mix "Percentage of issues still open")

This is a repo to work with and use Chainlink smart contracts in a python environment. If you're brand new to Chainlink, check out the beginner walkthroughs in remix to [learn the basics.](https://docs.chain.link/docs/beginners-tutorial)

You can also check out the more advanced Chainlink tutorials there as well. 

## Prerequisites

Please install or have installed the following:

- [nodejs and npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)
## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already. Here is a simple way to install brownie.

```bash
pip install eth-brownie
```

2. [Install ganache-cli](https://www.npmjs.com/package/ganache-cli)

```bash
npm install -g ganache-cli
```

3. Download the mix. 

```bash
brownie bake chainlink-mix
cd chainlink-mix
```

This will open up a new Chainlink project. Or, you can clone from source:

```bash
git clone https://github.com/PatrickAlphaC/chainlink-mix
cd chainlink-mix 
```

If you want to be able to deploy to testnets, do the following. 

1. Set your `WEB3_INFURA_PROJECT_ID`, and `PRIVATE_KEY` [environment variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). You can get this by getting a free trial of [Infura](https://infura.io/). At the moment, it does need to be infura. You can find your `PRIVATE_KEY` from your ethereum wallet like [metamask](https://metamask.io/). 

Otherwise, you can build, test, and deploy on your local environment. 

## Chainlink Price Feeds

This mix provides a simple template for working with Chainlink Smart Contracts. The easiest way to start is to fork the mainnet chain to a local ganache chain. This will allow you to deploy local smart contracts to interact with the [Chainlink Price Feeds](https://docs.chain.link/docs/get-the-latest-price). 

### Running Scripts

This will deploy a smart contract to kovan and then read you the latest price via [Chainlink Price Feeds](https://docs.chain.link/docs/get-the-latest-price). 
```
brownie run scripts/price_feed_scripts/deploy_price_consumer_v3.py --network kovan
brownie run scripts/price_feed_scripts/read_price_feed.py --network kovan
```

Otherwise, you can fork mainnet and use that in a local ganache development environment.
```bash
brownie console --network mainnet-fork
>>> price_feeds = PriceFeed.deploy('0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419', {'from': accounts[0]})
.
.
>>> latest_price = price_feeds.getLatestPrice()
>>> latest_price
59169208540
```

## Chainlink VRF

This will deploy a smart contract to kovan and get a Random number via [Chainlink VRF](https://docs.chain.link/docs/get-a-random-number). 
```
brownie run scripts/vrf_scripts/deploy_vrf.py --network kovan
brownie run scripts/vrf_scripts/fund_vrf.py --network kovan
brownie run scripts/vrf_scripts/request_randomness.py --network kovan
brownie run scripts/vrf_scripts/read_random_number.py --network kovan
```

## Chainlink API Call


This will deploy a smart contract to kovan and then make an API call via [Chainlink API Call](https://docs.chain.link/docs/make-a-http-get-request). 
```
brownie run scripts/chainlink_api_scripts/deploy_api_consumer.py --network kovan
brownie run scripts/chainlink_api_scripts/fund_chainlink_api.py --network kovan
brownie run scripts/chainlink_api_scripts/request_api.py --network kovan
brownie run scripts/chainlink_api_scripts/read_api.py --network kovan
```

## Testing

```
brownie test
```

For more information on effective testing with Chainlink, check out [Testing Smart Contracts](https://blog.chain.link/testing-chainlink-smart-contracts/)

Tests are really robust here! They work for local development and testnets. There are a few key differences between the testnets and the local networks. We utilize mocks so we can work with fake oracles on our testnets. 

There is a `test_unnecessary` folder, which is a good exersize for learning some of the nitty-gritty of smart contract development. It's overkill, so pytest will skip them intentionally. It also has a `test_samples` folder, which shows an example Chainlink API call transaction receipt. 


### To test development / local
```bash
brownie test
```
### To test mainnet-fork
This will test the same way as local testing, but you will need a connection to a mainnet blockchain (like with the infura environment variable.)
```bash
brownie test --network mainnet-fork
```
### To test a testnet
Kovan and Rinkeby are currently supported
```bash
brownie test --network kovan
```

## Adding additional Chains

If the blockchain is EVM Compatible, adding new chains can be accomplished by something like:

```
brownie networks add Ethereum binance-smart-chain host=https://bsc-dataseed1.binance.org chainid=56
```
or, for a fork: 

```
brownie networks add development binance-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://bsc-dataseed1.binance.org accounts=10 mnemonic=brownie port=8545
```

## Resources

To get started with Brownie:

* [Chainlink Documentation](https://docs.chain.link/docs)
* Check out the [Chainlink documentation](https://docs.chain.link/docs) to get started from any level of smart contract engineering. 
* Check out the other [Brownie mixes](https://github.com/brownie-mix/) that can be used as a starting point for your own contracts. They also provide example code to help you get started.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) is a good tutorial to help you familiarize yourself with Brownie.
* For more in-depth information, read the [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/).


Any questions? Join our [Discord](https://discord.gg/2YHSAey)

## License

This project is licensed under the [MIT license](LICENSE).
