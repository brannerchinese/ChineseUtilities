## Format Poem

On-going project to assist prosodic study of Chinese poetry.

[edited 20140312]

---

Tentative Flask server at `app5.py`. Run with `python app5.py`. Output not presently correct.

Function to clean the text of a poem, divide appropriately, and rotate for presentation in columns: `format_poem.py`. Functions:

 * `clean_poem(poem)`: 

   1. split into stanzas at `'\n\n'`;
   1. strip most whitespace, but not linebreaks or ideographic space `'\u3000'`;
   1. break into lines (each of which is a list of characters) at any punctuation specified in variable `to_break_at`;

 * `regularize_line_length(section)`
 * `rotate_lines(section)`

[end]
