# priorities: a-z = 1-26, A-Z = 27-52

def get_prio(x: str):
    if x.isupper():
        return ord(x) - 38
    else:
        return ord(x) - 96

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        sum = 0
        for l in f:
            l = l[:-1]
            half = len(l)//2
            ll = l[0:half]
            lr = l[half:]
            commonc = set(ll).intersection(set(lr))
            for e in commonc:
                sum += get_prio(e)
    print(sum)
