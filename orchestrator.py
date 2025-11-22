from agents.task_agent import TaskAgent
from agents.meal_planner_agent import MealPlannerAgent
from agents.calendar_agent import CalendarAgent
from agents.summary_agent import SummaryAgent

import asyncio

async def orchestrate(context):
    tasks = context.get("tasks", [])
    diet_pref = context.get("diet_pref", "vegetarian")
    day = context.get("day", 1)

    # Initialize agents
    task_agent = TaskAgent()
    meal_agent = MealPlannerAgent()
    calendar_agent = CalendarAgent()
    summary_agent = SummaryAgent()

    # Task plan
    task_plan_str = task_agent.run(context)

    # Meal plan feedback loop
    meal_plan_index = 0
    max_plans = 10
    while True:
        meal_plan = meal_agent.generate_meal_plan(diet_pref, meal_plan_index)
        print(f"\n===== DAY {day} MEAL PLAN {meal_plan_index + 1} =====")

        # Calendar
        calendar_str = calendar_agent.run(context, task_plan_str, meal_plan)

        # Summary
        summary_str = summary_agent.run(context, task_plan_str, meal_plan)

        # Show output
        print(f"\n--- Task Plan ---\n{task_plan_str}")
        print(f"\n--- Meal Plan ---\nBreakfast: {meal_plan['meals']['Breakfast']}\n"
              f"Lunch: {meal_plan['meals']['Lunch']}\n"
              f"Snack: {meal_plan['meals']['Snack']}\n"
              f"Dinner: {meal_plan['meals']['Dinner']}")
        print(f"\n--- Calendar ---\n{calendar_str}")
        print(f"\n--- Summary ---\n{summary_str}")

        # Ask feedback
        feedback = input("\nDid you like the meal plan? (yes/no/too many tasks): ").strip().lower()
        if feedback == "yes":
            break
        else:
            meal_plan_index += 1
            if meal_plan_index >= max_plans:
                # Show all 10 meal plans for selection
                print("\nYou have rejected all 10 meal plans. Please select from below:")
                for i in range(max_plans):
                    plan = meal_agent.generate_meal_plan(diet_pref, i)
                    print(f"{i+1}: Breakfast: {plan['meals']['Breakfast']}, "
                          f"Lunch: {plan['meals']['Lunch']}, "
                          f"Snack: {plan['meals']['Snack']}, "
                          f"Dinner: {plan['meals']['Dinner']}")
                while True:
                    choice = input(f"Enter the number of the meal plan you like (1-{max_plans}): ").strip()
                    if choice.isdigit() and 1 <= int(choice) <= max_plans:
                        meal_plan_index = int(choice) - 1
                        meal_plan = meal_agent.generate_meal_plan(diet_pref, meal_plan_index)
                        break
                    else:
                        print("Invalid choice. Try again.")
                break

    return {
        "task_plan": task_plan_str,
        "meal_plan": meal_plan,
        "calendar": calendar_str,
        "summary": summary_str
    }
