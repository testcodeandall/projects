
class TaskAgent:
    def run(self, context):
        tasks = context.get("tasks", [])
        high = tasks[:3]
        medium = tasks[3:6]
        low = tasks[6:]
        task_plan_str = (
            f"High Priority:\n{', '.join(high)}\n"
            f"Medium Priority:\n{', '.join(medium)}\n"
            f"Low Priority:\n{', '.join(low)}"
        )
        return task_plan_str
