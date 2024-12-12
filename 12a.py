from typing import Any


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
                [get(get(seq, i-1), j-1), get(get(seq, i-1), j), get(get(seq, i-1), j+1)],
                [get(get(seq, i), j-1), get(get(seq, i), j), get(get(seq, i), j+1)],
                [get(get(seq, i+1), j-1), get(get(seq, i+1), j), get(get(seq, i+1), j+1)],
            ]

print(next(windows3(s)))
