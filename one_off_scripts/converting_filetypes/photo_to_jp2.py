#! /usr/bin/env python3

import os
import subprocess
from time import sleep

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if not os.environ.get('REPO_DIR'):
    raise RuntimeError('Set the REPO_DIR environment variable, e.g. in a .env file (see README)')
REPO_DIR = os.path.expanduser(os.environ['REPO_DIR'])

for root, dirs, files in os.walk(REPO_DIR):
    for file in files:
        file_base, file_ext = file.split('.')
        for image_type in ('gif', 'jpg', 'tif', 'png',):
            if (image_type == file_ext.lower()) and ('{}.jp2'.format(file_base) not in files) and (os.path.getsize("{}/{}".format(root, file)) > 0):
                print("convert {0}/{1} {0}/{2}.jp2".format(root, file, file_base))
                subprocess.run(["convert", "{}/{}".format(root, file), "{}/{}.jp2".format(root, file_base)], check=True)
                sleep(0.1)
