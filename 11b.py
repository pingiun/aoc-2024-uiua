import math
import time
from collections import Counter

digits: Counter[int] = Counter([int(x) for x in open('11.input').read().strip().split()])

answers: dict[int, dict[int, int]] = {}

def grow(digit: int) -> list[int]:
    if digit == 0:
        return [1]
    if digit == 1:
        return [2024]
    size = math.floor(math.log10(digit)) + 1
    if size % 2 == 0:
        return [digit // (10 ** (size // 2)), digit % (10 ** (size // 2))]
    return [digit * 2024]

start = time.time()
for _ in range(75):
    newdigits: Counter[int] = Counter()
    for digit, cnt in digits.items():
        newdigits.update({newdigit: newcnt * cnt for newdigit, newcnt in Counter(grow(digit)).items()})
    digits = newdigits

print(digits.total())
print(f"Found in {time.time() - start} seconds")
