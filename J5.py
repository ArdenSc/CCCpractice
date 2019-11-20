def split_string(string):
    output = []
    buffer = ""
    for char in string:
        if char == ' ':
            output.append(buffer)
            buffer = ""
        else:
            buffer += char
    if buffer != "":
        output.append(buffer)
    return output


def find_subs(string):
    locations = []
    for i, rule in enumerate(rules):
        index = 0
        while True:
            location = string.find(rule[0], index)
            if location != -1:
                index = location + len(rule[0])
                locations.append([i + 1, location + 1, string[:location] + rule[1] + string[location + len(rule[0]):]])
            else:
                break
    return locations if locations != [] else False


def find_sol(section):
    for part in section:
        if tmp := find_subs(part["start"][3]):
            part["end"] = []
            for solution in tmp:
                if part["start"][0] + 1 == steps:
                    if solution[2] == final:
                        print(solution)
                        exit()
                else:
                    part["end"].append({"start": [part["start"][0] + 1] + solution})
            find_sol(part["end"])


with open("inputJ5.txt", 'r') as data:
    rules = []
    for lineNum, line in enumerate(data):
        line = line.strip()
        if lineNum < 3:
            rules.append(split_string(line))
        elif lineNum == 3:
            steps, initial, final = split_string(line)
            steps = int(steps)


find_sol([{"start": [0, 0, 0, initial]}])
