# --- Day 2: Rock Paper Scissors ---

# I need to calculate the scores of a series of RPS rounds

# Opponent:
# A: Rock
# B: Paper
# C: Scissors

# Me:
# X: Rock
# Y: Paper
# Z: Scissors

# Points:
# Rock: 1
# Paper: 2
# Scissors: 3
# Lose: 0
# Draw: 3
# Win: 6

# Open file
f = open("2_input.txt", "r")

# Sum the scores of each line (RPS round)
total_score = 0
for line in f:
    # Extract shapes
    opponent_shape = line[0]
    my_shape = line[2]

    # Calculate shape points
    match my_shape:
        case "X":
            total_score += 1
        case "Y":
            total_score += 2
        case "Z":
            total_score += 3

    # Calculate win points
    if (opponent_shape+my_shape) == "AX" or (opponent_shape+my_shape) == "BY" or (opponent_shape+my_shape) == "CZ":
        # Draw
        total_score += 3
    elif (opponent_shape+my_shape) == "AY" or (opponent_shape+my_shape) == "BZ" or (opponent_shape+my_shape) == "CX":
        # Win
        total_score += 6

print("Part 1 total score:", total_score)

# --- Part Two ---

# Strategy:
# X: Lose
# Y: Draw
# Z: Win

# Open file
f = open("2_input.txt", "r")

# Sum the scores of each line (RPS round)
total_score = 0
for line in f:
    # Extract shapes
    opponent_shape = line[0]
    strategy = line[2]

    # Calculate points
    if strategy == "Y":
        # Draw
        total_score += 3

        match opponent_shape:
            case "A":
                # Opponent played Rock
                total_score += 1
            case "B":
                # Opponent played Paper
                total_score += 2
            case "C":
                # Opponent played Scissors
                total_score += 3

    elif strategy == "Z":
        # Win
        total_score += 6

        match opponent_shape:
            case "A":
                # Opponent played Rock
                total_score += 2
            case "B":
                # Opponent played Paper
                total_score += 3
            case "C":
                # Opponent played Scissors
                total_score += 1
    else:
        # Lose
        match opponent_shape:
            case "A":
                # Opponent played Rock
                total_score += 3
            case "B":
                # Opponent played Paper
                total_score += 1
            case "C":
                # Opponent played Scissors
                total_score += 2

print("Part 2 total score:", total_score)
