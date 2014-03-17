def figure_confidence(matches, trials, exp_avg = 0.49672, round_to=2):
    mu = exp_avg * trials
    epsilon = abs(matches - mu) / float(mu)
    confidence = ((M.exp(epsilon) / ((1 + epsilon) ** (1 + epsilon)))) ** mu
    return abs(round(confidence, round_to))
