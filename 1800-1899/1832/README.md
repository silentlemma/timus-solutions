# 1832. Arirang Show

[Timus 1832](https://acm.timus.ru/problem.aspx?space=1&num=1832) · difficulty 953 · constructive

Original problem by Victor Kamashev (prepared by Daniil Aizenshtein), from the Fifteenth Ural Championship in Sports Programming, April 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n artists in a row split into d round dances, d an unknown proper
divisor of n: the j-th dance holds artists j, j + d, j + 2d, … in a
circle. Choose shirt colours from 26 so that neighbours in every dance
differ, whichever d is chosen, or report that this is impossible.

## Input

n (2 ≤ n ≤ 300000).

## Output

n lowercase letters, the colours of the artists, or "Impossible". Any
valid colouring is accepted.

## Examples

### Example 1

Input:

```
7
```

Output:

```
acacbdb
```

## Solution

Number the artists from 0. Two artists are neighbours for some d
exactly when they are d or n − d apart, with d a proper divisor of n.

Let m be the least number that does not divide n. Then m divides no
proper divisor either, so colouring by x mod m separates every two
artists d apart. Since lcm(1, …, 13) = 360360 exceeds 300000, m is at
most 13.

That leaves the wrap-around pairs n − d apart. With p the least prime
factor of n, every proper divisor is at most n/p, so these gaps are at
least n − n/p. Split the line into the first n − n/p artists and the
last n/p: no gap inside either part is that long, as n/p ≤ n − n/p.
Colour both parts by x mod m, the second part with its own m letters.
Then pairs inside a part are fine, and pairs across the parts never
share a colour. At most 2m ≤ 26 letters are used, so the answer is
never "Impossible". `O(n)`.

For n = 7, m = 2 and p = 7: the first six artists alternate a and b
and the last one gets c, giving abababc; the sample answer is another
valid colouring.

Pitfalls:

- the circles wrap around, so artists n − d apart are neighbours too;
- with d = n/2 a circle has only two artists, still a neighbouring
  pair;
- colouring by x mod m alone fails on the wrap: for n = 7 it gives
  artists 0 and 6 the same colour.

Every n from 2 to 3000 and many large ones, including those where all
26 letters are used, were checked against every proper divisor.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1832_constructive.cpp](1832_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 476 KB |
| [1832_constructive.go](1832_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 2192 KB |
| [1832_constructive.java](1832_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 2708 KB |
| [1832_constructive.py](1832_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.140 s | 5448 KB |
| [1832_constructive.rs](1832_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 492 KB |
