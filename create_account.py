"""
Methods in class to create account
"""

import os
import json


class CreateAccount:
    """
    Create account methods
    """
    def create_account(self, dob, aadhar_card, pin, account_details={}):
        """
        Method to create account
        """
        accountnumber = aadhar_card[-3:] + dob.replace('-', '') + pin[1:4]
        accountnumber = str(accountnumber)

        if os.path.exists('bank_account_details.json'):
            with open('bank_account_details.json', 'r', encoding='utf8') as fobj:
                data = json.load(fobj)
            if accountnumber in data.keys():
                raise Exception("Account Number Already Exists !!!")
        else:
            data = {}

        data.update({
                    accountnumber: {
                        "sur_name": account_details.get('surname'),
                        "first_name": account_details.get('firstname'),
                        "dob": dob,
                        "aadhar_card": aadhar_card,
                        "pin": pin,
                        "current_balance":  5000,
                        "previous_balance": 0,
                        "last_transaction_info": [],
                        "transaction_history": []
                    }
                    })

        with open('bank_account_details.json', 'w', encoding='utf8') as convert_file:
            convert_file.write(json.dumps(data))

        print("YOUR BANK ACCOUNT HAS BEEN SUCCESSFULLY CREATED : " +
              accountnumber)
