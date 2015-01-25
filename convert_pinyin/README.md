## Convert Pinyin

A Python 3 script to open old Pages files and convert the vowels bearing Pīnyīn-diacritics, in my old Shyrbaw, Longyan, and Pradtino fonts, to standard Unicode. It runs from the command line and looks in a directory "data" for any files it can convert. When finished, the old files are in a new subdirectory `old_files` and the converted files are in `converted`.

Program works for v. 3 of Pages ("Pages '08").

V. 4 ("Pages '09") and v. 5 ("Pages") use formats incompatible with the simple text-based, XML format used by Pages '08. I don't know how to interpret these more recent formats. Based on my reading on line in January, 2015, this is a recognized problem (see [Magnus Lewan's comments](http://pagesfaq.blogspot.com/2013/11/undocumented-proprietary-file-format-in.html), for example). Xcode will open such files, but I haven't found an automate-able way to then save them to another format. At present my work-around is to open the files in a current version of Pages and save them to RTF — generally by way of a wordprocessor.

A copy of the old Shyrbaw font is included in the repository for reference.

----

**To do**: 

 1. Test suite, using known in and out files (bearing extension `txt` in "reference" directory).
 1. Capitalized versions of the diacritic-bearing vowels are not yet treated, and neither is _ǖ_. At the moment I don't remember the mappings of those vowels in the Shyrbaw font; I will have to open it in a font editor.

[end]
