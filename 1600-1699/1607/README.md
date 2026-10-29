# 1607. Taxi

[Timus 1607](https://acm.timus.ru/problem.aspx?space=1&num=1607) · difficulty 46 · implementation

Original problem by Denis Musin, from the Ninth Ural State University Open Personal Contest, March 1, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Petya and a taxi driver haggle. Petya starts at a and raises the offer
by b each time; the driver starts at c and lowers the price by d each
time; they speak in turns, Petya first. Neither names a price past the
other's: the driver accepts Petya's offer instead of asking less than
it, and Petya accepts the driver's price instead of offering more than
it. How much does Petya pay? All numbers are from 1 to 10000.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

a, b, c and d.

## Output

The price of the ride.

## Examples

### Example 1

Input:

```
150 50 1000 100
```

Output:

```
450
```

## Solution

Play the haggle out. If a is already at least c, the driver takes it.
Otherwise Petya raises by b; if that reaches the driver's price, Petya
agrees to it. Then the driver lowers by d; if that reaches Petya's
offer, the driver agrees to the offer. The gap shrinks by at least 2 per
round, so at most about 5000 rounds are played: `O(max(1, c - a))`. The results
were compared with an independent implementation on 800 random
inputs.

Pitfalls:

- the side that would cross the other's price gives in at the other's
  price, so the answer is always a price that was actually named
  (tests 04 and 05);
- Petya can start above the driver's price; then no haggling happens and
  Petya pays a (test 02).

## Optimized solutions

The optimized Java solution parses the numbers byte by byte from
`System.in` instead of using `Scanner`: 316 KB instead of 1600 KB, with
the same time.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1607_implementation.cpp](1607_implementation.cpp) | G++ 13.2 x64 | implementation | O(max(1, c - a)) | AC | 0.015 s | 132 KB | 11288177 |
| [1607_implementation.go](1607_implementation.go) | Go 1.14 x64 | implementation | O(max(1, c - a)) | AC | 0.015 s | 1112 KB | 11288180 |
| [1607_implementation.java](1607_implementation.java) | Java 1.8 | implementation | O(max(1, c - a)) | AC | 0.140 s | 1600 KB | 11288188 |
| [1607_implementation.py](1607_implementation.py) | Python 3.12 x64 | implementation | O(max(1, c - a)) | AC | 0.093 s | 416 KB | 11288185 |
| [1607_implementation.rs](1607_implementation.rs) | Rust 1.75 x64 | implementation | O(max(1, c - a)) | AC | 0.031 s | 224 KB | 11288189 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1607_implementation_optimized.java](1607_implementation_optimized.java) \* | Java 1.8 | implementation | O(max(1, c - a)) | AC | 0.125 s | 316 KB | 11303763 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
