"""
Title: Homework 4
Name: Kyle Parker
Class: CST205
Date: 2025-11-06
Description: A program that utilizes flask and bootstrap 5 to create a website that has a home page
             that generates 3 random images each time it loads, and allows functionality to click on each one to display
             the image at full size & more information about the image.
"""


from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from random_images import random_three, image_details
from image_info import image_info
from PIL import Image
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# generates home page with 3 random images
@app.route('/')
def home():
    # parse random_three dict into names & image ids
    random_dict = random_three()
    info = list(random_dict.items())

    return render_template('index.html', info=info)

# generates webpages for each of the images based off of their image id
@app.route('/detail/<id>')
def detail(id):
    title = author = format = mode = ""
    width = height = 0

    # gets info from image_info.py, using the id as a key
    for i in image_info:
        if i['id'] == id:
            title = i['title']
            author = i['flickr_user']

    # gets PIL image data & passes to detail.html
    path = os.path.join("static", "images", id + ".jpg")
    width, height, format, mode = image_details(path)

    return render_template('detail.html', id=id, title=title, author=author, width=width, height=height, format=format, mode=mode)
