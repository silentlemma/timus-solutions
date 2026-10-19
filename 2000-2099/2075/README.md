# 2075. Drinking a layered cocktail through a straw

[Timus 2075](https://acm.timus.ru/problem.aspx?space=1&num=2075) · difficulty 2608 · fenwick

Original problem by Mikhail Rubinchik, prepared by Egor Shchelkonogov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Liqueurs are poured into a glass and form layers ordered by density: a
lexicographically smaller name is denser and lies lower, and a liqueur
poured again joins its existing layer. A drinker keeps a straw at a
fixed height H and drinks 1 mm per second from that height, so the
layers above slide down into the straw. Drinking stops as soon as the
cocktail no longer reaches H, unless a pour happens exactly at that
moment. Given the timed events (pours, straw placements, a burn that
takes the straw out), print the time intervals of drinking and the
liqueur drunk in each. The limits are 1 second and 256 MB.

## Input

n ≤ 10⁵ events in increasing distinct times T ≤ 10⁹: `T name h` pours
h ≤ 10⁹ mm of a liqueur (1 to 10 lower-case letters), `T Oleg H` puts
the straw at height H ≤ 10¹⁴, below the current top, and starts
drinking, `T fire` stops drinking (it comes only while drinking).

## Output

Lines `from-to name` in increasing time; two neighbouring lines of the
same liqueur must not touch, so touching pieces are merged.

## Examples

### Example 1

Input:

```
7
1 kahlua 1
2 baileys 1
3 cointreau 1
4 Oleg 0
5 kahlua 3
6 fire
20 Oleg 0
```

Output:

```
4-5 baileys
5-6 cointreau
20-24 kahlua
```

## Solution

The glass is a list of layers sorted by name. Drinking for d seconds at
level H removes the material lying in [H; H + d) and, since everything
above slides down, takes it in order from the bottom up. So the work is:
find the layer that contains level H, drink the part of it above H (or
less, if d runs out), and repeat with the next layer while time and
cocktail remain. The straw level does not move while this happens.

All names are read first and sorted, giving each liqueur a fixed slot,
and a Fenwick tree holds the heights of the slots. The layer that
contains level H is the first slot whose prefix sum exceeds H, found by
the usual descent over the tree in O(log m), together with how much of
that layer lies above H. Every step either ends the drinking or empties
the rest of a layer above the straw; a layer that is completely above
the straw disappears, so apart from O(1) steps per event the steps are
paid for by pours, and the total is O(n log n).

Between two events the drinker drinks for their time difference. If the
cocktail runs out earlier, drinking stops for good; if it runs out
exactly at the next event, drinking goes on, which matters only when
that event is a pour (a new straw or a burn sets the state anyway).
After the last event the drinker, if still drinking, empties everything
above the straw. Pieces of one liqueur that touch in time are merged
when they are recorded.

In the example the straw at 0 first takes baileys (4-5), then the
cointreau that slid down (5-6); at 20 only kahlua is left, 4 mm, drunk
in 20-24.

## Language notes

Heights reach 10¹⁴ and times about 10⁹ + 10¹⁴, so 64-bit integers are
used. The Python solution is submitted on PyPy: on CPython it is close
to the limit.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2075_fenwick.cpp](2075_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n log n) | AC | 0.531 s | 17600 KB |
| [2075_fenwick.go](2075_fenwick.go) | Go 1.14 x64 | fenwick | O(n log n) | AC | 0.343 s | 31640 KB |
| [2075_fenwick.java](2075_fenwick.java) | Java 1.8 | fenwick | O(n log n) | AC | 0.609 s | 46824 KB |
| [2075_fenwick.py](2075_fenwick.py) | PyPy 3.10 x64 | fenwick | O(n log n) | AC | 0.843 s | 79896 KB |
| [2075_fenwick.rs](2075_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n log n) | AC | 0.187 s | 27692 KB |
