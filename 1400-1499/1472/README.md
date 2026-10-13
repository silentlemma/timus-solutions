# 1472. Martian Army

[Timus 1472](https://acm.timus.ru/problem.aspx?space=1&num=1472) · difficulty 1035 · dp

Original problem by Alexander Ipatov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N soldiers (2 ≤ N ≤ 100000) form a tree: soldier i > 1 reports to
commander K_i < i, and the link costs C_i (0 ≤ C_i ≤ 1000) per megabyte.
Every soldier has a real reliability A_i: the general (soldier 1) has 1,
privates (soldiers without subordinates) have 0, the others are
unknown. The traffic billed on the link of soldier i is any amount of
at least max(0, A_K_i − A_i), chosen by the soldiers. Find the smallest
bill the provider can be sure of, with exactly two digits after the
point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N − 1 lines K_i C_i for i = 2 … N.

## Output

The guaranteed amount.

## Examples

### Example 1

Input:

```
7
1 10
2 5
2 3
3 1
3 2
3 3
```

Output:

```
8.00
```

## Solution

The soldiers bill the minimum and choose the unknown reliabilities to
minimize Σ C_i·max(0, A_K_i − A_i). Clipping every A into [0, 1] never
raises a term. Then slice at each level t between 0 and 1: the soldiers
with A ≥ t contain the general and no private, and the links from them
to soldiers below t form a cut separating the general from all privates.
The bill is the integral of these cut prices over t, so it is never less
than the cheapest cut, and setting A to 1 above that cut and 0 below it
reaches it. The answer is the cheapest such cut, always a whole number.

In a tree it is a bottom-up minimum: cut(v), the cheapest way to separate
v from every private below it, is the sum over its subordinates u of
min(C_u, cut(u)), where a private cannot be separated from itself and so
offers only its own link. Commanders have smaller numbers than their
subordinates, so a pass from N down to 2 finishes every soldier before
the commander. The answer is cut(1). `O(N)`.

Pitfalls:

- the reliabilities are real, but the optimum is a whole number and is
  printed with ".00" (all tests);
- a cheap link deep below can beat an expensive one above, and links
  of price 0 make a whole branch free (tests 03, 04);
- a private offers only the link to the commander (test 02);
- a chain of 100000 soldiers is too deep for recursion, which the
  numbering lets us avoid (gen2).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1472_dp.cpp](1472_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.109 s | 1760 KB |
| [1472_dp.go](1472_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.093 s | 5536 KB |
| [1472_dp.java](1472_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 2120 KB |
| [1472_dp.py](1472_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.109 s | 20020 KB |
| [1472_dp.rs](1472_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 6288 KB |
