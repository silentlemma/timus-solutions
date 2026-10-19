import sys

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * SECONDS_PER_MINUTE
MAX_INTERVAL = 500
INTERVAL_COUNT = 4


def parse_time(text):
    hour, minute, second = map(int, text.split(b":"))
    return hour * SECONDS_PER_HOUR + minute * SECONDS_PER_MINUTE + second


def format_time(seconds):
    hour, remainder = divmod(seconds, SECONDS_PER_HOUR)
    minute, second = divmod(remainder, SECONDS_PER_MINUTE)
    return f"{hour:02d}:{minute:02d}:{second:02d}\n"


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    take_take, take_land, land_take, land_land = (
        int(next(tokens)) for _ in range(INTERVAL_COUNT)
    )
    departures = [parse_time(next(tokens)) for _ in range(int(next(tokens)))]
    landings = [parse_time(next(tokens)) for _ in range(int(next(tokens)))]
    take_index = land_index = 0
    last_take = last_land = -MAX_INTERVAL
    take_result, land_result = [], []
    while take_index < len(departures) or land_index < len(landings):
        ready = 0
        if take_index < len(departures):
            ready = max(
                departures[take_index], last_take + take_take, last_land + land_take
            )
        if land_index < len(landings) and (
            take_index == len(departures) or landings[land_index] <= ready
        ):
            last_land = max(
                landings[land_index], last_take + take_land, last_land + land_land
            )
            land_result.append(last_land)
            land_index += 1
        else:
            last_take = ready
            take_result.append(last_take)
            take_index += 1
    sys.stdout.write("".join(map(format_time, take_result + land_result)))


main()
