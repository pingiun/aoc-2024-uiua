import tqdm

digits = [int(x) for x in open('11.input').read().strip().split()]

def blink(digits):
    newdigits = []
    for digit in digits:
        if digit == 0:
            newdigits += [1]
            continue
        sdigit = str(digit)
        slen = len(sdigit)
        if slen % 2 == 0:
            newdigits += [int(sdigit[:slen//2]), int(sdigit[slen//2:])]
            continue
        newdigits += [digit * 2024]
    return newdigits

for _ in tqdm.trange(75):
    print(len(digits))
    digits = blink(digits)

print(len(digits))
