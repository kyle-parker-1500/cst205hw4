from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from pasta import one_pot_recipes

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
  return render_template('home.html', pasta = one_pot_recipes)

@app.route('/random')
def random():
    return render_template('home.html')
    # return render_template('home.html', file_path = get_random())
