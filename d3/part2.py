# priorities: a-z = 1-26, A-Z = 27-52

def get_prio(x: str):
    if x.isupper():
        return ord(x) - 38
    else:
        return ord(x) - 96

if __name__ == "__main__":
    sum = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
        groups = [list(x) for x in zip(lines[0::3], lines[1::3], lines[2::3])]
        for g in groups:
            commonc = set(g[0][:-1]).intersection(
                set(g[1][:-1])).intersection(g[2][:-1])
            for e in commonc:
                sum += get_prio(e)
    print(sum)
