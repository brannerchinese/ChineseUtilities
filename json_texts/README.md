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
t = H.retrieve_data(filename)
        ```

[end]
