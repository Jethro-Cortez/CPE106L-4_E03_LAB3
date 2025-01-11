
class SavingsAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return f"SavingsAccount(name={self.name}, balance={self.balance})"
