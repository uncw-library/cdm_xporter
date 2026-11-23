#!/usr/bin/env/ python3

import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if not os.environ.get('REPO_DIR'):
    raise RuntimeError('Set the REPO_DIR environment variable, e.g. in a .env file (see README)')
REPO_DIR = os.path.expanduser(os.environ['REPO_DIR'])

for root, dirs, files in os.walk(REPO_DIR):
    for file in files:
        if ".mp4" in file:
            file_base, file_ext = file.split('.')
            if ('{}.png'.format(file_base) in files) or ('{}.tif'.format(file_base) in files):
                print(root, file)
                os.remove(os.path.join(root, file))
