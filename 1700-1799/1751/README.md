# 1751. Improbability Theory

[Timus 1751](https://acm.timus.ru/problem.aspx?space=1&num=1751) · difficulty 3496 · graphs

Original problem by Damir Akhmetzyanov, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A theory has n hypotheses, some resting on others, possibly in cycles.
Hypothesis i is admissible with probability pᵢ, independently, and
checking it takes tᵢ seconds, one check at a time. A hypothesis is true
when it and everything it rests on, directly or not, are admissible.
Find the expected time to learn which hypotheses are true, checking in
the best order.

## Input

n (1 ≤ n ≤ 500), then for each hypothesis tᵢ (1 ≤ tᵢ ≤ 1000), pᵢ
(0.0001 ≤ pᵢ ≤ 0.9999), kᵢ and the kᵢ hypotheses it rests on directly.

## Output

The expected time, with an error of at most 10⁻³.

## Examples

### Example 1

Input:

```
4
5 0.3 1 2
6 0.99 0
2 0.2 1 4
2 0.2 0
```

Output:

```
13.350
```

### Example 2

Input:

```
3
1 0.5 1 2
2 0.5 1 3
3 0.5 1 1
```

Output:

```
2.750
```

## Solution

Hypotheses on one cycle of dependencies rest on each other, so they are
all true or all false together. Tarjan's method splits the hypotheses
into such groups, listing every group after all the groups it rests
on.

A group needs checking only if every group it rests on turned out fully
admissible; any failure below already makes it false. Inside a group,
checks stop at the first failure, and the cheapest order is by
tᵢ / (1 − pᵢ), smallest first: swapping two neighbours in the wrong
order can only lower the expected time. So group g costs
E_g = t₁ + p₁t₂ + p₁p₂t₃ + … in that order and is fully admissible with
probability q_g = Πpᵢ. The answer is the sum over groups of E_g times
the product of q_h over all groups h that g rests on. That set is
built as a bitset, each group taking the sets of the groups it points
to, in the order Tarjan's method gives. `O(n² + n·m / 64)` for m
dependencies.

In the first example 2 and 4 are always checked, for 6 and 2 seconds,
1 only if 2 holds, 0.99 · 5, and 3 only if 4 holds, 0.2 · 2: 13.35 in
all.

Pitfalls:

- checking a group before the groups below it can waste time that a
  failure below would have saved;
- a group that is true must be checked completely;
- products over many groups can become tiny, which is harmless here.

The answers match the best adaptive strategy found by searching over
everything known so far, on 200 random theories of up to 6
hypotheses, and an independent accepted implementation on the large
tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1751_graphs.cpp](1751_graphs.cpp) | G++ 13.2 x64 | graphs | O(n^2 + n*m/64) | AC | 0.156 s | 1008 KB |
| [1751_graphs.go](1751_graphs.go) | Go 1.14 x64 | graphs | O(n^2 + n*m/64) | AC | 0.125 s | 4328 KB |
| [1751_graphs.java](1751_graphs.java) | Java 1.8 | graphs | O(n^2 + n*m/64) | AC | 0.484 s | 8164 KB |
| [1751_graphs.py](1751_graphs.py) | Python 3.12 x64 | graphs | O(n^2 + n*m/64) | AC | 0.234 s | 20332 KB |
| [1751_graphs.rs](1751_graphs.rs) | Rust 1.75 x64 | graphs | O(n^2 + n*m/64) | AC | 0.046 s | 3436 KB |
