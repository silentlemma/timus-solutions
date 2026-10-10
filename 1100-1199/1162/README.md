# 1162. Can a chain of currency exchanges with commissions increase the money

[Timus 1162](https://acm.timus.ru/problem.aspx?space=1&num=1162) · difficulty 185 · shortest_paths

Original problem by Nick Durov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N ≤ 100` currencies and `M ≤ 100` exchange points, each
working between two currencies in both directions with its own rate and
commission per direction: exchanging `x` gives `(x − commission)·rate`,
and the amount may never become negative. Starting with `V` units of
currency `S`, decide whether some sequence of exchanges ends in currency
`S` with more than `V`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, `M`, `S` and `V`, then `M` lines with two currencies and the rate
and commission each way.

`1 ≤ S ≤ N ≤ 100`, `1 ≤ M ≤ 100`, and `0 ≤ V ≤ 1000`.
Rates are in `[0.01, 100]` and commissions in `[0, 100]`, each with at most
two fractional digits. The number of fractional digits in `V` is not
restricted. For any exchange sequence using each exchange point at most
once, the ratio of the final amount to the initial amount is less than
`10000`.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
3 2 1 10.0
1 2 1.0 1.0 1.0 1.0
2 3 1.1 1.0 1.1 1.0
```

Output:

```
NO
```

### Example 2

Input:

```
3 2 1 20.0
1 2 1.0 1.0 1.0 1.0
2 3 1.1 1.0 1.1 1.0
```

Output:

```
YES
```

## Solution

Think of currencies as vertices and each exchange direction as an edge.
Use Bellman–Ford with `best[c]` equal to the largest reachable amount of
currency `c`. Initially only `S` is reachable, with amount `V`. Each pass
reads the previous array and writes a new one, so after pass `k` the
amounts are optimal among walks of at most `k` exchanges. Deduct the
commission before multiplying by the rate, and skip unaffordable exchanges.

Use exact integers instead of floating point. Let `P` be the larger of
two and the number of fractional digits in `V`; the initial common
denominator is `D = 10^P`. Store rates and commissions multiplied by 100.
For an amount numerator `x`, rate `R` and commission `C`, the next numerator
is `(x − C·(D/100))·R`, with denominator `100·D`. Multiply retained amounts
and the starting amount by 100 too, then update `D`. This preserves all
digits and makes every affordability and improvement comparison exact.

If no reachable cycle gains, deleting a repeated-vertex segment cannot
reduce the money, so simple paths of at most `N − 1` exchanges suffice.
Thus an improvement on pass `N` proves that a gaining cycle is reachable.
Its positive rates and nonnegative commissions imply a multiplier greater
than one; repetition grows the money without bound. Every exchange point
works both ways, so eventually the reverse path to `S` is affordable.
Return `YES` on such an improvement or as soon as `best[S] > V`; otherwise
return `NO` when a pass makes no improvement.

There are `O(N·M)` relaxations and `O(N²)` array entries to copy. Integers
have `O(P+N)` digits, giving `O(N·(N+M)·(P+N))` time and
`O(N·(P+N)+M)` space with exact arithmetic.

Pitfalls:

- the commission is paid first in the source currency; reaching zero is
  valid, and an unreachable currency must remain distinct from zero;
- a profit may require a cycle far from `S`;
- test **08** starts with `0.000000001` and doubles it: an absolute
  tolerance hides the gain, while removing it from floating-point code
  can mistake rounding for profit. Parse `V` exactly without rounding it
  to two decimal places.

Verification used all 8 stored tests, 101 generator cases, 2,500 random
inputs checked by exhaustive simple-path/cycle enumeration with exact
fractions, and 600 exact break-even and tiny-margin cases.

## Language notes

- All languages run the same passes over the same list of directed
  exchanges.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1162_shortest_paths.cpp](1162_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(N·(N+M)·(P+N)) | AC | 0.031 s | 700 KB |
| [1162_shortest_paths.go](1162_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(N·(N+M)·(P+N)) | AC | 0.015 s | 5444 KB |
| [1162_shortest_paths.java](1162_shortest_paths.java) | Java 1.8 | shortest_paths | O(N·(N+M)·(P+N)) | AC | 0.109 s | 4980 KB |
| [1162_shortest_paths.py](1162_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(N·(N+M)·(P+N)) | AC | 0.093 s | 740 KB |
| [1162_shortest_paths.rs](1162_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(N·(N+M)·(P+N)) | AC | 0.031 s | 312 KB |
