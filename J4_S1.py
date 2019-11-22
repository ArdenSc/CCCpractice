grid = [[
    1, 2
], [
    3, 4
]]

with open("inputJ4.txt", "r") as data:
    line = data.readline()

for char in line:
    if char == 'H':
        temp = grid[0]
        grid[0] = grid[1]
        grid[1] = temp
    else:
        for row in grid:
            temp = row[0]
            row[0] = row[1]
            row[1] = temp

print(f"{grid[0][0]} {grid[0][1]}\n{grid[1][0]} {grid[1][1]}")
