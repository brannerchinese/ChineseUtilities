# count_syllables.py
# David Prager Branner
# 20140113

"""Count and evaluate the number of syllables in a Pīnyīn expression.

In case of input from a file, file is in directory INPUT/"
"""

import sys
if sys.version_info[0] < 3:
    sys.stdout.write('Python 3 required; exiting.')
    sys.exit(1)
import os
import separate_pinyin as S

def process_expression(expression, max_syll, singletons, verbose, tally=None):
    """Report cases of more than the number of allowed syllable combinations.

    Examples are:

    1) more than `max_syll` consecutive syllables without spaces or
    2) more than `singletons` consecutive single syllables.

    Return `tally` in any case:

        [0]: more than `max_syll` consecutive syllables without spaces
        [1]: more than `singletons` consecutive single syllables

    All results are printed to STDOUT."""
    if tally == None:
        tallly = [0, 0]
    divided = expression.split()
    consec_sing_count = 0
    for item in divided:
        try:
            length = len(S.separate(item, 'r'))
        except TypeError as e:
            if verbose:
                print('    Skipping {}.'.format(item))
            continue
        if length > 1:
            # Report any case of excessive singletons before resetting counter.
            if consec_sing_count > singletons:
                if verbose:
                    print('{}:    {} consecutive single syllables.'.
                            format(expression, consec_sing_count))
                tally[1] += 1
            consec_sing_count = 0
            # Check for excessive number of syllables.
            if length > max_syll:
                if verbose:
                    print('{}:    {} has syllables numbering {} > {}.'.
                            format(expression, item, length, max_syll))
                tally[0] += 1
        else:
            consec_sing_count += 1
    # Once more, report any case of excessive singletons.
    if consec_sing_count > singletons:
        if verbose:
            print('{}:    {} consecutive single syllables.'.
                    format(expression, consec_sing_count))
        tally[1] += 1
    return tally

#def first_item_kanji(expression, max_syll, singletons):
#    """Process list in which item 0 is kanji expression."""
#    # Below: so far we only compare syllable count of kanji and Pīnyīn.
#    syllables = len(data[0])
#    for item in data[1:]:
#        separated = S.separate(item)
#        sep_sylls = len(separated)
#        if sep_sylls != syllables:
#            print('{} and {} are of different lengths: {} == {}.'.
#                    format(data[0], item, syllables, sep_sylls))
#        process_expression(item, max_syll, singletons)

def main(data=None, fname=None, max_syll=2, singletons=1, verbose=False):
    # options:
    #   Act on data or file `fname`
    #   max_syll=n: report any cases exceeding n syllables
    #   singletons=n: report cases of more than n single syllables in a row.
    if not (data or fname):
        print('\nEither a file name or actual data is required; exiting.\n')
        sys.exit(1)
    if data:
        # First process any data.
        if not isinstance(data, (str, list)):
            print('\nArgument `data` must be of type `str` or `list`; '
                    'type {} found.\n\nExiting.\n'.format(type(data)))
            sys.exit(1)
        # We have data of type str or list.
        print('\nProcessing data\n    {}\n'.format(data))
        # Embed the data-list into another list for processing as if file.
        contents = [data]
    if fname:
        # open file and process each line
        print('\nProcessing file \n    {}\nin directory INPUT/\n'.
                format(fname))
        try:
            with open(os.path.join('INPUT', fname), 'r') as f:
                contents = f.read()
        except FileNotFoundError as e:
            print(e, '\nExiting.\n')
            sys.exit(1)
        contents = contents.split('\n')
    # tally: [cases of syllables > max_syll, cases of consecutive singletons]
    tally = [0, 0]
    for line in contents:
        # Make any solitary string on a line into a list so that `for` works.
        # This also incidentally allows tab-delimited lines from the file to be
        # split.
        if isinstance(line, str):
            line = line.split('\t')
        for item in line:
            tally = process_expression(item, max_syll, singletons, verbose, 
                    tally)
    print('\nFinal tally: \n    {} cases of consecutive syllables in excess of '
            '{}.\n    {} cases of consecutive singletons in excess of {}.'.
            format(tally[0], max_syll, tally[1], singletons))
