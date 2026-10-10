# 1161. The lightest result of merging creatures by twice the geometric mean

[Timus 1161](https://acm.timus.ru/problem.aspx?space=1&num=1161) · difficulty 92 · greedy

Original problem by Nick Durov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 100` creatures have integer weights up to 10000. Two of them can
merge into one of weight `2·√(m₁·m₂)`, and merging goes on until one is
left. Find the smallest possible final weight, with two digits after the
point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the `N` weights.

## Output

The smallest final weight.

## Examples

### Example 1

Input:

```
2
72
50
```

Output:

```
120.00
```

### Example 2

Input:

```
3
72
30
50
```

Output:

```
120.00
```

## Solution

Merge the two heaviest first, then the result with the next heaviest, and
so on down to the lightest. In any order of merges, each weight ends up
inside a number of nested square roots: a weight merged `k` times enters
the result as its `2^k`-th root, times constants that depend only on the
shape of the merges. The final weight is smallest when the heaviest
weights are rooted the most often, and the chain from the heaviest down
does exactly that, giving the largest weights the deepest positions.
Sorting and one pass: `O(N log N)`.

Pitfalls:

- with one creature, its weight is the answer;
- the order matters: merging the lightest first gives a heavier result;
- the weight never exceeds 40000, well within double precision.

The answers were compared with trying every order of merges on 150
random colonies of up to seven creatures.

## Language notes

- All languages sort and fold the same way.
- Java rounds the result through `BigDecimal` with ties to even, as
  `printf` does in C.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1161_greedy.cpp](1161_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 216 KB |
| [1161_greedy.go](1161_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1096 KB |
| [1161_greedy.java](1161_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 1912 KB |
| [1161_greedy.py](1161_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 364 KB |
| [1161_greedy.rs](1161_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 248 KB |
