from recipe_api import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    ingredients = db.Column(db.String(1000), nullable=False)
    steps= db.Column(db.String(1000), nullable=False, default = 0.0)
    rate = db.Column(db.Float, nullable=False, default="/5 stars")

    def __init__(self, name, ingredients, steps,rate):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.rate = rate