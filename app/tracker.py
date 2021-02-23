class Tracker(object):
    expenses = dict()

    def __init__(self):
        pass

    def addExpense(self, expense):
        date = expense.date.__str__()
        self.expenses[date] = expense
