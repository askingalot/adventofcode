from pprint import pprint
from itertools import chain
from collections import namedtuple

Location = namedtuple('Location', ['pos', 'nearby_locations'])
NearbyLocation = namedtuple('NearbyLocation', ['pos', 'parent_location'])


def part1(filename):
    with open(filename) as input:
        coords = [ tuple(map(int, point.strip().split(', ')))
                   for point in input.readlines() ]

    location_by_pos = { pos: Location(pos, nearby_locations=[]) for pos in coords }
    biggest_x = max(point[0] for point in coords)
    biggest_y = max(point[1] for point in coords)
    grid_size = max([biggest_x, biggest_y]) + 1

    grid = [ [ val_at_pos((x, y), location_by_pos) for x in range(grid_size) ]
             for y in range(grid_size) ]

    for pos, location in location_by_pos.items():
        for x, y in get_surrounding_positions(pos, grid_size):
            if not grid[x][y]:
                nearby = NearbyLocation((x, y), location)
                location.nearby_locations.append(nearby)
                grid[x][y] = nearby

    print(grid)


def get_surrounding_positions(pos, size):
    max_pos = size - 1
    adjustments = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    return [ adj_pos 
                for adj_pos in ( 
                    (pos[0] + adj[0], pos[1] + adj[1]) for adj in adjustments 
                )
                if 0 <= adj_pos[0] <= max_pos and 0 <= adj_pos[1] <= max_pos ]


def val_at_pos(pos, location_by_pos):
    if pos in location_by_pos:
        return location_by_pos[pos]
    else:
        return None

part1('day6.txt')