"""
Fredy Perez Vicente
Lab 8, unittest
Sep 29, 2025
"""
import unittest
from bankaccount import BankAccount

print("\n---- LAB EXERCISE: Bank Account ----")
class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Creating default Bank Account instance
        self.account = BankAccount(owner="Jordan", balance=50.0)

    def test_initial_balance(self):
        # Bank account balance initialization
        self.assertEqual(self.account.get_balance(), 50.0)

    def test_deposit(self):
        # Test that deposit adds to balance
        self.account.deposit(125.0)
        self.assertEqual(self.account.get_balance(), 175.0) # 50 + 125 = 175

    def test_withdraw(self):
        # Test that withdrawal subtracts from balance
        self.account.withdraw(30.0)
        self.assertEqual(self.account.get_balance(), 20.0) # 50 - 30 = 20

    def test_withdraw_more_than_balance(self):
        # Test that withdrawing more than the balance ammount raises ValueError
        with self.assertRaises(ValueError):
            self.account.withdraw(70.0)

    def test_sequence_of_transactions(self):
        # Testing a series of deposits and withdrawals
        self.account.deposit(100.0)  # Balance: 150
        self.account.withdraw(50.0)  # Balance: 100
        self.account.deposit(25.0)   # Balance: 125
        self.account.withdraw(75.0)  # Balance: 50
        self.assertEqual(self.account.get_balance(), 50.0)

if __name__ =="__main__":
    unittest.main()