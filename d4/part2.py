def make_rng(x: str):
    x = x.split(sep="-")
    low = int(x[0])
    high = int(x[1])
    return range(low, high+1)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tot = 0
        for l in f:
            l = l[:-1]
            l = l.split(sep=",")
            x = set(make_rng(l[0]))
            y = set(make_rng(l[1]))
            intersect = x.intersection(y)
            if intersect:
                tot += 1
    print(tot)