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

## Optimized solutions

The new C++ and Go versions evaluate only four floor candidates. For floor f≥2 the exact time is max((n−f)u,R)+2(f−1)v+500 hundredths, where R=(k−1)v+1500. On either side of f=n−R/u this is linear: slope 2v−u to the left and 2v>0 to the right. A minimum on integer floors therefore lies at an endpoint or at one of the two adjacent integers around the kink. Take q=n−floor(R/u), test 2,n,q−1,q after clamping to [2,n], and compare with walking to floor 1. Exact integer hundredths preserve ties; explicitly prefer the higher floor on equal total time. Time and extra space are O(1). Keep every simple O(n) scan; Java, Python and Rust reuse their admitted bases.

The accepted base implementations [1602_implementation.java](1602_implementation.java), [1602_implementation.py](1602_implementation.py), [1602_implementation.rs](1602_implementation.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1602_implementation.cpp](1602_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 416 KB | 11288118 |
| [1602_implementation.go](1602_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1096 KB | 11288119 |
| [1602_implementation.java](1602_implementation.java) \* | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1680 KB | 11288121 |
| [1602_implementation.py](1602_implementation.py) \* | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 464 KB | 11288120 |
| [1602_implementation.rs](1602_implementation.rs) \* | Rust 1.75 x64 | implementation | O(n) | AC | 0.062 s | 236 KB | 11288123 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1602_math.cpp](1602_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 76 KB | 11315439 |
| [1602_math.go](1602_math.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 268 KB | 11315443 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
