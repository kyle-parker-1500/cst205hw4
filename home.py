from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from random_images import random_three
from PIL import Image

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    # parse random_three dict into names & image ids
    random_dict = random_three()
    
    # changing each image to have uniform size
    
    titles_and_images = [v for k, v in random_dict.items()]
    return render_template('index.html', info = titles_and_images)

## todo: images uniform size on home page
## todo: make each image interactable
