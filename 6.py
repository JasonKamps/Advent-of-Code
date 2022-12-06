# --- Day 6: Tuning Trouble ---

# I have to find the first string of unique characters

# Finds the first string of unique characters with a given length
# Returns the number of characters processed
def find_message(length):
    f = open("6_input.txt", "r")

    window = list(f.read(length))
    count = length
    while True:
        if len(set(window)) == len(window):
            return count

        window.pop(0)
        window.append(f.read(1))
        count += 1


print("Part 1 count:", find_message(4))
print("Part 2 count:", find_message(14))
