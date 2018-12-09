def part1(filename):
    with open(filename) as input:
        strand = list(input.readline().strip())
    return len(react(strand))


def part2(filename):
    with open(filename) as input:
        strand_str = input.readline().strip()
    
    print(len(set(strand_str.upper())))

    candidate_units = (
        ( chr(unit[0]), chr(unit[1]) )
        for unit in zip(range(ord('A'), ord('Z')+1), 
                        range(ord('a'), ord('z')+1)))

    min_strand_length = len(strand_str)
    for upper, lower in candidate_units:
        strand = list(strand_str.replace(upper, '').replace(lower, ''))
        candidate_length = len(react(strand))
        if candidate_length < min_strand_length:
            min_strand_length = candidate_length

    return min_strand_length

def react(strand):
    while True:
        indexes_to_delete = []
        i = 0
        while i < len(strand) - 1:
            if should_react(strand[i], strand[i+1]):
                indexes_to_delete.append(i)
                indexes_to_delete.append(i+1)
                i += 2
            else:
                i += 1

        for i in reversed(indexes_to_delete):
            del strand[i]

        if not len(indexes_to_delete):
            return strand


def should_react(ch1, ch2):
    return ch1 != ch2 and ch1.upper() == ch2.upper()


print(part1('day5.txt'))
print(part2('day5.txt'))
