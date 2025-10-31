from random_images import random_three as rt

random_dict = rt()
# lists = [v for k, v in random_dict.items()]
# print(lists)

# for i in random_dict:
#     print(random_dict[i])

im1_name = random_dict[0][1]
im1_title = random_dict[0][0]

im2_name = random_dict[1][1]
im2_title = random_dict[1][0]

im3_name = random_dict[2][1]
im3_title = random_dict[2][0]

print("Image 1: ", im1_title, im1_name, "\nImage 2: ", im2_title, im2_name, "\nImage 3: ", im3_title, im3_name)
