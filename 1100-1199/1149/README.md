# 1149. Writing out a nested expression of sines

[Timus 1149](https://acm.timus.ru/problem.aspx?space=1&num=1149) · difficulty 61 · strings

Original problem by Vladimir Gladkov, from the Ural Team Programming Championship, Perm, April 2001, trial round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Let `Aₙ = sin(1−sin(2+sin(3−…sin(n)…)))`, with the signs alternating
minus and plus, and
`S_N = (…((A₁+N)A₂+N−1)A₃+…+2)A_N+1`. For `1 ≤ N ≤ 200`, print the text of
`S_N` exactly as in the example, without spaces.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

The expression `S_N`.

## Examples

### Example 1

Input:

```
3
```

Output:

```
((sin(1)+3)sin(1-sin(2))+2)sin(1-sin(2+sin(3)))+1
```

## Solution

Only the text is asked for, nothing is computed. `Aₙ` is `sin(1`, then for
each next `k` the sign (minus after an odd number, plus after an even one)
and `sin(k`, and finally `n` closing brackets. `S_N` opens with `N − 1`
brackets; then for `i` from 1 to `N` it has `Aᵢ`, a plus, the number
`N − i + 1`, and a closing bracket after every part but the last. The
output has about `4·N²` characters, 165 thousand for `N = 200`, built in
one string. `O(N²)`.

Pitfalls:

- the sign after `k` depends on `k`, not on the depth of the sine;
- the last part `A_N+1` has no closing bracket;
- for `N = 1` the answer is just `sin(1)+1`;
- there are no spaces anywhere.

The answers were compared with a second construction that wraps the
expression from the inside out, `(S)Aᵢ+…`, with `Aᵢ` built by recursion,
for every test.

## Optimized solutions

The optimized C++ solution uses `scanf`, `printf` and `putchar`
instead of `iostream` and prints the expression piece by piece instead
of building it in a `std::string`, so the long answer is never held in
memory: 128 KB instead of 768 KB.

The optimized Java solution writes the expression straight into a 4 KB
byte buffer instead of building strings, and parses the number byte by
byte instead of using `Scanner`: 0.046 s instead of 0.125 s and 372 KB
instead of 4356 KB. The optimized Python solution writes the pieces as
they are made and builds each sine by extending the opening part of the
previous one: 384 KB instead of 780 KB, with the same time.

## Language notes

- The simple Python solution joins parts; the other simple solutions use
  strings or builders.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1149_strings.cpp](1149_strings.cpp) | G++ 13.2 x64 | strings | O(N²) | AC | 0.015 s | 768 KB | 11280016 |
| [1149_strings.go](1149_strings.go) | Go 1.14 x64 | strings | O(N²) | AC | 0.015 s | 2976 KB | 11280150 |
| [1149_strings.java](1149_strings.java) | Java 1.8 | strings | O(N²) | AC | 0.125 s | 4356 KB | 11280213 |
| [1149_strings.py](1149_strings.py) | Python 3.12 x64 | strings | O(N²) | AC | 0.046 s | 780 KB | 11280177 |
| [1149_strings.rs](1149_strings.rs) | Rust 1.75 x64 | strings | O(N²) | AC | 0.015 s | 636 KB | 11280243 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1149_strings_optimized.cpp](1149_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(N²) | AC | 0.015 s | 128 KB | 11303572 |
| [1149_strings_optimized.java](1149_strings_optimized.java) | Java 1.8 | strings | O(N²) | AC | 0.046 s | 372 KB | 11303716 |
| [1149_strings_optimized.py](1149_strings_optimized.py) | Python 3.12 x64 | strings | O(N²) | AC | 0.062 s | 384 KB | 11303717 |
