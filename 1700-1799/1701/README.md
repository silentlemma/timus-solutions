# 1701. Ostap and Partners

[Timus 1701](https://acm.timus.ru/problem.aspx?space=1&num=1701) · difficulty 639 · dsu

Original problem by Dmitry Ivankov, from the Thirteenth Ural Championship in Sports Programming, April 4, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A notebook holds statements "employee i earns d more than employee j".
Employee 0, Vasily, earns 0, and nobody else earns more than 10⁹ (or
less than 0). Find salaries that fit every statement, or the number of
the first statement that cannot be fitted together with the earlier
ones.

## Input

n and m (1 ≤ n, m ≤ 50000), then m statements i j d
(0 ≤ i, j < n; |d| ≤ 20000).

## Output

Possible and the n salaries, or "Impossible after i statements". Any
fitting salaries are accepted.

## Examples

### Example 1

Input:

```
5 6
3 4 1200
4 1 -5500
2 3 4300
3 0 8200
0 4 -7000
2 1 0
```

Output:

```
Possible
0
12500
12500
8200
7000
```

### Example 2

Input:

```
3 5
1 2 5
0 2 0
1 0 -5
1 2 5
2 2 0
```

Output:

```
Impossible after 3 statements
```

### Example 3

Input:

```
3 2
1 0 871
1 2 903
```

Output:

```
Impossible after 2 statements
```

## Solution

Process the statements in order with a weighted union-find. Each
employee stores the difference between their salary and their parent's,
so salary(x) = salary(root) + offset(x) once the path is compressed.
Each set also keeps the range of values its root's salary may take
while all its salaries stay within 0 … 10⁹. Vasily's set starts with
the single value 0.

A statement salary(i) − salary(j) = d inside one set must agree with
the offsets. Between two sets it fixes salary(rⱼ) = salary(rᵢ) + shift.
The joined root's range is then the old range intersected with the other
root's range moved by −shift, and an empty range means the statement
breaks things. At the end every root takes the lowest value of its
range, and every salary follows from the offsets.
`O((n + m) α(n))`.

Pitfalls:

- a statement can contradict only the bounds, not the other statements:
  in the third example the second statement makes a salary negative;
- a statement may compare an employee with themselves, and then d must
  be 0 (test 05);
- the upper bound never binds here, since |d| ≤ 20000 and at most
  49999 links keep every difference below 10⁹, but the lower bound does;
- the finds use iterative path compression; union by size keeps the
  trees shallow.

The checker verifies Vasily's 0, the ranges and every statement, or the
exact Impossible line; an independent accepted implementation passes it
on the same tests.

## Optimized solutions

The C++ version uses one record per employee. At a root, the parent field stores the negative component size. At other nodes it stores the parent index. Path compression accumulates the salary difference up to the root, and union by size keeps the recursion shallow. A byte buffer reads the comparisons without creating input tokens. Time is O((n + m) α(n)), and space is O(n). The metrics come from submission 11316975.

The Python version reads the statements one line at a time and uses path halving in the weighted disjoint-set structure. It keeps only the component data and the salaries needed for output. This uses O(n) space. Metrics come from submission 11317043.

Rust reads one comparison at a time and reuses the line buffer. Each disjoint-set record stores the parent or negative size, the offset to the parent, and the feasible salary interval for a root. Submission 11317269 took 0.046 s and used 992 KB, versus 0.031 s and 5152 KB for the base.

Go reads comparisons through a buffered byte parser. The weighted disjoint set uses one record of four 32-bit integers per employee and writes salaries through a reusable digit buffer. Submission 11317271 took 0.015 s and used 1712 KB, versus 0.109 s and 5968 KB for the base.

Java parses comparisons directly from a byte buffer and stores the disjoint-set data in four integer arrays. It reuses a digit buffer for salary output. Submission 11317272 took 0.125 s and used 1320 KB, versus 0.14 s and 6400 KB for the base.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11318326 · Java 1.8 №11318331 · Python 3.12 x64 №11318337 · Rust 1.75 x64 №11318346.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1701_dsu.cpp](1701_dsu.cpp) | G++ 13.2 x64 | dsu | O((n + m) α(n)) | AC | 0.109 s | 2768 KB | 11318326 |
| [1701_dsu.go](1701_dsu.go) | Go 1.14 x64 | dsu | O((n + m) α(n)) | AC | 0.109 s | 5968 KB | 11322029 |
| [1701_dsu.java](1701_dsu.java) | Java 1.8 | dsu | O((n + m) α(n)) | AC | 0.14 s | 6400 KB | 11318331 |
| [1701_dsu.py](1701_dsu.py) | Python 3.12 x64 | dsu | O((n + m) α(n)) | AC | 0.343 s | 18168 KB | 11318337 |
| [1701_dsu.rs](1701_dsu.rs) | Rust 1.75 x64 | dsu | O((n + m) α(n)) | AC | 0.031 s | 5152 KB | 11318346 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1701_dsu_optimized.cpp](1701_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O((n + m) α(n)) | AC | 0.015 s | 928 KB | 11316975 |
| [1701_dsu_optimized.go](1701_dsu_optimized.go) \* | Go 1.14 x64 | dsu | O((n + m) α(n)) | AC | 0.015 s | 1712 KB | 11317271 |
| [1701_dsu_optimized.java](1701_dsu_optimized.java) \* | Java 1.8 | dsu | O((n + m) α(n)) | AC | 0.125 s | 1320 KB | 11317272 |
| [1701_dsu_optimized.py](1701_dsu_optimized.py) \* | Python 3.12 x64 | dsu | O((n + m) α(n)) | AC | 0.234 s | 7652 KB | 11317043 |
| [1701_dsu_optimized.rs](1701_dsu_optimized.rs) \* | Rust 1.75 x64 | dsu | O((n + m) α(n)) | AC | 0.046 s | 992 KB | 11317269 |

\* Accepted. The Python rating target remains open. The Rust rating target remains open. The Go rating target remains open. The Java rating target remains open.
