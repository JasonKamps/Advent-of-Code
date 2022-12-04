# --- Day 4: Camp Cleanup ---

# I need to find the assignment pairs where one range fully contains the other

# Open file
f = open("4_input.txt", "r")

# Count the assignment pairs where one range fully contains the other
pairs_count = 0
for line in f:
    bounds = []  # [elf1_lower, elf1_upper, elf2_lower, elf2_upper)
    for assignment in line.split(","):
        for bound in assignment.split("-"):
            bounds.append(int(bound))

    # Check if elf1 range is greater than elf2 range
    if bounds[0] <= bounds[2] and bounds[1] >= bounds[3]:
        pairs_count += 1
    # Check if elf2 range is greater than elf1 range
    elif bounds[2] <= bounds[0] and bounds[3] >= bounds[1]:
        pairs_count += 1

print("Part 1 pairs count:", pairs_count)

# --- Part Two ---

# I need to find the assignment pairs where ranges overlap

# Open file
f = open("4_input.txt", "r")

# Count the assignment pairs where ranges overlap
pairs_count = 0
for line in f:
    bounds = []  # [elf1_lower, elf1_upper, elf2_lower, elf2_upper)
    for assignment in line.split(","):
        for bound in assignment.split("-"):
            bounds.append(int(bound))

    # Check if elf1 upper or lower is within elf2 range
    if bounds[2] <= bounds[1] <= bounds[3] or bounds[2] <= bounds[0] <= bounds[3]:
        pairs_count += 1
    # Check if elf2 upper or lower is within elf1 range
    elif bounds[0] <= bounds[2] <= bounds[1] or bounds[0] <= bounds[3] <= bounds[1]:
        pairs_count += 1

print("Part 2 pairs count:", pairs_count)
