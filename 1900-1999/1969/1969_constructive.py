import sys


SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR


def recover(first, passages):
    count = len(passages)
    offset = passages[0] - first
    total_span = passages[-1] - first + offset
    present = set(passages)
    marked = [0] * (passages[-1] + 1)
    epoch = 0
    for first_return in passages[1 : count // 2 + 1]:
        period = first_return - first + offset
        if period % 2 or period <= 2 * offset:
            continue
        trips = total_span // period
        if trips == 0 or count % (2 * trips):
            continue
        tram_count = count // (2 * trips)
        gap = period - 2 * offset
        epoch += 1
        departures = []
        failed = False
        for time in passages:
            if marked[time] == epoch:
                continue
            departure = time - offset
            if departure >= first + period or len(departures) == tram_count:
                failed = True
                break
            outward = time
            for _ in range(trips):
                returning = outward + gap
                if (outward not in present or returning not in present
                        or marked[outward] == epoch or marked[returning] == epoch):
                    failed = True
                    break
                marked[outward] = marked[returning] = epoch
                outward += period
            if failed:
                break
            departures.append(departure)
        if not failed and len(departures) == tram_count:
            return period // 2, trips, departures
    raise ValueError('The guaranteed schedule was not found')


def parse_time(text):
    hours, minutes, seconds = map(int, text.split(b':'))
    return hours * SECONDS_PER_HOUR + minutes * SECONDS_PER_MINUTE + seconds


def format_time(value):
    hours, remainder = divmod(value, SECONDS_PER_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_PER_MINUTE)
    return f'{hours:02}:{minutes:02}:{seconds:02}'


def main():
    times = [parse_time(word) for word in sys.stdin.buffer.read().split()]
    duration, trips, departures = recover(times[0], times[1:])
    for departure in departures:
        print(' '.join(format_time(departure + step * duration) for step in range(2 * trips + 1)))


if __name__ == '__main__':
    main()
