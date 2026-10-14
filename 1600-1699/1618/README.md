# 1618. Arrays Printing

[Timus 1618](https://acm.timus.ru/problem.aspx?space=1&num=1618) · difficulty 4085 · combinatorics

Original problem from the SPbSU ITMO Contest at the Petrozavodsk Training Camp, Winter 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A Java array shaped like `new Object[a1][a2]…[an][0]` (n ≤ 100,
a1, …, an are positive integers, a1 · … · an ≤ 512) is printed with
`Arrays.deepToString`, giving the string S (at most 10⁵ characters).
Array elements are references, so
one array object may appear in several places. Two configurations are
the same when every two index paths lead to the same object in one
exactly when they do in the other. Count the configurations that print
as S, modulo 10007.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The string S.

## Output

The number of configurations modulo 10007.

## Examples

### Example 1

Input:

```
[[], []]
```

Output:

```
2
```

### Example 2

Input:

```
[[[[]]]]
```

Output:

```
1
```

### Example 3

Input:

```
[[[]], [[]]]
```

Output:

```
3
```

## Solution

Parsing the brackets gives the sizes a1, …, an. Count from the bottom.
m references to empty arrays may be grouped into objects in any way: a
set partition, so B(m) ways (Bell numbers). One level up, m references to
arrays of width w are first split into k distinct objects, S(m, k) ways
(Stirling numbers of the second kind); those k objects hold k · w
references to the next level, whose configurations are counted together:

f(m) = Σₖ S(m, k) · g(k · w),

where g counts the level below. Distinct objects may still hold the same
references, so the lower level is free. The root is one array with a1
references, so the answer is f(a1) at the top. At each non-empty level,
m never exceeds 512 / w nor the number of positions at that depth.
`O(|S| + n · 512²)`.

Pitfalls:

- `[]` alone has no references and exactly one configuration (test 04);
- the two arrays in the first example may or may not be one object: 2;
- the counts grow fast and are taken modulo 10007 from the Stirling
  table on.

The answers match an independent accepted implementation on 100
random shapes.

## Language notes

- Python runs under PyPy: CPython exceeds the 2 s limit on the judge's
  test 6.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1618_combinatorics.cpp](1618_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n · 512²) | AC | 0.015 s | 1212 KB |
| [1618_combinatorics.go](1618_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n · 512²) | AC | 0.031 s | 4348 KB |
| [1618_combinatorics.java](1618_combinatorics.java) | Java 1.8 | combinatorics | O(n · 512²) | AC | 0.156 s | 2872 KB |
| [1618_combinatorics.py](1618_combinatorics.py) | PyPy 3.10 x64 | combinatorics | O(n · 512²) | AC | 0.421 s | 6788 KB |
| [1618_combinatorics.rs](1618_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n · 512²) | AC | 0.031 s | 2468 KB |
