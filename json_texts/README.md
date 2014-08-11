## Tools for Manipulating Poetry in JSON Format

 1. `handle_files.py`:

   1. This program uses the shell's `gpg` program. Make sure `gpg` is installed and a private key set up. Place the passphrase in a file `phrase.ignore`. There are two caveats: 

     1. The `.gitignore` file will not allow files with `.ignore` extensions to be pushed to the repository, but that does not mean your passphrase is safe this way! 

     1. Here `subprocess.call` is called without the argument `shell=True`, so `shell` is `False` by default, which provides a measure of safety against shell injection. But a measure of safety is not perfect safety.

   1. To encrypt an existing file, `filename`:

        ```
import handle_files as H
H.store_data('', filename)
        ```

   1. To decrypt `filename`:

        ```
import handle_files as H
text = H.retrieve_data(filename)
        ```

 1. `prosodic_count_tools.py`:

   1. First use `handle_files` to fetch a JSON-formatted text. Then instantiate `Counter` and use its methods on the text. The most important is `find_all_tones`:

        ```
In [1]: import handle_files as H
In [2]: import prosodic_count_tools as P
In [3]: text = H.retrieve_data(filename)
In [4]: C = P.Counter(text)
In [5]: C.find_all_tones()
Out[5]: 
{('pyng', 'nonrhyme'): 170,
 ('pyng', 'rhyme'): 289,
 ('ruh', 'rhyme'): 104,
 ('chiuh', 'nonrhyme'): 97,
 ('ruh', 'nonrhyme'): 76,
 ('shaang', 'nonrhyme'): 70,
 ('shaang', 'rhyme'): 116,
 ('chiuh', 'rhyme'): 104}
        ```

   1. Another is `count_poetic_lines`

        ```
In [6]: C.count_poetic_lines()
Out[6]: 1026
        ```

### To do

 1. Revise JSON schema toprovide an additional attribute of "lines" for alternate transcriptions, for the purposes of _shyeyunn_.
 1. Write `name_rhyming_tone`.
 1. Write `count_shanqwoei`.

[end]
