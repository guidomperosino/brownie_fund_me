from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    account = get_account()
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})
    print("Funded!")


def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    print("Withdrawing...")
    fund_me.withdraw({"from": account})
    print("Withdrawn!")


def main():
    fund()
    withdraw()
