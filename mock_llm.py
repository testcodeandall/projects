# mock_llm.py
import random

class MockLLM:
    def generate(self, prompt):
        if "tasks" in prompt.lower():
            return "1. High priority tasks\n2. Medium priority tasks\n3. Low priority tasks"
        elif "meal" in prompt.lower():
            return "Breakfast: Oats\nLunch: Rice + Veg\nDinner: Chapati + Curry"
        elif "summary" in prompt.lower():
            return "Today you completed most tasks. Good job! Keep consistency tomorrow."
        else:
            return random.choice(["Processed successfully.", "Output generated.", "Done."])
