import sys

STEP = {"d": -1, "h": 0, "u": 1}  # letters in the order of the book


def finishes(height, left):
    # can a garland at this height end at the ground in exactly `left` links?
    # on the ground a link must go up, above it horizontal links can pad
    if height == 0:
        return left == 0 or left >= 2
    return left >= height


def allowed(letter, height):
    # never below the ground, and no horizontal link on it
    return height + STEP[letter] >= 0 and not (letter == "h" and height == 0)


def main():
    data = sys.stdin.read().split()
    n, s = int(data[0]), data[1]
    heights = [0]
    for c in s:
        heights.append(heights[-1] + STEP[c])
    # the last link that can take a larger letter and still be finished
    for i in range(n - 1, -1, -1):
        for c in "hu":
            if c > s[i] and allowed(c, heights[i]) and finishes(heights[i] + STEP[c], n - i - 1):
                out = list(s[:i]) + [c]
                height = heights[i] + STEP[c]
                # the rest is the smallest garland that still finishes
                for left in range(n - i - 1, 0, -1):
                    for d in "dhu":
                        if allowed(d, height) and finishes(height + STEP[d], left - 1):
                            out.append(d)
                            height += STEP[d]
                            break
                print("".join(out))
                return
    print("No solution")


main()
