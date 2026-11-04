FIRST = 2


def quiet(count):
    step = FIRST
    while count >= step:
        quotient, remainder = divmod(count, step)
        # q stays fixed while c-q*j >= q*(k+j); the upper bound only loosens.
        jumps = remainder // (2 * quotient) + 1
        count -= quotient * jumps
        step += jumps
    return count


left, right = map(int, input().split())
print(quiet(right) - quiet(left - 1))
