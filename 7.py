# --- Day 7: No Space Left On Device ---

# I have to determine the size of directories in a filesystem

# Open file
f = open("7_input.txt", "r")

directories_stack = []
current_directory = ""
files_counted = []
directories = {}  # {name : size}
total_size = 0

# Navigate filesystem and keep track of directory sizes
for line in f:
    l = line.split()
    print()
    print(line[:-1])

    # Check for "cd X"
    if l[0] == "$" and l[1] == "cd" and l[2] != "..":
        # Move down into directory
        current_directory = l[2] + ''.join(directories_stack)  # Concatenate with directories_stack to make directory name unique
        directories_stack.append(current_directory)  # Push to stack
        print("Move into", current_directory)

    # Check for "cd .."
    if l[0] == "$" and l[1] == "cd" and l[2] == "..":
        # Move up to parent directory
        current_directory = directories_stack.pop()  # Pop from stack to get parent directory
        print("Move up to", current_directory)

    # Check for file
    if l[0].isnumeric():
        # Process file size
        filename = l[1] + current_directory  # Concatenate with current_directory to make filename unique
        if filename not in files_counted:
            file_size = int(l[0])
            # Add file size to every directory in stack
            for d in directories_stack:
                if d not in directories.keys():
                    directories[d] = file_size
                else:
                    directories[d] = directories[d] + file_size
                print("Adding", file_size, "to", d)

            total_size += file_size
            files_counted.append(filename)  # Store filename to avoid recounting it


# Sum all file with size <= 100000
count = 0
for size in directories.values():
    if size <= 100000:
        count += size
print("\nPart 1 sum:", count)


# --- Part Two ---

# I need to find the smallest file that would free up 30000000 of space

print("\nUsed space:", total_size)
free_space = 70000000 - total_size
print("Free space", free_space)

# Find files that would free up 30000000
candidates = []
for size in directories.values():
    if size >= 30000000 - free_space:
        candidates.append(size)
candidates.sort()
print("Part 2 size:", candidates[0])
