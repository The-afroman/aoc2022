def find_marker(line: str):
    buffLen = 14
    start = 0
    end = buffLen + start
    buff = line[start:end]
    while len(set(buff)) != len(buff):
        start += 1
        end = buffLen + start
        buff = line[start:end]
    return end

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        for l in f:
            if l != "\n": print(find_marker(l))
