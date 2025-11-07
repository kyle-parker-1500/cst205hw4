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
    # need image id -> pass
    ids = [i['id'] for i in info]
    # need image title -> pass
    names = [i['title'] for i in info]
    # shuffles names every time page is loaded
    random.shuffle(names)
    
    list_images = {i['title'] : i['id'] for i in info}

    # choose random 3 images
    random_dict = {}
    for i in range(3):
        temp_list = []
        temp_list.append(names[i])
        
        # make images (mostly uniform)
        # pull ids -> access images -> resize -> add to temp_list
        img = Image.open(os.path.join("static", "images", list_images[names[i]] + ".jpg"))
        img.resize((500, 500))

        temp_list.append(list_images[names[i]])
        random_dict[i] = temp_list

    return random_dict
