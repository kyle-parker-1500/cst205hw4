from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from random_images import random_three

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    # parse random_three dict into names & image ids
    ids = [i for i in random_three().values]
    return render_template('home.html', pasta = one_pot_recipes)
