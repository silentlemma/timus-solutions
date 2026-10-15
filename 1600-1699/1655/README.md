# 1655. Somali Pirates

[Timus 1655](https://acm.timus.ru/problem.aspx?space=1&num=1655) · difficulty 1818 · dp

Original problem by Denis Musin, from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A laser gun on a ship turns at up to w revolutions a minute and fires
instantly, sinking whatever lies on its line. n pirate ships approach
straight towards it, ship i from azimuth bᵢ at distance dᵢ nautical miles
with speed vᵢ knots. No pirate may come closer than one nautical mile.
Starting with the gun at azimuth a, find the least time to sink them all
and a shooting order, or report that it is impossible.

## Input

a, w and n (0 ≤ a < 360, 0.01 ≤ w ≤ 1, 1 ≤ n ≤ 500), then n lines
bᵢ dᵢ vᵢ (0 ≤ bᵢ < 360, 1 ≤ dᵢ ≤ 1000, 0.01 ≤ vᵢ ≤ 100), all pirate
azimuths distinct.

## Output

The least time in minutes with precision 10⁻³ and the order of ships,
one number per line, or `Impossible`.

## Examples

### Example 1

Input:

```
0.0 0.05 2
144.0 22.0 100.0
216.0 22.0 100.0
```

Output:

```
12.000
2
1
```

### Example 2

Input:

```
0.0 0.05 2
144.0 20.0 100.0
216.0 20.0 100.0
```

Output:

```
Impossible
```

## Solution

Ship i must be shot within (dᵢ − 1) / vᵢ · 60 minutes. Measure every
azimuth clockwise from the gun's start; ships straight ahead are shot at
time 0. As the gun can fire while turning, any ship it sweeps over may
as well be shot then, so at every moment the sunk ships form an arc
around the start: some taken turning left (counter-clockwise), some
turning right.

So the state is (i, j, end): the i ships nearest the start on the left
and the j nearest on the right are gone, and the gun points at the left
or right end of that arc. The earliest time of each state comes from
the two smaller states, either continuing on the same side or crossing
back through the start from the other end, and a step is allowed only
if it reaches the new ship by its deadline. The answer is the best
state with i + j equal to the number of remaining ships; the stored
choices give the order. `O(n²)` states, at most 125 751 (i, j) pairs.

Pitfalls:

- crossing from one end to the other passes the start, so it costs the
  sum of the two distances, not their difference;
- a ship already at one mile is fine only if it is straight ahead
  (test 03);
- when both directions are equally fast (the first example), the
  program prefers ending on the left, as an independent accepted
  implementation does; a checker accepts any order with the least time.

The answers match an independent accepted implementation on 60 random
tests, order included.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1655_dp.cpp](1655_dp.cpp) | G++ 13.2 x64 | dp | O(n²) | AC | 0.031 s | 4224 KB |
| [1655_dp.go](1655_dp.go) | Go 1.14 x64 | dp | O(n²) | AC | 0.046 s | 9508 KB |
| [1655_dp.java](1655_dp.java) | Java 1.8 | dp | O(n²) | AC | 0.187 s | 12828 KB |
| [1655_dp.py](1655_dp.py) | Python 3.12 x64 | dp | O(n²) | AC | 0.359 s | 15848 KB |
| [1655_dp.rs](1655_dp.rs) | Rust 1.75 x64 | dp | O(n²) | AC | 0.031 s | 7732 KB |
