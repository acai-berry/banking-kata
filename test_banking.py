from banking import Account
import pytest
from datetime import datetime


def test_should_make_deposit():
    #given
    account = Account()
    amount = 50
    #when
    account.deposit(amount)
    #then
    assert account.balance == amount

def test_account_provides_operations_history():
    #given
    account = Account()
    #when
    deposit_amount = 50
    account.deposit(deposit_amount)
    #then
    history = account.history
    assert history[0] == datetime.datetime.now().date()
    assert history[1] == deposit_amount
    assert history[2] ==
    


def test_should_make_withdraw_correct_amount():
    #given
    account = Account()
    amount = 50
    account.deposit(amount)
    #when
    amount_to_withraw = 20
    account.withdraw(amount_to_withraw)
    expected_value = amount - amount_to_withraw
    #then
    assert account.balance == expected_value

def test_should_make_withdraw_incorrect_amount():
    #given
    account = Account()
    amount = 50
    account.deposit(amount)
    #when
    amount_to_withraw = 70
    #then
    with pytest.raises(ValueError):
        account.withdraw(amount_to_withraw)
