# --- Day 5: Supply Stacks ---

# I have to move crates between stacks

# Manually initialised stacks (also removed this data from the input file)
stacks = [['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],
          ['V', 'W', 'J'],
          ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
          ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
          ['F', 'W', 'S', 'M', 'P', 'R', 'G'],
          ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],
          ['D', 'H', 'G', 'M', 'R'],
          ['H', 'N', 'M', 'V', 'Z', 'D'],
          ['G', 'N', 'F', 'H']]

# Open file
f = open("5_input.txt", "r")

# Move crates between stacks
for line in f:
    # Parse
    split_line = line.split()
    quantity = int(split_line[1])
    start_stack = int(split_line[3]) - 1
    end_stack = int(split_line[5]) - 1

    # Move
    for _ in range(quantity):
        temp = stacks[start_stack].pop()
        stacks[end_stack].append(temp)

top_crates = ""
for s in stacks:
    top_crates += s[-1]
print("Part 1 top crates:", top_crates)

# --- Part Two ---

# Crates now retain their order when moved

# Manually initialised stacks
stacks = [['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],
          ['V', 'W', 'J'],
          ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
          ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
          ['F', 'W', 'S', 'M', 'P', 'R', 'G'],
          ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],
          ['D', 'H', 'G', 'M', 'R'],
          ['H', 'N', 'M', 'V', 'Z', 'D'],
          ['G', 'N', 'F', 'H']]

# Open file
f = open("5_input.txt", "r")

# Move crates between stacks
for line in f:
    # Parse
    split_line = line.split()
    quantity = int(split_line[1])
    start_stack = int(split_line[3]) - 1
    end_stack = int(split_line[5]) - 1

    # Move
    temp = []
    for _ in range(quantity):
        temp.append(stacks[start_stack].pop())
    for _ in range(len(temp)):
        stacks[end_stack].append(temp.pop())

top_crates = ""
for s in stacks:
    top_crates += s[-1]
print("Part 2 top crates:", top_crates)
