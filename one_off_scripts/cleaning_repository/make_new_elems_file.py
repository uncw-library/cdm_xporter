#! /usr/bin/env python3

import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if not os.environ.get('REPO_DIR'):
    raise RuntimeError('Set the REPO_DIR environment variable, e.g. in a .env file (see README)')
REPO_DIR = os.path.expanduser(os.environ['REPO_DIR'])


pointers = [
    os.path.splitext(file)[0]
    for file in os.listdir(os.path.join(REPO_DIR, 'LSU_LNP'))
    if os.path.splitext(file)[1] == '.pdf'
]
cpd_pointers = [
    os.path.splitext(file)[0].replace('_cpd', '')
    for file in os.listdir(os.path.join(REPO_DIR, 'LSU_LNP', 'Cpd'))
    if '_cpd.xml' in file
]


template = f"""{{"pager":{{"start": "1", "maxrecs": "100", "total": {len(pointers)+len(cpd_pointers)}}},"records": ["""
for pointer in pointers:
    template += f"""{{"collection": "LSU_LNP", "pointer": {pointer}, "filetype": "pdf", "parentobject": -1, "dmrecord": "{pointer}", "find": "{pointer}.pdf"}},"""
for pointer in cpd_pointers:
    template += f"""{{"collection": "LSU_LNP", "pointer": {pointer}, "filetype": "cpd", "parentobject": -1, "dmrecord": "{pointer}", "find": "{pointer}.cpd"}},"""
template = template[:-1]
template += "]}"
print(template)
