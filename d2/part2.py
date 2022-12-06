# rock paper scissors
#
# A = Rock      1pt
# B = Paper     2pt
# C = Scissors  3pt
# Z = Win = 6pt, Y = Draw = 3pt, X = Loose = 0pt


def play(strat, move):
    match move:
        case "A":
            if strat == "Z":
                return 6+2
            elif strat == "Y":
                return 3+1
            else:
                return 0+3
        case "B":
            if strat == "Z":
                return 6+3
            elif strat == "Y":
                return 3+2
            else:
                return 0+1
        case "C":
            if strat == "Z":
                return 6+1
            elif strat == "Y":
                return 3+3
            else:
                return 0+2

if __name__ == "__main__":
    score = 0
    with open("input.txt", "r") as f:
        for l in f:
            l = l[:-1]
            if l:
                print(l[-1],l[0])
                score += play(l[-1],l[0])
    
    print(score)