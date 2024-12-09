from typing import Optional, Tuple


s = open("9.input").read().strip()

Disk = list[Optional[int]]

disk: Disk = []

def printdisk(disk: Disk):
    print("".join((x == 0 or x) and str(x) or '.' for x in disk))

class Defragmenter:
    def __init__(self):
        self.start_pointer = 0
        self.end_pointer = None
        self.end_steps = []
        self.start_steps = []

    def next_bit_from_end(self, disk: Disk) -> Tuple[int, Optional[int]]:
        if self.end_pointer is None:
            self.end_pointer = len(disk)
        steps = 0
        for i in reversed(range(0, self.end_pointer)):
            x = disk[i]
            steps += 1
            if x is not None:
                self.end_pointer = i
                self.end_steps.append(steps)
                return i, x
        return -1, None

    def next_bit_from_front(self, disk: Disk) -> Optional[int]:
        steps = 0
        for i in range(self.start_pointer, len(disk)):
            x = disk[i]
            steps += 1
            if x is None:
                self.start_pointer = i
                self.start_steps.append(steps)
                return i

    def step(self, disk: Disk) -> bool:
        index, item = self.next_bit_from_end(disk)
        if item is None:
            return False
        firstempty = self.next_bit_from_front(disk)
        if firstempty is None:
            return False
        if firstempty >= index:
            return False
        # print("Moving", item, "to position", firstempty)
        disk[firstempty], disk[index] = disk[index], disk[firstempty]
        return True

for i, c in enumerate(s):
    if i % 2 == 0:
        disk += [i//2] * int(c)
        # print(str(i//2) * int(c), end='')
    else:
        disk += [None] * int(c)
        # print('.' * int(c), end='')
printdisk(disk)

defragmenter = Defragmenter()

steps = 0
while defragmenter.step(disk):
    steps += 1
    # printdisk(disk)

print(f"Done {steps} steps")
print("Average end steps:", sum(defragmenter.end_steps) / len(defragmenter.end_steps))
print("Average start steps:", sum(defragmenter.start_steps) / len(defragmenter.start_steps))
ans = 0
for i, num in enumerate(disk):
    if num is None:
        continue
    ans += i * num

print(ans)
