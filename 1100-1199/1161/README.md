# 1161. The lightest result of merging creatures by twice the geometric mean

[Timus 1161](https://acm.timus.ru/problem.aspx?space=1&num=1161) · difficulty 93 · greedy

Original problem by Nick Durov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 100` creatures have integer weights from 1 to 10000. Two of them
can merge into one of weight `2·√(m₁·m₂)`, and merging goes on until one
is left. Find the smallest possible final weight, with two digits after
the point.

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
- the order matters: merging the lightest first can give a heavier result;
- the weight never exceeds 40000, well within double precision.

The answers were compared with trying every order of merges on 150
random colonies of up to seven creatures.

## Optimized solutions

The optimized C++ solution keeps the at most 100 weights in a fixed
array instead of a `vector`, so it needs no heap allocation: 136 KB
instead of 216 KB. The sorting and the rounding are the same.

The optimized Java solution reads the input in 4 KB blocks and parses
the numbers by hand instead of using `Scanner`, and rounds without
`BigDecimal`. A `double` is exactly an integer mantissa below `2^53`
divided by `2^shift`. Each merge gives at most `2·√(x·10000)`, so the
total stays below 40000 and the shift is from 37 to 52; 100 times the
mantissa is below `100·2^53` and still fits in a `long`. So 100 times
the total is an exact fraction of two `long` values, and the code rounds
it half to even, as `printf` does: 0.093 s instead of 0.140 s and 444 KB
instead of 1912 KB.

## Language notes

- All languages sort and fold the same way.
- The simple Java solution rounds the result through `BigDecimal` with
  ties to even, as `printf` does in C.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1161_greedy.cpp](1161_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 216 KB | 11281794 |
| [1161_greedy.go](1161_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1096 KB | 11281809 |
| [1161_greedy.java](1161_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 1912 KB | 11281833 |
| [1161_greedy.py](1161_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 364 KB | 11281821 |
| [1161_greedy.rs](1161_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 248 KB | 11281889 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1161_greedy_optimized.cpp](1161_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 136 KB | 11303573 |
| [1161_greedy_optimized.java](1161_greedy_optimized.java) | Java 1.8 | greedy | O(N log N) | AC | 0.093 s | 444 KB | 11303959 |
