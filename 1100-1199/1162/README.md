# 1162. Can a chain of currency exchanges with commissions increase the money

[Timus 1162](https://acm.timus.ru/problem.aspx?space=1&num=1162) · difficulty 197 · shortest_paths

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

Think of currencies as vertices and every direction of an exchange point
as an edge. Let `best[c]` be the most money of currency `c` that can be
held, starting from `best[S] = V`. The Bellman–Ford relaxation
`best[b] = max(best[b], (best[a] − fee)·rate)`, allowed only when
`best[a] ≥ fee`, improves these amounts pass after pass. Each step is
increasing in the amount, so more money is never worse.

If no cycle gains, the best amounts are reached by simple paths, which
have at most `N − 1` exchanges, and the passes stop changing by then. So
if a pass still changes something after `N` passes, a gaining cycle is
reachable; going around it again and again makes any commission
negligible, and the way back to `S` exists because every point works in
both directions, so the answer is `YES`. It is also `YES` as soon as
`best[S]` exceeds `V`. Otherwise it is `NO`. `O(N·M)`.

Pitfalls:

- the commission is taken first, in the source currency, and an exchange
  with less money than the commission is impossible;
- a gain may need a detour through a cycle far from `S`;
- doubles are compared with a small tolerance, so rounding noise does not
  look like a gain.

The answers were compared on every test and on 150 random inputs with the
same relaxation in exact fractions, run for ten times as many passes.

## Language notes

- All languages run the same passes over the same list of directed
  exchanges.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1162_shortest_paths.cpp](1162_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(N·M) | AC | 0.015 s | 212 KB |
| [1162_shortest_paths.go](1162_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(N·M) | AC | 0.015 s | 1120 KB |
| [1162_shortest_paths.java](1162_shortest_paths.java) | Java 1.8 | shortest_paths | O(N·M) | AC | 0.093 s | 752 KB |
| [1162_shortest_paths.py](1162_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(N·M) | AC | 0.093 s | 592 KB |
| [1162_shortest_paths.rs](1162_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(N·M) | AC | 0.031 s | 264 KB |
