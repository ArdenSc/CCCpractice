with open("input.txt", "r") as data:
    apples = []
    bananas = []
    for i, line in enumerate(data):
        if i < 3:
            apples.append(int(line.strip()))
        else:
            bananas.append(int(line.strip()))


applesScore = apples[0]*3 + apples[1]*2 + apples[2]
bananasScore = bananas[0]*3 + bananas[1]*2 + bananas[2]


if applesScore == bananasScore:
    print("T")
elif applesScore > bananasScore:
    print("A")
else:
    print("B")
