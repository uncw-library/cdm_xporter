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
        for movie_type in ('m4v', 'mov',):
            if (movie_type == file_ext.lower()) and ('{}.mp4'.format(file_base) not in files) and ('{}.mp3'.format(file_base) not in files) and (os.path.getsize("{}/{}".format(root, file)) > 0):
                print("convert {0}/{1} {0}/{2}.mp4".format(root, file, file_base))
                subprocess.run(["ffmpeg", "-i", "{}/{}".format(root, file), "{}/{}.mp4".format(root, file_base)], check=True)
                sleep(0.2)
