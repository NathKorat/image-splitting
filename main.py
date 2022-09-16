import os
import argparse
from splitting import split_img
import json
import matplotlib.pyplot as plt
import numpy as np

pargser = argparse.ArgumentParser()

pargser.add_argument('-p', '--path', type=str, required= True,
    help="image folder")
pargser.add_argument('-f', '--factor', type=int, required=True,
    help="splitting factor of picture x by x ex. 2 (2 x 2)")

pargser.add_argument('-s', '--save', type=bool, default=True,
    help="save result")


arg = pargser.parse_args()

base_path = arg.path


test = {}
for i in range(len(os.listdir(base_path))):
    tem = (base_path + "/" + os.listdir(base_path)[i])
    print(os.listdir(base_path)[i] + ' spliting.....')
    arr_tem = split_img(tem, arg.factor)
    a = 0
    for x in range(arg.factor):
        for y in range(arg.factor):
            test[os.listdir(base_path)[i] + str(x) + str(y) + '.jpg'] = np.array(arr_tem[a]).tolist()
            a += 1

print(np.array(test[list(test.keys())[0]]))
    
with open('image_data.json', 'w') as file:
    json.dump(test, file)

#
def visual(arr):
    plt.imshow(arr)
    plt.show()

# visual(test[list(test.keys())[0]])

print(test)