import unittest
import datetime
from app.tracker import Tracker, group_expenses_by_category
from app.expense import Expense


class TestTrackYourExpenses(unittest.TestCase):
    def test_should_add_a_new_expense(self):
        tracker = Tracker()
        expense = Expense("spesa cibo", 12, datetime.date(2021, 2, 23))
        tracker.add_expense(expense)
        self.assertEqual(tracker.expenses["2021-02-23"], expense)

    def test_should_retrieve_expenses_for_a_specific_month_number_2(self):
        tracker = Tracker()
        expense1 = Expense("cibo", 40, datetime.date(2021, 2, 14))
        expense2 = Expense("spesa cibo", 12, datetime.date(2021, 2, 23))
        expense3 = Expense("spesa cibo", 12, datetime.date(2021, 3, 3))
        tracker.add_expense(expense1)
        tracker.add_expense(expense2)
        tracker.add_expense(expense3)
        expenses = tracker.get_expenses_by_month_and_year(2, 2021)
        self.assertEqual(True, expense1 in expenses.values())
        self.assertEqual(True, expense2 in expenses.values())
        self.assertEqual(False, expense3 in expenses.values())

    def test_should_retrieve_expenses_for_a_specific_month_number_3(self):
        tracker = Tracker()
        expense1 = Expense("cibo", 40, datetime.date(2021, 2, 14))
        expense2 = Expense("spesa cibo", 12, datetime.date(2021, 2, 23))
        expense3 = Expense("spesa cibo", 12, datetime.date(2021, 3, 3))
        tracker.add_expense(expense1)
        tracker.add_expense(expense2)
        tracker.add_expense(expense3)
        expenses = tracker.get_expenses_by_month_and_year(3, 2021)
        self.assertEqual(False, expense1 in expenses.values())
        self.assertEqual(False, expense2 in expenses.values())
        self.assertEqual(True, expense3 in expenses.values())

    def test_should_return_an_empty_dictionary_if_no_expenses_are_available_for_a_specific_month(self):
        tracker = Tracker()
        expense1 = Expense("cibo", 40, datetime.date(2021, 2, 14))
        expense2 = Expense("spesa cibo", 12, datetime.date(2021, 2, 23))
        expense3 = Expense("spesa cibo", 12, datetime.date(2021, 3, 3))
        tracker.add_expense(expense1)
        tracker.add_expense(expense2)
        tracker.add_expense(expense3)
        expenses = tracker.get_expenses_by_month_and_year(4, 2021)
        self.assertEqual(True, len(expenses.keys()) == 0)

    def test_should_group_expenses_by_category(self):
        tracker = Tracker()
        expense1 = Expense("spesa cibo", 40, datetime.date(2021, 2, 14))
        expense2 = Expense("spesa cibo", 12, datetime.date(2021, 2, 23))
        expense3 = Expense("benzina", 20, datetime.date(2021, 2, 26))
        tracker.add_expense(expense1)
        tracker.add_expense(expense2)
        tracker.add_expense(expense3)
        expenses = tracker.get_expenses_by_month_and_year(2, 2021)
        grouped_expenses = group_expenses_by_category(expenses)
        self.assertEqual(True, expense1 in grouped_expenses["spesa cibo"])
        self.assertEqual(True, expense2 in grouped_expenses["spesa cibo"])
        self.assertEqual(True, expense3 in grouped_expenses["benzina"])


