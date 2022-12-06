# rock paper scissors
#
# A = X = Rock      1pt
# B = Y = Paper     2pt
# C = Z = Scissors  3pt
# Win = 6pt, Draw = 3pt, Loose = 0pt


def play(you, opponent):
    match opponent:
        case "A":
            if you == "X":
                return 3+1
            elif you == "Y":
                return 6+2
            else:
                return 0+3
        case "B":
            if you == "X":
                return 0+1
            elif you == "Y":
                return 3+2
            else:
                return 6+3
        case "C":
            if you == "X":
                return 6+1
            elif you == "Y":
                return 0+2
            else:
                return 3+3

if __name__ == "__main__":
    score = 0
    with open("input.txt", "r") as f:
        for l in f:
            l = l[:-1]
            print(l[-1],l[0])
            score += play(l[-1],l[0])
    
    print(score)