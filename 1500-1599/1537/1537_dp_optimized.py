from array import array


def main():
    k, modulus = map(int, input().split())
    top = k // 2
    if top == 0 or modulus == 1:
        print(0)
        return
    if top == 1:
        print(1)
        return
    half = top // 2
    quarter = half // 2
    saved = array("I", [0]) * (quarter + 1)
    current = 1
    if quarter:
        saved[1] = current
    for m in range(2, quarter + 1):
        current += saved[m >> 1]
        if current >= modulus:
            current -= modulus
        saved[m] = current
    total = current if quarter == 0 else 0
    for m in range(max(2, quarter + 1), half + 1):
        current += saved[m >> 1]
        if current >= modulus:
            current -= modulus
        total += current
    # Increments in the unevaluated half use each g(j) twice, except endpoints.
    answer = 2 * total
    if half % 2 == 0:
        answer += saved[quarter]
    if top % 2:
        answer += current
    print(answer % modulus)


main()
