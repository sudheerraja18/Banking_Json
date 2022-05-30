"""
Main class where execution starts
"""

import sys
import logging

from datetime import date
from transaction import Transaction
from create_account import CreateAccount
from delete_account import DeleteAccount

logging.basicConfig(filename="logging.log", format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()


class MainClass:
    """
    Main method
    """
    def main_method(self):
        """
        Main method do transactions based on inputs
        """
        transaction_obj = Transaction()
        print("Please Select The Option In Below ...  \n1. New Customer \n2. \
Existing Customer \n3. Delete Customer \n")
        option = int(input("Enter The Option : "))

        if option == 1:
            print("To Create New Customer Account... Please Enter The \
Following Data...")

            string_pattern = '^[a-zA-Z]+$'
            surname = input("Enter Surname : ")
            result = transaction_obj.validate_inputs(string_pattern, surname)
            while not result:
                surname = input("Surname Should Contains Only Alphabets... \
Please Enter Only Alphabets ")
                result = transaction_obj.validate_inputs(string_pattern,
                                                         surname)
            firstname = input("Enter Firstname : ")
            result = transaction_obj.validate_inputs(string_pattern,
                                                     firstname)
            while not result:
                firstname = input("Firstname Should Contains Only Alphabets \
... Please Enter Only Alphabets ")
                result = transaction_obj.validate_inputs(string_pattern,
                                                         firstname)

            dob_pattern = r'^\d{2}-\d{2}-\d{4}$'
            dateofbirth = input("Enter DOB in dd-mm-yyyy Format : ")
            result = transaction_obj.validate_inputs(dob_pattern, dateofbirth)
            while not result:
                dateofbirth = input("DOB Should be in dd-mm-yyyy Format ...\
Please Enter Again : ")
                result = transaction_obj.validate_inputs(dob_pattern,
                                                         dateofbirth)
            age = transaction_obj.calculate_age(date(int(dateofbirth.
                                                split('-')[2]),
                                                int(dateofbirth.split('-')[1]),
                                                int(dateofbirth.
                                                    split('-')[0])))
            if age > 18:
                print("************** AGE GREATER THAN 18... YOU ARE ELIGIBLE \
FOR NEW ACCOUNT CREATION **************")
            else:
                print("To Open Account ..... Age Should Be Greater Than 18")
                logger.info("To Open Account ..... Age Should Be Greater \
                             Than 18")
                sys.exit(0)

            aadhar_pattern = r'^\d{4}-\d{4}-\d{4}$'
            aadhar_num = input("Enter Aadhar Number in xxxx-xxxx-xxxx Format \
: ")
            result = transaction_obj.validate_inputs(aadhar_pattern,
                                                     aadhar_num)
            while not result:
                aadhar_num = input("Aadhar Should be in xxxx-xxxx-xxxx Format \
                ... Please Enter Again")
                result = transaction_obj.validate_inputs(aadhar_pattern,
                                                         aadhar_num)

            pin_pattern = r'^\d{6}$'
            pin_num = input("Enter Pin Number in xxxxxx Format : ")
            result = transaction_obj.validate_inputs(pin_pattern, pin_num)
            while not result:
                pin_num = input("Pin Should be in xxxxxx Format ... Please\
                                 Enter Again")
                result = transaction_obj.validate_inputs(pin_pattern, pin_num)

            create_account_obj = CreateAccount()
            account_details = {'surname': surname, 'firstname': firstname}
            create_account_obj.create_account(dateofbirth, aadhar_num,
                                              pin_num, account_details)
        elif option == 2:
            account_number = input("To Do Operations On Existing Customer...\
Please Enter Account Number : ")
            if transaction_obj.validate_customer(account_number):
                print("\n***** Account Exists *****")
                print("\nPlease Select The Option In Below ... \n1. Check \
Balance \n2. Deposit Amount \n3. Withdraw \
Amount\n4. Display Transactions\n")
                user_option = input("Enter The Option : ")
                if user_option == '1':
                    current_balance = transaction_obj.\
                        check_balance(account_number)
                    print("Current Balance : "+str(current_balance)+"\n")
                elif user_option == '2':
                    transaction_type = "Deposited"
                    amount = int(input("Enter Amount To Deposit : "))
                    transaction_obj.deposit_amount(account_number, amount)
                    transaction_obj.transaction_update(account_number,
                                                       transaction_type,
                                                       amount)
                elif user_option == '3':
                    transaction_type = "Withdrawn"
                    amount = int(input("Enter Amount To Withdraw : "))
                    current_balance = transaction_obj.\
                        check_balance(account_number)
                    if current_balance > 5000:
                        withdrawable_balance = current_balance - 5000
                        if withdrawable_balance >= amount:
                            transaction_obj.withdraw_amount(account_number,
                                                            amount)
                            transaction_obj. \
                                transaction_update(account_number,
                                                   transaction_type,
                                                   amount)
                        else:
                            print("Withdrawable Balance Only : ",
                                  withdrawable_balance)
                    else:
                        print("Amount Available is < 5000 ... \
Hence Withdrawl Not Permitted")
                elif user_option == '4':
                    transaction_list = []
                    transaction_list = transaction_obj.\
                        get_transaction_history(account_number)
                    for transaction in transaction_list:
                        print(transaction)
                    current_balance = transaction_obj. \
                        check_balance(account_number)
                    print("\nCurrent Balance : "+str(current_balance) + "\n")
            else:
                print("Account Does Not Exists")
                logger.info("Account Does Not Exists")
        elif option == 3:
            delete_account_obj = DeleteAccount()
            account_number = input("Please Enter The Customer Number, To \
Delete The Customer : ")

            if transaction_obj.validate_customer(account_number):
                delete_account_obj.delete_account(account_number)
                if not transaction_obj.validate_customer(account_number):
                    print("\nCustomer number deleted")
                else:
                    print("\nCustomer number not deleted")
            else:
                print("\nCustomer number does not exist")
                logger.info("\nCustomer number does not exist...\
To delete the account")
        else:
            pass


mainObj = MainClass()
mainObj.main_method()
