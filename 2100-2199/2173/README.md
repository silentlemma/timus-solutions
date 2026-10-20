# 2173. Counting placements of sponsors, at most two per problem

[Timus 2173](https://acm.timus.ru/problem.aspx?space=1&num=2173) · difficulty 831 · dp, combinatorics

Original problem by Vadim Barinov, from the Ural School Programming Contest 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are M problems and N sponsors; sponsor i must appear in exactly
sᵢ different problems, and a problem may mention at most two sponsors.
Count the placements modulo 10⁹ + 7; two placements differ when some
problem gets a different set of sponsors. The limits are 2 seconds and
256 MB.

## Input

N and M, 1 ≤ N ≤ 1000, 1 ≤ M ≤ 2000, then s₁ … s_N with 1 ≤ sᵢ ≤ M and
a total of at most 2M.

## Output

The number of placements modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
2 2
1 1
```

Output:

```
4
```

### Example 2

Input:

```
5 13
1 1 1 1 1
```

Output:

```
351780
```

## Solution

Add the sponsors one by one. After t mentions are placed, the problems
fall into three groups: j of them hold one sponsor, (t − j) / 2 hold
two, and the rest are empty. Which problem is in which group is all
that matters for the next sponsors, so the state is j alone.

The next sponsor with wish s takes a problems that already have one
sponsor and s − a empty problems, which can be chosen in
C(j, a) · C(e, s − a) ways, e being the number of empty problems. The new
state is j − a + (s − a). The answer is the sum over all final states.

The state has the parity of t, so at most M / 2 + 1 states are live, and
a sponsor with wish s costs O(M · s) transitions. In total this is
O(M · Σ sᵢ) = O(M²) with factorials and inverse factorials prepared
once.

In the first example the two sponsors either share one problem (two
ways) or take one problem each (two ways), four in total.

## Language notes

The Python solution runs on PyPy 3.10; in CPython the 5 · 10⁶ inner steps
take about a second.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2173_dp_combinatorics.cpp](2173_dp_combinatorics.cpp) | G++ 13.2 x64 | dp, combinatorics | O(M sum s) | AC | 0.031 s | 256 KB |
| [2173_dp_combinatorics.go](2173_dp_combinatorics.go) | Go 1.14 x64 | dp, combinatorics | O(M sum s) | AC | 0.062 s | 12392 KB |
| [2173_dp_combinatorics.java](2173_dp_combinatorics.java) | Java 1.8 | dp, combinatorics | O(M sum s) | AC | 0.375 s | 6288 KB |
| [2173_dp_combinatorics.py](2173_dp_combinatorics.py) | PyPy 3.10 x64 | dp, combinatorics | O(M sum s) | AC | 0.218 s | 6836 KB |
| [2173_dp_combinatorics.rs](2173_dp_combinatorics.rs) | Rust 1.75 x64 | dp, combinatorics | O(M sum s) | AC | 0.046 s | 312 KB |
