# separate_pinyin.py
# David Prager Branner
# 20130823
'''Create random strings of Pīnyīn and attempt to parse them into discrete
syllables'''

import os
import re
import string

def get_all_letters():
    all_e = ['ē', 'é', 'ě', 'è', 'e']
    all_o = ['ō', 'ó', 'ǒ', 'ò', 'o']
    all_u = ['ū', 'ú', 'ǔ', 'ù', 'u']
    all_v = ['ǖ', 'ǘ', 'ǚ', 'ǜ', 'ü']
    all_vowels = [
            'ā', 'á', 'ǎ', 'à', 'a',
            'ī', 'í', 'ǐ', 'ì', 'i']
    all_vowels.extend(all_e)
    all_vowels.extend(all_o)
    all_vowels.extend(all_u)
    all_vowels.extend(all_v)
    all_vowels_and_ngrm = all_vowels[0:]
    all_vowels_and_ngrm.extend(['n', 'g', 'r', 'm'])
    all_vowels_and_ngrm = r'(' + '|'.join(all_vowels_and_ngrm) + r')'
    all_vowels_and_gr = all_vowels[0:]
    all_vowels_and_gr.extend(['g', 'r'])
    all_vowels_and_gr = r'(' + '|'.join(all_vowels_and_gr) + r')'
    all_e = r'(' + '|'.join(all_e) + r')'
    all_o = r'(' + '|'.join(all_o) + r')'
    all_u = r'(' + '|'.join(all_u) + r')'
    all_vowels = r'(' + '|'.join(all_vowels) + r')'
    consonants_not_hngr = [
            'b', 'p', 'm', 'f',
            'd', 't', 'l', 
            'k', 
            'j', 'q', 'x', 
            'z', 'c', 's',
            'y', 'w']
    consonants_not_hngr = r'(' + '|'.join(consonants_not_hngr) + r')'
    return (all_vowels, all_e, all_vowels_and_ngrm, all_vowels_and_gr,
            consonants_not_hngr)

def get_py_syllables(filename):
    '''Retrieve a list of all possible Pīnyīn syllables (lower case only).'''
    with open(os.path.join('DATA', filename)) as f:
        contents = f.read()
    contents = contents.split('\n')[1:]
    # Syllables marked "True" are unattested; we exclude those here.
    return [i.split()[0] for i in contents if len(i.split()) == 1]

def validate_cleaned_syllables(finished_string, all_syllables):
    for i, item in enumerate(finished_string):
        if item not in all_syllables:
            if item == 'r':
                finished_string[i-1] = finished_string[i-1] + 'r'
                finished_string[i] = ''
                continue
            return (1, item) # error found
    # Eliminate empty indices, where 'r' was removed.
    finished_list = [i for i in finished_string if i]
    return (0, finished_list) # no error found

def separate(initial_string, filename='pinyin_syllables_20130728.txt'):
    '''Breaks a string of Pīnyīn into its component syllables. 
    
    Reports the first error encountered, if any.
    
    Use separate() for standard syllables; use separate('r') for all syllables,
    including those with epenthetic -r.'''
    if filename == 'r':
        filename = 'pinyin_syllables_with_r_20130728.txt'
    all_syllables = get_py_syllables(filename)
    (all_vowels, all_e, all_vowels_and_ngrm, all_vowels_and_gr, 
            consonants_not_hngr) = get_all_letters()
    # Punctuation marks are always a syllable-boundary.
    # And convert to lower case throughout.
    any_punct = ('[{}]'.
            format(r''.join(
                [i for i in string.punctuation[:-1]]) + 
                string.punctuation[-1] + '’' + '‧'))
    string_in_midprocess = re.sub(
            any_punct, r' ', initial_string.lower())
    # Vowel/n/g/r/m + consonant always straddles a syllable-boundary 
    # except when the consonant is in {hngr}. 
    string_in_midprocess = re.sub(
            all_vowels_and_ngrm + consonants_not_hngr, 
            r'\1 \2', 
            string_in_midprocess)
    # Vowel/g/r + h/g always straddles a syllable-boundary.
    string_in_midprocess = re.sub(
            all_vowels_and_gr+r'(h|H|g|G)', 
            r'\1 \2', 
            string_in_midprocess)
    # r/n/g + n/r/h always straddles a syllable-boundary.
    string_in_midprocess = re.sub(
            r'(r|R|n|N|g|G)'+r'(n|N|r|R|h|H)', 
            r'\1 \2', 
            string_in_midprocess)
    # n/r/g + vowel always straddles a syllable-boundary if a letter
    # immediately precedes n/r/g. Syllables beginning with vowels will
    # have been separated by the apostrophe rules.
    string_in_midprocess = re.sub(
            r'([^ ])(r|R|n|N|g|G)' + all_vowels, 
            r'\1 \2\3', 
            string_in_midprocess)
    # "hm" is always a discrete syllable.
    string_in_midprocess = re.sub(
            r'((hm)|(HM))', r' \1 ', string_in_midprocess)
    # "er" preceded by space or string-start is now always discrete.
    string_in_midprocess = re.sub(
            r'((^| )' + all_e + r'r|R)', r'\1\2 ', string_in_midprocess)
    # vowel+r, if not part of discrete "er" (above) and preceded by a
    # letter, now always straddles a syllable-boundary.
    string_in_midprocess = re.sub(
            r'([^ ])' + all_vowels + r'(r|R)', 
            r'\1\2 \3', 
            string_in_midprocess)
    # vowel + n + vowel occurring here always has n as syllable-start.
    # This rule is *not* redundant in spite of the "n/r/g + vowel"
    # rule.
    string_in_midprocess = re.sub(
            all_vowels + r'(n|N)' + all_vowels,
            r'\1 \2\3',
            string_in_midprocess.strip())
    finished_string = string_in_midprocess.split()
    response = validate_cleaned_syllables(finished_string, set(all_syllables))
    if response[0]:
        print('String "{}" appears to be incorrect Pīnyīn in "{}".'.
                format(response[1], initial_string))
    else:
        return response[1]
