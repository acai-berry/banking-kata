from dataclasses import dataclass, field
from datetime import datetime
from typing import TypeAlias
import enum
from tabulate import tabulate


Money: TypeAlias = float

class AccountOperations(enum.Enum):
    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'

@dataclass
class AccountEvent:
    date: datetime.date
    amount: Money
    balance: Money

    def __iter__(self):
        yield from self.events_history

@dataclass
class AccountHistory:
    events_history: list[AccountEvent] = field(default_factory=list)

    def add_event(self, event: AccountEvent):
        self.events_history.append(event)

    #napisac metode iter, zeby dalo sie iterowac 
    def __iter__(self):
        yield from self.events_history

@dataclass
class Account:
    history: AccountHistory
    balance: Money = 0

    def deposit(self, amount: Money):
        self.balance += amount
        event = AccountEvent(date=datetime.now().date(), amount=amount, balance=self.balance)
        self.history.add_event(event=event)

    def withdraw(self, amount: Money):
        if amount > self.balance:
            raise ValueError
        self.balance -= amount
        event = AccountEvent(date=datetime.now().date(), amount=-amount, balance=self.balance)
        self.history.add_event(event=event)

    def print_history(self):
        # event_lists = []
        # for event in self.history.events_history:
        #     event_lists.append([event.date, event.amount, event.balance])
        # print(tabulate(event_lists, headers=["Date", "Amount", "Balance"]))
        print(tabulate(self.history.events_history, headers=["Date", "Amount", "Balance"]))




        
        