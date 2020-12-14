# chainlink-mix

This is a repo to work with and use Chainlink smart contracts in a python environment. If you're brand new to Chainlink, check out the beginer walkthroughs in remix to [learn the basics.](https://docs.chain.link/docs/beginners-tutorial)

You can also check out the more advanced Chainlink tutorials there as well. 

## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already. Here is a simple way to install brownie.

```bash
pip install eth-brownie
```

2. Download the mix. #TODO

Until the mix is uploaded, you can just do the following:

```bash
git clone https://github.com/PatrickAlphaC/chainlink-mix
cd chainlink-mix 
```

Once it becomes a mix, it will look like: 

```bash
brownie bake chainlink-mix
cd chainlink-mix
```

3. Set your `WEB3_INFURA_PROJECT_ID`. You can get this by getting a free trial of [Infura](https://infura.io/). At the moment, it does need to be infura. 

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
brownie run scripts/price_feed_scripts/deploy_vrf.py --network kovan
brownie run scripts/price_feed_scripts/fund_vrf.py --network kovan
brownie run scripts/price_feed_scripts/request_randomness.py --network kovan
brownie run scripts/price_feed_scripts/read_random_number.py --network kovan
```

## Chainlink API Call


This will deploy a smart contract to kovan and then make an API call via [Chainlink API Call](https://docs.chain.link/docs/make-a-http-get-request). 
```
brownie run scripts/price_feed_scripts/deploy_api_consumer.py --network kovan
brownie run scripts/price_feed_scripts/fund_chainlink_api.py --network kovan
brownie run scripts/price_feed_scripts/request_api.py --network kovan
brownie run scripts/price_feed_scripts/read_api.py --network kovan
```

## Testing

To run basic tests from `mainnet-fork` network

```
brownie test
```

There are 3 types of tests you can run:

1. Development tests
   1. These test using a local ganache chain. They are unit tests and do not interact with Chainlink nodes.
   2. Right now this is blank
2. Mainnet-fork tests
   1. These run on a mainnet forked local ganache chain. They are used to interact with pricefeed contracts deployed to mainnet. 
3. Testnet/Staging tests
   1. These are the pre-production tests. They are used to test a specific testnet. 
   2. Right now we have them hard coded to kovan. 


### To test development (Currently blank)
```bash
brownie test --network development
```
### To test mainnet-fork
This will test Chainlink API Calls and Chainlink VRF
```bash
brownie test --network mainnet-fork
```
### To test staging/testnet
This will test Chainlink Price Feeds
```bash
brownie test --network kovan
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
