# 1303. Minimal Coverage

[Timus 1303](https://acm.timus.ru/problem.aspx?space=1&num=1303) · difficulty 181 · greedy

Original problem from the Second Ural Team Student Programming Championship, Yekaterinburg, April 3–4, 1998.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given up to 99 999 segments [Li, Ri] with integer ends
(−50 000 ≤ Li < Ri ≤ 50 000), choose as few of them as possible that
together cover [0, M], 1 ≤ M ≤ 5000. Print their number and the
chosen segments in increasing order of left ends, or `No solution`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

M, then the segments, one pair per line, ended by the pair `0 0`.

## Output

The count and then the segments, one per line, or `No solution`.

## Checking

Any minimal cover is accepted. The checker verifies that the count is
the minimum, that every printed segment appears in the input (no more
often than there), that the left ends do not decrease, and that the
segments leave no point of [0, M] uncovered. When no cover exists, the
output must be `No solution`.

## Examples

### Example 1

Input:

```
1
-1 0
-5 -3
2 5
0 0
```

Output:

```
No solution
```

### Example 2

Input:

```
1
-1 0
0 1
0 0
```

Output:

```
1
0 1
```

## Solution

The classic greedy. Keep the right end c of the part [0, c] covered so
far, starting with c = 0. Among the segments with L ≤ c take the one
with the largest R. If even that R is not beyond c, a point just to the
right of c can never be covered: `No solution`. Otherwise take it and
set c = R. Stop when c ≥ M.

Taking the furthest reach is safe: whatever segment an optimal cover
uses at this point ends no further, so swapping it for ours keeps the
cover valid and the count the same.

With the segments sorted by left end, one pointer moves through them
once, since a segment passed over once cannot help later (its R is at
most the current c). The chosen segments come out in increasing order
of left ends automatically. `O(N log N)` for the sort.

Pitfalls:

- covering means no gap inside [0, M]: segments that only touch at a
  point, like [0, 2] and [2, 5], are fine (test 04), but [0, 4] and
  [5, 10] leave a gap (test 06);
- a segment ending at 0 does not help (tests 02 and 09);
- the pair `0 0` is only the end marker, since every real segment has
  L < R.

The greedy counts were compared with a breadth-first search over
reachable right ends on 400 small random inputs.

## Language notes

- All languages break ties the same way, by the first segment in
  sorted order, so they print the same cover.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1303_greedy.cpp](1303_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.125 s | 1372 KB |
| [1303_greedy.go](1303_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.046 s | 8068 KB |
| [1303_greedy.java](1303_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.218 s | 8312 KB |
| [1303_greedy.py](1303_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.250 s | 24780 KB |
| [1303_greedy.rs](1303_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 3716 KB |
