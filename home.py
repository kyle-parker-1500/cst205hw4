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
    info = list(random_dict.items())

    return render_template('index.html', info=info)

@app.route('/detail/<id>')
def detail(id):
    image = random_three()

    title = author = format = mode = ""
    width = height = 0

    
    

    return render_template('detail.html', id=id, title=title, author=author, width=width,
                           height=height, format=format, mode=mode)

## todo: images uniform size on home page
## todo: make each image interactable
