import sqlite3  # Import SQLite to manage database operations

class BankAccount:
    def __init__(self, user_id):
        self.user_id = user_id  # Store the user's ID
        self.conn = sqlite3.connect('bank.db')  # Connect to the SQLite database file
        self.cursor = self.conn.cursor()  # Create a cursor object to interact with the database
        self.create_table()  # Ensure the accounts table exists

    def create_table(self):
        # Create the accounts table if it doesn't exist already
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                user_id TEXT PRIMARY KEY,
                balance REAL DEFAULT 0.0
            )
        ''')
        self.conn.commit()  # Save changes to the database

    def create_account(self):
        # Add a new account if it doesn't already exist
        self.cursor.execute('INSERT OR IGNORE INTO accounts (user_id, balance) VALUES (?, ?)', (self.user_id, 0.0))
        self.conn.commit()

    def deposit(self, amount):
        # Add funds to the account balance
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        self.cursor.execute('UPDATE accounts SET balance = balance + ? WHERE user_id = ?', (amount, self.user_id))
        self.conn.commit()
        print(f"Deposited ${amount:.2f} successfully.")

    def withdraw(self, amount):
        # Withdraw funds if enough balance exists
        if amount <= 0:s
            print("Amount must be greater than zero.")
            return
        self.cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (self.user_id,))
        balance = self.cursor.fetchone()[0]

        if balance >= amount:
            self.cursor.execute('UPDATE accounts SET balance = balance - ? WHERE user_id = ?', (amount, self.user_id))
            self.conn.commit()
            print(f"Withdrew ${amount:.2f} successfully.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        # Retrieve and return the user's balance
        self.cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (self.user_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            print("Account not found.")
            return 0.0



    # TODO: Add the following functions:
    # def deposit(self, amount):
    # def withdraw(self, amount):
    # def get_balance(self):