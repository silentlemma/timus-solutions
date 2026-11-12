# 1579. Coat Transportation

[Timus 1579](https://acm.timus.ru/problem.aspx?space=1&num=1579) · difficulty 499 · greedy

Original problem by Alexander Kokovin, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 10⁵ coats with sizes given in non-decreasing order are carried out
of a shop by wearing them one over another. A coat fits over another
only if its size is larger by more than R. Split the coats into the
fewest trips and print each trip as its number of coats and their
numbers in increasing order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and R, then the N sizes.

## Output

The number K of trips, then K lines with the coats of each trip. Any
best answer is accepted.

## Examples

### Example 1

Input:

```
8 3
1 2 3 5 7 10 12 13
```

Output:

```
3
2 3 6
3 1 4 7
3 2 5 8
```

## Solution

Coats whose sizes all lie within R of each other can never share a
trip, so the largest number of sizes in a window [x, x + R] is a lower
bound K; two pointers over the sorted sizes find it in one pass.

K trips are also enough: deal the coats round, coat i to trip
i mod K. In a trip, the coat after coat i is coat i + K, and the K + 1
coats from i to i + K do not fit into one window, so the size of coat
i + K is more than R above the size of coat i. `O(N)`. The results
were checked against an exhaustive search over all splits into trips
on 400 random small cases.

Pitfalls:

- the size must grow by more than R, so sizes exactly R apart cannot
  share a trip (test 04);
- with R = 0, equal sizes need separate trips (tests 03, gen2);
- several answers are valid, so a checker tests the trips.

## Optimized solutions

The C++, Go and Rust versions keep the two-pointer window and cyclic assignment. Sizes and their nonnegative differences are at most 10⁹, so the size array takes 4N bytes. For trip t numbered from zero, the coat numbers start at t+1 and grow by K while they are at most N. The trip contains ⌊(N−1−t)/K⌋+1 coats, so its length can be printed before enumerating the numbers. Input uses 4096-byte blocks and output uses an 8192-byte buffer. The scan and enumeration take O(N) time and the size array takes O(N) space. Java and Python use their admitted base versions.

The accepted base implementations [1579_greedy.java](1579_greedy.java), [1579_greedy.py](1579_greedy.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1579_greedy.cpp](1579_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.109 s | 984 KB | 11287884 |
| [1579_greedy.go](1579_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.093 s | 4040 KB | 11287886 |
| [1579_greedy.java](1579_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.140 s | 9960 KB | 11287889 |
| [1579_greedy.py](1579_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.203 s | 19332 KB | 11287887 |
| [1579_greedy.rs](1579_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.046 s | 7672 KB | 11287890 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1579_greedy_optimized.cpp](1579_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.015 s | 512 KB | 11315408 |
| [1579_greedy_optimized.go](1579_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(N) | AC | 0.015 s | 1232 KB | 11315410 |
| [1579_greedy_optimized.rs](1579_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N) | AC | 0.015 s | 600 KB | 11315417 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
