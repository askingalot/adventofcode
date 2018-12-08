import re
from collections import namedtuple
from itertools import chain

SleepWakeRec = namedtuple('SleepWakeRec', ['date', 'hour', 'minute', 'action'])
GuardRec = namedtuple('GuardRec', ['date','hour', 'minute', 'id'])

def main(filename):
    with open(filename) as input:
        lines = input.readlines()

    records = parse(lines)
    sorted_records = sorted(records, key=lambda r: (r.date, r.hour, r.minute))
    guard_shifts = make_guard_shifts(sorted_records)

    return (part1(guard_shifts), part2(guard_shifts))


def part2(guard_shifts):
    sleepiest_guard_id = 0
    sleepiest_minute = 0
    minute_count = 0

    for guard_id in guard_shifts.keys():
        candidate_count_per_minute = [0] * 60
        shifts = guard_shifts[guard_id].values()
        for shift in shifts:
            for minute, is_asleep in enumerate(shift):
                if is_asleep:
                    candidate_count_per_minute[minute] += 1

        candidate_count = max(candidate_count_per_minute)
        if candidate_count > minute_count:
            minute_count = candidate_count
            sleepiest_minute = candidate_count_per_minute.index(candidate_count)
            sleepiest_guard_id = guard_id

    return sleepiest_minute * int(sleepiest_guard_id)


def part1(guard_shifts):
    sleepiest_guard_id = max(guard_shifts.keys(), 
                             key=lambda k: total_sleep_minutes(guard_shifts[k]))
    sleepiest_guard = guard_shifts[sleepiest_guard_id]
    shifts = sleepiest_guard.values()

    sleepiest_minute = 0
    max_sleep_count = 0
    for minute in range(0, 60):
        count = sum(1 for shift in shifts if shift[minute])
        if count > max_sleep_count:
            max_sleep_count = count
            sleepiest_minute = minute
            
    return sleepiest_minute * int(sleepiest_guard_id)

    
def total_sleep_minutes(guard):
    all_sleep_wake = chain.from_iterable(guard.values())
    return sum(1 for is_asleep in all_sleep_wake if is_asleep)


def make_guard_shifts(sorted_records):
    guard_shifts = {}
    i = 0
    while i < len(sorted_records):
        guard_rec = sorted_records[i]
        if guard_rec.id not in guard_shifts:
            guard_shifts[guard_rec.id] = {}

        i += 1
        sleep_wake_rec = sorted_records[i]
        while type(sleep_wake_rec) == SleepWakeRec:
            shift_dict = guard_shifts[guard_rec.id]
            if sleep_wake_rec.date not in shift_dict:
                is_asleep_per_minute = [False] * 60
                shift_dict[sleep_wake_rec.date] = is_asleep_per_minute
            
            is_asleep_per_minute = shift_dict[sleep_wake_rec.date]
            minute = int(sleep_wake_rec.minute)
            is_asleep = sleep_wake_rec.action == 'falls asleep'
            is_asleep_per_minute = is_asleep_per_minute[:minute] + ([is_asleep] * (60 - minute))
            shift_dict[sleep_wake_rec.date] = is_asleep_per_minute

            i += 1
            if i < len(sorted_records):
                sleep_wake_rec = sorted_records[i]
            else:
                sleep_wake_rec = None

    return guard_shifts


def parse(lines):
    records = []
    for line in lines:
        guard_match = re.match(r'^\[(\S+) (\d\d):(\d\d)\] Guard #(\d+).*', line)
        if guard_match:
            records.append(GuardRec(date = guard_match[1], 
                                    hour = guard_match[2],
                                    minute = guard_match[3],
                                    id = guard_match[4]))
        else:
            sleep_wake_match = re.match(r'^\[(\S+) 00:(\d\d)\] (.*)', line)
            records.append(SleepWakeRec(date = sleep_wake_match[1], 
                                        hour = '00',
                                        minute = sleep_wake_match[2], 
                                        action = sleep_wake_match[3]))

    return records
 

print(main('day4.txt'))