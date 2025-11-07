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

    titles_and_images = [v for k, v in random_dict.items()]
    return render_template('index.html', info = titles_and_images)

@app.route('/detail/<id>')
def detail(id):
    image = random_three()
    id_list = [v for k, v in image.items()]

    title = author = format = mode = ""
    width = height = 0

    for i in id_list:
        if i == id:
            title = i[-1]
            author = i[2]
            width, height, format, mode = i[3]
            break

    return render_template('detail.html', id=id, title=title, author=author, width=width,
                           height=height, format=format, mode=mode)

## todo: images uniform size on home page
## todo: make each image interactable
