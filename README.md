## ChineseUtilities

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
 
 1. `separate_pinyin` takes a string of Pīnyīn as input and returns a list of the discrete component syllables. 

[end]

