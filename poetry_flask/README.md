## Format Poem

On-going project to assist prosodic study of Chinese poetry.

[edited 20140312]

---

**Tentative Flask server** at `app5.py`. Run with `python app5.py`. Output not presently correct.

**Function to prepare poem for presentation**: clean the text of a poem, divide appropriately, and rotate for presentation in columns: `format_poem.py`. Functions may take a "section" (maximum 8 or user-set number of lines) or "poem" (whole poem):

 * `clean_poem(poem)`: 

   1. split into stanzas at `'\n\n'`;
   1. strip most whitespace, but not linebreaks or ideographic space `'\u3000'`;
   1. break into lines (each of which is a list of characters) at any punctuation specified in optional variable `to_break_at`.

 * `regularize_line_length(section)`:

   1. find the longest line in the section;
   1. add ideographic space `'\u3000'` to the end of any lines shorted than that maximum so that all lines are the same length.

 * `rotate_lines(section)`: Rotate each section for display in columns.

**Test suite** in `test/`. Run using `py.test test`. Poetry and other test-structures are in a discrete file `data_for_testing_format_poem.py`.

[end]
