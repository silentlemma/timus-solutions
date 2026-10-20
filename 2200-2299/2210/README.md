# 2210. Most money after T days of working or buying businesses

[Timus 2210](https://acm.timus.ru/problem.aspx?space=1&num=2210) · difficulty 2003 · dp

Original problem by Valentin Zuev, from the University Academic School Olympiad in Informatics 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each day a player either works for 1 coin or buys one business of any
of N kinds, which costs Aᵢ and brings Bᵢ coins every day from the next
day on; then the income of the businesses bought earlier is paid. For
each of Q durations T, find the most coins after T days, starting from
zero. The limits are 2 seconds and 256 MB.

## Input

N, 1 ≤ N ≤ 100, then the pairs Aᵢ, Bᵢ from 1 to 100, then Q,
1 ≤ Q ≤ 5 · 10⁴, and the durations 1 ≤ T ≤ 10⁸.

## Output

The largest amount for each T.

## Examples

### Example 1

Input:

```
1
1 100
1
5
```

Output:

```
401
```

### Example 2

Input:

```
2
1 1
4 10
1
8
```

Output:

```
42
```

## Solution

Only kinds that bring more than every cheaper kind matter, so they form
a list with growing cost and income, ending with the most expensive one,
cost C and income I.

A state is (income, money). One day either works or buys a kind that is
affordable, and a state with no more income and no more money than
another is dropped, so each day keeps a short staircase of states. The
DP runs day by day with two exits:

- **Work from now on.** A state (r, m) on day d that only works
  afterwards ends with m + (r + 1)(T − d), a line in T. Every state adds
  such a line.
- **Rich states.** Once income and money are both at least C, money
  never limits anything, and buying as early as possible is never
  worse. Then each remaining day independently takes the better of
  working, worth 1, and buying the kind that pays most for the k days
  left, worth Bk − A. From C + 1 days left on that is always the top
  kind, worth Ik − C, so after a fixed prefix the total is a quadratic
  in T whose T² part is the same for every rich state. Removing it
  leaves one line per rich state.

States below C money that are not rich keep working or buying, and the
loop stops once every state has become rich, which in the worst cases
takes a few hundred days. Small T up to
that point are answered from a table, and larger T take the best value
over the work lines and over the rich lines, each kept as an upper
convex hull and queried by binary search.

In the first example buying the only kind on the first day gives 100 a
day for four days, 401 in total.

The DP keeps at most C + 2I + 1 ≤ 301 states a day for a few hundred
days, and each query costs O(log).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2210_dp.cpp](2210_dp.cpp) | G++ 13.2 x64 | dp | O(D (C + I) N + Q log D) | AC | 0.046 s | 304 KB |
| [2210_dp.go](2210_dp.go) | Go 1.14 x64 | dp | O(D (C + I) N + Q log D) | AC | 0.078 s | 2716 KB |
| [2210_dp.java](2210_dp.java) | Java 1.8 | dp | O(D (C + I) N + Q log D) | AC | 0.187 s | 8628 KB |
| [2210_dp.py](2210_dp.py) | Python 3.12 x64 | dp | O(D (C + I) N + Q log D) | AC | 0.312 s | 11044 KB |
| [2210_dp.rs](2210_dp.rs) | Rust 1.75 x64 | dp | O(D (C + I) N + Q log D) | AC | 0.046 s | 2448 KB |
