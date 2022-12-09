# --- Day 9: Rope Bridge ---

# I have to simulate the movement of a robe and count the number of positions the rope's tail visits

# Open and read file
f = open("9_input.txt", "r")
lines = f.readlines()
f.close()


class Knot:
    row = 0
    col = 0


def simulate_rope(num_knots):
    # Create rope
    rope = []
    for _ in range(num_knots):
        rope.append(Knot())

    visited_coordinates = []

    for line in lines:
        direction, steps = line.split()

        for step in range(int(steps)):
            # Move head
            match direction:
                case "U":
                    rope[0].row += 1
                case "D":
                    rope[0].row -= 1
                case "L":
                    rope[0].col -= 1
                case "R":
                    rope[0].col += 1

            # Store tail location
            visited_coordinates.append((rope[-1].row, rope[-1].col))

            # Move remainder of rope
            # Not elegant but it works :)
            for i in range(len(rope) - 1):
                # Move knot to follow the knot in front of it
                if (rope[i].row - rope[i + 1].row) > 1:
                    # Head is above tail
                    rope[i + 1].row += 1
                    if rope[i].col > rope[i + 1].col:
                        rope[i + 1].col += 1
                    elif rope[i].col < rope[i + 1].col:
                        rope[i + 1].col -= 1
                elif (rope[i + 1].row - rope[i].row) > 1:
                    # Head is below tail
                    rope[i + 1].row -= 1
                    if rope[i].col > rope[i + 1].col:
                        rope[i + 1].col += 1
                    elif rope[i].col < rope[i + 1].col:
                        rope[i + 1].col -= 1
                elif (rope[i].col - rope[i + 1].col) > 1:
                    # Head is right of tail
                    rope[i + 1].col += 1
                    if rope[i].row > rope[i + 1].row:
                        rope[i + 1].row += 1
                    elif rope[i].row < rope[i + 1].row:
                        rope[i + 1].row -= 1
                elif (rope[i + 1].col - rope[i].col) > 1:
                    # Head is left of tail
                    rope[i + 1].col -= 1
                    if rope[i].row > rope[i + 1].row:
                        rope[i + 1].row += 1
                    elif rope[i].row < rope[i + 1].row:
                        rope[i + 1].row -= 1

    return len(set(visited_coordinates))


print("Part one number of visited position:", simulate_rope(2))
print("Part two number of visited position:", simulate_rope(10) + 1)
