"""Validate any explanation pairing every event exactly once."""

from pathlib import Path
import sys


def judge(a, b, records, feasible, output):
    tokens = output.split()
    if tokens == ["Liar"]:
        return (not feasible, "ok" if not feasible else "a legal explanation exists")
    if tokens[:2] != ["No", "reason"]:
        return False, "wrong answer header"
    if not feasible:
        return False, "no legal explanation exists"
    entries = {time for time, direction in records if direction == 0}
    exits = {time for time, direction in records if direction == 1}
    if len(entries) != len(exits) or len(tokens) != 2 + 2 * len(entries):
        return False, "wrong number of pairs"
    try:
        values = list(map(int, tokens[2:]))
    except ValueError:
        return False, "pair contains a noninteger"
    for position in range(0, len(values), 2):
        entry, exit_time = values[position : position + 2]
        if entry not in entries or exit_time not in exits:
            return False, "unknown or reused event"
        duration = exit_time - entry
        if duration <= 0 or not (duration <= b or duration >= a):
            return False, "forbidden duration"
        entries.remove(entry)
        exits.remove(exit_time)
    return (not entries and not exits, "ok")


def main():
    data = list(map(int, Path(sys.argv[1]).read_text().split()))
    a, b, count = data[:3]
    records = list(zip(data[3::2], data[4::2]))
    if len(records) != count:
        raise ValueError("wrong event count in input")
    feasible = Path(sys.argv[2]).read_text().split()[:1] != ["Liar"]
    passed, detail = judge(a, b, records, feasible, Path(sys.argv[3]).read_text())
    print(detail)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
