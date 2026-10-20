import sys
from bisect import bisect_left, bisect_right


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(data)
    by_u = []
    by_v = []
    for _ in range(count):
        x = next(data)
        y = next(data)
        u = x + y
        v = x - y
        by_u.append((u, v))
        by_v.append((v, u))
    by_u.sort()
    by_v.sort()

    answers = []
    for _ in range(next(data)):
        x = next(data)
        y = next(data)
        distance = next(data)
        u = x + y
        v = x - y
        if distance == 0:
            point = (u, v)
            answer = bisect_right(by_u, point) - bisect_left(by_u, point)
        else:
            left = u - distance
            right = u + distance
            bottom = v - distance
            top = v + distance
            answer = bisect_right(by_u, (left, top)) - bisect_left(by_u, (left, bottom))
            answer += bisect_right(by_u, (right, top)) - bisect_left(by_u, (right, bottom))
            # The vertical sides already include all four corners.
            answer += bisect_left(by_v, (bottom, right)) - bisect_right(by_v, (bottom, left))
            answer += bisect_left(by_v, (top, right)) - bisect_right(by_v, (top, left))
        answers.append(str(answer))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
