# --- Day 10: Cathode-Ray Tube ---

# I have to monitor CPU operations and determine signal strengths

# Open and read file
f = open("10_input.txt", "r")
lines = f.readlines()
f.close()

signal_strength_sum = 0


def check_signal_strength(cycles, x_val):
    points_of_interest = [20, 60, 60, 100, 140, 180, 220]
    global signal_strength_sum
    if cycles in points_of_interest:
        signal_strength_sum += cycles * x_val


x = 1
num_cycles = 0
for line in lines:
    l = line.strip().split()
    num_cycles += 1
    check_signal_strength(num_cycles, x)

    if l[0] == "addx":
        num_cycles += 1  # 'addx' takes an additional cycle
        check_signal_strength(num_cycles, x)
        x += int(l[1])

print("Signal strength sum:", signal_strength_sum)

# --- Part Two ---

# I have to determine and draw a CRT's output

crt = []


# Draws the CRT output visually
def draw_crt(crt_list):
    for index, pixel in enumerate(crt_list):
        if (index + 1) % 40 == 0:
            print()
        else:
            print(pixel, end="")


# Adds a pixel to the CRT list
def check_pixel(crt_list, cycles, x_val):
    if abs(((cycles - 1) % 40) - x_val) <= 1:
        crt_list.append("#")
    else:
        crt_list.append(".")


num_cycles = 0
x = 1
for line in lines:
    l = line.strip().split()
    num_cycles += 1
    check_pixel(crt, num_cycles, x)

    if l[0] == "addx":
        num_cycles += 1  # 'addx' takes an additional cycle
        check_pixel(crt, num_cycles, x)
        x += int(l[1])

draw_crt(crt)
