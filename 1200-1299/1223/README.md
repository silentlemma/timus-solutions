# 1223. The fewest egg drops that find the critical floor

[Timus 1223](https://acm.timus.ru/problem.aspx?space=1&num=1223) · difficulty 291 · dp

Original problem: folklore, proposed by Alexander Klepinin, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

All eggs are equally strong: an egg survives a drop from floor `E` or
lower and breaks from any higher floor. With a given number of eggs and
floors, both at most 1000, find the fewest drops that determine `E` for
certain in the worst case; eggs that survive can be dropped again. Up to
1000 queries, ended by `0 0`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

One query per line: the number of eggs and the number of floors.

## Output

For each query, the fewest drops in the worst case.

## Examples

### Example 1

Input:

```
1 10
2 5
0 0
```

Output:

```
10
3
```

## Solution

Turn the question around: with `d` drops and `k` eggs, how many floors
can be settled? The first drop goes from some floor; if the egg breaks,
the floors below remain with `d − 1` drops and `k − 1` eggs, and if it
survives, the floors above remain with `d − 1` drops and `k` eggs. So

`reach(d, k) = reach(d − 1, k − 1) + reach(d − 1, k) + 1`,

with `reach(0, k) = reach(d, 0) = 0`. The answer for `n` floors is the
smallest `d` with `reach(d, k) ≥ n`. Ten eggs already allow a plain
binary search over 1000 floors, so more eggs never help and `k` is capped
at 10. Filling, for each `k`, the answers for every `n` as `d` grows takes
`O(10 · 1000)` once, and every query is then a table lookup.

Pitfalls:

- with one egg the only safe way is floor by floor, so the answer is the
  number of floors;
- any number of eggs above 10 behaves like 10, so the egg count is capped
  before the lookup;
- the floor counts grow like binomial coefficients, so they are capped at
  1000 too, or they overflow long before the table is complete.

The answers were checked against the direct minimax recurrence for up to
5 eggs and 60 floors, and compared with a separately written solution on
every test.

## Language notes

- All languages build the same table and answer the queries from it.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1223_dp.cpp](1223_dp.cpp) | G++ 13.2 x64 | dp | O(10 · 1000) once, O(1) per query | AC | 0.015 s | 172 KB |
| [1223_dp.go](1223_dp.go) | Go 1.14 x64 | dp | O(10 · 1000) once, O(1) per query | AC | 0.031 s | 1216 KB |
| [1223_dp.java](1223_dp.java) | Java 1.8 | dp | O(10 · 1000) once, O(1) per query | AC | 0.078 s | 668 KB |
| [1223_dp.py](1223_dp.py) | Python 3.12 x64 | dp | O(10 · 1000) once, O(1) per query | AC | 0.078 s | 812 KB |
| [1223_dp.rs](1223_dp.rs) | Rust 1.75 x64 | dp | O(10 · 1000) once, O(1) per query | AC | 0.015 s | 376 KB |
