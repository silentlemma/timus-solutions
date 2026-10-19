"""Count adjacent nonempty palindromic occurrences with exact endpoint counts."""

from array import array
import sys


def palindrome_counts(word):
    n = len(word)
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
    count_ending = count_starting = 0
    for index in range(n):
        count_ending += ending[index]
        count_starting += starting[index]
        ending[index], starting[index] = count_ending, count_starting
    return ending, starting


def solve(word):
    ending, starting = palindrome_counts(word)
    return sum(ending[cut] * starting[cut + 1] for cut in range(len(word) - 1))


def main():
    print(solve(sys.stdin.buffer.readline().strip()))


if __name__ == "__main__":
    main()
