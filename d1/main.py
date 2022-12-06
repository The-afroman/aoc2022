
f = open("input.txt", "r")
lines = f.readlines()
elf_food = []
sum = 0
for l in lines:
    if l != "\n":
        sum += int(l[:-1])
    else:
        elf_food.append(sum)
        sum = 0
elf_food.sort(reverse=True)
print(elf_food[0])
sum = 0
for x in elf_food[0:3]:
    sum += x
print(sum)