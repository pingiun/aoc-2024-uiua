from typing import Any
from collections import Counter

s = [line for line in open('12.test').read().strip().splitlines()]

def get(seq: list[Any], i: int):
    if seq is None:
        return None
    if i < 0 or i >= len(seq):
        return None
    return seq[i]

def windows3(seq):
    for i in range(len(seq)):
        for j in range(len(seq[0])):
            yield [
                #get(get(seq, i-1), j-1),
                get(get(seq, i-1), j), # get(get(seq, i-1), j+1),
                get(get(seq, i), j-1), get(get(seq, i), j), get(get(seq, i), j+1),
                # get(get(seq, i+1), j-1),
                get(get(seq, i+1), j), # get(get(seq, i+1), j+1),
            ]

totals_counter = Counter()

for window in windows3(s):
    middle = window[2]
    print([*window[:2], *window[3:]])
    counts = Counter([*window[:2], *window[3:]])
    print(f' {window[0] or " "} ')
    print(f'{window[1] or " "}{window[2]}{window[3] or " "}')
    print(f' {window[4] or " "} ')
    print()
    del[counts[middle]]
    if middle == 'R':
        print(counts)
    totals_counter[middle] += counts.total()

print(totals_counter)
