
import os
import json


class DeleteAccount:

    def delete_account(self, accountnumber):
        if os.path.exists('bank_account_details.json'):
            with open('bank_account_details.json', 'r') as fobj:
                data = json.load(fobj)
                del data[accountnumber]

        with open('bank_account_details.json', 'w') as convert_file:
            convert_file.write(json.dumps(data))
