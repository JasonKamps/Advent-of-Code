# --- Day 1: Calorie Counting ---

# I need to find the elf carrying the most calories

# Open file
f = open("1_input.txt", "r")

# Sum the number of calories of each elf and store in list
elf_calories = []
calorie_sum = 0
for line in f:
    if line != "\n":
        calorie_sum += int(line)
    else:
        elf_calories.append(calorie_sum)
        calorie_sum = 0

print(elf_calories)

# Print highest in list
print("Highest:", max(elf_calories))

# --- Part Two ---

# I have to sum the calorie count of the top three elves

# Sort list highest -> lowest
elf_calories.sort(reverse=True)
print(elf_calories)

# Sum top three
print("Sum top three:", elf_calories[0] + elf_calories[1] + elf_calories[2])