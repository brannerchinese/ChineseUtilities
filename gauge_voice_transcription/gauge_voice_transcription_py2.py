# gauge_voice_transcription_py2.py
# 20140128
# David Prager Branner

def percent_matching(s1, s2):
    #
    # Strip punctuation and lower-case all words
    s1 = re.sub(r'[^\w\s]', '', s1).split()
    s2 = re.sub(r'[^\w\s]', '', s2).split()
    #
    # Get set of all unique words
    all_unique = set(s1)
    all_unique.update(set(s2))
    #
    # Place all unique words in dict {word : item + 32} 
    #     Note that 32 is first printable character, for ease displaying most 
    #     (not necessarily all) of resulting string
    words_as_chars = {word:chr(i + 32) for i, word in enumerate(all_unique)}
    #
    # Convert each list to a string using the value corresp to each list-element
    s1 = ''.join([words_as_chars[w] for w in s1])
    s2 = ''.join([words_as_chars[w] for w in s2])
    #
    # Apply difflib to the two resulting strings. 
    #     Note: uses Ratcliff/Obershelp pattern recognition
    #     (see http://www.nist.gov/dads/HTML/ratcliffObershelp.html)
    return round(
            difflib.SequenceMatcher(None, s1, s2, autojunk=False).ratio(), 1)
