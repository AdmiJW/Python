from __future__ import annotations
from typing import List

class Category:
    def __init__(self, category:str):
        self.category = category        #   Category name
        self.expenses = 0               #   Total expenses
        self.availableBal = 0           #   Available balance to withdraw
        self.ledger = []                #   Record of transactions

    #   Add balance into current account
    def deposit(self, amount: float, desc: str='' ) -> None:
        self.availableBal += amount
        self.ledger.append( {'amount': amount, 'description': desc} )

    #   Withdraw balance from current account. Return True if successfully withdrawn
    def withdraw(self, amount: float, desc: str='' ) -> bool:
        #   Insufficient funds
        if not self.check_funds(amount): return False

        self.availableBal -= amount
        self.expenses += amount
        self.ledger.append( {'amount': -amount, 'description': desc} )
        return True

    #   Return the current available balance
    def get_balance(self) -> float:
        return self.availableBal

    #   Transfer funds from this account to another account passed in as argument
    def transfer(self, amount:float, transTo: Category) -> bool:
        #   Insufficient funds
        if not self.withdraw(amount, 'Transfer to {}'.format(transTo.category) ):
            return False

        transTo.deposit(amount, 'Transfer from {}'.format(self.category) )
        return True

    #   Returns True if the amount to withdraw is sufficient, else False
    def check_funds(self, amount: float) -> bool:
        return self.availableBal >= amount

    #   Returns a string representing transaction record. Used in print statements or equivalent expressions
    def __str__(self):
        res = ''

        #   Line 1 - The name of category
        asteriskCnt = 15 - ( len(self.category) // 2 )
        res += ('*' * asteriskCnt) + (self.category) + ('*' * (asteriskCnt - (len(self.category) % 2 ) ) ) + '\n'

        #   Subsequent lines - Transaction Records
        for record in self.ledger:
            res += '{:23}{:>7.2f}\n'.format(record['description'][:23], record['amount'] )

        #   Last line - Total
        res += 'Total: {:.2f}'.format( self.availableBal )
        return res


#   Take in a LIST of category instances, will return a string representing bar chart showing how many percentage
#   spending each category is taking up
def create_spend_chart(categories: List) -> str:
    total = sum( x.expenses for x in categories )
    percentages = [ x.expenses * 100 / total for x in categories ]
    longeststr = max( len(x.category) for x in categories)

    #   First line
    res = 'Percentage spent by category\n'

    #   Percentages line
    for i in range(100, -1, -10):
        res += '{:>3}|'.format(i)
        for percent in percentages:
            res += ' o ' if percent >= i else '   '
        res += ' \n'

    #   X axis
    res += '    ' + ('---' * len(categories) ) + '-\n'

    #   Category names
    for i in range(longeststr):
        res += '    '
        for x in categories:
            res += ' {} '.format(x.category[i]) if i < len(x.category) else '   '
        res += ' \n' if i != longeststr - 1 else ' '

    return res

