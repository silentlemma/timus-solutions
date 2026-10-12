# 1326. Bottle Taps

[Timus 1326](https://acm.timus.ru/problem.aspx?space=1&num=1326) · difficulty 391 · bitmask

Original problem: idea by Evgeny Kobzev, prepared by Pavel Atnashev and Alexander Mironenko, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A collector misses N ≤ 20 bottle caps. Each can be bought alone for its
own price, and there are M ≤ 100 offers of sets of caps, each with one
price for the whole set. All prices are positive and at most 1000. Find
the least money that buys every cap of a given list.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

N and the N single prices, then M and M lines, each with the price of a
set, the number of caps in it and their numbers. The last line has the
number of wanted caps and their numbers.

## Output

The least total price.

## Examples

### Example 1

Input:

```
4
10
11
12
13
3
17 2 1 3
25 3 2 3 4
15 2 3 4
3 1 3 4
```

Output:

```
25
```

## Solution

Only the wanted caps matter, so they get the bits of a mask of at most
20 bits, and every offer, a single cap or a set, becomes a price and the
mask of the wanted caps it holds. Let cheapest[s] be the least money
that buys at least the caps of s. Some bought offer has to hold the
lowest cap of s, and after it only the caps of s outside that offer are
left:

cheapest[s] = min over offers o holding the lowest cap of s of
price(o) + cheapest[s without the caps of o].

The remaining set is a smaller number, so going through s in increasing
order works, and cheapest[full set] is the answer. An offer is never
needed twice: the rest no longer holds any of its caps.
`O(2^K · (N + M))` for K wanted caps.

Pitfalls:

- a set may be cheaper than buying even one of its caps alone, and it
  may hold caps that are not wanted (tests 03 and 04);
- the list of wanted caps can be empty, and the answer is then 0
  (test 02);
- there may be no sets at all (test 05).

The answers were compared with trying every choice of offers on 400
random cases with up to 6 caps and 7 sets.

## Language notes

- Python puts the caps held by the fewest offers on the lowest bits,
  since the lowest cap of s picks the offers to try. It also drops every
  offer that another one beats, holding as many caps for no more money.
  Even so CPython needs about 4 seconds when the sets are of similar
  value, so the Python solution is submitted under PyPy 3.10, where it
  takes about 0.2 seconds.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1326_bitmask.cpp](1326_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^K·(N + M)) | AC | 0.078 s | 3884 KB |
| [1326_bitmask.go](1326_bitmask.go) | Go 1.14 x64 | bitmask | O(2^K·(N + M)) | AC | 0.125 s | 10076 KB |
| [1326_bitmask.java](1326_bitmask.java) | Java 1.8 | bitmask | O(2^K·(N + M)) | AC | 0.218 s | 4428 KB |
| [1326_bitmask.py](1326_bitmask.py) | PyPy 3.10 x64 | bitmask | O(2^K·(N + M)) | AC | 0.296 s | 11124 KB |
| [1326_bitmask.rs](1326_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^K·(N + M)) | AC | 0.078 s | 8308 KB |
