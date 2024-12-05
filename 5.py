from collections import defaultdict
from functools import reduce, cmp_to_key

f = open("5.input").read()

ordering, pages = f.split("\n\n")
def push(acc: dict[str, set[str]], key, val):
    acc[key].add(val)
    return acc
def sort_key(a, b):
    if b in order_lookup[a]:
        return -1
    if a in order_lookup[b]:
        return 1
    if b in lookup_rev[a]:
        return 1
    if a in lookup_rev[b]:
        return -1
    return 0

order_lookup = reduce(lambda acc, val: push(acc, val[0], val[1]), [line.split('|') for line in ordering.split('\n')], defaultdict(set))
print(order_lookup)
lookup_rev  = reduce(lambda acc, val: push(acc, val[1], val[0]), [line.split('|') for line in ordering.split('\n')], defaultdict(set))
print(lookup_rev)
sorted_pages = [x for line in ordering.split('\n') for x in line.split('|')]
sorted_pages = sorted(list(set(sorted_pages)), key=cmp_to_key(sort_key))
print(sorted_pages)

spl = dict((b,a) for (a,b) in enumerate(sorted_pages))

manuals = [[page for page in line.split(',')] for line in pages.split('\n') if line.strip() != '']
ans = 0
for manual in manuals:
    middle = manual[len(manual)//2]

    for page in manual:
        if page not in sorted_pages:
            print("Not found")

    sorting = [spl[page] for page in manual]
    if sorted(sorting) == sorting:
        ans += int(middle)

print(ans)
