import string

def part1(filename):
    with open(filename) as input:
        strand = list(input.readline().strip())
    return len(react(strand))


def part2(filename):
    with open(filename) as input:
        strand_str = input.readline().strip()
    
    min_strand_length = len(strand_str)
    for upper_unit in string.ascii_uppercase:
        strand = list(strand_str.replace(upper_unit, '')
                                .replace(upper_unit.lower(), ''))
        candidate_length = len(react(strand))
        if candidate_length < min_strand_length:
            min_strand_length = candidate_length

    return min_strand_length

def react(strand):
    while True:
        did_react = False
        i = 0
        while i < len(strand) - 1:
            if should_react(strand[i], strand[i+1]):
                strand[i] = '_'
                strand[i+1] = '_'
                did_react = True
                i += 2
            else:
                i += 1

        if did_react:
            strand = [ unit for unit in strand if unit != '_' ]
        else:
            return strand


def should_react(ch1, ch2):
    return ch1 != ch2 and ch1.upper() == ch2.upper()


print(part1('day5.txt'))
print(part2('day5.txt'))
