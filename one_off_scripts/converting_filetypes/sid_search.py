#! /usr/bin/env python3

import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if not os.environ.get('REPO_DIR'):
    raise RuntimeError('Set the REPO_DIR environment variable, e.g. in a .env file (see README)')
REPO_DIR = os.path.expanduser(os.environ['REPO_DIR'])
# import subprocess
# from time import sleep

for root, dirs, files in os.walk(os.path.join(REPO_DIR, 'AAW')):
    for file in files:
        if (".sid" in file) and ("{}.jp2".format(file.strip('.sid')) not in files):
            print(root, file)
