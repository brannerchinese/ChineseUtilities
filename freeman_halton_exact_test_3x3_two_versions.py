# freeman_halton_exact_test_3x3_two_versions.py
# 20130626, works.
# David Prager Branner
# For Python 3

'''For a 3x3 contingency table:

          1   2   3
        -------------
    a   | a | d | g |
        -------------
    b   | b | e | h |
        -------------
    c   | c | f | i |
        -------------

, input as nine elements, return the exact probability p.

Implemented using two (apparently congruent) equations:

    1. That found at http://www.danielsoper.com/statcalc3/calc.aspx?id=59

    2. That found as (15, right side) of Arthur W. Ghent, A Method for Exact
    Testing of 2X2, 2X3, 3X3, and Other Contingency Tables, Employing Binomial
    Coefficients; American Midland Naturalist, Vol. 88, No. 1. (Jul., 1972),
    pp. 15-27.

As of 20130626, the results of the two equations are identical, and different
from the results being returned by the danielsoper.com on-line calculator.

Results have been checked against a number of those shown on
http://www.physics.csbsju.edu/stats/exact.html (20130626) and found correct.

'''

from math import factorial

def binomial(n, k):
    return (factorial(n) / (factorial(k) * factorial(n-k)))

def main(a, b, c, d, e, f, g, h, i):
    n = a + b + c + d + e + f + g + h + i
    soper_p = ( binomial((a+b+c), a) * binomial((b+c), b) * 
          binomial((d+e+f), d) * binomial((e+f), e) * 
          binomial((g+h+i), g) * binomial((h+i), h) * 
          factorial(a+d+g) * factorial(b+e+h) * factorial(c+f+i) / 
          factorial(n) )
    # Below is for Ghent's method, right side of eqn 15
    prod_of_all_factorials = ( 
            factorial(a) * factorial(d) * factorial(g) *
            factorial(b) * factorial(e) * factorial(h) *
            factorial(c) * factorial(f) * factorial(i) )
    top_three_factorials = ( 
            factorial(a+b+c) * factorial(d+e+f) * factorial(g+h+i) )
    bottom_three_factorials = ( 
            factorial(a+d+g) * factorial(b+e+h) * factorial(c+f+i) )
    ghent_p1 = ( (top_three_factorials/prod_of_all_factorials) / 
          (factorial(n) / bottom_three_factorials) )
    print('Soper', soper_p)
    print('Ghent', ghent_p1)
