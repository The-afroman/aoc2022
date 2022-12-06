from typing import TextIO
import re

def parse_cargo(file: TextIO):
    letters = r"[a-zA-Z]"
    numbers = r"[0-9]"
    stacks = {}
    l = file.readline()
    while l != "\n":
        stackItem = None
        ccnt = 0
        for c in l:
            if re.match(letters,c):
                stackItem = c
                ccnt += 1
            elif re.match(numbers,c):
                pass
            else:
                ccnt += 1
            
            if ccnt % 4 == 0 and stackItem != None:
                stackNum = ccnt//4
                if stacks.get(stackNum):
                    stacks[stackNum].append(stackItem)
                else:
                    stacks[stackNum] = [stackItem]
                stackItem = None

        l = file.readline()
    return stacks

def move_crates(file: TextIO, stacks: dict[list[str]]):
    newStacks = stacks
    for l in file:
        if l != "\n":
            l = l.split()
            count = int(l[1])
            src = int(l[3])
            dst = int(l[-1])
            for _ in range(count):
                x = newStacks[src].pop(0)
                newStacks[dst].insert(0, x)
    return newStacks

if __name__ == "__main__":
    f = open("input.txt", "r")
    stacks = parse_cargo(f)
    stacks = dict(sorted(move_crates(f, stacks).items()))
    for _, x in stacks.items():
        print(str(x[0]),end="")
