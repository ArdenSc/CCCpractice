lines = []


with open("inputJ2.txt", 'r') as data:
    for line in data:
        line = line.strip()
        num = ""
        op = ''
        for char in line:
            if char.isdigit():
                num += char
            elif char != ' ':
                op = char
                break
        if op != '':
            lines.append([int(num), op])


output = ""
for line in lines:
    newline = ""
    for _ in range(line[0]):
        newline += line[1]
    output += newline + "\n"


print(output)
