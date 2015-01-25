## Convert Pinyin

A Python 3 script to open old Pages files and convert the vowels bearing Pīnyīn-diacritics, in my old Shyrbaw, Longyan, and Pradtino fonts, to standard Unicode. It runs from the command line and looks in a directory "data" for any files it can convert. When finished, the old files are in a new subdirectory `old_files` and the converted files are in `converted`.

Program works for v. 8 of Pages; v. 9 and later use a different format and I don't know how to interpret its bytes.

To do: test suite, using known in and out files (bearing extension `txt` in "reference" directory).

[end]
