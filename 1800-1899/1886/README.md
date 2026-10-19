# 1886. Trip 2

[Timus 1886](https://acm.timus.ru/problem.aspx?space=1&num=1886) · difficulty 2047 · dp

Original problem by Denis Dublennykh, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Denis is at airport 1 at time 0 and must reach airport n. Each flight
leaves airport a for b at time t and flies f minutes, but with
probability p% it arrives d minutes late. Denis buys each ticket only
after landing, changes planes instantly, and chooses flights so that
he surely reaches airport n and the expected arrival time is as small
as possible. Print that expected time, or "Fail" if he cannot be sure
to get there.

## Input

n and m (2 ≤ n ≤ 100 000, 1 ≤ m ≤ 100 000), then m flights a, b, t, f, p,
d (1 ≤ t, f, d ≤ 10⁹, 1 ≤ p ≤ 99).

## Output

The expected arrival time with absolute or relative error at most 10⁻⁶, or "Fail".

## Examples

### Example 1

Input:

```
4 5
1 4 10 10 90 20
1 2 5 5 50 5
2 4 15 10 50 5
2 3 1 14 10 1
3 4 15 1 50 1
```

Output:

```
27.500
```

### Example 2

Input:

```
2 1
2 1 20 19 50 1
```

Output:

```
Fail
```

## Solution

Let E(a, T) be the best expected arrival for someone at airport a at
time T: E(n, T) = T, and otherwise the minimum over the flights from a
leaving at T or later of (1 − p/100)·E(b, t + f) + (p/100)·E(b, t + f + d). A
flight whose either outcome leads to infinity is useless, because
arrival must be sure. Both arrivals are later than the departure, so
handle the flights from the latest departure down. When a flight is
handled, every flight its passenger could connect to is already known.
For each airport keep its handled flights in that order with a running
minimum: E(a, T) is the running minimum at the last flight leaving at T
or later, found by binary search. The answer is E(1, 0).
`O(n + m log m)`.

In the first example the direct flight 1 → 4 gives 0.1·20 + 0.9·40 = 38
minutes. Flying 1 → 2 lands at 10 or 15, both in time for the flight
2 → 4 at 15, which lands at 25 or 30: 27.5 minutes.

Pitfalls:

- a flight is allowed only if both its on-time and its delayed arrival
  still lead surely to airport n;
- a connection leaving exactly at the arrival time can be taken;
- flights out of airport n are irrelevant: Denis stops on arrival;
- times reach about 3·10⁹ per flight, beyond signed 32-bit integers;
- the Python solution keeps the flights in flat numeric arrays and skips
  unreachable and dominated departures: 14 MB on the judge, where an
  earlier version with tuples and lists took 65 MB on test 15.

The answers match a search by the definition on 3000 small random
schedules, and an independent accepted implementation on large ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1886_dp.cpp](1886_dp.cpp) | G++ 13.2 x64 | dp | O(n + m log m) | AC | 0.312 s | 12500 KB |
| [1886_dp.go](1886_dp.go) | Go 1.14 x64 | dp | O(n + m log m) | AC | 0.140 s | 15964 KB |
| [1886_dp.java](1886_dp.java) | Java 1.8 | dp | O(n + m log m) | AC | 0.234 s | 18828 KB |
| [1886_dp.py](1886_dp.py) | Python 3.12 x64 | dp | O(n + m log m) | AC | 0.546 s | 13932 KB |
| [1886_dp.rs](1886_dp.rs) | Rust 1.75 x64 | dp | O(n + m log m) | AC | 0.093 s | 24620 KB |
