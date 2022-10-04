from banking import Account, AccountHistory
import pytest
from datetime import datetime


def test_should_make_deposit():
    #given
    history = AccountHistory()
    account = Account(history)
    amount = 50
    #when
    account.deposit(amount)
    #then
    assert account.balance == amount

def test_account_provides_operations_history():
    #given
    given_history = AccountHistory()
    account = Account(given_history)
    #when
    deposit_amount = 50
    account.deposit(deposit_amount)
    #then
    events = account.history.events_history
    assert events[0].date == datetime.now().date()
    assert events[0].amount == deposit_amount
    assert events[0].balance == deposit_amount
    assert len(events) == 1
    

def test_should_withdraw_correct_amount():
    #given
    history = AccountHistory()
    account = Account(history)
    amount = 50
    account.deposit(amount)
    #when
    amount_to_withraw = 20
    account.withdraw(amount_to_withraw)
    expected_value = amount - amount_to_withraw
    #then
    assert account.balance == expected_value

def test_should_not_withdraw_incorrect_amount():
    #given
    history = AccountHistory()
    account = Account(history)
    amount = 50
    account.deposit(amount)
    #when
    amount_to_withraw = 70
    #then
    with pytest.raises(ValueError):
        account.withdraw(amount_to_withraw)
