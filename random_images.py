import random
from image_info import image_info as info
from PIL import Image
import os

# get info from dict
# parse into objects/vars
# choose 3 random using random.shuffle(my_images) -> where my_images is a list of all image id's
# <img src="/static/images/{{ ... }}.jpg" class="w-50" /> -> keep in mind that this is how the html tag should look to get an img
# Note the .jpg on the outside of the path -> so we're only passing the image id

# returns dict of 3 selected random images & their titles
def random_three():
    data = info[:]
    random.shuffle(data)

    random_dict = {}
    for item in data[:3]:
        path = os.path.join("static", "images", item['id'] + ".jpg")
        width, height, format, mode = image_details(path)

        random_dict[item['id']] = [
            item['title'],
            item['flickr_user'],
            (width, height, format, mode)
        ]

    return random_dict

# gets image info such as width, height, format, and mode
# returns a tuple containing all of this info
def image_details(image_path):
    img = Image.open(image_path)
    width, height = img.size
    format = img.format
    mode = img.mode

    return (width, height, format, mode)
