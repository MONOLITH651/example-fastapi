from app.calculations import add, InsufficientFunds
import pytest
from app.calculations import BankAccount

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(num1, num2, expected):

    print("testing and function")
    sum = add(num1, num2)
    assert sum == expected 
    




def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_default_amount(zero_bank_account):
    print("Running test for default amout")
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.balance == 20

def test_deposit(bank_account):
    bank_account.deposit(30)
    assert bank_account.balance == 80

def test_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])

def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(zero_bank_account):
     with pytest.raises(InsufficientFunds):
        zero_bank_account.withdraw(100)