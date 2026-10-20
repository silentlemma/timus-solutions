import sys

EXTENSION = 25


class Solver:
    def __init__(self, source):
        self.text = []
        self.border = [0]
        self.rank = [0]
        self.answer = [-1] * (EXTENSION + 1)
        self.total = 0
        for symbol in source:
            self.total += self.append(symbol)

    def append(self, symbol):
        text, border, rank = self.text, self.border, self.rank
        matched = border[-1]
        while matched and text[matched] != symbol:
            matched = border[matched]
        if text and text[matched] == symbol:
            matched += 1
        text.append(symbol)
        border.append(matched)
        period = len(text) - matched
        previous = matched - border[matched]
        rank.append(rank[matched] + (period != previous))
        return rank[matched]

    def rollback(self, length):
        del self.text[length:]
        del self.border[length + 1 :]
        del self.rank[length + 1 :]

    def finish(self, depth, total):
        text, border, rank = self.text, self.border, self.rank
        answer = self.answer
        length = len(text)
        remaining = EXTENSION - depth
        zero = [0] * length
        one = [0] * length
        for state, symbol in enumerate(text):
            fallback = border[state]
            if symbol == 0:
                zero[state] = state + 1
                one[state] = one[fallback] if state else 0
            else:
                one[state] = state + 1
                zero[state] = zero[fallback] if state else 0

        seeds = [[] for _ in range(remaining + 1)]
        ancestor = border[length]
        while length - ancestor <= remaining:
            period = length - ancestor
            score = total
            for step in range(1, remaining + 1):
                symbol = text[len(text) - period]
                matched = border[-1]
                if matched >= length:
                    other = symbol ^ 1
                    while matched >= length and text[matched] != other:
                        matched = border[matched]
                    if matched >= length:
                        matched += 1
                    else:
                        matched = zero[matched] if other == 0 else one[matched]
                    if matched < length:
                        seeds[step].append((matched, score + rank[matched]))
                score += self.append(symbol)
                answer[depth + step] = max(answer[depth + step], score)
            self.rollback(length)
            if ancestor == 0:
                break
            ancestor = border[ancestor]

        current = [-1] * length
        current[border[length]] = total
        active = [border[length]]
        for step in range(1, remaining + 1):
            following = [-1] * length
            next_active = []
            for state, score in seeds[step]:
                if following[state] == -1:
                    next_active.append(state)
                if score > following[state]:
                    following[state] = score
            for state in active:
                score = current[state]
                for target in (zero[state], one[state]):
                    if target < length:
                        value = score + rank[target]
                        if following[target] == -1:
                            next_active.append(target)
                        if value > following[target]:
                            following[target] = value
            if next_active:
                best = max(following[state] for state in next_active)
                answer[depth + step] = max(answer[depth + step], best)
            current, active = following, next_active

    def search(self, depth, split, total):
        if depth == split:
            self.finish(depth, total)
            return
        length = len(self.text)
        for symbol in (0, 1):
            score = total + self.append(symbol)
            self.answer[depth + 1] = max(self.answer[depth + 1], score)
            self.search(depth + 1, split, score)
            self.rollback(length)

    def solve(self):
        split = max(0, (EXTENSION - len(self.text) + 1) // 2)
        self.search(0, split, self.total)
        return self.answer[1:]


def main():
    source = [symbol == ord("X") for symbol in sys.stdin.buffer.readline().strip()]
    answer = Solver(source).solve()
    sys.stdout.write("\n".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
