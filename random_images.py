import random
from image_info import image_info as info
from PIL import Image
import os

# returns dict of 3 selected random images & their titles
def random_three():
    # copys dict & shuffles data
    data = info[:]
    random.shuffle(data)

    # generates dict to get 3 images and their information
    random_dict = {}
    for item in data[:3]:
        # genrates id locally for image_details method to function
        path = os.path.join("static", "images", item['id'] + ".jpg")
        width, height, format, mode = image_details(path)

        # creates random dict with 'id' as the key
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
