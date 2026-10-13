from array import array
import sys

PLAYERS = 3
SUITS = 4
RANKS = 8
HAND = 10
RANK_NAMES = ("7", "8", "9", "10", "J", "Q", "K", "A")
CACHE_BITS = 18
CACHE_SIZE = 1 << CACHE_BITS
KEY_BITS = 64
KEY_MASK = (1 << KEY_BITS) - 1
GOLDEN = 0x9E3779B97F4A7C15
ENTRY_BITS = 2
PRESENT = 2
LAST_DISCARD_PAIR = PLAYERS + 1
FIRST_DISCARD_PAIR = PLAYERS + 2


def solve(words):
    owner = [[-1] * RANKS for _ in range(SUITS)]
    for player in range(PLAYERS):
        for t in words[player * HAND : (player + 1) * HAND]:
            t = t.decode()
            owner["SCDH".index(t[-1])][RANK_NAMES.index(t[:-1])] = player
    initials = [tuple(player for player in row if player >= 0) for row in owner]
    # Every suit state is a subsequence of one of the four dealt suits.
    strings = {()}
    for row in initials:
        for mask in range(1 << len(row)):
            strings.add(tuple(player for rank, player in enumerate(row) if mask >> rank & 1))
    strings = sorted(strings, key=lambda x: (len(x), x))
    ids = {row: index for index, row in enumerate(strings)}
    size = len(strings)
    width = (size - 1).bit_length()
    signatures = []
    heights = []
    for row in strings:
        signatures.append((row.count(0), tuple(player for player in row if player)))
        heights.append(
            tuple(
                sum(player != 0 for player in row[:rank])
                for rank, player in enumerate(row)
                if player == 0
            )
        )

    # With defender order fixed, raising the declarer's cards can only hurt the declarer.
    # Keep the hardest comparable successor for each defender move.
    def prune(steps, packed=False):
        keep = []
        for step in set(steps):
            suit = step // 2 if packed else step
            harder = False
            for other in steps:
                other_suit = other // 2 if packed else other
                if suit == other_suit or (packed and step % 2 != other % 2):
                    continue
                if signatures[suit] == signatures[other_suit] and all(
                    x <= y for x, y in zip(heights[suit], heights[other_suit])
                ):
                    harder = True
                    break
            if not harder:
                keep.append(step)
        return tuple(sorted(keep))

    own = [bytearray(size) for _ in range(PLAYERS)]
    discard = [[()] * size for _ in range(PLAYERS)]
    transitions = [[None] * size for _ in range(PLAYERS)]
    danger = [bytearray(size) for _ in range(PLAYERS)]
    missing = [[None] * size for _ in range(PLAYERS)]
    harmless = bytearray(size)
    for suit, row in enumerate(strings):
        masks = [
            sum(1 << rank for rank, owner in enumerate(row) if owner == player)
            for player in range(PLAYERS)
        ]
        reps = [[] for _ in range(PLAYERS)]
        for rank, player in enumerate(row):
            if rank == 0 or row[rank - 1] != player:
                reps[player].append(1 << rank)
        for player in range(PLAYERS):
            own[player][suit] = masks[player]
            if masks[player]:
                bits = [1 << (masks[player].bit_length() - 1)] if player == 0 else reps[player]
                discard[player][suit] = array(
                    "H",
                    prune(
                        tuple(
                            ids[
                                tuple(
                                    owner for rank, owner in enumerate(row) if not bit >> rank & 1
                                )
                            ]
                            for bit in bits
                        )
                    ),
                )
        for lead in (1, 2):
            missing[lead][suit] = tuple(
                player
                for player in ((lead + 1) % PLAYERS, (lead + 2) % PLAYERS)
                if not masks[player]
            )
            groups = []
            losing = False
            for a in reps[lead]:
                group = set()
                for b in reps[PLAYERS - lead] or [0]:
                    # Following suit, discard the highest certainly safe card.
                    # In second seat the last defender can play their lowest card.
                    if masks[0]:
                        limit = max(a, b) if lead == 1 else max(a, masks[1] & -masks[1])
                        safe = masks[0] & (limit - 1)
                        if not safe:
                            losing = True
                            break
                        c = 1 << (safe.bit_length() - 1)
                    else:
                        c = 0
                    removed = a | b | c
                    following = ids[
                        tuple(player for rank, player in enumerate(row) if not removed >> rank & 1)
                    ]
                    win = lead if a > b else PLAYERS - lead
                    if masks[0] and danger[win][following]:
                        losing = True
                    group.add(following * 2 + win - 1)
                if losing:
                    break
                if lead == 2 and not masks[0]:
                    groups.append(tuple(sorted(group)))
                else:
                    groups.extend((step,) for step in sorted(group))
            danger[lead][suit] = losing
            if masks[0]:
                groups = [(step,) for step in prune(tuple(group[0] for group in groups), True)]
            transitions[lead][suit] = tuple(array("H", group) for group in dict.fromkeys(groups))
        # Harmless suits stay safe with arbitrary defender leads and discards.
        # The shorter suit states have already been solved.
        harmless[suit] = not masks[0] or (
            not danger[1][suit]
            and not danger[2][suit]
            and all(
                harmless[following]
                for player in (1, 2)
                for following in discard[player][suit] or ()
            )
            and all(
                harmless[step // 2]
                for lead in (1, 2)
                for group in transitions[lead][suit]
                for step in group
            )
        )
    # Prefer discards that remove an immediate threat or finish making a suit safe.
    risk = bytearray(size)
    priority = [bytearray(size) for _ in range(PLAYERS)]
    for suit in range(size):
        if own[0][suit] and not harmless[suit]:
            risk[suit] = 1 + risk[discard[0][suit][0]]
        for lead in range(PLAYERS):
            priority[lead][suit] = (RANKS + 1 - risk[suit] if not harmless[suit] else 0) + (
                RANKS + 1
            ) * danger[lead][suit]
    # In harmless suits only declarer card count and defender order matter.
    classes = {}
    normal = array("H")
    for suit, row in enumerate(strings):
        signature = (
            (row.count(0), tuple(player for player in row if player)) if harmless[suit] else row
        )
        normal.append(classes.setdefault(signature, suit))
    memo = array("Q", [0]) * CACHE_SIZE

    def finish(state, lead, absent):
        if not absent:
            return search(*state, lead)
        # Cache pending discards too, preserving their order of play.
        state = sorted(normal[suit] for suit in state)
        context = (
            absent[0] + 1
            if len(absent) == 1
            else (LAST_DISCARD_PAIR if absent[0] == 2 else FIRST_DISCARD_PAIR)
        )
        key = (lead - 1) + 2 * context
        for suit in state:
            key = key << width | suit
        slot = ((key * GOLDEN) & KEY_MASK) >> (KEY_BITS - CACHE_BITS)
        entry = memo[slot]
        if entry >> ENTRY_BITS == key and entry & PRESENT:
            return bool(entry & 1)
        player = absent[0]
        order = (
            sorted(enumerate(state), key=lambda item: priority[lead][item[1]], reverse=True)
            if player == 0
            else enumerate(state)
        )
        for other_index, suit in order:
            if other_index and suit == state[other_index - 1]:
                continue
            if own[player][suit]:
                for following in discard[player][suit]:
                    state[other_index] = following
                    ok = finish(state, lead, absent[1:])
                    state[other_index] = suit
                    if ok == (player == 0):
                        memo[slot] = key << ENTRY_BITS | PRESENT | ok
                        return ok
        ok = player != 0
        memo[slot] = key << ENTRY_BITS | PRESENT | ok
        return ok

    def search(a, b, c, d, lead):
        a, b, c, d = normal[a], normal[b], normal[c], normal[d]
        if harmless[a] and harmless[b] and harmless[c] and harmless[d]:
            return True
        if danger[lead][a] or danger[lead][b] or danger[lead][c] or danger[lead][d]:
            return False
        state = sorted((a, b, c, d))
        key = lead - 1
        for suit in state:
            key = key << width | suit
        slot = ((key * GOLDEN) & KEY_MASK) >> (KEY_BITS - CACHE_BITS)
        entry = memo[slot]
        if entry >> ENTRY_BITS == key and entry & PRESENT:
            return bool(entry & 1)
        for index, suit in enumerate(state):
            if index and suit == state[index - 1]:
                continue
            if not own[lead][suit]:
                continue
            absent = missing[lead][suit]
            # Declarer discards before seeing the last defender play.
            if lead == 2 and not own[0][suit]:
                for group in transitions[lead][suit]:
                    ok = False
                    order = sorted(
                        enumerate(state), key=lambda item: priority[0][item[1]], reverse=True
                    )
                    for other_index, other_suit in order:
                        if not own[0][other_suit]:
                            continue
                        state[other_index] = discard[0][other_suit][0]
                        good = True
                        for step in group:
                            state[index] = step // 2
                            win = step % 2 + 1
                            if not finish(state, win, absent[1:]):
                                good = False
                                break
                        state[index] = suit
                        state[other_index] = other_suit
                        if good:
                            ok = True
                            break
                    if not ok:
                        memo[slot] = key << ENTRY_BITS | PRESENT
                        return False
            else:
                for group in transitions[lead][suit]:
                    step = group[0]
                    state[index] = step // 2
                    ok = (
                        finish(state, step % 2 + 1, absent)
                        if absent
                        else search(*state, step % 2 + 1)
                    )
                    state[index] = suit
                    if not ok:
                        memo[slot] = key << ENTRY_BITS | PRESENT
                        return False
        memo[slot] = key << ENTRY_BITS | PRESENT | 1
        return True

    initial = [ids[row] for row in initials]
    lead = int(words[(PLAYERS * HAND)]) - 1
    if lead:
        result = search(*initial, lead)
    else:
        # Declarer leads only once; try one certainly safe card per suit.
        result = False
        for index, suit in enumerate(initial):
            row = strings[suit]
            mask = own[0][suit]
            limit = max(own[1][suit] & -own[1][suit], own[2][suit] & -own[2][suit])
            if not limit:
                continue
            safe = mask & (limit - 1)
            if not safe:
                continue
            a = 1 << (safe.bit_length() - 1)
            choices = []
            for player in (1, 2):
                opts = []
                for rank, owner in enumerate(row):
                    if owner == player and (not rank or row[rank - 1] != player):
                        opts.append(1 << rank)
                choices.append(opts or [0])
            good = True
            for b in choices[0]:
                for c in choices[1]:
                    removed = a | b | c
                    following = ids[
                        tuple(player for rank, player in enumerate(row) if not removed >> rank & 1)
                    ]
                    state = initial[:]
                    state[index] = following
                    absent = tuple(player for player in (1, 2) if not own[player][suit])
                    if not finish(state, 1 if b > c else 2, absent):
                        good = False
                        break
                if not good:
                    break
            if good:
                result = True
                break
    return result


print(";)" if solve(sys.stdin.buffer.read().split()) else ";(")
