# fisher_exact_test.py
# 20130526
# David Prager Branner
'''Perform Fisher's Exact test on four variables, a two-by-two contingency
table.'''

import math

def main(a, b, c, d):
    return ((math.factorial(a + b) * math.factorial(c+d) * math.factorial(a+c) *
            math.factorial(b+d)) / (math.factorial(a) * math.factorial(b) * 
            math.factorial(c) * math.factorial(d) * math.factorial(a+b+c+d)))
