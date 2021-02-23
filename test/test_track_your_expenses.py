import unittest
import datetime
from app.tracker import Tracker
from app.expense import Expense

class TestTrackYourExpenses(unittest.TestCase):
    def test_should_add_a_new_expense(self):
        tracker = Tracker()
        expense = Expense('spesa cibo', 12, datetime.date(2021, 2, 23))
        tracker.addExpense(expense)
        self.assertEqual(tracker.expenses['2021-02-23'], expense)

