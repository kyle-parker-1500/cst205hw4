from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from random_images import random_three, image_details
from image_info import image_info
from PIL import Image
import os

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
    title = author = format = mode = ""
    width = height = 0

    for i in image_info:
        if i['id'] == id:
            title = i['title']
            author = i['flickr_user']

    path = os.path.join("static", "images", id + ".jpg")
    width, height, format, mode = image_details(path)

    return render_template('detail.html', id=id, title=title, author=author, width=width, height=height, format=format, mode=mode)

## todo: images uniform size on home page
## todo: make each image interactable
