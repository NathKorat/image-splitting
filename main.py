import os
import argparse

pargser = argparse.ArgumentParser()

pargser.add_argument('-p', '--path', type=str, required= True,
    help="image folder")


arg = pargser.parse_args()

img_list = os.listdir(arg.path)

print(img_list)