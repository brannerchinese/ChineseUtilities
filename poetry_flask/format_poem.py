# format_poem.py
# David Prager Branner
# 20140303

import re
import pprint

def format_poem(poem, to_break_at=['。', '，'], to_strip=None):
    """Format a Chinese poem. Assume no punctuation, lines are \n-separated."""
    if to_strip == None:
        to_strip = []
    # Remove whitespace of various kinds, but not ideographic space \u3000.
    poem = re.sub(r'''\u0020|\u00a0|\u2002|\u2003|\u2004|\u2005|\u2006|'''
            r'''\u2007|\u2008|\u2009|\u200a|\u200b|\200c|\205f|\t''', '', poem)
    # Replace to_break_at items with linebreaks
    #     and consolidate multiple linebreaks.
    for item in to_break_at:
        pattern = re.compile(re.escape(item) + r'[\n\r]{0,}')
        poem = pattern.sub('\n', poem)
    poem = poem.splitlines()
    poem = [
            [char for char in line if char not in to_strip] 
            for line in poem]
#    pprint.pprint(poem)
    print('\n')
    # Pad all lines to make them as long as the longest line.
    longest_length = max([len(line) for line in poem])
    print(longest_length)
    # Rotate poem.
    rotated = []
    for row in range(len(poem)):
        line = []
        for char in range(len(poem)):
            old_line = poem[len(poem) - 1 - char]
#            print(row, char, old_line)
            if row >= len(old_line):
                continue
            line.append(poem[len(poem) - 1 - char][row])
#        print(line)
        rotated.append(line)
#    rotated = [
#            pass
#            ]
#    formatted = ['<tr>' + 
#            '\n'.join(['<td>' + str(char) + '</td>' for char in line])
#            + '</tr>' for line in poem]
    return rotated
