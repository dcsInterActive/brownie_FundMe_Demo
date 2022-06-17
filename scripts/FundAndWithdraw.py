from brownie import FundMe

from scripts.HelperScripts import GetAccount


def Fund():
    fund_me_last = FundMe[-1]
    account = GetAccount()
    entranceFee = fund_me_last.GetEntranceFee()
    print("ETH price", fund_me_last.GetPrice() / 10**8, "USD")
    print("ETH price", fund_me_last.GetPrice(), "USD w/ 8 Decimals")
    n = 1
    print(
        n, "dollar(s) will purchase", fund_me_last.GetConversionRate(n) / 10**8, "Eth"
    )  # in USD
    print(
        n,
        "dollar(s) will purchase",
        fund_me_last.GetConversionRate(n),
        "Eth w/ 8 Decimals",
    )
    print("$50 Fee paid in", entranceFee / 10**8, "Eth")
    print(entranceFee, "Eth w/ 8 Decimals")
    fund_me_last.Fund({"from": account, "value": entranceFee})


def Balance():
    fundMeContract = FundMe[-1]
    balance = fundMeContract.Balance()
    print("Balance", balance)


def Inquire(address):
    fundMeContract = FundMe[-1]
    print(fundMeContract)
    balance = fundMeContract.Inquire(address)
    print("Balance", balance)


def Withdraw():
    fundMeContract = FundMe[-1]
    account = GetAccount()
    fundMeContract.Withdraw({"from": account})


def main():
    Inquire("0x56a121D7f661B4542A051e86d96D63C429FCcB41")
    Withdraw()
    Inquire("0x56a121D7f661B4542A051e86d96D63C429FCcB41")
