from date import datetime
from date import date, datetime
xercler=[]
class Expense:
        def __init__(self, amount, target, date):
            self.amount=amount
            self.target=target
            self.date=date
        def printExpense(self):
            print(f'{self.date} tarixinde {self.target} meqsedile {self.amount} qeder pul xerclenilib')
xercler.append(
    Expense(98, 'kitab', datetime.now()),
    Expense(198, 'telefon', datetime.now()),
    Expense(200,'hediyye',dtaetime.now()),
    Expense(20,'kseroks', datetime.now())
)                                     