import sys

TEAM_SIZE = 3


def ways_to_choose(available, count):
    if count < 0 or count > available:
        return 0
    if count == 0:
        return 1
    if count == 1:
        return available
    return available * (available - 1) // 2


def count_teams(total, special_count, first_special):
    special = special_count - first_special
    ordinary = total - special_count - (1 - first_special)
    remaining_teams = total // TEAM_SIZE - 1
    answer = 0
    for chosen_special in range(TEAM_SIZE):
        removed_special = first_special + chosen_special
        if removed_special == 0 or special_count - removed_special < remaining_teams:
            continue
        answer += ways_to_choose(special, chosen_special) * ways_to_choose(
            ordinary, TEAM_SIZE - 1 - chosen_special
        )
    return answer


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    total, special_count = values[:2]
    print(count_teams(total, special_count, int(1 in values[2:])))


if __name__ == "__main__":
    main()
