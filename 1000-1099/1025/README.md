# 1025. The fewest supporters to win a two-level majority vote

[Timus 1025](https://acm.timus.ru/problem.aspx?space=1&num=1025) · difficulty 67 · greedy, sorting

Original problem from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Voters are split into `K` groups (`K` odd, `1 ≤ K ≤ 101`), each of an odd
size; the total is at most 9999. A group says "yes" when more than half of
its members vote yes, and a decision passes when more than half of the
groups say "yes". Find the smallest number of supporters that, placed in the
right groups, pass any decision.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`K`, then the `K` group sizes.

## Output

The smallest number of supporters.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5
9 3 11 1 7
```

Output:

```
7
```

### Example 2

Input:

```
1
9999
```

Output:

```
5000
```

## Solution

To pass a decision the supporters must win `K / 2 + 1` groups (integer
division, `K` is odd), and winning a group of `s` voters (`s` odd) takes
`s / 2 + 1` supporters; any more in that group are wasted, and supporters in
lost groups are wasted too.

So choose `K / 2 + 1` groups with the smallest total cost `s / 2 + 1`. The
cost grows with the size, so the best groups are simply the smallest ones:
sort the sizes and add up the costs of the first `K / 2 + 1`.
`O(K log K)`.

Pitfalls:

- the majority of groups is `K / 2 + 1`, and the majority inside a group of
  `s` is `s / 2 + 1`, not `s / 2`;
- the sizes are not sorted in the input.

## Language notes

The same sort and sum everywhere.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1025_greedy_sorting.cpp](1025_greedy_sorting.cpp) | G++ 13.2 x64 | greedy, sorting | O(K log K) | AC | 0.001 s | 192 KB |
| [1025_greedy_sorting.go](1025_greedy_sorting.go) | Go 1.14 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 1076 KB |
| [1025_greedy_sorting.java](1025_greedy_sorting.java) | Java 1.8 | greedy, sorting | O(K log K) | AC | 0.109 s | 1724 KB |
| [1025_greedy_sorting.py](1025_greedy_sorting.py) | Python 3.12 x64 | greedy, sorting | O(K log K) | AC | 0.093 s | 372 KB |
| [1025_greedy_sorting.rs](1025_greedy_sorting.rs) | Rust 1.75 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 220 KB |
