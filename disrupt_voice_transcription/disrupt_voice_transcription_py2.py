# disrupt_voice_transcription_py2.py
# 20140129, working.
# David Prager Branner

"""Return quantitative gauges of the accuracy of voice transcription."""

import re
import difflib
import nltk
import sys

if sys.version_info[0] != 2 or sys.version_info[1] < 6:
    print("This program requires Python 2, versions 2.6 or above.")
    sys.exit(1)

# Treebank and WordNet POS need correspondences specified in order for the
# NLTK lemmatizer to work correctly on the tagged output. Only the following
# five have application, however.
TB2WN = {
    'J': nltk.wordnet.wordnet.ADJ,
    'R': nltk.wordnet.wordnet.ADV,
    'N': nltk.wordnet.wordnet.NOUN,
    'V': nltk.wordnet.wordnet.VERB,
    'S': nltk.wordnet.wordnet.ADJ_SAT
    }
WNL = nltk.stem.WordNetLemmatizer()

def percent_matching(s1, s2):
    """Compare the likeness of two input strings."""
    #
    # Case 1. Simple case: strings are compared character by character.
    #
    # Strip punctuation and lower-case all words
    s1_cleaned = re.sub(r'[^\w\s]', '', s1.lower())
    s2_cleaned = re.sub(r'[^\w\s]', '', s2.lower())
    #
    # Apply difflib to the two resulting strings in each case.
    #     Note: uses Ratcliff/Obershelp pattern recognition
    #     (see http://www.nist.gov/dads/html/ratcliffobershelp.html).
    gauge_raw = difflib.SequenceMatcher(
            None, s1_cleaned, s2_cleaned, autojunk=False).ratio()
    #
    # Case 2. Case of whole words rather than characters.
    #
    # Get set of all unique words.
    s1_split = s1_cleaned.split()
    s2_split = s2_cleaned.split()
    all_unique = set(s1_split)
    all_unique.update(set(s2_split))
    #
    # Place all unique words in dict {word : item + 32}.
    #     Note that 32 is first printable character, for ease displaying most
    #     (not necessarily all) of resulting string.
    words_as_chars = {word:unichr(i + 32) for i, word in enumerate(all_unique)}
    #
    # Convert each list to a string using the value corresponding to each 
    # list-element.
    s1_words = ''.join([words_as_chars[w] for w in s1_split])
    s2_words = ''.join([words_as_chars[w] for w in s2_split])
    #
    # Apply difflib.
    gauge_word = difflib.SequenceMatcher(
            None, s1_words, s2_words, autojunk=False).ratio()
    #
    # Case 3. Case of normalized whole words.
    #
    # Normalize each word via NLTK and create additional pair of strings.
    s1_norm = clean_and_normalize(s1)
    s2_norm = clean_and_normalize(s2)
    #
    # Get set of all unique words.
    all_unique_lemm = set(s1_norm)
    all_unique_lemm.update(set(s2_norm))
    #
    # Convert contents of all_unique_norm to strings.
    norm_words_as_chars = {lemma:unichr(i + 32) for i, lemma in
            enumerate(all_unique_lemm)}
    s1_norm = ''.join([norm_words_as_chars[w] for w in s1_norm])
    s2_norm = ''.join([norm_words_as_chars[w] for w in s2_norm])
    #
    # Apply difflib
    gauge_lemma = difflib.SequenceMatcher(
            None, s1_norm, s2_norm, autojunk=False).ratio()
    #
    # Report results
    print ('''By character:       {}\nBy word:            {}'''
            '''\nBy normalized word: {}'''.format(
            round(gauge_raw, 1), round(gauge_word, 1), round(gauge_lemma, 1)))

def clean_and_normalize(the_str):
    """Return all-lower case, unpunctuated, lemmatized list of words in string."""
    # Annoyingly, nltk.word_tokenize does not handle contractions well.
    # The substitutions below are best guesses; some will occasionally be wrong.
    # In particular, 's is not handled at all here, since it includes
    # possessive and the contraction of is and has: "Tom's" could be "belonging
    # to Tom", "Tom is", or "Tom has".
    the_str = the_str.lower()
    the_str = re.sub(r"won't", 'will not', the_str)
    the_str = re.sub(r"can't", 'cannot', the_str)
    the_str = re.sub(r"it's", 'it is', the_str)
    substitutions = {r"'ll": ' will',
            r"n't": ' not',
            r"'m": ' am',
            r"'d": ' would',
            r"'ve": ' have',
            r"'re": ' are',
            r"'ve": ' have'}
    for s in substitutions:
        the_str = re.sub(s, substitutions[s], the_str)
    # Remove all other punctuation and normalize.
    the_str = re.sub(r'[^\w\s]', '', the_str)
    tokenized = nltk.word_tokenize(the_str)
    tagged = nltk.pos_tag(tokenized)
    lemmata = [WNL.lemmatize(item[0], TB2WN[item[1][0]])
            if item[1][0] in TB2WN else item[0] for item in tagged]
    return lemmata

