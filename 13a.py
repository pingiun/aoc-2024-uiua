import re
from typing import Iterable
button_re = re.compile(r'Button [AB]: X\+(\d+), Y\+(\d+)')
prize_re = re.compile(r'Prize: X=(\d+), Y=(\d+)')

i = open('13.test').read().strip()
machines = [(*button_re.findall(machine), prize_re.findall(machine)[0]) for machine in i.split('\n\n')]

def ints(seq):
    if isinstance(seq, list):
        return [ints(x) for x in seq]
    if isinstance(seq, tuple):
        return tuple(ints(x) for x in seq)
    if isinstance(seq, int):
        return seq
    if isinstance(seq, str):
        try:
            return int(seq)
        except ValueError:
            return seq
    return seq

machines = ints(machines)

for btn_a, btn_b, prize in machines:
    print(btn_a)
