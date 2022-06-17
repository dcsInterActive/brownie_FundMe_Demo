from brownie import FundMe, MockV3Aggregator, network, config

from scripts.HelperScripts import (
    GetAccount,
    DeployMockNetwork,
    LOCAL_BLOCKCHAIN_ENVIROMENTS,
)


def Deploy_FundMe():
    account = GetAccount()
    print("Got Account")
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "ETH_USD_PRICE_FEED"
        ]
    else:
        DeployMockNetwork()
        price_feed_address = MockV3Aggregator[-1].address

    fundmeContract = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("VERIFY"),
    )
    print(f"Contract deployed to {fundmeContract.address}")
    return fundmeContract


def main():
    Deploy_FundMe()
