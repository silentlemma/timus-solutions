import sys


def radii(word):
    size = len(word)
    odd = [0] * size
    left, right = 0, -1
    for center in range(size):
        radius = 1 if center > right else min(odd[left + right - center], right - center + 1)
        while center >= radius and center + radius < size:
            if word[center - radius] != word[center + radius]:
                break
            radius += 1
        odd[center] = radius
        if center + radius - 1 > right:
            left, right = center - radius + 1, center + radius - 1
    even = [0] * size
    left, right = 0, -1
    for center in range(size):
        radius = 0 if center > right else min(even[left + right - center + 1], right - center + 1)
        while center > radius and center + radius < size:
            if word[center - radius - 1] != word[center + radius]:
                break
            radius += 1
        even[center] = radius
        if center + radius - 1 > right:
            left, right = center - radius, center + radius - 1
    return odd, even


def solve(word):
    size = len(word)
    odd, even = radii(word)

    def palindrome(start, end):
        length = end - start
        center = (start + end) // 2
        if length & 1:
            return odd[center] >= length // 2 + 1
        return even[center] >= length // 2

    maximum = [-1] * (size + 1)
    maximum[0] = 0
    first = [-1] * (size // 2 + 1)
    last = [-1] * (size // 2 + 1)
    highest = -1
    for end in range(1, size + 1):
        position = end - 2
        if position >= 0 and maximum[position] >= 0:
            value = maximum[position]
            if first[value] < 0:
                first[value] = position
            last[value] = position
            highest = max(highest, value)
        for value in (highest, highest - 1):
            if value < 0 or first[value] < 0:
                continue
            start = first[value]
            if not palindrome(start, end):
                maximum[end] = value + 1
                break
            if last[value] != start and not palindrome(last[value], end):
                maximum[end] = value + 1
                break
    if maximum[size] < 0:
        return -1, -1
    minimum = 2 if palindrome(0, size) else 1
    return minimum, maximum[size]


def main():
    minimum, maximum = solve(sys.stdin.buffer.readline().strip())
    if minimum < 0:
        print(-1)
    else:
        print(minimum, maximum)


if __name__ == "__main__":
    main()
