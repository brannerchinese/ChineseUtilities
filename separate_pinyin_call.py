# separate_pinyin_call.py
# David Prager Branner
# 20130823
'''Create random strings of Pīnyīn and attempt to parse them into discrete
syllables'''

import os
import random
import re
import time
import separate_pinyin as S

all_e = ['ē', 'é', 'ě', 'è', 'e']
all_o = ['ō', 'ó', 'ǒ', 'ò', 'o']
all_u = ['ū', 'ú', 'ǔ', 'ù', 'u']
all_v = ['ǖ', 'ǘ', 'ǚ', 'ǜ', 'ü']
all_uv = all_u[0:]
all_uv.extend(all_v)
all_vowels = [
        'ā', 'á', 'ǎ', 'à', 'a',
        'ī', 'í', 'ǐ', 'ì', 'i']
all_vowels.extend(all_e)
all_vowels.extend(all_o)
all_vowels.extend(all_u)
all_vowels.extend(all_v)
all_vowels_set = set(all_vowels)
not_e = r'([^' + ''.join(all_e) + r'])'
all_e = r'(' + '|'.join(all_e) + r')'
all_o = r'(' + '|'.join(all_o) + r')'
all_u = r'(' + '|'.join(all_u) + r')'
all_uv = r'(' + '|'.join(all_uv) + r')'
all_vowels = r'(' + '|'.join(all_vowels) + r')'

def get_random_string(a_list, all_vowels):
    '''Produce a random string of Pīnyīn syllables. Note that we are not
    inserting necessary apostrophes yet.'''
    syllables = [random.choice(a_list) for i in range(random.randint(1, 6))]
    # Insert ' before any non-initial syllable beginning with a vowel.
    temp = [syllables[0]]
    temp.extend(["'" + str(i) if i[0] in all_vowels_set else str(i)
            for i in syllables[1:]])
    return ''.join(temp), syllables

def main(filename='pinyin_syllables_20130728.txt'):
    '''Runs never-ending test of separate_pinyin.py.
    
    Use main() for standard syllables; use main('r') for all syllables,
    including those with epenthetic -r.
    
    Randomly generates a string of Pīnyīn up to six syllables long,
    separates it into component syllables using separate_pinyin.py,
    checks whether returned components are the same as the originals or not.

    Repeats this process until interrupted with control-c, and then reports the
    number of trials done. The process also terminates in the case of a failed
    trial.'''
    
    print('''Tests of separate_pinyin.py run indefinitely until '''
            '''\n\n 1) an error is encountered or'''
            '''\n 2) control-c is pressed. '''
            '''\n\nIf the latter, statistics are then output.'''
            '''\n\nInventory of possible syllables includes''', end=' ')
    if filename == 'r':
        print('all those with -r.')
        filename = 'pinyin_syllables_with_r_20130728.txt'
    else:
        print('only those without added -r.')
    all_syllables = S.get_py_syllables(filename)
    all_vowels, _, _, _, _ = S.get_all_letters()
    counter = 0
    start_time = time.time()
    try:
        while True:
            counter += 1
            string_in_midprocess, original_list = get_random_string(
                    all_syllables, all_vowels)
            finished_list = S.separate(string_in_midprocess, filename)
            if finished_list != original_list:
                print('Bad!', finished_list, '\n vs.', original_list)
    except KeyboardInterrupt:
        total_time = time.time() - start_time
        print('\n{:.0f} tests/second'.
                format(counter/total_time))
        print('Total tests run:', counter)
