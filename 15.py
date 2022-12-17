from typing import List, Tuple
import re

inp_file = "15.txt"

with open(inp_file) as f:
    lines = f.read().splitlines()

def manhatten_distance(pos1: Tuple[int, int], pos2: Tuple[int, int]):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)


class Sensor:
    def __init__(self, pos: Tuple[int, int], beacon: Tuple[int, int]):
        self.pos = pos
        self.beacon = beacon
        self.manhatten_to_beacon = self.beacon_distance()
    
    def beacon_distance(self):
        return manhatten_distance(self.pos, self.beacon)

def map_input(lines: List[str]):
    ret = []
    min_x = 99999999
    max_x = -99999999

    for line in lines:
        matches = re.search(r"Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)", line)
        sensor_pos = (int(matches.group(1)), int(matches.group(2)))
        beacon_pos = (int(matches.group(3)), int(matches.group(4)))
        
        sensor = Sensor(sensor_pos, beacon_pos)
        min_x_candidate_raw = min(sensor.pos[0], beacon_pos[0])
        max_x_candidate_raw = max(sensor.pos[0], beacon_pos[0])

        min_x_candidate = min_x_candidate_raw - sensor.manhatten_to_beacon
        max_x_candidate = max_x_candidate_raw + sensor.manhatten_to_beacon

        min_x = min(min_x, min_x_candidate)
        max_x = max(max_x, max_x_candidate)

        # Append sensor
        ret.append(sensor)

    return ret, min_x, max_x

def get_manhatten_pairs(distance: int):
    ret = []
    for d in range(distance + 1):
        remainder = distance - d
        ret.append((d, remainder))
        if d != 0:
            ret.append((-d, remainder))
        if remainder != 0:
            ret.append((d, -remainder))

    return ret

def part1(sensors: List[Sensor], min_x: int, max_x: int, target: int = 10):
    counter = 0
    for x in range(min_x - 1, max_x + 1):
        pos_in_row = (x, target)
        for sensor in sensors:
            if sensor.beacon == pos_in_row:
                continue
            row_distance = manhatten_distance(sensor.pos, pos_in_row)
            if row_distance <= sensor.manhatten_to_beacon:
                counter += 1
                break
    return counter




def part1_fast(sensors: List[Sensor], target: int = 10):
    beacons = set()
    poses = set()
    for sensor in sensors:
        sx, sy = sensor.pos
        bx, by = sensor.beacon
        if by == target:
            beacons.add(bx)
        curr_distance = sensor.manhatten_to_beacon
        if (r := curr_distance - abs(target - sy)) >= 0:
            poses.update([x for x in range(sx - r, sx + r + 1)])
    poses.difference_update(beacons)
    return len(poses)


def part2(sensors: List[Sensor], max_value: int):
    # Very time and memomry consuming...
    points = set()
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3
    found = False

    for sensor in sensors:
        sx, sy = sensor.pos
        curr_distance = sensor.manhatten_to_beacon
        for direction in range(4):
            for offset in range(curr_distance):
                if direction == RIGHT:
                    # Triangle top right
                    cx = sx + curr_distance + 1 - offset
                    cy = sy + offset
                elif direction == UP:
                    # Triange top left
                    cx = sx - offset
                    cy = sy + curr_distance + 1 - offset
                elif direction == LEFT:
                    # Triangle bottom left
                    cx = sx - curr_distance - 1 + offset
                    cy = sy - offset
                elif direction == DOWN:
                    # Triangle bottom right
                    cx = sx + offset
                    cy = sy - curr_distance - 1 + offset
                
                point_in_range = 0 <= cx <= max_value and 0 <= cy <= max_value
                if point_in_range and (cx, cy) not in points:
                    # Check if point is in all sensor beacon distances.
                    found = all((abs(cx - sensor.pos[0]) + abs(cy - sensor.pos[1])) > sensor.manhatten_to_beacon for sensor in sensors)
                
                if found:
                    return 4000000 * cx + cy
                else:
                    points.add((cx, cy))

sensors, min_x, max_x = map_input(lines)
print("Part 1: ", part1_fast(sensors, target=2000000))
print("Part 2: ", part2(sensors, max_value=4000000))