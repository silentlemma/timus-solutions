import sys


def main():
    data = sys.stdin.buffer.read().split()
    team_count = int(data[0])
    names = data[1:]
    no_position = sum(len(name) for name in names)
    transitions = [{}]
    length = [0]
    link = [-1]
    positive = [None]
    missing = [1]
    negative = [team_count]
    first_end = [no_position]

    def new_state(longest, outgoing, suffix):
        state = len(length)
        transitions.append(outgoing)
        length.append(longest)
        link.append(suffix)
        positive.append(None)
        missing.append(1)
        negative.append(team_count)
        first_end.append(no_position)
        return state

    def extend(last, char):
        target = transitions[last].get(char, 0)
        if target:
            if length[target] == length[last] + 1:
                return target
            clone = new_state(length[last] + 1, transitions[target].copy(), link[target])
            while last != -1 and transitions[last].get(char, 0) == target:
                transitions[last][char] = clone
                last = link[last]
            link[target] = clone
            return clone

        current = new_state(length[last] + 1, {}, 0)
        while last != -1 and char not in transitions[last]:
            transitions[last][char] = current
            last = link[last]
        if last == -1:
            return current
        target = transitions[last][char]
        if length[target] == length[last] + 1:
            link[current] = target
            return current
        clone = new_state(length[last] + 1, transitions[target].copy(), link[target])
        while last != -1 and transitions[last].get(char, 0) == target:
            transitions[last][char] = clone
            last = link[last]
        link[target] = clone
        link[current] = clone
        return current

    positive_times = []
    for time, name in enumerate(names):
        coached = name.endswith(b"+")
        if coached:
            name = name[:-1]
            rank = len(positive_times)
            positive_times.append(time)
        state = 0
        for position, char in enumerate(name):
            state = extend(state, char)
            if time == 0:
                first_end[state] = position
            elif coached:
                if positive[state] is None:
                    positive[state] = {rank}
                else:
                    positive[state].add(rank)
            elif time < negative[state]:
                negative[state] = time
    positive_times.append(team_count)
    transitions.clear()

    buckets = [None] * (team_count + 1)
    order = sorted(range(1, len(length)), key=length.__getitem__, reverse=True)
    for state in order:
        bag = positive[state]
        absent = missing[state]
        if bag is not None:
            while absent in bag:
                absent += 1
        if first_end[state] != no_position:
            shortest = length[link[state]] + 1
            left = first_end[state] - shortest + 1
            deadline = min(negative[state], positive_times[absent])
            candidate = (shortest, left)
            if buckets[deadline] is None or candidate < buckets[deadline]:
                buckets[deadline] = candidate

        parent = link[state]
        # Reuse the larger set, so every copied document moves only logarithmically often.
        if bag is not None:
            parent_bag = positive[parent]
            if parent_bag is None:
                positive[parent] = bag
            elif len(parent_bag) < len(bag):
                bag.update(parent_bag)
                positive[parent] = bag
            else:
                parent_bag.update(bag)
        positive[state] = None
        if absent > missing[parent]:
            missing[parent] = absent
        if negative[state] < negative[parent]:
            negative[parent] = negative[state]
        if first_end[state] < first_end[parent]:
            first_end[parent] = first_end[state]

    answer = [""] * team_count
    best = None
    for time in range(team_count - 1, -1, -1):
        candidate = buckets[time + 1]
        if candidate is not None and (best is None or candidate < best):
            best = candidate
        if best is None:
            answer[time] = "-1 -1"
        else:
            size, left = best
            answer[time] = f"{left} {left + size - 1}"
    sys.stdout.write("\n".join(answer) + "\n")


if __name__ == "__main__":
    main()
