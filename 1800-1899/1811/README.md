# 1811. Dual-SIM Phone

[Timus 1811](https://acm.timus.ru/problem.aspx?space=1&num=1811) · difficulty 1419 · binary_search

Original problem from the Tavrida NU Akai Contest, Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n mobile operators and k routes "via operator x to a number of
operator y for price c". A dual-SIM phone holds two operators and sends
each message through the cheaper one that can reach the target. Choose
two operators that reach numbers of every operator, so that the dearest
message is as cheap as possible.

## Input

n and k (2 ≤ n ≤ 10⁴, 0 ≤ k ≤ 10⁵), then k lines x y c
(1 ≤ x, y ≤ n, 1 ≤ c ≤ 10⁹).

## Output

The least possible price of the dearest message, or "No solution".

## Examples

### Example 1

Input:

```
4 13
1 1 1
1 2 3
1 3 3
1 4 5
2 1 2
2 2 1
2 3 2
3 1 4
3 3 4
3 4 1
4 1 2
4 2 3
4 4 3
```

Output:

```
2
```

### Example 2

Input:

```
2 2
1 1 3
2 1 4
```

Output:

```
No solution
```

## Solution

Binary search on the answer. For a price limit, keep only the routes
that cost at most that much and give every operator x the set of
targets it reaches, a bit set. A good pair exists when two sets cover
everything. Their sizes add up to at least n, so one of them, a, covers
at least half. For every such a, the targets a misses must all lie in
the partner's set. Pick the missed target with the fewest routes into
it overall: the partner has to be one of the operators reaching it, and each is
tested with a bitwise check that it covers everything a misses. The
routes are sorted by price and the limit is a prefix of them, so moving
from one limit to the next only adds or removes the routes in between,
which keeps all the bit sets up to date for about k changes in total.
`O(n²/64 + k log(k+1) · n/64)` in the worst case, far less in practice.

In the first example, at the limit 2 operator 2 reaches 1, 2 and 3, and
operator 3 reaches 4 for 1, so the pair 2 and 3 works. At the limit 1
no pair reaches operators 1 and 3 both.

Pitfalls:

- repeated routes between the same operators: keep the cheapest;
- an operator nobody reaches makes the answer "No solution";
- one operator that reaches everybody is enough, with any partner.

The answers agree with a direct search over all pairs on 90 small
cases, and with an independent accepted implementation on up to 10⁵
routes among a few hundred operators, on 10⁴ operators with a few
covering half of everybody, and on complete price tables.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1811_binary_search.cpp](1811_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n²/64 + k log(k+1) n / 64) | AC | 0.234 s | 21604 KB |
| [1811_binary_search.go](1811_binary_search.go) | Go 1.14 x64 | binary_search | O(n²/64 + k log(k+1) n / 64) | AC | 0.125 s | 24504 KB |
| [1811_binary_search.java](1811_binary_search.java) | Java 1.8 | binary_search | O(n²/64 + k log(k+1) n / 64) | AC | 0.281 s | 19976 KB |
| [1811_binary_search.py](1811_binary_search.py) | Python 3.12 x64 | binary_search | O(n log n + k log(k+1) n / 64) | AC | 0.625 s | 61252 KB |
| [1811_binary_search.rs](1811_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n²/64 + k log(k+1) n / 64) | AC | 0.031 s | 25552 KB |
