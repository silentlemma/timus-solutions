import sys

ROLE_COUNT = 4
MASK_COUNT = 1 << ROLE_COUNT
ROLE_CODES = b"WMCR"
ROLE_NAMES = ("warrior", "mage", "cleric", "rogue")


def main():
    tokens = sys.stdin.buffer.read().split()
    member_count = int(tokens[0])
    reachable = [False] * MASK_COUNT
    reachable[0] = True

    for qualifications in tokens[1 : member_count + 1]:
        skills = 0
        for role, code in enumerate(ROLE_CODES):
            if code in qualifications:
                skills |= 1 << role

        # Descending masks prevent assigning this member more than one role.
        for mask in range(MASK_COUNT - 1, -1, -1):
            if not reachable[mask]:
                continue
            for role in range(ROLE_COUNT):
                bit = 1 << role
                if skills & bit and not mask & bit:
                    reachable[mask | bit] = True

    best = 0
    common = MASK_COUNT - 1
    for mask, possible in enumerate(reachable):
        if not possible:
            continue
        size = mask.bit_count()
        if size > best:
            best = size
            common = mask
        elif size == best:
            common &= mask

    output = [str(best)]
    if best < ROLE_COUNT:
        wanted = [name for role, name in enumerate(ROLE_NAMES) if not common & (1 << role)]
        output.append("Looking for " + " ".join(wanted))
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
