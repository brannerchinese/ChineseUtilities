#! /usr/bin/env python
# prosodic_count_tools.py
# David Prager Branner
# 20140810, works

"""Provide methods for counting number of syllables and lines in poetry."""

import re

class Counter():
    def __init__(self, text):
        self.text = text
        self.count = 0
        self.textones = {
                'pyng': '[^ptkQH]-',
                'shaang': '[Q]-',
                'chiuh': '[H]-',
                'ruh': '[ptk]-'
                }
        self.states = ['rhyme', 'nonrhyme']

    def count_sylls(self, feature, prosodic_type='rhyme'):
        """Return number of syllables of a specific type, as integer."""
        self.count = 0
        for section in self.text:
            for line in section["section"]["lines"]:
                if ("prosodic_type" in line and 
                        "transc" in line and
                        line["prosodic_type"] == prosodic_type and 
                        re.search(feature, line["transc"][-1])):
    #                print(line["transc"][-1])
                    self.count += 1
        return self.count
    
    def find_all_tones(self):
        """Return dictionary of all tone-counts, rhyming and non-rhyming."""
        all_tones = {
                (tone, state): self.count_sylls(self.textones[tone], state) 
                for tone in self.textones 
                for state in self.states
                }
        return all_tones
    
    def count_poetic_lines(self):
        """Return number of rhyme and nonrhyme lines, as integer."""
        self.count = 0
        for section in self.text:
            for line in section["section"]["lines"]:
                if (line["text_type"] == 'verse' and 
                        (line["prosodic_type"] == 'rhyme' or 
                        line["prosodic_type"] == 'nonrhyme')):
    #                print(line["transc"][-1])
                    self.count += 1
        return self.count
    
    def count_shanqwoei(self):
        # In a given section,
        # decide the rhyming tone;
        # count the cases of that tone in nonrhyme lines.
        pass