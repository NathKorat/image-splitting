import os
import argparse
from splitting import splited_show

pargser = argparse.ArgumentParser()

pargser.add_argument('-p', '--path', type=str, required= True,
    help="image folder")
pargser.add_argument('-f', '--factor', type=int, required=True,
    help="splitting factor of picture x by x ex. 2 (2 x 2)")

pargser.add_argument('-s', '--save', type=bool, default=True,
    help="save result")


arg = pargser.parse_args()

base_path = arg.path


test = []
for i in range(len(os.listdir(base_path))):
    test.append(base_path + "/" + os.listdir(base_path)[i])
    print(os.listdir(base_path)[i] + ' spliting.....')
    splited_show(base_path + "/" + os.listdir(base_path)[i], arg.factor, arg.save)
    