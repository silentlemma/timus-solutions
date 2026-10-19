# 1869. New Year Cruise

[Timus 1869](https://acm.timus.ru/problem.aspx?space=1&num=1869) · difficulty 240 · prefix_sums

Original problem by Denis Dublennykh, from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A train goes from Vladivostok (station 1) to Moscow (station n),
stopping at stations 1, …, n, and then back the same way. aᵢⱼ people
bought tickets from station i to station j: they ride the outbound
train when i < j and the return train when i > j. Every car has 36
seats. How many cars does the train need so that everybody gets a
seat?

## Input

n (2 ≤ n ≤ 100), then the n × n matrix aᵢⱼ (0 ≤ aᵢⱼ ≤ 1000, aᵢᵢ = 0).

## Output

The least number of cars.

## Examples

### Example 1

Input:

```
3
0 180 180
0 0 180
360 0 0
```

Output:

```
10
```

## Solution

The train must hold the largest number of people on board at once, on
any leg in either direction. For each direction, add aᵢⱼ where the
passengers get on and subtract it where they get off. The running sum
of these changes along the route is the load on each leg. The answer
is the largest load divided by 36 and rounded up. `O(n²)`.

In the example 360 people ride the outbound train on both legs (the
180 from station 1 to 3 together with the 180 from 1 to 2 or from 2 to
3), and 360 ride back all the way: 10 cars.

Pitfalls:

- the two directions are separate trips, so their loads must not be
  added;
- the division rounds up: 37 people need two cars;
- with no tickets at all the answer is 0.

The answers agree with an independent accepted implementation on 150
random matrices.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1869_prefix_sums.cpp](1869_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 196 KB |
| [1869_prefix_sums.go](1869_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(n^2) | AC | 0.031 s | 1244 KB |
| [1869_prefix_sums.java](1869_prefix_sums.java) | Java 1.8 | prefix_sums | O(n^2) | AC | 0.109 s | 448 KB |
| [1869_prefix_sums.py](1869_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(n^2) | AC | 0.093 s | 1440 KB |
| [1869_prefix_sums.rs](1869_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 344 KB |
