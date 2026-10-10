# 1191. Can a police officer catch a thief who keeps changing trams?

[Timus 1191](https://acm.timus.ru/problem.aspx?space=1&num=1191) · difficulty 248 · math

Original problem by Leonid Volkov, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A thief runs `L` minutes ahead of a police officer at the same speed. At each
of `N` stops the thief waits for a tram of a route running every `Ki`
minutes, at an unknown phase, and rides it to the next stop; the
officer follows to the same stop and takes the next tram of the same
route, making an arrest if the thief is still waiting. All trams move
at the same speed. Decide whether the officer can possibly catch the
thief before the `N` rides are over.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`L` and `N`, then `K1 … KN`, all whole numbers below 100.

## Output

`YES` if a catch is possible, otherwise `NO`.

## Examples

### Example 1

Input:

```
8 3
6 4 3
```

Output:

```
NO
```

### Example 2

Input:

```
15 4
7 3 13 6
```

Output:

```
YES
```

## Solution

Only the gap between them matters, and it changes only at stops. If the
thief reaches a stop with a gap of `g` minutes and waits `w` minutes
(`0 ≤ w < K`, depending on the schedule), the officer arrives `g`
minutes later. If `w ≥ g`, the thief is still there. Otherwise the
officer leaves on the first tram after arriving, a whole number of
intervals after the thief's tram, which makes the new gap a multiple of
`K` that is at least `g − w`. Choosing `w = g mod K` gives the smallest
possible new gap, `g − g mod K`.

A smaller gap is never worse later, since `g − g mod K` only grows with
`g`. So follow the luckiest case: replace the gap by `g − g mod K` at each
stop, and a catch is possible exactly when the gap becomes 0 at some
stop, which happens when it is below the interval there. `O(N)`.

Pitfalls:

- a gap equal to the interval does not give a catch, it just stays;
- intervals of 1 minute never change the gap;
- once the gap is a multiple of an interval, later stops can still cut it
  down.

The answers were compared with a separately written solution on 300
random chases and on every test.

## Language notes

- All languages update the gap with the remainder operator.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1191_math.cpp](1191_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 124 KB |
| [1191_math.go](1191_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1060 KB |
| [1191_math.java](1191_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 1636 KB |
| [1191_math.py](1191_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 352 KB |
| [1191_math.rs](1191_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 212 KB |
