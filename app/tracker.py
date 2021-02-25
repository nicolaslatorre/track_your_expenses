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

    def group_expenses_by_category(self, expenses):
        grouped_expenses = dict()
        for key, value in expenses.items():
            if value.category not in grouped_expenses:
                grouped_expenses[value.category] = [value]
            else:
                grouped_expenses[value.category].append(value)
        return grouped_expenses
