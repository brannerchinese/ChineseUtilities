#! /usr/bin/env python
# convert_pinyin.py
# David Prager Branner
# 20150124

import os
import gzip

def convert(filename="Untitled.pages"):#Colloq Chin Patterns  03-08.pages"):
    # Old-version pages "files" are actually directories; new ones are not.
    filename = os.path.join('data', filename)
    if os.path.isdir(filename):
        # In old ones, the actual content is a gzip-ed XML file.
        old_style = True
        with gzip.open(os.path.join(filename, 'index.xml.gz'), 'rb') as f:
            contents = f.read()
    else:
        old_style = False
        with open(filename, 'rb') as f:
            contents = f.read()
    print(contents)
    if old_style:
        diacritics = {
                # '§': 'ǎ', '¶': 'ě', '•': 'ǐ', 'ª': 'ǒ', 'º': 'ǔ', '√': 'ǚ',
                '&#xA1;': '&#x101;', '&#x2211;': '&#x113;', '&#xA3;': '&#x12B;',
                '&#xA2;': '&#x14D;', '&#x221E;': '&#x16B;',
                # '¡': 'ā', '™': 'ē', '£': 'ī', '¢': 'ō', '∞': 'ū'
                '&#xA7;': '&#x1CE;', '&#xB6;': '&#x11B;', '&#x2022;': '&#x1D0;',
                '&#xAA;': '&#x1D2;', '&#xBA;': '&#x1D4;', '&#x221A;': '&#x1DA;',
                }
    else:
        diacritics = {
                # '§': 'ǎ', '¶': 'ě', '•': 'ǐ', 'ª': 'ǒ', 'º': 'ǔ', '√': 'ǚ',
                '\xa1': '\x101', '\x2211': '\x113', '\xa3': '\x12b',
                '\xa2': '\x14d', '\x221e': '\x16b',
                # '¡': 'Ā', '™': 'Ē', '£': 'Ī', '¢': 'Ō', '∞': 'Ū'
                '\xa7': '\x1ce', '\xb6': '\x11b', '\x2022': '\x1d0',
                '\xaa': '\x1d2', '\xba': '\x1d4', '\x221a': '\x1da',
                }
    for i, c in enumerate(contents):
        if c in diacritics:
            contents[i] = diacritics[c]
    if old_style:
        with gzip.open(os.path.join(filename, 'index.xml.gz'), 'wb') as f:
            f.write(contents)
    else:
        with open(filename, 'wb') as f:
            f.write(contents)
    return contents
