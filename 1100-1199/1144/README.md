# 1144. Sharing boxes of gold among generals as evenly as possible

[Timus 1144](https://acm.timus.ru/problem.aspx?space=1&num=1144) · difficulty 1947 · greedy

Original problem by HNT.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 10000` boxes with values from 1 to 1000 are shared among
`M ≤ N`, `M ≤ 1000` generals; every box goes whole to one general.
Make the gap between the richest and the poorest general as small as
possible. The answer is accepted when the gap is at most a given `K`.
Print the gap, then the boxes of each general.

Time limit: 1 second. Memory limit: 4 MB.

## Input

`N`, `M` and `K`, then the `N` values.

## Output

The gap, then `M` lines with the box numbers of each general.

## Checking

Any sharing is accepted if its gap is at most `K`. The checker verifies
that every box is given exactly once, that the printed gap is the real
one, and that it does not exceed `K`. In the large tests `K` is the gap
this search reaches; where that is `1` it is also the best possible,
since the total is not divisible by `M`.

## Examples

### Example 1

Input:

```
10 3 4
12 95 16 37 59 50 47 3 41 95
```

Output:

```
4
1 2 7
3 4 8 10
5 6 9
```

## Solution

Splitting numbers into `M` groups with equal sums is NP-hard, so this is
a heuristic: a good start and a local search that stops as soon as the gap
is at most `K`.

The start is the classic "largest first" rule: take the boxes from the
most valuable down and give each to the general who has the least gold so
far, found with a heap (Java scans all generals instead).

Then repeat, while the gap is above `K`, with the richest general `hi` and
the poorest `lo`, gap `d`:

1. **Move or swap.** Moving a box of value `v` from `hi` to `lo` leaves
   their pair gap `|d − 2v|`; swapping boxes `a` from `hi` and `b` from
   `lo` leaves `|d − 2(a − b)|`. Each general keeps its boxes sorted, so a
   binary search finds the box closest to `d/2`, and for every distinct
   value `a` the box `b` closest to `a − d/2`. The best change is made if it
   narrows the pair.
2. If `hi` and `lo` admit none, the same is tried between `hi` and every
   other general, poorest first, and between every general, richest
   first, and `lo`.
3. **Exact split.** If no single move or swap helps, the boxes of two
   generals are pooled and split as evenly as possible by a subset-sum
   table kept as bitsets, one row per prefix (including empty) to read the
   split back. The bit data must fit in 4 million bits, about half a megabyte.
4. If nothing helps, the search stops.

Each change narrows the gap of two generals without raising the richer one
or lowering the poorer one, so the sum of squares of the amounts drops
every time and the search ends; a cap on the rounds keeps the time safe.
On random tests with many boxes per general the gap reaches `1`, which is
optimal when the total is not divisible by `M`. With one or two boxes per
general it stays larger, and part of that is forced.

If the first stage still leaves a gap above `K`, try a bounded exact
depth-first search from empty groups. Process boxes in decreasing value order,
breaking ties by box number, and try generals in number order. For total `T`,
every final sum lies in `[L, U]`, where
`L = max(1, ceil((T - (M-1)K)/M))` and
`U = floor((T + (M-1)K)/M)`: a general's sum differs from every other
sum by at most `K`. These bounds tighten the average-based bounds
`[ceil(T/M)-K, floor(T/M)+K]`.

With partial sums `s` and remaining gold `A`, tighten the bounds to
`low = max(L, max(s)-K)` and `high = min(U, min(s)+A+K)`.
Reject a branch if a sum exceeds `high`, the deficits below `low` exceed
`A`, the total capacity below `high` is less than `A`, or there are more
empty generals than remaining boxes. At each level, try only the first
general with each distinct total, including zero. Interchangeable generals
make this safe; positive values and the empty-group check keep groups
nonempty. Explicit frames avoid recursion. Stop at the first sharing
within `K`. The caps are `B = SEARCH_NODES = 100000` candidate nodes and
`W = SEARCH_WORK = 1000000`, charging `M` work units per candidate.
If either cap is reached, retain the first stage's sharing. Thus the
overall method is still a heuristic on unrestricted large inputs.

Pitfalls:

- the memory limit of 4 MB rules out large subset-sum tables, hence the
  size check before each exact split;
- every general keeps at least one box: moves never empty `hi`, and a
  split that leaves a side empty is dropped;
- the printed gap must equal the real gap of the printed sharing.

The answers were checked by the checker on every test; all five languages
print identical sharings.

In the complexity table, `R = 20000` caps local-search rounds and
`P = SPLIT_BITS = 4000000` caps subset-sum bits.

## Language notes

- All languages make the same choices with the same tie-breaking, so
  their results are identical.
- Go, Java and Rust store a box as one integer, its value shifted left by
  14 bits plus its number, which sorts the same way as the pair.
- Java keeps everything in primitive arrays, reuses one buffer for the
  subset-sum tables and avoids lambdas: with the 4 MB limit, boxed
  numbers, short-lived tables and the machinery lambdas load in Java 8
  made the heap grow past it.
- Python drops input tokens and the initial order after use to stay
  within 4 MB.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1144_greedy.cpp](1144_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N + R·M·(N log N + P) + min(B·M, W)) | AC | 0.046 s | 404 KB |
| [1144_greedy.go](1144_greedy.go) | Go 1.14 x64 | greedy | O(N log N + R·M·(N log N + P) + min(B·M, W)) | AC | 0.109 s | 1948 KB |
| [1144_greedy.java](1144_greedy.java) | Java 1.8 | greedy | O(N² + R·M·(N log N + P) + min(B·M, W)) | AC | 0.156 s | 3628 KB |
| [1144_greedy.py](1144_greedy.py) | Python 3.12 x64 | greedy | O(N log N + R·M·(N log N + P) + min(B·M, W)) | AC | 0.671 s | 3512 KB |
| [1144_greedy.rs](1144_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N + R·M·(N log N + P) + min(B·M, W)) | AC | 0.046 s | 740 KB |
