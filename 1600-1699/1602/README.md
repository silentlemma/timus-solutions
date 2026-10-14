# 1602. Elevator

[Timus 1602](https://acm.timus.ru/problem.aspx?space=1&num=1602) · difficulty 457 · implementation

Original problem by Vladimir Yakovlev, from the Ninth Ural State University Open Personal Contest, March 1, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Petya is on the top floor n of a skyscraper and wants to get to the
first floor. The elevator is at floor k going down to the first floor;
there it stands for 15 seconds before it can go up. It passes a floor in
v seconds, Petya runs down a floor in u seconds (0.1 < v < u < 100, at
most two decimals), and boarding takes 5 seconds. Which floor should
Petya walk down to in order to reach the first floor as soon as
possible? Among equally good floors, choose the one with the least
walking.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

n, k, u and v.

## Output

The floor.

## Examples

### Example 1

Input:

```
50 49 4.8 0.2
```

Output:

```
45
```

## Solution

Try every floor f. Walking all the way down (f = 1) takes (n − 1)·u.
Otherwise Petya calls the elevator on reaching floor f, at time
(n − f)·u. The elevator can leave the first floor at (k − 1)·v + 15, so
it starts up at the later of the two moments, climbs f − 1 floors, waits
5 seconds for the boarding and comes down f − 1 floors again. The best
total wins, and on equal totals the higher floor, which means less
walking: `O(n)`.

The example settles the reading: the elevator only starts up when called
from floor f. If it could come up right after its stop, floor 44 would
beat floor 45 in the example.

The results were compared with an independent implementation on 3500
random and tie-prone inputs.

Pitfalls:

- u and v have at most two decimals, and exact ties do happen (test 09, floors 3
  and 4); in hundredths of a second every time is an exact integer, so
  no comparison of doubles is needed;
- walking the whole way is an option and often the best one in short
  buildings (test 02);
- ties go to the higher floor, so the comparison keeps later floors on
  equal totals.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1602_implementation.cpp](1602_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 416 KB |
| [1602_implementation.go](1602_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1096 KB |
| [1602_implementation.java](1602_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1680 KB |
| [1602_implementation.py](1602_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 464 KB |
| [1602_implementation.rs](1602_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.062 s | 236 KB |
