# format_poem.py
# David Prager Branner
# 20140304

import re
import pprint

def temp(it):
    return it

def format_poem(poem, to_break_at=['。', '，', '？'], to_strip=None):
    """Format a Chinese poem. Assume no punctuation, lines are \n-separated."""
    poem = clean_poem(poem, to_break_at=['。', '，', '？'], to_strip=None)
    poem = regularize_line_length(poem)
    poem = rotate_poem(poem)
    poem = make_html_table(poem)
    return poem

def clean_poem(poem, to_break_at=['。', '，', '？'], to_strip=None):
    if to_strip == None:
        to_strip = []
    # Remove whitespace of various kinds, but not these:
    # \n, \r, ideographic space \u3000. Hence \s can't be used here.
    poem = re.sub(r'''\u0020|\u00a0|\u2002|\u2003|\u2004|\u2005|\u2006|'''
            r'''\u2007|\u2008|\u2009|\u200a|\u200b|\u200c|\u205f|\t''',
            r'', poem)
    # Replace to_break_at items with linebreaks
    #     and consolidate multiple linebreaks.
    for item in to_break_at:
        pattern = re.compile(re.escape(item) + r'[\n\r]{0,}')
        poem = pattern.sub('\n', poem)
    poem = poem.splitlines()
    poem = [
            [char for char in line if char not in to_strip]
            for line in poem if any(line)]
    return poem

def regularize_line_length(poem):
    """Pad all lines to make them as long as the longest line."""
    max_len = max([len(line) for line in poem])
    for i, line in enumerate(poem):
        poem[i].extend(['\u3000'] * (max_len - len(line)))
    return poem

def rotate_poem(poem):
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

def make_html_table(rotated):
    formatted = '\n'.join(
            ['<table>\n  <tr>\n    ' + '\n    '.join(
                ['<td>' + str(char) + '</td>' for char in line]
                ) + '\n  </tr>\n</table>' for line in rotated
                ]
            )
    return formatted
