ChineseUtilities
================

Utilities to help me with Chinese-language work

 1. `character_count.py`: Count the Chinese characters (only) in a file and return their overall percentages. File to be opened must be in directory `DATA`.
 1. `fisher_exact_test.py`: Calculate the Fisher exact probability for a 2x2 contingency table.
 2. `freeman_halton_exact_test_3x3_two_versions.py`: Calculate the Freeman-Halton exact probability for a 3x3 contingency table. For a table

                   1   2   3                                                        
                 -------------                                                       
             a   | a | d | g |                                                       
                 -------------                                                       
             b   | b | e | h |                                                       
                 -------------                                                       
             c   | c | f | i |                                                       
                 -------------                                                       
 run 
 
         main(a, b, c, d, e, f, g, h, i)

 Output is the exact probability, calculated using two congruent but different methods.
 
 1. `separate_pinyin.py` takes a string of Pīnyīn as input and returns a list of the discrete component syllables. In an interpeter use

        >>> import separate_pinyin as S
        >>> S.separate('hànyǔpīnyīn')
        ['hàn', 'yǔ', 'pīn', 'yīn']

 To include *érhuà* 兒化 syllables, use a second argument, `'r'`:
 
        >>> import separate_pinyin as S
        >>> S.separate('hǎojǐběnr')
        ['hǎo', 'jǐ', 'běnr']

 Ordinary syllables `ér`, `ěr`, `èr` belong to the basic syllable-inventory and do not require the argument `'r'`. Two files containing the syllable inventories are found in a `DATA` directory; note that those that are not actually attested in Standard Mandarin (such as `*dén`) are included but marked as `True` in a second field; they will raise an error in `separate_pinyin.py`.
 
 `separate_pinyin.py` can be tested with an infinite loop of randomly generated syllables, using ``separate_pinyin_call.py`. On control-c the loop terminates and statistics are reported. The loop also terminates if an error is found, but without statistics.

[end]

