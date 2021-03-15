import datetime
from functools import reduce


def group_expenses_by_category(expenses):
    grouped_expenses = dict()
    for key, value in expenses.items():
        if value.category not in grouped_expenses:
            grouped_expenses[value.category] = [value]
        else:
            grouped_expenses[value.category].append(value)
    return grouped_expenses


def compute_total_by_category(expenses_by_category):
    # return a list of tuples, where the first item is the category, and the second item is the total
    return list(map(lambda elem: (elem[0], reduce((lambda x, y: x.value + y.value), elem[1])), expenses_by_category.items()))


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
