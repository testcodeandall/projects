# agents/meal_planner_agent.py

class MealPlannerAgent:
    def __init__(self):
        # Predefined 10 vegetarian meal plans
        self.veg_plans = [
            {"Breakfast": "Oats", "Lunch": "Rice + Veg", "Snack": "Fruit", "Dinner": "Chapati + Curry"},
            {"Breakfast": "Smoothie", "Lunch": "Quinoa + Veg", "Snack": "Nuts", "Dinner": "Veg Stir-fry"},
            {"Breakfast": "Pancakes", "Lunch": "Pasta + Veg", "Snack": "Yogurt", "Dinner": "Dal + Rice"},
            {"Breakfast": "Granola + Milk", "Lunch": "Salad + Bread", "Snack": "Apple", "Dinner": "Paneer Curry + Chapati"},
            {"Breakfast": "Poha", "Lunch": "Khichdi", "Snack": "Banana", "Dinner": "Veg Biryani"},
            {"Breakfast": "Idli + Sambar", "Lunch": "Curd Rice", "Snack": "Dry Fruits", "Dinner": "Chole + Roti"},
            {"Breakfast": "Toast + Peanut Butter", "Lunch": "Veg Wrap", "Snack": "Carrot Sticks", "Dinner": "Mushroom Curry + Rice"},
            {"Breakfast": "Upma", "Lunch": "Mixed Veg Curry + Rice", "Snack": "Orange", "Dinner": "Rajma + Roti"},
            {"Breakfast": "Cornflakes + Milk", "Lunch": "Veg Pulao", "Snack": "Dates", "Dinner": "Aloo Gobi + Chapati"},
            {"Breakfast": "Banana Smoothie", "Lunch": "Veg Sandwich", "Snack": "Papaya", "Dinner": "Palak Paneer + Rice"}
        ]

        # Predefined 10 non-vegetarian meal plans
        self.nonveg_plans = [
            {"Breakfast": "Eggs + Toast", "Lunch": "Chicken + Rice", "Snack": "Yogurt", "Dinner": "Fish Curry + Rice"},
            {"Breakfast": "Omelette", "Lunch": "Mutton Curry + Rice", "Snack": "Nuts", "Dinner": "Chicken Stir-fry"},
            {"Breakfast": "Paratha + Eggs", "Lunch": "Grilled Fish + Salad", "Snack": "Apple", "Dinner": "Chicken Biryani"},
            {"Breakfast": "Egg Sandwich", "Lunch": "Prawn Curry + Rice", "Snack": "Banana", "Dinner": "Mutton Stew"},
            {"Breakfast": "Scrambled Eggs", "Lunch": "Egg Curry + Rice", "Snack": "Dates", "Dinner": "Grilled Chicken + Veg"},
            {"Breakfast": "Egg Muffin", "Lunch": "Chicken Salad", "Snack": "Papaya", "Dinner": "Fish Fry + Rice"},
            {"Breakfast": "Oats + Milk + Egg", "Lunch": "Chicken Wrap", "Snack": "Carrot Sticks", "Dinner": "Prawn Pulao"},
            {"Breakfast": "Boiled Eggs + Toast", "Lunch": "Mutton Kebabs + Rice", "Snack": "Orange", "Dinner": "Egg Curry + Chapati"},
            {"Breakfast": "Egg Smoothie", "Lunch": "Grilled Chicken + Veg", "Snack": "Dry Fruits", "Dinner": "Fish Curry + Rice"},
            {"Breakfast": "Omelette + Toast", "Lunch": "Prawn Stir-fry", "Snack": "Nuts", "Dinner": "Chicken Curry + Roti"}
        ]

    def generate_meal_plan(self, diet_pref, plan_index):
        """Return the meal plan for the user based on diet and plan index"""
        if diet_pref.lower() == "vegetarian":
            return {"meals": self.veg_plans[plan_index % len(self.veg_plans)]}
        else:
            return {"meals": self.nonveg_plans[plan_index % len(self.nonveg_plans)]}
