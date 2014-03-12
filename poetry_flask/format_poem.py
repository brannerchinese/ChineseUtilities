# format_poem.py
# David Prager Branner
# 20140312, works

"""Divide a poem into stanzas or sections and rotate each.

Stanzas are those delimited by two \n.

Sections are eight lines long.
"""

import re
import pprint
import math

def format_poem(poem, stanza_len = 8, to_strip=None):
    """Format a Chinese poem. Assume no punctuation, lines are \n-separated."""
    stanzas = clean_poem(poem)
    processed = []
    for stanza in stanzas:
        n_secs = math.ceil(len(stanza) / stanza_len)
        for i in range(n_secs):
            # Create sections for single-screen display.
            section = stanza[0:stanza_len]
            stanza = stanza[stanza_len:]
            section = regularize_line_length(section)
            section = rotate_lines(section)
            processed.append(section)
    return processed

def clean_poem(poem, to_strip=['《', '》', '“', '”']):
    """Strip whitespace from string, return as trebly nested char-list."""
    if to_strip == None:
        to_strip = []
    to_break_at = [r'。', r'，', r'？', r'！', r'：', r'○', r'；']
    # Break into any stanzas.
    stanzas = []
    for stanza in poem.split('\n\n'):
        if stanza == []:
            continue
        # Remove whitespace of various kinds, but not these:
        # \n, \r, ideographic space \u3000. Hence \s can't be used here.
        stanza = re.sub(r'''\u0020|\u00a0|\u2002|\u2003|\u2004|\u2005|\u2006|'''
                r'''\u2007|\u2008|\u2009|\u200a|\u200b|\u200c|\u205f|\t''',
                r'', stanza)
        # Replace to_break_at items with linebreaks
        #     and consolidate multiple linebreaks.
        for item in to_break_at:
            pattern = re.compile(re.escape(item) + r'[\n\r]*?')
            stanza = pattern.sub('\n', stanza)
        stanza = stanza.splitlines()
        stanza = [
                [char for char in line if char not in to_strip]
                for line in stanza if any(line)]
        if any(stanza):
            stanzas.append(stanza)
    return stanzas

def regularize_line_length(section):
    """Pad all lines to make them as long as the longest line; return list."""
    max_len = max(len(line) for line in section)
#    max_len = max([len(line) for section in poem for line in section])
#    to_return = [line + ['\u3000'] * (max_len - len(line)) for section in
#            F.clean_poem(tsyr1) for line in section]
    regularized = [
            line + ['\u3000'] * (max_len - len(line)) for line in section]
    return regularized

def rotate_lines(poem):
    """Rotate each eight-line list-of-lists and return a list of those."""
    # Create empty matrix.
    rows = len(poem) # this many column-elements
    cols = len(poem[0]) # in each of this many row-lists
    rotated = [
                [[] for i in range(rows)]
                    for i in range(cols)]
    # Populate
    for row in range(rows):
        for char in range(cols):
            rotated[char][rows - 1 - row] = poem[row][char]
    return rotated
