import sys
from ast import literal_eval
import os


infile = open(os.path.join(os.path.dirname(__file__), 'prime_pairs.txt'))
PRIME_PAIRS = literal_eval(infile.read())
for key in PRIME_PAIRS.keys():
    PRIME_PAIRS[key] = set(PRIME_PAIRS[key])  # literal_eval doesn't support sets, hence we convert here
infile.close()


def prime_set(wanted_size):
    candidate_queue = [([], set(PRIME_PAIRS.keys()))]
    best_sum, best_val = sys.maxint, None
    while candidate_queue:
        verified, candidates = candidate_queue.pop()
        if sum(verified) >= best_sum:
            continue
        if len(verified) == wanted_size:
            best_sum = sum(verified)
            best_val = verified
            continue
        if len(candidates) + len(verified) < wanted_size:
            continue
        candidate = candidates.pop()
        candidate_queue = [(verified + [candidate], PRIME_PAIRS[candidate] & candidates)] + candidate_queue
        candidate_queue = [(verified, candidates)] + candidate_queue
    return sorted(best_val)


