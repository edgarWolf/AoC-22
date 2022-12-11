from typing import List
from math import prod
import copy
inp_file = "11.txt"


def parse_items(items_line):
    items = items_line.split(":")[1].split(",")
    return list(map(int, items))

def parse_operation(operation_line):
    operation_string = operation_line.split("=")[1]
    operator = operation_string[5]
    op_number = operation_string[6:].strip()
    if op_number.isdigit():
        op_number = int(op_number)
    return (operator, op_number)

def parse_test_divisor(test_divisor_line):
    return int(test_divisor_line[-2:])


def parse_throw(throw_lines):
    true_line, false_line = [line.strip() for line in throw_lines]
    true_monkey = int(true_line[-1])
    false_monkey = int(false_line[-1])
    return {True : true_monkey, False : false_monkey}

# Monkey structure:
class Monkey:
    def __init__(self, items, operation, test_divisor, throw):
        self.items = items
        self.operation = operation
        self.test_divisor = test_divisor
        self.throw = throw
        pass


    @classmethod
    def from_description(cls, description):
        lines = description.splitlines()
        starting_items_line = lines[1]
        operation_line = lines[2]
        test_divisor_line = lines[3]
        throw_lines = lines[4:5 + 1]
        items = parse_items(starting_items_line)
        operation = parse_operation(operation_line)
        test_divisor = parse_test_divisor(test_divisor_line)
        throw = parse_throw(throw_lines)
        return cls(items, operation, test_divisor, throw)


with open(inp_file) as f:
    line_blocks = f.read().split("\n\n")


def map_input(line_blocks: List[str]):
    monkeys = []
    for line_block in line_blocks:
        monkey = Monkey.from_description(line_block)
        monkeys.append(monkey)
    return monkeys

monkeys = map_input(line_blocks)

def part1(monkeys: List[Monkey], verbose=False, rounds=20, divide_by_3=True):
    monkeys_copy = copy.deepcopy(monkeys)
    inspections = [0 for _ in monkeys]
    if not divide_by_3:
        cap = prod(m.test_divisor for m in monkeys_copy)
    for _ in range(rounds):
        for idx, monkey in enumerate(monkeys_copy):
            if verbose:
                print("Monkey ", idx, " :")
            items = monkey.items[:]
            for item in items:
                inspections[idx] += 1
                if verbose:
                    print(f"Monkey inspects an item with a worry level of {item}.")
                operator, number = monkey.operation
                new_worry_level = None
                number = item if number == "old" else number
                if operator == "+":
                    new_worry_level = item +  number
                    if verbose:
                        print(f"Worry level increases by {number} to {new_worry_level}.")
                else:
                    new_worry_level = item * number
                    if verbose:
                        print(f"Worry level is multiplied by {number} to {new_worry_level}.")
                if divide_by_3:
                    new_worry_level //= 3
                    if verbose:
                        print(f"Monkey gets bored with item. Worry level is divided by 3 to {new_worry_level}.")
                # Part 2
                else:
                    new_worry_level %= cap
                which_monkey = new_worry_level % monkey.test_divisor == 0

                if new_worry_level % monkey.test_divisor == 0:
                    if verbose:
                        print(f"Current worry level is divisible by {monkey.test_divisor}.")
                else:
                    if verbose:
                        print(f"Current worry level is not divisible by {monkey.test_divisor}.")
                to = monkey.throw[which_monkey]
                if verbose:
                    print(f"Item with worry level {new_worry_level} is thrown to monkey {to}.")
                monkey.items.remove(item)
                monkeys_copy[to].items.insert(0, new_worry_level)
    max_two_obs = list(sorted(inspections))[-2:]
    return max_two_obs[0] * max_two_obs[1]

print("Part 1: ", part1(monkeys))
print("Part 2: ", part1(monkeys, rounds=10000, divide_by_3=False))