"""Count adjacent nonempty palindromic occurrences with exact endpoint counts."""

from array import array
import sys

TRIPLE_DIVISOR = 6
ODD_LENGTH_DIVISOR = 3


def solve(word):
    n = len(word)
    if n < 2:
        return 0
    # A constant word permits every choice of three ordered boundaries.
    if word.count(word[:1]) == n:
        return (n + 1) * n * (n - 1) // TRIPLE_DIVISOR
    # With alternating letters, exactly the odd-length substrings qualify.
    if word[0] != word[1] and word[:-2] == word[2:]:
        half = n // 2
        if n % 2:
            return half * (half + 1) * (half + 2) // ODD_LENGTH_DIVISOR
        return half * (half + 1) * (2 * half + 1) // TRIPLE_DIVISOR

    radii = array("i", [0]) * n
    ending = array("i", [0]) * (n + 1)
    starting = array("i", [0]) * (n + 1)
    left, right = 0, -1
    for center in range(n):
        radius = 1 if center > right else min(radii[left + right - center], right - center + 1)
        while (
            center - radius >= 0
            and center + radius < n
            and word[center - radius] == word[center + radius]
        ):
            radius += 1
        radii[center] = radius
        if center + radius - 1 > right:
            left, right = center - radius + 1, center + radius - 1
        ending[center] += 1
        ending[center + radius] -= 1
        starting[center - radius + 1] += 1
        starting[center + 1] -= 1
    left, right = 0, -1
    for center in range(n):
        radius = 0 if center > right else min(radii[left + right - center + 1], right - center + 1)
        while (
            center - radius - 1 >= 0
            and center + radius < n
            and word[center - radius - 1] == word[center + radius]
        ):
            radius += 1
        radii[center] = radius
        if center + radius - 1 > right:
            left, right = center - radius, center + radius - 1
        if radius:
            ending[center] += 1
            ending[center + radius] -= 1
            starting[center - radius] += 1
            starting[center] -= 1
    count_ending, count_starting = 0, starting[0]
    answer = 0
    for cut in range(n - 1):
        count_ending += ending[cut]
        count_starting += starting[cut + 1]
        answer += count_ending * count_starting
    return answer


def main():
    print(solve(sys.stdin.buffer.readline().strip()))


if __name__ == "__main__":
    main()
