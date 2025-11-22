# agents/calendar_agent.py

class CalendarAgent:
    def run(self, context, task_plan_str, meal_plan):
        tasks = context.get("tasks", [])
        meals = meal_plan.get("meals", {})

        # Split tasks dynamically into Morning, Afternoon, Evening
        num_tasks = len(tasks)
        if num_tasks == 0:
            morning_tasks = afternoon_tasks = evening_tasks = []
        else:
            morning_tasks = tasks[:max(1, num_tasks // 3)]
            afternoon_tasks = tasks[max(1, num_tasks // 3):2 * (num_tasks // 3)]
            evening_tasks = tasks[2 * (num_tasks // 3):]

        calendar = (
            "--- Daily Calendar ---\n\n"
            f"Morning Tasks: {', '.join(morning_tasks) if morning_tasks else 'None'}\n"
            f"Breakfast: {meals.get('Breakfast', '')}\n"
            f"Afternoon Tasks: {', '.join(afternoon_tasks) if afternoon_tasks else 'None'}\n"
            f"Lunch: {meals.get('Lunch', '')}\n"
            f"Snack: {meals.get('Snack', '')}\n"
            f"Evening Tasks: {', '.join(evening_tasks) if evening_tasks else 'None'}\n"
            f"Dinner: {meals.get('Dinner', '')}"
        )
        return calendar
