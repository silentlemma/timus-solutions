# 1658. Sum of Digits

[Timus 1658](https://acm.timus.ru/problem.aspx?space=1&num=1658) · difficulty 203 · dp

Original problem by Vladimir Yakovlev (idea by Stanislav Vasilyev), from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For each of t queries, given the sum s₁ of the digits of a positive
integer and the sum s₂ of their squares, print the smallest such integer,
or `No solution` if there is none with at most 100 digits.

## Input

t (at most 10000), then t pairs s₁ s₂ (1 ≤ s₁, s₂ ≤ 10000).

## Output

The smallest number for each query, or `No solution`.

## Examples

### Example 1

Input:

```
4
9 81
12 9
6 10
7 9
```

Output:

```
9
No solution
1122
111112
```

## Solution

The smallest number has the fewest digits, and among those it is the
smallest string. It never contains a zero: a zero adds a digit without
changing either sum, so it would not be shortest. With at most 100
digits the sums stay within 900 and 8100, so larger queries have no
answer.

Except in Python, a table of the fewest nonzero digits for every pair (s₁, s₂) up to
900 × 8100 comes from one pass over the table: each cell is one more
than the best cell reached by taking away a digit d and d². The answer
is then built greedily: the first digit is the smallest d after which
the rest still needs exactly one digit fewer, and so on. The digits come
out sorted, so each search can start from the previous digit.
`O(S₁ · S₂ · 9)` for the table, `O(100)` per query.

Pitfalls:

- the table has 7.3 million cells, so it is kept in bytes;
- a sum of squares below the sum of digits, or above nine times it, is
  impossible; the table handles that with no special case;
- s₁ = 900 with s₂ = 8100 is a hundred nines, one digit more is already
  too long (test 02).

The answers match an independent accepted implementation on 80 000
queries.

## Language notes

- Python cannot fill a 7.3-million-cell table in time, so it keeps, for
  each number of digits k, a big integer per digit sum whose bits mark
  the reachable square sums; a new layer is an or of the previous one
  shifted by d² for each digit d. That takes about 16 MB and a fraction
  of a second. With K = 100, building costs `O(K · S₁ · S₂ · 9)` bit
  operations and each query `O(K · S₂)`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1658_dp.cpp](1658_dp.cpp) | G++ 13.2 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.140 s | 9592 KB |
| [1658_dp.go](1658_dp.go) | Go 1.14 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.203 s | 12960 KB |
| [1658_dp.java](1658_dp.java) | Java 1.8 | dp | O(S₁ · S₂ · 9) | AC | 0.265 s | 14264 KB |
| [1658_dp.py](1658_dp.py) | Python 3.12 x64 | dp | O(K · S₁ · S₂ · 9) | AC | 1.578 s | 23432 KB |
| [1658_dp.rs](1658_dp.rs) | Rust 1.75 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.140 s | 9596 KB |
