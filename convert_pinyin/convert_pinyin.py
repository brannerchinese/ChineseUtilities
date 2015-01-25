#! /usr/bin/env python
# convert_pinyin.py
# David Prager Branner
# 20150125

import os
import gzip
import re
import sys
import subprocess

def main():
    print('Files to be converted will be looked for in the "data" directory.')
    if os.path.exists('data'):
        for filename in os.listdir('data'):
            if filename == '.DS_Store':
                continue
            print('\nTrying file\n    "{}"'.format(filename))
            if convert(filename):
                print('        Conversion successful.')
        print('\nNo more files found.\n')
    else:
        print('No directory "data" found.')

def convert(filename):
    """Convert tonal diacritics from font Shyrbaw to standard Unicode"""
    if filename == None:
        return
    # Old-version pages "files" are actually directories; new ones are not.
    if os.path.isdir(os.path.join('data', filename)):
        # In the old version, the actual content is a gzip-ed XML file.
        old_style = True
        gz_filename = os.path.join('data', filename, 'index.xml.gz')
        with gzip.open(gz_filename, 'rb') as f:
            contents = f.read()
#        print(contents[-1000:]) # debug-print statement
    else:
        # Not sure yet how to deal with the new version (v. 9 and later).
        sys.exit('File\n    {}\n    cannot be converted.'.format(filename))
        old_style = False
        with open(filename, 'rb') as f:
            contents = f.read()
    diacritics = {
            # Original mapping, five vowels tone 1:
            # '¡': 'ā', '™': 'ē', '£': 'ī', '¢': 'ō', '∞': 'ū'
            b'&#xA1;': b'&#x101;', b'&#x2122;': b'&#x113;',
            b'&#xA3;': b'&#x12B;', b'&#xA2;': b'&#x14D;',
            b'&#x221E;': b'&#x16B;',
            # Original mapping, five vowels tone 3:
            # '§': 'ǎ', '¶': 'ě', '•': 'ǐ', 'ª': 'ǒ', 'º': 'ǔ',
            b'&#xA7;': b'&#x1CE;', b'&#xB6;': b'&#x11B;',
            b'&#x2022;': b'&#x1D0;', b'&#xAA;': b'&#x1D2;',
            b'&#xBA;': b'&#x1D4;',
            # Original mapping, u-umlaut:
            # '∞': 'ǘ', '√': 'ǚ', 'π': 'ǜ'
            b'&#x2248;': b'&#x1D8;', b'&#x221A;': b'&#x1DA;',
            b'&#x3C0;': b'&#x1DC;',
            # Note: five vowels, tones 2 and 4, were originally handled
            # correctly in standard upper ASCII and so are the same as current
            # Unicode.
            #
            # Note 2: I do not currently have a way to learn how ǖ or the
            # capitalized vowels with diacritics were mapped.
            }
    for k in diacritics:
        contents = re.sub(k, diacritics[k], contents)
    if old_style:
        # This is done inefficiently because of apparent filesystem issues.
        old_files = os.path.join('data', 'old_files')
        if not os.path.exists(old_files):
            os.mkdir(old_files)
        subprocess.call(
                ['/bin/cp', '-R', os.path.join('data', filename), old_files])
        with gzip.open(gz_filename, 'wb') as f:
            f.write(contents)
        converted_files = os.path.join('data', 'converted_files')
        if not os.path.exists(converted_files):
            os.mkdir(converted_files)
        subprocess.call(
                ['/bin/mv', os.path.join('data', filename), converted_files])
        os.rename(os.path.join(converted_files, filename),
                os.path.join(converted_files, filename +
                    '_converted_to_unicode.pages'))
    else:
        with open(filename, 'wb') as f:
            f.write(contents)
    return True

if __name__ == '__main__':
    main()
