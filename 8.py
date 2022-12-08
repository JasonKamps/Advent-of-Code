# --- Day 8: Treetop Tree House ---

# I have to find tall trees that are visible from outside the grid

# Open and read file
f = open("8_input.txt", "r")
lines = f.readlines()
f.close()

# Create a 2D list of tree heights
num_rows = len(lines)
num_cols = len(lines[0].strip())
trees = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
for index, line in enumerate(lines):
    trees[index] = list(line.strip())
print(trees)

# Count hidden trees and calculate tree scores
hidden_trees = 0
highest_score = 0
for row_index, row in enumerate(trees):
    for col_index, height in enumerate(row):
        height = int(height)

        # Check left
        left = False
        left_dist = 0
        for index in reversed(range(0, row_index)):
            left_dist += 1
            if int(trees[index][col_index]) >= height:
                left = True
                break

        # Check right
        right = False
        right_dist = 0
        for index in range(row_index + 1, len(row)):
            right_dist += 1
            if int(trees[index][col_index]) >= height:
                right = True
                break

        # Check above
        above = False
        above_dist = 0
        for index in reversed(range(0, col_index)):
            above_dist += 1
            if int(trees[row_index][index]) >= height:
                above = True
                break

        # Check below
        below = False
        below_dist = 0
        for index in range(col_index + 1, len(row)):
            below_dist += 1
            if int(trees[row_index][index]) >= height:
                below = True
                break

        if left and right and above and below:
            hidden_trees += 1

        score = left_dist * right_dist * above_dist * below_dist
        if score > highest_score:
            highest_score = score

total_trees = num_rows * num_cols
print(total_trees)
print("Visible trees:", total_trees - hidden_trees)
print("Top score:", highest_score)
