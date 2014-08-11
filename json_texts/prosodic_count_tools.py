#! /usr/bin/env python
# prosodic_count_tools.py
# David Prager Branner
# 20140810, works

import re

def count_syllables(t, feature, prosodic_type='rhyme'):
    count = 0
    for section in t:
        for line in section["section"]["lines"]:
            if ("prosodic_type" in line and 
                    "transc" in line and
                    line["prosodic_type"] == prosodic_type and 
                    re.search(feature, line["transc"][-1])):
#                print(line["transc"][-1])
                count += 1
    return count

def find_all_tone_counts(t):
    all_tone_count = {}
    pyng = '[^ptkQH]-'
    shaang = '[Q]-'
    chiuh = '[H]-'
    ruh = '[ptk]-'
    all_tone_count[('pyng', 'rhyme')] = count_syllables(t, pyng, 'rhyme')
    all_tone_count[('pyng', 'nonrhyme')] = count_syllables(t, pyng, 'nonrhyme')
    all_tone_count[('shaang', 'rhyme')] = count_syllables(t, shaang, 'rhyme')
    all_tone_count[('shaang', 'nonrhyme')] = count_syllables(
            t, shaang, 'nonrhyme')
    all_tone_count[('chiuh', 'rhyme')] = count_syllables(t, chiuh, 'rhyme')
    all_tone_count[('chiuh', 'nonrhyme')] = count_syllables(
            t, chiuh, 'nonrhyme')
    all_tone_count[('ruh', 'rhyme')] = count_syllables(t, ruh, 'rhyme')
    all_tone_count[('ruh', 'nonrhyme')] = count_syllables(t, ruh, 'nonrhyme')
    return all_tone_count

def count_poetic_lines(t):
    count = 0
    for section in t:
        for line in section["section"]["lines"]:
            if (line["text_type"] == 'verse' and 
                    (line["prosodic_type"] == 'rhyme' or 
                    line["prosodic_type"] == 'nonrhyme')):
#                print(line["transc"][-1])
                count += 1
        print('end of lines')
    return count

def count_shanqwoei():
    # In a given section,
    # decide the rhyming tone;
    # count the cases of that tone in nonrhyme lines.
    pass