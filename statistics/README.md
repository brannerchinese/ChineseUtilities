## ChineseUtilities/statistics/

Utilities to help me with Chinese-language work

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
 
[end]

