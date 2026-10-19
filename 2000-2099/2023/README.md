# 2023. Walking between three destinations

[Timus 2023](https://acm.timus.ru/problem.aspx?space=1&num=2023) · difficulty 40 · implementation

Original problem by Alex Samsonov, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three destinations occupy consecutive positions 0, 1 and 2 on a line.
Each recipient label belongs to exactly one destination according to
this complete table:

| Position | Recipient labels |
| --- | --- |
| 0 | Alice, Ariel, Aurora, Phil, Peter, Olaf, Phoebus, Ralph, Robin |
| 1 | Bambi, Belle, Bolt, Mulan, Mowgli, Mickey, Silver, Simba, Stitch |
| 2 | Dumbo, Genie, Jiminy, Kuzko, Kida, Kenai, Tarzan, Tiana, Winnie |
Process a sequence of `n` labels in its given order, starting at
position 0. Moving to an adjacent position costs one step; processing a
label at its destination costs nothing. Find the total steps needed. The
route ends at the final destination: there is no required return to
position 0. Labels may repeat. Limits: `1 ≤ n ≤ 1000`, 1 second, 64 MB.

## Input

The first line contains `n`. Each of the following `n` lines contains
one label from the table, with exactly the displayed spelling and
capitalization. The line order is the processing order. All labels
contain only letters and have length at most seven.

## Output

Print one integer: the total number of steps, between 0 and `2n` inclusive.

## Checking

Outputs are compared token by token.

## Examples

```
4
Aurora
Tiana
Ariel
Mulan
```

```
5
```

## Solution

Only the current position matters after each item. The initials in the
three groups are disjoint: `A, P, O, R` identify position 0; `B, M, S`
identify position 1; all remaining permitted initials (`D, G, J, K, T,
W`) identify position 2. This shortcut applies because the input is
guaranteed to contain only labels from the table.

Initialize `position = 0` and `steps = 0`. For each label, obtain its
destination `target`, add `abs(target - position)` to `steps`, then
replace `position` by `target`. Print `steps` after processing exactly
`n` labels. Do not sort, merge or reorder the input.

To prove correctness, consider one transition from position `p` to
position `q`. Every step changes the coordinate by one, so at least
`|q-p|` steps are necessary. Walking directly toward `q` achieves that
bound. The required order fixes every consecutive pair of destinations,
including the initial position 0. Thus adding these exact distances
gives the required total. Inductively, after each processed label the
counters record its destination and the exact distance walked so far.
There is no extra transition after the final label.

In the example, the positions are `0 → 0 → 2 → 0 → 1`. The distances are
`0 + 2 + 2 + 1 = 5`. Time is `O(n)` because names have bounded length.
The scan uses `O(1)` counters; these programs store the input labels, so
their total additional storage is `O(n)`. A streaming implementation
could reduce that storage to `O(1)`.

Pitfalls:

- Start at the leftmost position, even before reading the first label.
- A jump between the two outer positions costs two steps; equal
  positions cost zero.
- Preserve repeated labels and the original order; do not add a final
  return journey.
- `Mickey`, `Kuzko` and `Phoebus` use the spellings in the table. The
  initials encode destinations, not alphabetical blocks or the position
  of a particular slot.

## Language notes

All five programs use the same scan and ordinary integers; the maximum
answer is 2000. C++ uses string membership, Go rune membership for the
ASCII initial, Rust byte membership, Java `indexOf`, and Python string
membership. Buffered input is sufficient for 1000 labels; CPython needs
no alternative runtime.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2023_implementation.cpp](2023_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 460 KB |
| [2023_implementation.go](2023_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1160 KB |
| [2023_implementation.java](2023_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 596 KB |
| [2023_implementation.py](2023_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 388 KB |
| [2023_implementation.rs](2023_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.062 s | 248 KB |
