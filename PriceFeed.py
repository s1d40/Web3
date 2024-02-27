# THIS IS EXAMPLE CODE THAT USES HARDCODED VALUES FOR CLARITY.
# THIS IS EXAMPLE CODE THAT USES UN-AUDITED CODE.
# DO NOT USE THIS CODE IN PRODUCTION.

from web3 import Web3
import time


def  get_prices(addresses, names):
    
    # Change this to use your own RPC URL
    web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth_sepolia'))
    # AggregatorV3Interface ABI
    abi = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
    # Price Feed address
    for i in range(0,len(addresses)):
        addr = addresses[i]
        # Set up contract instance
        contract = web3.eth.contract(address=addr, abi=abi)
        # Make call to latestRoundData()
        latestData = contract.functions.latestRoundData().call()
        print(names[i], (latestData[1]/1e8) )

def main():
    while True:
        prices_addresses = ['0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43', '0x694AA1769357215DE4FAC081bf1f309aDC325306']
        prices_names = ['BTC / USD', 'ETH / USD']
        get_prices(prices_addresses,prices_names)
        time.sleep(60)

if __name__ == "__main__":
    main()