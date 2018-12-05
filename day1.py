from itertools import cycle

def part1(filename):
    with open(filename) as input:
        freq_changes = input.readlines()

    return sum(int(change) for change in freq_changes)


def part2(filename):
    with open(filename) as input:
        freq_changes = input.readlines()

    current_freq = 0
    seen_freqs = set([current_freq])
    for change in cycle(freq_changes):
        current_freq += int(change)

        if current_freq in seen_freqs:
            return current_freq

        seen_freqs.add(current_freq)


print(part1('day1.txt'))

print(part2('day1.txt'))