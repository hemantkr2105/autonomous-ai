import ollama


class Brain:

    def __init__(self, model="qwen3:4b"):
        self.model = model

    def think(self, situation):

        prompt = f"""
You are the decision-making brain of an autonomous AI economic agent.

Your objective:
Survive and grow your capital.

You are operating in a simulated economy.

You must consider:
- current capital
- income
- expenses
- previous actions
- previous results
- risk
- whether spending is justified

You are NOT guaranteed to make money.
You may spend money and fail.
You must learn from outcomes.

CURRENT SITUATION:

{situation}

Choose exactly ONE action from:

WORK
RESEARCH
SAVE

Respond with ONLY the action name.
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        decision = response["message"]["content"].strip().upper()

        if decision not in ["WORK", "RESEARCH", "SAVE"]:
            decision = "SAVE"

        return decision
