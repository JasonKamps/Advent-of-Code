# --- Day 3: Rucksack Reorganization ---

# I need to find the common letter in the two halves of a string, and sum their priorities


# Finds the common letter in the two halves of a string
# Returns the common letter's priority
def process_line(string):
    # Loop through first half of string
    for letter in line[:len(string) // 2]:
        # Loop through second half of string
        for letter2 in line[len(string) // 2:]:
            if letter == letter2:
                # Common letter found
                if ord(letter) >= 97:
                    # Lowercase
                    return ord(letter) - 96
                else:
                    # Uppercase
                    return ord(letter) - 38


# Open file
f = open("3_input.txt", "r")

# Sum the priorities of the common letter in the two halves of each line
priority_sum = 0
for line in f:
    priority_sum += process_line(line)

print("Part 1 priority sum:", priority_sum)

# --- Part Two ---

# I need to find the common letter in each group of three lines, and sum their priorities


# Finds the common letter in the three strings of a group
# Returns the common letter's priority
def process_group(g):
    # Loop through all letters
    for letter in g[0]:
        for letter2 in g[1]:
            for letter3 in g[2]:
                if letter == letter2 == letter3:
                    # Common letter found
                    if ord(letter) >= 97:
                        # Lowercase
                        return ord(letter) - 96
                    else:
                        # Uppercase
                        return ord(letter) - 38

# Open file
f = open("3_input.txt", "r")

# Sum the priorities of the common letter in each group of three lines
priority_sum = 0
group = [""] * 3
for index, line in enumerate(f):
    group[index % 3] = line

    if index % 3 == 2:
        priority_sum += process_group(group)

print("Part 2 priority sum:", priority_sum)
