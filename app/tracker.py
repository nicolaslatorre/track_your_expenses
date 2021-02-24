import datetime

class Tracker(object):
    expenses = dict()

    def __init__(self):
        pass

    def add_expense(self, expense):
        date = expense.date.__str__()
        self.expenses[date] = expense

    def get_expenses_by_month_and_year(self, month, year):
        return dict(filter(
            lambda elem:
            datetime.date.fromisoformat(elem[0]).month == month and
            datetime.date.fromisoformat(elem[0]).year == year,
            self.expenses.items()
        ))
