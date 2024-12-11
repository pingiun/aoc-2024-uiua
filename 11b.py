import math
import functools
import tqdm

# digits = [int(x) for x in open('11.input').read().strip().split()]

digits = [5, 62914, 65, 972, 0, 805922, 6521, 1639064]

@functools.cache
def grow(digit):
    if digit == 0:
        return [1]
    if digit == [1]:
        return [2024]
    size = math.floor(math.log10(digit)) + 1
    if size % 2 == 0:
        return [digit // (10 ** (size // 2)), digit % (10 ** (size // 2))]
    return [digit * 1024]

def blink(digits):
    return [newdigit for digit in digits for newdigit in grow(digit)]

for _ in tqdm.trange(75):
    print(len(digits))
    digits = blink(digits)

print(len(digits))
