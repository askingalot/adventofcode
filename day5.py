print(part1('day5.txt'))

def part1(filename):
    with open(filename) as input:
        strand = list(input.readline().strip())
    return len(react(strand))


def should_react(ch1, ch2):
    return ch1 != ch2 and ch1.upper() == ch2.upper()


def react(strand):
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

    if len(indexes_to_delete):
        return react(strand)
    else:
        return strand


