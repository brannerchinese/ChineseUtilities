## ChineseUtilities

 1. `separate_pinyin.py` takes a string of Pīnyīn as input and returns a list of the discrete component syllables. In an interpeter use

        >>> import separate_pinyin as S
        >>> S.separate('hànyǔpīnyīn')
        ['hàn', 'yǔ', 'pīn', 'yīn']

 1. To include *érhuà* 兒化 syllables, use a second argument, `'r'`:
 
        >>> import separate_pinyin as S
        >>> S.separate('hǎojǐběnr', 'r')
        ['hǎo', 'jǐ', 'běnr']

 1. Ordinary syllables `ér`, `ěr`, `èr` belong to the basic syllable-inventory and do not require the argument `'r'`. Two files containing the syllable inventories are found in the `DATA` directory; those are not actually attested in Standard Mandarin (such as `*dén`) are present in the file but marked as `True` in a second field; they will raise an error in `separate_pinyin.py`; attested syllables have no such notation.
 
 1. **Notes**: 
  * All capitalized Pīnyīn letters are automatically reduced to lower case in order to simplify the processes.
  * Syllables both with and without tone-marks are included in the inventories. No attempt is made to decide whether a particular Pīnyīn string actually means anything — this is purely a tool to break well-formed Pīnyīn strings into their component syllables, without regard to meaning.

 1. `separate_pinyin.py` can be tested with an infinite loop of randomly generated syllables, using ``separate_pinyin_call.py`. On control-c the loop terminates and statistics are reported. The loop also terminates if an error is found, but without statistics.

        >>> C.main()

 or
        
        >>> C.main('r')
 
 To see test-by-test output of `separate_pinyin_call.py`, use a third argument `output=True` (the default is `False`):
 
        >>> C.main(output=True)

 or
        
        >>> C.main('r', output=True)
 
 Output:
 
        From remòshuǎngyuan
            produced ['re', 'mò', 'shuǎng', 'yuan'].
        From yǒusan
            produced ['yǒu', 'san'].
        From lōujuǎn
            produced ['lōu', 'juǎn'].
        From gáguàichèyǎo
            produced ['gá', 'guài', 'chè', 'yǎo'].
        From dēikūn
            produced ['dēi', 'kūn'].
        From dunchāibiao
            produced ['dun', 'chāi', 'biao'].
        From fēngcěipènglaifěngdǎ
            produced ['fēng', 'cěi', 'pèng', 'lai', 'fěng', 'dǎ'].

[end]
