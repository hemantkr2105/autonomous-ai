import random
from economy import Economy


class AI:

    def __init__(self, ai_id="AI-001"):
        self.ai_id = ai_id
        self.goal = "Survive and grow capital"
        self.work = "Looking for opportunities"

        self.economy = Economy(10000)

        self.memory = []

    def observe(self):
        print("\n👁️ OBSERVING")
        print(f"Capital: ₹{self.economy.balance}")
        print(f"Income: ₹{self.economy.total_income}")
        print(f"Expenses: ₹{self.economy.total_expenses}")

    def think(self):
        print("\n🧠 THINKING")

        actions = [
            "work",
            "research",
            "save"
        ]

        decision = random.choice(actions)

        print(f"Decision: {decision}")

        return decision

    def act(self, decision):

        print("\n⚙️ ACTING")

        if decision == "work":

            self.work = "Working on a business opportunity"

            income = random.randint(500, 2000)

            self.economy.earn(income)

            self.memory.append(
                f"Worked and earned ₹{income}"
            )

        elif decision == "research":

            self.work = "Researching money-making opportunities"

            cost = random.randint(100, 500)

            self.economy.spend(cost)

            self.memory.append(
                f"Research cost ₹{cost}"
            )

        elif decision == "save":

            self.work = "Saving capital"

            self.memory.append(
                "Saved capital"
            )

            print("🏦 AI decided to save.")

    def is_alive(self):
        return self.economy.is_alive()

    def show(self):

        print("\n================================")
        print(f"🤖 {self.ai_id}")
        print("================================")

        print(f"Goal: {self.goal}")
        print(f"Current work: {self.work}")

        self.economy.show()

        print(f"🧠 Memories: {len(self.memory)}")
