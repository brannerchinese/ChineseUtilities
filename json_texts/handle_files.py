#! /usr/bin/env python
# handle_files.py
# David Prager Branner
# 20140809, works

"""Decrypt and encrypt research JSON file, and delete temporary copy."""

import json
import subprocess
import os

def retrieve_data(filename='ban_guh_hannshu_shiuhjuann_shiah.ignore.gpg'):
    """Decrypt and return JSON file of working data."""
    with open('phrase.ignore', 'r') as f:
        phrase = f.read().strip('\n')
    subprocess.call(['gpg', '-o', 'temp.ignore', '--passphrase', phrase, 
            '-d', filename])
    text = json_load('temp.ignore')
    os.remove('temp.ignore')
    return text

def store_data(text, filename='ban_guh_hannshu_shiuhjuann_shiah.ignore'):
    """Save and encrypt JSON file of working data."""
    if not text:
        text = json_load(filename)
    content = json.dumps(text)
    with open('phrase.ignore', 'r') as f:
        phrase = f.read().strip('\n')
    with open('temp.ignore', 'w') as f:
        f.write(content)
    subprocess.call(['gpg', '-o', filename + '.gpg', '--passphrase', phrase, 
            '-e', 'temp.ignore'])
    os.remove('temp.ignore')

def json_load(filename):
    """Load JSON data from file."""
    with open(filename, 'r') as f:
        content = f.read()
        text = json.loads(content)
    return text
