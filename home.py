from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from random_images import random_three

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    # parse random_three dict into names & image ids
    random_dict = random_three()
    titles_and_images = [v for k, v in random_dict.items()]
    return render_template('home.html', info = titles_and_images)
