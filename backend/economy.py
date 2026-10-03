class Economy:
    def __init__(self, starting_balance=10000):
        self.balance = starting_balance
        self.total_income = 0
        self.total_expenses = 0

    def earn(self, amount):
        self.balance += amount
        self.total_income += amount
        print(f"💰 AI earned ₹{amount}")

    def spend(self, amount):
        if amount > self.balance:
            print("❌ AI cannot afford this.")
            return False

        self.balance -= amount
        self.total_expenses += amount
        print(f"💸 AI spent ₹{amount}")

        return True

    def is_alive(self):
        return self.balance > 0

    def status(self):
        if self.is_alive():
            return "🟢 ALIVE"
        return "💀 DEAD"

    def show(self):
        print("\n========== AI ECONOMY ==========")
        print(f"Balance: ₹{self.balance}")
        print(f"Total income: ₹{self.total_income}")
        print(f"Total expenses: ₹{self.total_expenses}")
        print(f"Status: {self.status()}")
        print("================================\n")
