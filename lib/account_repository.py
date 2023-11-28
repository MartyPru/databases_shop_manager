from lib.account import Account

class AccountRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM accounts;")
        accounts = []
        for row in rows:
            account = Account(row['id'], row['username'], row['email_address'])
            accounts.append(account)
        return accounts
    
    def find(self, account_id):
        match = self.connection.execute("SELECT * FROM accounts WHERE id = %s", [account_id])[0]
        account = Account(match['id'], match['username'], match['email_address'])
        return account