import os
import sys

import download_dataset as movies

dwn = '-download' in sys.argv
resize = '-resize' in sys.argv

start = 0
for arg in sys.argv:
    if arg.startswith('-start='):
        start = int(arg.split('=')[1])

r = [60, 70]
images_path = 'data/images/'
base_images_path = images_path + '100/'

if not os.path.isdir(base_images_path):
    os.makedirs(base_images_path)

if dwn:
    movies.download_posters(start=start)

if resize:
    for ratio in r:
        directory_path = images_path + str(ratio)
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)
            command = 'mogrify -path "' + directory_path + '/" -resize ' \
                      + str(ratio) + '% ' + base_images_path + '*.jpg -verbose'
            print(command)
            os.system(command)
