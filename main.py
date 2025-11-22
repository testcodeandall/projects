import asyncio
import json
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from orchestrator import orchestrate

console = Console()
HISTORY_FILE = "user_history.json"

# Load history
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        user_history = json.load(f)
else:
    user_history = {}

console.print("\n=== Welcome to DayPilot AI Personal Planner ===\n", style="bold green")

while True:
    console.print("\nChoose an action:", style="bold cyan")
    console.print("1. View history")
    console.print("2. Plan for new user")
    console.print("3. Exit")
    choice = console.input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        if not user_history:
            console.print("No users in history yet.", style="red")
            continue

        console.print("\nExisting users:", style="bold yellow")
        for uid in user_history.keys():
            console.print("-", uid, style="magenta")

        selected_ids = console.input("\nEnter user IDs to view (comma separated): ").strip()
        selected_ids = [uid.strip() for uid in selected_ids.split(",") if uid.strip()]

        for uid in selected_ids:
            if uid in user_history:
                console.print(Panel(f"=== History for User: {uid} ===", style="bold green"))
                for plan in user_history[uid]:
                    day = plan["day"]
                    console.print(f"\n[bold underline]Day {day} Plan[/bold underline]", style="cyan")

                    # Tasks Table
                    task_table = Table(title="Task Plan")
                    task_table.add_column("Priority", style="yellow")
                    task_table.add_column("Tasks", style="magenta")
                    tasks_dict = plan["tasks"]
                    if isinstance(tasks_dict, dict):
                        for prio, t_list in tasks_dict.items():
                            task_table.add_row(prio, ", ".join(t_list))
                    else:
                        task_table.add_row("Tasks", ", ".join(tasks_dict))
                    console.print(task_table)

                    # Meal Plan Table
                    meal_table = Table(title="Meal Plan", style="green")
                    meal_table.add_column("Meal", style="cyan")
                    meal_table.add_column("Menu", style="magenta")

                    meal_plan_data = plan["meal_plan"]
                    if isinstance(meal_plan_data, dict) and "meals" in meal_plan_data:
                        meal_plan_data = meal_plan_data["meals"]

                    if isinstance(meal_plan_data, dict):
                        for meal, menu in meal_plan_data.items():
                            meal_table.add_row(meal, str(menu))
                        console.print(meal_table)
                    else:
                        console.print(Panel(str(meal_plan_data), title="Meal Plan", style="green"))

                    # Calendar Table
                    calendar_data = plan["calendar"]
                    if isinstance(calendar_data, dict):
                        calendar_table = Table(title="Calendar", style="blue")
                        calendar_table.add_column("Time", style="cyan")
                        calendar_table.add_column("Tasks/Meals", style="magenta")
                        for time_slot, items in calendar_data.items():
                            if isinstance(items, list):
                                calendar_table.add_row(time_slot, ", ".join(items))
                            else:
                                calendar_table.add_row(time_slot, str(items))
                        console.print(calendar_table)
                    else:
                        console.print(Panel(str(calendar_data), title="Calendar", style="blue"))

                    # Summary
                    console.print(Panel(plan["summary"], title="Summary", style="bold green"))
            else:
                console.print(f"No history found for user ID: {uid}", style="red")

    elif choice == "2":
        while True:
            try:
                num_users = int(console.input("\nHow many users? "))
                if num_users <= 0:
                    console.print("Enter a valid positive number.", style="red")
                else:
                    break
            except ValueError:
                console.print("Please enter a number.", style="red")

        for i in range(num_users):
            while True:
                user_id = console.input(f"\nEnter user {i+1} ID/name: ").strip()
                if user_id in user_history:
                    console.print("User ID already exists. Please enter a unique ID.", style="red")
                else:
                    break

            tasks_input = console.input(f"Enter tasks for {user_id} (comma separated): ").strip()
            tasks = [t.strip() for t in tasks_input.split(",") if t.strip()]

            while True:
                diet_pref = console.input(f"Enter diet preference for {user_id} (veg/non veg): ").strip().lower()
                if diet_pref in ["veg", "non veg"]:
                    break
                else:
                    console.print("Invalid input. Please enter 'veg' or 'non veg'.", style="red")

            while True:
                try:
                    num_days = int(console.input("\nEnter number of days to plan: "))
                    if num_days <= 0:
                        console.print("Enter a valid positive number.", style="red")
                    else:
                        break
                except ValueError:
                    console.print("Please enter a number.", style="red")

            user_history[user_id] = []

            for day in range(1, num_days + 1):
                console.print(f"\n=== Planning Day {day} for {user_id} ===", style="bold green")
                context = {
                    "user_id": user_id,
                    "tasks": tasks,
                    "diet_pref": diet_pref,
                    "day": day
                }

                result = asyncio.run(orchestrate(context))

                # Ensure tasks stored as dictionary with priorities
                tasks_with_priority = result["tasks"] if isinstance(result["tasks"], dict) else {
                    "High Priority": result["tasks"][:len(result["tasks"])//3],
                    "Medium Priority": result["tasks"][len(result["tasks"])//3:2*len(result["tasks"])//3],
                    "Low Priority": result["tasks"][2*len(result["tasks"])//3:]
                }

                # Save plan in history
                user_history[user_id].append({
                    "day": day,
                    "tasks": tasks_with_priority,
                    "meal_plan": result["meal_plan"],
                    "calendar": result["calendar"],
                    "summary": result["summary"]
                })

    elif choice == "3":
        break
    else:
        console.print("Invalid choice. Please enter 1, 2, or 3.", style="red")

# Save history
with open(HISTORY_FILE, "w") as f:
    json.dump(user_history, f, indent=4)

console.print("\nAll user plans saved in memory and history file.", style="bold green")
console.print("\n=== Thank you for using DayPilot! ===", style="bold cyan")
