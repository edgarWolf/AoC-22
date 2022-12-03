with open("2.txt") as f:
    lines = f.read().splitlines()

def map_input(lines):
    pairs = []
    for line in lines:
        parts = line.split(" ")
        pairs.append((parts[0], parts[1]))
    return pairs

matches = map_input(lines)

# X = Stein
# Y = Papier
# Z = Schere

# A = Stein
# B = Papier
# C = Schere

def round_score(opponent, me):
    if opponent == "A" and me == "X":
        return 3
    if opponent == "B" and me == "Y":
        return 3
    if opponent == "C" and me == "Z":
        return 3
    if opponent == "A" and me == "Y":
        return 6
    if opponent == "B" and me == "Z":
        return 6
    if opponent == "C" and me == "X":
        return 6
    return 0

def part_1(matches):
    shape_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    counter = 0
    for op, me in matches:
        counter += shape_scores[me]
        counter += round_score(op, me)
    return counter


def round_score_part_2(opponent, me):
    if me == "X":
        losing_symbol = ""
        if opponent == "A":
            losing_symbol  = "Z"
        if opponent == "B":
            losing_symbol  = "X"
        if opponent == "C":
            losing_symbol  = "Y"
        return (0, losing_symbol)

    if me == "Y":
        draw_symbol = ""
        if opponent == "A":
            draw_symbol  = "X"
        if opponent == "B":
            draw_symbol  = "Y"
        if opponent == "C":
            draw_symbol  = "Z"
        return (3, draw_symbol)

    if me == "Z":
        winning_symbol = ""
        if opponent == "A":
            winning_symbol  = "Y"
        if opponent == "B":
            winning_symbol  = "Z"
        if opponent == "C":
            winning_symbol  = "X"
        return (6, winning_symbol)
        

def part_2(matches):
    shape_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    counter = 0
    for op, me  in matches:
        round_score, symb = round_score_part_2(op, me)
        counter += shape_scores[symb]
        counter += round_score
    return counter



print(f"Part 1: {part_1(matches)}")
print(f"Part 2: {part_2(matches)}")