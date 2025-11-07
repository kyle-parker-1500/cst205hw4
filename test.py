from random_images import random_three as rt
from PIL import Image
import os

random_dict = rt()
# lists = [v for k, v in random_dict.items()]
# print(lists)

# for i in random_dict:
#     print(random_dict[i])

for k, v in random_dict.items():
    image_open = os.path.join("static", "images", v[1] + ".png")
    img = Image.open(image_open)
    img.resize((500, 500))
