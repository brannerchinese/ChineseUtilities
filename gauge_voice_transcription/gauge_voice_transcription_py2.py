# gauge_voice_transcription_py2.py
# 20140128
# David Prager Branner

"""Return quantitative gauges of the accuracy of voice transcription."""

import re
import difflib

def percent_matching(s1, s2):
    """Compare the closeness of two input strings."""
    #
    # 1. Simple case. 
    # Strip punctuation and lower-case all words
    s1_cleaned = re.sub(r'[^\w\s]', '', s1)
    s2_cleaned = re.sub(r'[^\w\s]', '', s2)
    #
    # Apply difflib to the two resulting strings in each case.
    #     note: uses Ratcliff/Obershelp pattern recognition
    #     (see http://www.nist.gov/dads/html/ratcliffobershelp.html)
    gauge_raw = difflib.SequenceMatcher(
            None, s1_cleaned, s2_cleaned, autojunk=False).ratio()
    #
    # 2. Case of whole words rather than characters. 
    # Get set of all unique words
    s1_split = s1_cleaned.split()
    s2_split = s2_cleaned.split()
    all_unique = set(s1_split)
    all_unique.update(set(s2_split))
    #
    # Place all unique words in dict {word : item + 32} 
    #     Note that 32 is first printable character, for ease displaying most 
    #     (not necessarily all) of resulting string
    words_as_chars = {word:unichr(i + 32) for i, word in enumerate(all_unique)}
    #
    # Convert each list to a string using the value corresp to each list-element
    s1_words = ''.join([words_as_chars[w] for w in s1_split])
    s2_words = ''.join([words_as_chars[w] for w in s2_split])
    print 's1_words, s2_words:', s1_words, s2_words
    #
    # Apply difflib
    gauge_by_word = difflib.SequenceMatcher(
            None, s1_words, s2_words, autojunk=False).ratio()
    #
    # 3. Case of lemmatized whole words.
    # Lemmatize each word via NLTK and create additional pair of strings.
    s1_lemmata = s1_words # temporary
    s2_lemmata = s2_words # temporary
    print 's1_lemmata, s2_lemmata:', s1_lemmata, s2_lemmata
    # Lemmatize contents of all_unique
    lemmata_as_chars = {lemma:unichr(i + 32) for i, lemma in
            enumerate(all_unique)}
    s1_lemmata = ''.join([lemmata_as_chars[w] for w in s1_split])
    s2_lemmata = ''.join([lemmata_as_chars[w] for w in s2_split])
    print 's1_lemmata, s2_lemmata:', s1_lemmata, s2_lemmata
    #
    # Apply difflib
    gauge_by_lemma = difflib.SequenceMatcher(
            None, s1_lemmata, s2_lemmata, autojunk=False).ratio()
    #
    # Report results
    return round(gauge_raw, 1), round(gauge_by_word, 1), round(gauge_by_lemma,
            1)
