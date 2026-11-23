#! /usr/bin/env python3

import os
import subprocess
from time import sleep

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if not os.environ.get('REPO_DIR'):
    raise RuntimeError('Set the REPO_DIR environment variable, e.g. in a .env file (see README)')
REPO_DIR = os.path.expanduser(os.environ['REPO_DIR'])

for root, dirs, files in os.walk(os.path.join(REPO_DIR, 'PSL')):
    for file in files:
        if ('.gif' in file) and ('{}.jp2'.format(file.strip('.gif')) not in files) and (os.path.getsize("{}/{}".format(root, file)) > 0):
            print("convert {0}/{1} {0}/{2}.jp2".format(root, file, file.strip('.gif')))
            subprocess.run(["convert", "{}/{}".format(root, file), "{}/{}.jp2".format(root, file.strip('.gif'))], check=True)
            sleep(0.2)
