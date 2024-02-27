# Example code for fetching real-time price data from the Sepolia testnet.
# Note: This script uses hardcoded values for demonstration purposes only and includes un-audited code.
# Do not use this code in production environments.

from web3 import Web3
import time

def get_prices(addresses, names):
    """
    Fetches and prints the latest price data for given addresses.

    Args:
        addresses (list): A list of contract addresses to fetch the price data from.
        names (list): A list of names corresponding to each contract address for better readability.
    """
    # Initialize a Web3 connection to the Sepolia testnet
    web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth_sepolia'))
    
    # Define the AggregatorV3Interface ABI to interact with the price feed contracts
    abi = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
    
    # Iterate through the provided addresses to fetch and print their latest price data
    for i in range(len(addresses)):
        addr = addresses[i]
        contract = web3.eth.contract(address=addr, abi=abi)  # Set up contract instance
        latestData = contract.functions.latestRoundData().call()  # Call the latestRoundData function
        print(names[i], (latestData[1] / 1e8))  # Print the name and the price (adjusted for scale)

def main():
    """
    Main function to continuously fetch and print price data every minute.
    """
    while True:
        # List of contract addresses for price data
        prices_addresses = ['0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43', '0x694AA1769357215DE4FAC081bf1f309aDC325306']
        # Corresponding names for the contract addresses
        prices_names = ['BTC / USD', 'ETH / USD']
        get_prices(prices_addresses, prices_names)  # Fetch and print the prices
        time.sleep(60)  # Wait for one minute before fetching the prices again

if __name__ == "__main__":
    main()
