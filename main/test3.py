from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        restrictions = request.form.getlist('restrictions')
        meal = generate_meal(restrictions)
        #return render_template('meal.html', meal=meal)
        return render_template('dietary_restrictions.html')
    #return render_template('meal.html', meal=meal)

@app.route('/meal', methods=['GET', 'POST'])
def meal():
    if request.method == 'POST':
        restrictions = request.form.getlist('restrictions')
        meal = generate_meal(restrictions)
        return render_template('meal.html', meal=meal)
    

def generate_meal(restrictions):
    meals = [
        {'name': 'Grilled salmon with asparagus', 'restrictions': ['gluten-free', 'nut-free']},
        {'name': 'Roasted vegetable stir-fry', 'restrictions': ['vegetarian', 'vegan']},
        {'name': 'Spaghetti with meat sauce', 'restrictions': ['nut-free']},
        {'name': 'Carrot Soup', 'restrictions': ['gluten-free', 'nut-free', 'vegetarian']}
    ]

    available_meals = []
    for meal in meals:
        if all(restriction in meal['restrictions'] for restriction in restrictions):
            available_meals.append(meal)

    # if len(available_meals) > 0:
    #     meal_name = available_meals[0]['name']
    #     recipe = available_meals[0]['recipe']
    #     return meal_name, recipe

    if len(available_meals) == 0:
        return 'No meals available with these restrictions'

    return random.choice(available_meals)['name']

if __name__ == '__main__':
    app.run(debug=True)
# hello