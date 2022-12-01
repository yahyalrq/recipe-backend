from flask import Flask, request
from recipe_api import app,db
from recipe_api.models import Recipe


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/recipes', methods=['POST'])
def create_recipe():
    name = request.json['name']
    ingredients = request.json['ingredients']
    steps = request.json['steps']
    rate = request.json['rate']
    recipe = Recipe(name, ingredients,steps, rate)
    db.session.add(recipe)
    db.session.commit()
    return format_recipe(recipe)


@app.route('/recipes', methods=['GET'])
def get_accounts():
    accounts = Recipe.query.all()
    return {'recipes': [format_recipe(account) for account in accounts]}


@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return format_recipe(recipe)


@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    db.session.commit()
    return format_recipe(recipe)


@app.route('/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)


def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'steps': recipe.steps,
        'rate': recipe.rate,
    }
