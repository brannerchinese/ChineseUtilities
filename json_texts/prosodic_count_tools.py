#! /usr/bin/env python
# prosodic_count_tools.py
# David Prager Branner
# 20140818, works

"""Provide methods for counting number of syllables and lines in poetry."""

import re

class Counter():
    def __init__(self, text):
        self.text = text
        self.count = 0
        self.tones = {
                'pyng': '[^ptkQH]-',
                'shaang': '[Q]-',
                'chiuh': '[H]-',
                'ruh': '[ptk]-'
                }
        self.states = ['rhyme', 'nonrhyme']

    def count_sylls(self, feature, prosodic_type='rhyme'):
        """Return number of syllables of a specific type, as integer."""
        self.count = 0
        for stanza in self.text:
            for line in stanza["lines"]:
                if ("prosodic_type" in line and
                        "transc" in line and
                        line["prosodic_type"] == prosodic_type and
                        re.search(feature, line["transc"][-1])):
                    self.count += 1
        return self.count

    def find_all_tones(self):
        """Return dictionary of all tone-counts, rhyming and non-rhyming."""
        all_tones = {
                (tone, state): self.count_sylls(self.tones[tone], state)
                for tone in self.tones
                for state in self.states
                }
        return all_tones

    def count_poetic_lines(self):
        """Return number of rhyme and nonrhyme lines, as integer."""
        self.count = 0
        for stanza in self.text:
            for line in stanza["lines"]:
                if (line["text_type"] == 'yunnwen' and
                        (line["prosodic_type"] == 'rhyme' or
                        line["prosodic_type"] == 'nonrhyme')):
                    self.count += 1
        return self.count

    def count_stanzas_per_rhyme(self):
        """Report number of stanzas wholly in each rhyme, & in mixed rhymes."""
        stanzas_rhyming_in_tone = {
                'pyng': 0,
                'shaang': 0,
                'chiuh': 0,
                'ruh': 0,
                'mixed': 0
                }
        for stanza in self.text:
            if stanza["section_type"] == "stanza":
                rhymeword_tones = self.name_rhyming_tone(stanza)
                print(rhymeword_tones)
                if len(rhymeword_tones) == 1:
                    stanzas_rhyming_in_tone[str(list(rhymeword_tones)[0])] += 1
                elif rhymeword_tones:
                    stanzas_rhyming_in_tone['mixed'] += 1
        return stanzas_rhyming_in_tone

    def count_shanqwoei(self, stanza):
        # In a given stanza,
        # call `self.name_rhyming_tone(stanza)` to decide the rhyming tone;
        # If valid return value, count the cases of that tone in nonrhyme lines.
        pass

    def name_rhyming_tone(self, stanza):
        """Report the tone(s) of the rhymewords appearing in the stanza."""
        rhymeword_tones = set()
        if stanza['section_type'] == 'stanza':
            for line in stanza['lines']:
                if line['prosodic_type'] == 'rhyme':
                    for tone in self.tones:
                        if re.search(self.tones[tone], line['transc'][-1]):
                            rhymeword_tones.add(tone)
                            break
        return rhymeword_tones
