# 1194. How many handshakes when a party splits up on the way home

[Timus 1194](https://acm.timus.ru/problem.aspx?space=1&num=1194) · difficulty 83 · math

Original problem by Leonid Volkov, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 20000` hobbits, `K` of them married couples, leave a party together.
At every crossroads a group splits into smaller groups, and everyone
shakes hands with everyone they are parting from. Groups keep splitting
until each is a single hobbit or a married couple. The splits are given;
count all handshakes.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `K`, then for each split the group number, the number of new
groups and the number and size of each.

## Output

The number of handshakes.

## Examples

### Example 1

Input:

```
3 0
1 2 2 2 3 1
2 2 4 1 5 1
```

Output:

```
3
```

## Solution

Any two hobbits shake hands exactly once: at the split where they first
end up in different groups. The only pairs that never part are the
married couples, which go home together. So the answer is
`N·(N − 1)/2 − K`, and the description of the splits does not matter.
`O(1)`, apart from reading the first line.

Pitfalls:

- the split lines may be skipped altogether, but a solution that adds up
  the pairs parted at each split gets the same number;
- `N·(N − 1)/2` reaches about `2·10⁸`, which still fits in 32 bits, though
  64-bit arithmetic costs nothing here.

The answers were compared with a separately written solution, which sums
the handshakes split by split, on 200 random parties and on every test.

## Language notes

- All languages read only `N` and `K`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1194_math.cpp](1194_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 128 KB |
| [1194_math.go](1194_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1064 KB |
| [1194_math.java](1194_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1552 KB |
| [1194_math.py](1194_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 328 KB |
| [1194_math.rs](1194_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 208 KB |
