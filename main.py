# def a_func():
#     container=[]
#     container.append(1)
#     print(container)

# a_func()
# a_func()

# def a_func2(container=[]):
#     container.append(1)
#     print(container)

# a_func2()
# a_func2()
# a_func2()

from banking import Account, AccountHistory

history = AccountHistory()
account1 = Account(history)
account1.deposit(50)
account1.deposit(100)
account1.withdraw(30)
account1.withdraw(40)
account1.print_history()