from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 5000000000


def GetAccount():

    i = 0  # test account, from accounts, to use
    # print(f"The active network is {network.show_active()}")
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ):
        print("Using Brownie 'accounts'", i, "of", len(accounts))
        return accounts[i]
    else:
        print("Using config 'account'")
        return accounts.add(config["wallets"]["from_key"])


def DeployMockNetwork():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    # if len(MockV3Aggregator) <= 0:
    MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": GetAccount()})
    print("Deployed")
