# 2094. When to take a seat in a filling row

[Timus 2094](https://acm.timus.ru/problem.aspx?space=1&num=2094) · difficulty 5142 · dp, probability

Original problem by Denis Dublennykh, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cinema row has n seats; some are taken, one is Alex's, and every
vacant seat stays vacant until the film starts with probability p %,
independently. The other spectators come in one at a time in random
order, and everybody reaches a seat from the left end of the row. Alex
may wait in the aisle and choose when to go; if still waiting at the
start, Alex goes then. Minimise the expected number of spectators Alex
passes plus the number who pass Alex. The limits are 1 second and 64 MB.

## Input

Integers n and p (1 ≤ n ≤ 1000, 0 ≤ p ≤ 100), then a string of n
characters: 0 for vacant, 1 for taken, 2 for Alex's seat. The string
contains exactly one 2.

## Output

The expected value with an absolute or relative error of at most 10⁻⁶.

## Examples

### Example 1

Input:

```
5 0
01120
```

Output:

```
2.500
```

### Example 2

Input:

```
3 50
020
```

Output:

```
0.375
```

## Solution

Taken seats to the left are passed whatever Alex does, so they add a
constant. What matters is the vacant seats: l of them to the left and r
to the right, v = l + r in total. Each will be filled with probability
1 − p/100, so the number of arrivals is binomial; after some arrivals
have been seen, the chance that one more comes and the expected number
still to come depend only on how many vacant seats are left, and both
follow from a short recurrence over that number. Every next arrival
takes each still vacant seat with the same probability.

A DP over (l, r) then compares two choices. Going now costs the expected
number of later arrivals to the right, r times the expected arrivals
still to come divided by l + r. Waiting for the next arrival costs
nothing if nobody else comes; otherwise the newcomer sits on the left
with probability l / (l + r) (Alex will have to pass that person: 1 plus
the value at (l − 1, r)) or on the right (the value at (l, r − 1)). With
nothing vacant on the left Alex can simply wait, and with nothing on the
right Alex can go: both cost 0. The answer is the taken seats on the
left plus the value at the start, O(n²) in total.

In the first example everyone comes (p = 0); waiting for the spectator
to the right costs 2 or 3 depending on who comes first, so the answer is
2.5.

Pitfall (test 03): the answer for a single seat is 0. Both `0` and
`0.000` are valid; judging must compare numeric values with the stated
tolerance, rather than require identical text.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2094_dp_probability.cpp](2094_dp_probability.cpp) | G++ 13.2 x64 | dp, probability | O(n^2) | AC | 0.015 s | 468 KB |
| [2094_dp_probability.go](2094_dp_probability.go) | Go 1.14 x64 | dp, probability | O(n^2) | AC | 0.031 s | 1132 KB |
| [2094_dp_probability.java](2094_dp_probability.java) | Java 1.8 | dp, probability | O(n^2) | AC | 0.109 s | 544 KB |
| [2094_dp_probability.py](2094_dp_probability.py) | Python 3.12 x64 | dp, probability | O(n^2) | AC | 0.125 s | 740 KB |
| [2094_dp_probability.rs](2094_dp_probability.rs) | Rust 1.75 x64 | dp, probability | O(n^2) | AC | 0.015 s | 256 KB |
