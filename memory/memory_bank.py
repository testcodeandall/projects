# memory/memory_bank.py

class MemoryBank:
    def __init__(self):
        self.data = {}  # Store memory in memory during runtime

    def load(self):
        """Return the entire memory dictionary"""
        return self.data

    def save(self, new_data):
        """Update memory with new data"""
        self.data.update(new_data)

    def get_user_history(self, user_id):
        """Return history for a specific user"""
        return self.data.get(user_id, [])

    def append_user_day(self, user_id, day_data):
        """Append a day's plan to user's history"""
        if user_id not in self.data:
            self.data[user_id] = []
        self.data[user_id].append(day_data)
