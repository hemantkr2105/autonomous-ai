from economy import Economy
from brain import Brain


class AI:

    def __init__(self, ai_id="AI-001"):

        self.ai_id = ai_id
        self.goal = "Survive and grow capital"
        self.work = "Looking for opportunities"

        self.economy = Economy(10000)

        self.memory = []

        # AI brain
        self.brain = Brain()

    def observe(self):

        print("\n👁️ OBSERVING")

        print(f"Capital: ₹{self.economy.balance}")
        print(f"Income: ₹{self.economy.total_income}")
        print(f"Expenses: ₹{self.economy.total_expenses}")

    def think(self):

        print("\n🧠 THINKING")

        situation = f"""
AI ID: {self.ai_id}

Goal:
{self.goal}

Current capital:
₹{self.economy.balance}

Total income:
₹{self.economy.total_income}

Total expenses:
₹{self.economy.total_expenses}

Previous memories:
{self.memory[-5:]}
"""

        decision = self.brain.think(situation)

        print(f"AI Decision: {decision}")

        return decision

    def act(self, decision):

        print("\n⚙️ ACTING")

        if decision == "WORK":

            self.work = "Working on a business opportunity"

            income = 0

            print("AI is attempting to generate income...")

            # Temporary simulation
            # Later this will be replaced with real business experiments
            self.economy.earn(income)

            self.memory.append(
                "Attempted to work. No guaranteed income."
            )

        elif decision == "RESEARCH":

            self.work = "Researching money-making opportunities"

            cost = 300

            if self.economy.spend(cost):

                self.memory.append(
                    f"Spent ₹{cost} researching opportunities."
                )

        elif decision == "SAVE":

            self.work = "Preserving capital"

            self.memory.append(
                "Decided to preserve capital."
            )

            print("🏦 AI decided to save capital.")

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

   
