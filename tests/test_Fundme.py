from brownie import network, exceptions, accounts
from scripts.HelperScripts import GetAccount, LOCAL_BLOCKCHAIN_ENVIROMENTS
from scripts.Deploy import Deploy_FundMe
import pytest


def test_FundAndWithdraw():
    account = GetAccount()
    contract = Deploy_FundMe()
    fee = contract.GetEntranceFee()
    transaction = contract.Fund({"from": account, "value": fee})
    transaction.wait(1)
    assert contract.mapAddressToAmountFunded(account.address) == fee
    transaction2 = contract.Withdraw({"from": account})
    transaction2.wait(1)
    # assert contract.mapAddressToAmountFunded(account.address) == 0
    assert contract.Inquire(contract) == 0


def test_OnlyOwnerCanWithdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        pytest.skip("only for LOCAL testing")
    account = GetAccount()
    contract = Deploy_FundMe()
    notOwner = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        contract.Withdraw({"from": account})
