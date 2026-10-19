from array import array
import sys

ALPHABET_SIZE = 26
LETTER_BASE = ord("a")


def palindrome_radii(text, odd):
    count = len(text)
    radius = array("i", [0]) * count
    left, right = 0, -1
    if odd:
        for center in range(count):
            current = (
                0
                if center > right
                else min(radius[left + right - center], right - center)
            )
            while (
                center - current - 1 >= 0
                and center + current + 1 < count
                and text[center - current - 1] == text[center + current + 1]
            ):
                current += 1
            radius[center] = current
            if center + current > right:
                left, right = center - current, center + current
    else:
        for center in range(count):
            current = (
                0
                if center > right
                else min(radius[left + right - center + 1], right - center + 1)
            )
            while (
                center - current - 1 >= 0
                and center + current < count
                and text[center - current - 1] == text[center + current]
            ):
                current += 1
            radius[center] = current
            if center + current - 1 > right:
                left, right = center - current, center + current - 1
    return radius


def suffix_automaton(pattern):
    capacity = 2 * len(pattern)
    transitions = array("i", [-1]) * (capacity * ALPHABET_SIZE)
    length = array("i", [0]) * capacity
    link = array("i", [-1]) * capacity
    first_end = array("i", [-1]) * capacity
    states, last = 1, 0
    for position, letter in enumerate(pattern):
        symbol = letter - LETTER_BASE
        current = states
        states += 1
        length[current] = length[last] + 1
        first_end[current] = position
        previous = last
        while previous >= 0 and transitions[previous * ALPHABET_SIZE + symbol] < 0:
            transitions[previous * ALPHABET_SIZE + symbol] = current
            previous = link[previous]
        if previous < 0:
            link[current] = 0
        else:
            following = transitions[previous * ALPHABET_SIZE + symbol]
            if length[previous] + 1 == length[following]:
                link[current] = following
            else:
                clone = states
                states += 1
                length[clone] = length[previous] + 1
                link[clone] = link[following]
                first_end[clone] = first_end[following]
                source, destination = following * ALPHABET_SIZE, clone * ALPHABET_SIZE
                transitions[destination : destination + ALPHABET_SIZE] = transitions[
                    source : source + ALPHABET_SIZE
                ]
                while (
                    previous >= 0
                    and transitions[previous * ALPHABET_SIZE + symbol] == following
                ):
                    transitions[previous * ALPHABET_SIZE + symbol] = clone
                    previous = link[previous]
                link[following] = link[current] = clone
        last = current
    return transitions, length, link, first_end


def find_rotations(first, second):
    first_size, second_size = len(first), len(second)
    middle_size = first_size - second_size
    doubled = first + first
    radius = palindrome_radii(doubled, middle_size % 2)
    half = middle_size // 2
    center_offset = second_size + half
    if not any(radius[start + center_offset] >= half for start in range(first_size)):
        return None
    reversed_second = second[::-1]
    pattern = reversed_second + reversed_second[:-1]
    transitions, length, link, first_end = suffix_automaton(pattern)
    state, matched = 0, 0
    for position in range(first_size + second_size - 1):
        symbol = doubled[position] - LETTER_BASE
        while state and transitions[state * ALPHABET_SIZE + symbol] < 0:
            state = link[state]
            matched = length[state]
        following = transitions[state * ALPHABET_SIZE + symbol]
        if following >= 0:
            state = following
            matched += 1
        else:
            state, matched = 0, 0
        start = position - second_size + 1
        if (
            start >= 0
            and matched >= second_size
            and radius[start + center_offset] >= half
        ):
            reversed_start = first_end[state] - second_size + 1
            return start, (second_size - reversed_start) % second_size
    return None


def main():
    first, second = sys.stdin.buffer.read().split()
    answer = find_rotations(first, second)
    if answer is None:
        print("No")
    else:
        print("Yes")
        print(answer[0] + 1, answer[1] + 1)


if __name__ == "__main__":
    main()
