"""
   Transaction methods
"""

import re
import json

from datetime import date, datetime

"""
Class where all transactions methods are placed
"""


class Transaction:
    """
    Transactions methods
    """

    def deposit_amount(self, account_number, amount):
        """
        Method to deposit amount
        """
        data = self.get_account_details()
        print("Balance Before Deposit : " + str(data[account_number]['current_balance']))
        data[account_number]['previous_balance'] = \
            data[account_number]['current_balance']
        last_transaction_info = "Deposit of {}".format(amount)
        data[account_number]['last_transaction_info'] = last_transaction_info
        amount_after_deposit = data[account_number]['current_balance'] + amount
        data[account_number]['current_balance'] = amount_after_deposit
        print("Balance After Deposit : " + str(data[account_number]['current_balance']))
        self.update_account_details(data)

    def withdraw_amount(self, account_number, amount):
        """
        Method to withdraw amount
        """
        data = self.get_account_details()
        print("Balance Before Withdraw : " + str(data[account_number]['current_balance']))
        data[account_number]['previous_balance'] = \
            data[account_number]['current_balance']
        last_transaction_info = "Withdraw of {}".format(amount)
        data[account_number]['last_transaction_info'] = last_transaction_info
        amount_after_withdrawn = data[account_number]['current_balance'] - \
            amount
        data[account_number]['current_balance'] = amount_after_withdrawn
        print("Balance After Withdraw : " + str(data[account_number]['current_balance']))
        self.update_account_details(data)

    def get_account_details(self):
        """
        Method to get account details
        """
        with open('bank_account_details.json', 'r', encoding='utf8') as fobj:
            data = json.load(fobj)
        return data

    def update_account_details(self, data):
        """
        Method to update account details
        """
        with open('bank_account_details.json', 'w', encoding='utf8') as \
                convert_file:
            convert_file.write(json.dumps(data))

    def get_current_date_time(self):
        """
        Method to get current date and time
        """
        current_time = datetime.now()
        return current_time

    def check_balance(self, account_number):
        """
        Method to check balance
        """
        data = self.get_account_details()
        return data[account_number]['current_balance']

    def transaction_update(self, account_number, transaction, amt):
        """
        Method for transaction update
        """
        data = self.get_account_details()
        tmp_str = transaction + " : " + str(amt) + " on " + \
            str(self.get_current_date_time())
        data[account_number]['transaction_history'].append(tmp_str)
        self.update_account_details(data)

    def get_transaction_history(self, account_number):
        """
        Method for transaction history
        """
        data = self.get_account_details()
        return data[account_number]['transaction_history']

    def validate_customer(self, account_number):
        """
        Method to validate customer
        """
        data = self.get_account_details()
        if account_number in data.keys():
            return True
        return False

    def calculate_age(self, birth_date):
        """
        Method to calculate age
        """
        today = date.today()
        age = today.year - birth_date.year - \
            ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def validate_inputs(self, pattern, input_value):
        """
        Method to validate inputs
        """
        result = re.match(pattern, input_value)
        if result:
            return True
        return False
