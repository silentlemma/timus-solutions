from sys import stdin, stdout

MIN_DIVISOR = 3
FIRST_EVEN_DIVISOR = 4
LAST_SMALL_PRIME = 5
FIRST_WHEEL_DIVISOR = 7
WHEEL_GAPS = (4, 2, 4, 2, 4, 6, 2, 6)

buttons = int(stdin.readline())
if buttons % MIN_DIVISOR == 0:
    answer = MIN_DIVISOR - 1
elif buttons % FIRST_EVEN_DIVISOR == 0:
    answer = FIRST_EVEN_DIVISOR - 1
elif buttons % LAST_SMALL_PRIME == 0:
    answer = LAST_SMALL_PRIME - 1
else:
    # The smallest remaining legal divisor is coprime to30.
    divisor = FIRST_WHEEL_DIVISOR
    gap = 0
    answer = (buttons // 2 if buttons % 2 == 0 else buttons) - 1
    # Four wheel checks per backedge avoid a hot tiny loop and its JIT cache.
    while divisor * divisor <= buttons:
        if divisor * divisor > buttons:
            break
        if buttons % divisor == 0:
            answer = divisor - 1
            break
        divisor += WHEEL_GAPS[gap]
        gap = (gap + 1) % len(WHEEL_GAPS)
        if divisor * divisor > buttons:
            break
        if buttons % divisor == 0:
            answer = divisor - 1
            break
        divisor += WHEEL_GAPS[gap]
        gap = (gap + 1) % len(WHEEL_GAPS)
        if divisor * divisor > buttons:
            break
        if buttons % divisor == 0:
            answer = divisor - 1
            break
        divisor += WHEEL_GAPS[gap]
        gap = (gap + 1) % len(WHEEL_GAPS)
        if divisor * divisor > buttons:
            break
        if buttons % divisor == 0:
            answer = divisor - 1
            break
        divisor += WHEEL_GAPS[gap]
        gap = (gap + 1) % len(WHEEL_GAPS)
stdout.write(str(answer))
