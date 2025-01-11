from savingsaccount import SavingsAccount

class Bank:
    def __init__(self):
        self.accounts = []  # Initialize an empty list to store bank accounts

    def add_account(self, account):
        self.accounts.append(account)  # Append the new account to the accounts list

    def __str__(self):
        sorted_accounts = sorted(self.accounts)  # Sort the accounts for display
        return "\n".join(str(account) for account in sorted_accounts)  # Return a string representation of sorted accounts

def main():
    bank = Bank()  # Create an instance of the Bank class
    num_accounts = int(input("Enter the number of accounts: "))  # Prompt user for the number of accounts
    
    for _ in range(num_accounts):
        name = input("Enter account holder's name: ")  # Get the account holder's name
        balance = float(input("Enter account balance: "))  # Get the account balance as a float
        bank.add_account(SavingsAccount(name, balance))  # Create a SavingsAccount and add it to the bank

    print(bank)  # Print the bank's accounts

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly
