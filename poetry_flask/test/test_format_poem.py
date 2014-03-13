# test_format_poem.py
# David Prager Branner
# 20140312, works

"""Test the basic functions for preparing a Chinese poem for display."""

import format_poem as F
from data_for_testing_format_poem import (
        poem_list, cleaned_list, rotation_list, format_list)

def test_clean_01():
    for poem, cleaned in zip(poem_list, cleaned_list):
        assert F.clean_poem(poem) == cleaned

def test_regularize_line_length_01():
    """Test whether all lines now have the same length."""
    for poem in poem_list:
        poem = F.clean_poem(poem)
        section = F.regularize_line_length(poem[0])
        lengths = [len(line) for line in section]
        assert max(lengths) == min(lengths)

def test_rotate_01():
    """Test whether rotated poem-section matches expected form."""
    for poem, rotation in zip(poem_list, rotation_list):
        poem = F.clean_poem(poem)
        section = F.regularize_line_length(poem[0])
        assert F.rotate_lines(section) == rotation

def test_rotate_02():
    """Test whether four consecutive rotations bring us back to the original."""
    for poem in poem_list:
        (F.regularize_line_length(F.clean_poem(poem)) ==
                F.rotate_lines(
                        F.rotate_lines(F.rotate_lines(F.rotate_lines(
                                F.regularize_line_length(F.clean_poem(poem))))
                        )
                )
        )

def test_format_01():
    """Test full formatting function."""
    for poem, formatted in zip(poem_list, format_list):
        assert F.format_poem(poem, stanza_len=8) == formatted
