# Wow, this code is...less than good.
#  MUCH less than good...


import re
from collections import namedtuple

Claim = namedtuple('Claim', ['id', 'left', 'top', 'right', 'bottom'])

def part1_and_2(filename):
    with open(filename) as input:
        claim_lines = input.readlines()

    claims = []
    for claim_line in claim_lines:
        match = re.match(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim_line)
        id, left, top, width, height = (
            int(match[1]), int(match[2]), int(match[3]), int(match[4]), int(match[5]))
        claim = Claim(id, left, top, right=left+width, bottom=top+height)
        claims.append(claim)

    overlap_ids = []
    overlap_coords = []
    for i in range(len(claims) - 1):
        claim1 = claims[i]
        for j in range(i+1, len(claims)):
            claim2 = claims[j]
            coords = find_overlap_coords(claim1, claim2)

            if len(coords):
                overlap_coords.extend(coords)
                overlap_ids.append(claim1.id)
                overlap_ids.append(claim2.id)


    all_ids = [ claim.id for claim in claims ]
    return len(set(overlap_coords)), set(all_ids).difference(overlap_ids)


def find_overlap_coords(claim1, claim2):
    left_claim, right_claim = (claim1, claim2) if claim1.left < claim2.left else (claim2, claim1)
    top_claim, bottom_claim = (claim1, claim2) if claim1.top < claim2.top else (claim2, claim1)

    left_x, right_x = (-1, -1)
    top_y, bottom_y = (-1, -1)
    if left_claim.right > right_claim.left:
        if left_claim.right < right_claim.right:
            left_x, right_x = right_claim.left, left_claim.right
        else:
            left_x, right_x = right_claim.left, right_claim.right
    if top_claim.bottom > bottom_claim.top:
        if top_claim.bottom < bottom_claim.bottom:
            top_y, bottom_y = bottom_claim.top, top_claim.bottom
        else:
            top_y, bottom_y = bottom_claim.top, bottom_claim.bottom

    if -1 in [left_x, right_x, top_y, bottom_y]:
        return []

    return [ (x, y) 
            for x in range(left_x, right_x) 
            for y in range(top_y, bottom_y) ]


print(part1_and_2('day3.txt'))