from collections import Counter

def part1(filename):
    with open(filename) as input:
        ids = input.readlines()
    
    two_total = 0
    three_total = 0
    for id in ids:
        char_counts =  Counter(id)
        count_counts = char_counts.values()
        two_total += 1 if 2 in count_counts else 0
        three_total += 1 if 3 in count_counts else 0

    return two_total * three_total


def part2(filename):
    with open(filename) as input:
        ids = [ id.strip() for id in input.readlines() ]

    for i in range(len(ids) - 1):
        first_id = ids[i]
        for j in range(i+1, len(ids)):
            second_id = ids[j]
            common_chars = [ first_id[k] 
                             for k in range(len(first_id)) 
                             if first_id[k] == second_id[k] ]
            
            if len(first_id) - len(common_chars) == 1:
                return ''.join(common_chars)


print(part1('day2.txt'))
print(part2('day2.txt'))