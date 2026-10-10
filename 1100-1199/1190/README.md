# 1190. Can a chocolate label with a few percentages be honest?

[Timus 1190](https://acm.timus.ru/problem.aspx?space=1&num=1190) · difficulty 339 · greedy

Original problem by Leonid Volkov, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A label lists `N ≤ 5000` ingredients in non-increasing order of their
shares; some shares are printed, in hundredths of a percent. Every real
share is a whole number from 1 to 10000 hundredths, and all of them add up
to exactly 100%. Decide whether real shares exist that agree with the
order and with every printed value.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then for each ingredient its name, `0`, or `1` and its share.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
4
Water 0
Cocoa-butter 0
Cocoa-powder 1 4000
Lecithin 0
```

Output:

```
NO
```

## Solution

Because shares never grow down the list, an ingredient without a printed
value is at least the next printed value below it (or 1 if there is none)
and at most the last printed value above it (or 10000). Printed values
are fixed. Taking every share at its lowest gives a valid non-increasing
list with the smallest total, and at its highest the largest total.

Every total in between is reachable too: starting from the lowest list,
raise the first share one by one up to its highest value, then the second,
and so on; the list stays non-increasing all the way, and the total grows
by one at each step. So the answer is `YES` exactly when the lowest total
is at most 10000 and the highest total at least 10000. `O(N)`.

Pitfalls:

- an unknown share is still at least 1, which can push the lowest total
  over 100%;
- with no printed values above, an unknown share can be as large as
  100%, not only as large as the first printed value;
- a label with no printed values at all is always honest, since
  `N ≤ 5000` shares of at least 1 fit into 10000.

The answers were compared with a separately written solution on 300
random labels and on every test.

## Language notes

- All languages make two passes, one from each end, keeping the nearest
  printed value.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1190_greedy.cpp](1190_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.031 s | 432 KB |
| [1190_greedy.go](1190_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 1336 KB |
| [1190_greedy.java](1190_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.171 s | 6296 KB |
| [1190_greedy.py](1190_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.062 s | 1372 KB |
| [1190_greedy.rs](1190_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.015 s | 448 KB |
