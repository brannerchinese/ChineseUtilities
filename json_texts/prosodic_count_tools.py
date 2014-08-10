import re
def count_syllables(feature, prosodic_type='rhyme'):
    count = 0
    for section in t:
        for line in section["section"]["lines"]:
            if ("prosodic_type" in line and 
                    "transc" in line and
                    line["prosodic_type"] == prosodic_type and 
                    re.search(feature, line["transc"][-1])):
                print(line["transc"][-1])
                count += 1
    return count
--

# Ideally, tabulate all values, rhyming and non-rhyming, in a single function.
# pyng:   feature = '[^ptkQH]-'
# shaang: feature = '[Q]-'
# chiuh:  feature = '[H]-'
# ruh:    feature = '[ptk]-'


def count_poetic_lines():
    count = 0
    for section in t:
        for line in section["section"]["lines"]:
            if (line["text_type"] == 'verse' and 
                    (line["prosodic_type"] == 'rhyme' or 
                    line["prosodic_type"] == 'nonrhyme')):
                print(line["transc"][-1])
                count += 1
        print('end of lines')
    return count
--

def count_shanqwoei():
    # In a given section,
    # decide the rhyming tone;
    # count the cases of that tone in nonrhyme lines.
    pass