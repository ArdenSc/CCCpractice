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


with open("inputS3.txt", 'r') as data:
    grid = []
    for i, line in enumerate(data):
        grid.append([])
        line = line.strip()
        for integer in split_string(line):
            grid[i].append(integer)

