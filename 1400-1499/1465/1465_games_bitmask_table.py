"""Generate the losing residues and finite exceptions for positive Dawson rows."""

PERIOD = 34
PREFIX = 52
TAKE = 3


def grundy_values(limit):
    values = [0] * (limit + 1)
    for length in range(1, limit + 1):
        options = {values[max(0, length - 2)]}
        for left in range(length - TAKE + 1):
            right = length - TAKE - left
            options.add(values[left] ^ values[right])
        while values[length] in options:
            values[length] += 1
    return values


if __name__ == "__main__":
    # At this length any split of n+PERIOD-3 has a part >= PREFIX+PERIOD,
    # and any split of n-3 has a part >= PREFIX. Move PERIOD between the
    # corresponding long parts to pair their option values by induction.
    induction_start = 2 * PREFIX + PERIOD + TAKE - 1
    values = grundy_values(induction_start + PERIOD - 1)
    assert all(values[n] == values[n + PERIOD] for n in range(PREFIX, induction_start))

    losing = {n % PERIOD for n in range(PREFIX, PREFIX + PERIOD) if values[n] == 0}
    mask = sum(1 << residue for residue in losing)
    extra_losses = [n for n in range(1, PREFIX) if values[n] == 0 and n % PERIOD not in losing]
    assert all(values[n] == 0 for n in range(1, PREFIX) if n % PERIOD in losing)
    print(f"static final long LOSING_RESIDUES = 0x{mask:x}L;")
    print("Additional losing lengths:", *extra_losses)
