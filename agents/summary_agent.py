# agents/summary_agent.py

class SummaryAgent:
    def run(self, context, task_plan_str, meal_plan):
        tasks = context.get("tasks", [])
        num_tasks = len(tasks)
        completed_str = f"You have {num_tasks} tasks today."

        summary = (
            f"Summary:\n{completed_str}\n"
            "Today you completed most tasks. Good job! Keep consistency tomorrow."
        )
        return summary
