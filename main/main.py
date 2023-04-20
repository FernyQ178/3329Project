class MealPlanner:
    def __init__(self):
        self.user_info = {}
        
    def collect_user_info(self):
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        dietary_restrictions = input("Please enter any dietary restrictions (separated by commas if multiple): ").split(",")
        allergies = input("Please enter any allergies (separated by commas if multiple): ").split(",")
        self.user_info = {
            "name": name,
            "age": age,
            "dietary_restrictions": dietary_restrictions,
            "allergies": allergies
        }
        
    def display_meal_suggestions(self):
        print(f"Hello {self.user_info['name']}, based on your age of {self.user_info['age']} and your dietary restrictions of {self.user_info['dietary_restrictions']} and allergies of {self.user_info['allergies']}, here are some meal suggestions:")
        # Logic to generate meal suggestions based on user info goes here
        
# Example usage
meal_planner = MealPlanner()
meal_planner.collect_user_info()
meal_planner.display_meal_suggestions()

# ----------------------------------------------------------------------------------------------------------

import random

# Define some lists of ingredients
proteins = ["chicken", "beef", "tofu", "fish"]
vegetables = ["broccoli", "carrots", "spinach", "peppers"]
starches = ["rice", "potatoes", "pasta", "quinoa"]
sauces = ["tomato", "cream", "teriyaki", "pesto"]

# Generate a random meal by choosing one item from each list
protein = random.choice(proteins)
vegetable = random.choice(vegetables)
starch = random.choice(starches)
sauce = random.choice(sauces)

# Print out the meal
print("Your random meal is:")
print(protein + " with " + vegetable + " and " + starch + " in a " + sauce + " sauce.")

