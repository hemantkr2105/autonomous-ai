from agent import AI
import time


ai = AI()

print("🚀 AUTONOMOUS AI ECONOMY STARTED")

for cycle in range(10):

    if not ai.is_alive():
        print("\n💀 AI-001 HAS DIED")
        break

    print(f"\n\n========== CYCLE {cycle + 1} ==========")

    ai.observe()

    decision = ai.think()

    ai.act(decision)

    ai.show()

    time.sleep(2)

print("\n🏁 SIMULATION FINISHED")
