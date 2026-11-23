#! /usr/bin/env/ python3

import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if not os.environ.get('REPO_DIR'):
    raise RuntimeError('Set the REPO_DIR environment variable, e.g. in a .env file (see README)')
REPO_DIR = os.path.expanduser(os.environ['REPO_DIR'])

for root, dirs, files in os.walk(REPO_DIR):
    for file in files:
        if ".ram.mp3" in file:
            print(file, file.replace('.ram.mp3', '.mp3'))
            os.rename(os.path.join(root, file), os.path.join(root, file.replace('.ram.mp3', '.mp3')))
        if ".rm.mp3" in file:
            print(file, file.replace('.rm.mp3', '.mp3'))
            os.rename(os.path.join(root, file), os.path.join(root, file.replace('.rm.mp3', '.mp3')))