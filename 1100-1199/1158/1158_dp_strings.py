import sys


def safe_transitions(letters, forbidden):
    prefixes = {b""}
    for word in forbidden:
        prefixes.update(word[:length] for length in range(1, len(word)))
    longest_first = sorted(prefixes, key=len, reverse=True)

    transitions = {}
    for prefix in prefixes:
        targets = []
        for letter in letters:
            extended = prefix + letter
            if not extended.endswith(forbidden):
                suffix = next(p for p in longest_first if extended.endswith(p))
                targets.append(suffix)
        transitions[prefix] = targets
    return transitions


def main():
    _alphabet_size, length, _word_count, alphabet, *forbidden = sys.stdin.buffer.read().split()
    letters = [bytes([letter]) for letter in alphabet]
    transitions = safe_transitions(letters, tuple(forbidden))

    ways = {b"": 1}
    for _ in range(int(length)):
        following = {}
        for prefix, count in ways.items():
            for suffix in transitions[prefix]:
                following[suffix] = following.get(suffix, 0) + count
        ways = following
    print(sum(ways.values()))


main()
