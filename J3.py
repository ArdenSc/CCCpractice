lines = []
newLines = ""

while True:
    console_in = input()
    if console_in == "":
        break
    lines.append(console_in)

for i, line in enumerate(lines):
    newLine = ""
    if i == 0:
        continue
    count = 1
    lastChar = ''
    for char in line:
        if char == lastChar:
            count += 1
        elif lastChar != '':
            newLine += str(count) + " " + lastChar + " "
            count = 1
        lastChar = char
    newLine += str(count) + " " + lastChar + " "
    newLines += newLine + "\n"

print(newLines)
