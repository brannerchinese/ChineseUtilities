## ChineseUtilities

 1. `separate_pinyin.py` takes a string of Pīnyīn as input and returns a list of the discrete component syllables. In an interpeter use

        >>> import separate_pinyin as S
        >>> S.separate('hànyǔpīnyīn')
        ['hàn', 'yǔ', 'pīn', 'yīn']

 1. To include *érhuà* 兒化 syllables, use a second argument, `'r'`:
 
        >>> import separate_pinyin as S
        >>> S.separate('hǎojǐběnr', 'r')
        ['hǎo', 'jǐ', 'běnr']

 1. Ordinary syllables `ér`, `ěr`, `èr` belong to the basic syllable-inventory and do not require the argument `'r'`. Two files containing the syllable inventories are found in a `DATA` directory; note that those that are not actually attested in Standard Mandarin (such as `*dén`) are included but marked as `True` in a second field; they will raise an error in `separate_pinyin.py`.
 
 1. `separate_pinyin.py` can be tested with an infinite loop of randomly generated syllables, using ``separate_pinyin_call.py`. On control-c the loop terminates and statistics are reported. The loop also terminates if an error is found, but without statistics.

 1. All capitalized Pīnyīn letters are automatically reduced to lower case in order to simplify the processes.

[end]

