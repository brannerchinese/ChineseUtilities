# bernoulli.py
# David Prager Branner
# 20131116

import math

def prob(trials, successes, prob_success):
    combinations = (math.factorial(trials) / 
            (math.factorial(successes) * math.factorial(trials - successes)))
    bernoulli_prob = (combinations * (prob_success ** successes) * 
            (1-prob_success) ** (trials - successes))
    return bernoulli_prob
