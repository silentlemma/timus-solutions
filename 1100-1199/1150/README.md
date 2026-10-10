# 1150. How many times each digit appears in the page numbers from 1 to N

[Timus 1150](https://acm.timus.ru/problem.aspx?space=1&num=1150) · difficulty 249 · math

Original problem by Evgeny Bryzgalov, from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Pages are numbered from 1 to `N`, `N < 10⁹`. Count how many times each
digit from 0 to 9 is written.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

Ten lines: the counts of zeros, ones, …, nines.

## Examples

### Example 1

Input:

```
12
```

Output:

```
1
5
2
1
1
1
1
1
1
1
```

## Solution

Count every decimal position separately. For the position with weight
`p` (1, 10, 100, …), split `N` into the part above it, `high = N / (10p)`,
the digit `cur` there and the part below, `low = N mod p`. Look at the
numbers from 1 to `N` by their part above this position:

- every upper part from `0` to `high − 1` is followed by all `10p` lower
  endings, so each digit appears `p` times at this position for each of
  them;
- with the upper part equal to `high`, a digit `d < cur` appears `p` more
  times, `d = cur` appears `low + 1` more times (for the endings `0` to
  `low`), and larger digits not at all.

Zeros are different: a zero at this position is written only if some
nonzero digit stands above it, so the upper part `0` does not count. That
gives `(high − 1)·p` for the full upper parts from 1, and then `p` or
`low + 1` as above, all only when `high > 0`. There are at most nine
positions. `O(log N)`.

Pitfalls:

- leading zeros are not written, which is why zeros need the separate
  rule;
- the counts reach `9·10⁸` for `N = 999999999`, still within 32 bits;
- `N` itself is included.

The answers were compared with writing out every number for all `N` up
to 3000 and many up to 30000, and with a digit-by-digit count over the
decimal form of `N` on every test.

## Language notes

- All languages run the same loop over positions.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1150_math.cpp](1150_math.cpp) | G++ 13.2 x64 | math | O(log N) | AC | 0.015 s | 128 KB |
| [1150_math.go](1150_math.go) | Go 1.14 x64 | math | O(log N) | AC | 0.031 s | 1084 KB |
| [1150_math.java](1150_math.java) | Java 1.8 | math | O(log N) | AC | 0.109 s | 1568 KB |
| [1150_math.py](1150_math.py) | Python 3.12 x64 | math | O(log N) | AC | 0.062 s | 460 KB |
| [1150_math.rs](1150_math.rs) | Rust 1.75 x64 | math | O(log N) | AC | 0.015 s | 236 KB |
