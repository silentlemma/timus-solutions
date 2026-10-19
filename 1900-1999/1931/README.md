# 1931. Who Participates in the Most Comparisons?

[Timus 1931](https://acm.timus.ru/problem.aspx?space=1&num=1931) · difficulty 169 · simulation

Original problem from Open Ural FU Championship 2012 | by Olga Soboleva.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

People stand in a fixed order with distinct positive scores. Initially
person 1 is the incumbent. Compare each later person with the incumbent;
replace the incumbent exactly when the newcomer has a smaller score.
Both people participate in that comparison, including when it replaces
the incumbent. Output a person who participates in the most comparisons.
Any tied maximum is valid. Limits: 1 second, 64 MB.

## Input

First n, 1≤n≤100000. Then n pairwise distinct integers a1..an,
1≤ai≤1000000000. Identifiers 1..n follow the input order.

## Output

One identifier with a maximum comparison count. For n=1 output 1,
since the only person has zero comparisons.

## Checking

Any valid answer: checker.py requires exactly one integer in 1..n,
literally simulates the process with a separate counter per person,
and verifies that the selected counter is maximal. The stored index
is only one of them; any other tied winner is accepted.

## Examples

```
6
2 5 3 4 1 9
```

```
1
```

## Solution

Keep the current incumbent's score, index and comparison count, plus
the largest count and its index seen so far. Initially the current count
is zero. At each newcomer, first increment the OLD incumbent's count
and update the best result if that count is larger. Only then compare
scores. If the newcomer is smaller, replace the incumbent and set the
new count to 1: the newcomer has already taken part in this comparison.
If the incumbent stays, the newcomer's entire lifetime count is 1.

The incumbent is always the minimum-score person in the processed prefix,
and the current counter tracks every comparison during that person's
incumbency, including the incoming and outgoing ones where applicable.
An unselected newcomer cannot beat the recorded maximum: its sole
comparison is paired with an incumbent whose just-incremented count
is already at least 1. The same argument covers a new incumbent's initial
count. Every later increase happens while that person is incumbent and
is explicitly tested. Replaced people never return, so their totals stay
fixed. Induction therefore makes the recorded result a global maximum.
The initial answer 1 also handles the no-comparison case.

O(n) time and O(1) working counters. These programs buffer the input
as a vector, array or token storage, so total space is O(n).

The person with the smallest score need not be the most compared.
Count the outgoing incumbent's losing comparison BEFORE replacement.
The new incumbent starts at 1, not 0. Return an identifier, not the count.
Do not reject a different answer merely because the maximum is tied.
For example, [3,2,1,4] allows either 2 or 3.

## Language notes

Scores fit signed 32-bit integers; counters are at most n−1≤99999.
Only comparisons are made between scores. Java uses buffered integer
input; C++, Go and Rust store a primitive value array. Python iterates
over parsed tokens through a generator. No per-person counter array
is needed by the submitted algorithm; the independent checker uses one.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1931_simulation.cpp](1931_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 812 KB |
| [1931_simulation.go](1931_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.093 s | 3468 KB |
| [1931_simulation.java](1931_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.109 s | 828 KB |
| [1931_simulation.py](1931_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.125 s | 8392 KB |
| [1931_simulation.rs](1931_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 2136 KB |
