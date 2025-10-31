from random_images import random_three as rt

random_dict = rt()
lists = [v for k, v in random_dict.items()]
print(lists)

for i in random_dict:
    print(random_dict[i])
