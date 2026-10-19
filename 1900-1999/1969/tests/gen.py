"""Print seed mode; seed is the first departure in seconds.
Modes: many_large_offset, many_small_offset, single_long_run,
mixed_100, mixed_500, mixed_1250, minimal. Generated schedules are physical.
"""
import sys


DAY_SECONDS = 86400
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
TRAM_LIMIT = 2500


def build(first, mode):
    if mode == 'many_large_offset':
        duration, offset, trips, relative = 20000, 10000, 1, list(range(TRAM_LIMIT))
    elif mode == 'many_small_offset':
        duration, offset, trips, relative = 20000, 1, 1, list(range(TRAM_LIMIT))
    elif mode == 'single_long_run':
        duration, offset, trips, relative = 2, 1, TRAM_LIMIT, [0]
    elif mode == 'mixed_100':
        duration, offset, trips, relative = 200, 1, 25, [3 * i for i in range(100)]
    elif mode == 'mixed_500':
        duration, offset, trips, relative = 1000, 1, 5, [3 * i for i in range(500)]
    elif mode == 'mixed_1250':
        duration, offset, trips, relative = 4000, 1, 2, [3 * i for i in range(1250)]
    elif mode == 'minimal':
        duration, offset, trips, relative = 2, 1, 1, [0]
    else:
        raise ValueError('Unknown physical schedule mode')
    departures = [first + value for value in relative]
    if first < 0 or departures[-1] + 2 * trips * duration >= DAY_SECONDS:
        raise ValueError('Schedule leaves the day')
    passages = []
    for departure in departures:
        for leg in range(2 * trips):
            distance = offset if leg % 2 == 0 else duration - offset
            passages.append(departure + leg * duration + distance)
    if len(set(passages)) != len(passages):
        raise ValueError('Simultaneous observed passages')
    return sorted(passages), duration, trips, departures


def format_time(value):
    total_minutes, seconds = divmod(value, SECONDS_PER_MINUTE)
    hours, minutes = divmod(total_minutes, MINUTES_PER_HOUR)
    return f'{hours:02}:{minutes:02}:{seconds:02}'


def main():
    first = int(sys.argv[1])
    passages, _, _, _ = build(first, sys.argv[2])
    print(format_time(first))
    print('\n'.join(map(format_time, passages)))


if __name__ == '__main__':
    main()
