import sys


def extended_gcd(a, b):
    x, next_x = 1, 0
    while b:
        quotient = a // b
        a, b = b, a % b
        x, next_x = next_x, x - quotient * next_x
    return a, x


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    limit, size = data[:2]
    progressions = list(zip(data[2::2], data[2 + 1 :: 2]))

    def count_union(begin, first, step, sign):
        answer = 0
        for i in range(begin, size):
            other_first, other_step = progressions[i]
            merged_first, merged_step = first, step
            if step == 0:
                if first < other_first or (first - other_first) % other_step:
                    continue
            else:
                divisor, inverse = extended_gcd(step, other_step)
                difference = other_first - first
                if difference % divisor:
                    continue
                modulus = other_step // divisor
                offset = (difference // divisor * inverse) % modulus
                merged_step = step * modulus
                merged_first = first + step * offset
                if merged_first < other_first:
                    gap = other_first - merged_first
                    merged_first += ((gap - 1) // merged_step + 1) * merged_step
                if merged_first > limit:
                    continue
                # A zero step stores an intersection with just one in-range value.
                if merged_step > limit - merged_first:
                    merged_step = 0
            count = 1 if merged_step == 0 else (limit - merged_first) // merged_step + 1
            answer += sign * count
            answer += count_union(i + 1, merged_first, merged_step, -sign)
        return answer

    print(count_union(0, 1, 1, 1))


if __name__ == "__main__":
    main()
