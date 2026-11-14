# 1870. Zinium 2

[Timus 1870](https://acm.timus.ru/problem.aspx?space=1&num=1870) · difficulty 714 · constructive

Original problem by Igor Chevdar (prepared by Eugene Kurpilyanskiy), from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Place n queens on an n × n toroidal chessboard (the top row is glued to
the bottom one and the left column to the right one, so diagonals wrap
around) so that no two queens attack each other, or say that this is
impossible.

## Input

n (4 ≤ n ≤ 10⁵).

## Output

"Yes" and, for x = 1, …, n, the row of the queen in column x; or "No".
Any valid placement is accepted.

## Examples

### Example 1

Input:

```
5
```

Output:

```
Yes
2 4 1 3 5
```

### Example 2

Input:

```
8
```

Output:

```
No
```

## Solution

Number rows and columns from 0. On the torus two queens attack each
other when they share x, y, x + y mod n or x − y mod n, so each of
these must take every value once.

If n is prime to 6, put the queen of column i on row 2i mod n. The rows
2i, the sums 3i and the differences −i are all different because 2 and
3 are invertible modulo n.

Otherwise there is no placement. If n is even, add up x + y over all
queens. Since the sums take every residue once, the total is
n(n − 1)/2 ≡ n/2 (mod n). But it is also Σx + Σy = n(n − 1) ≡ 0, a
contradiction. If 3 divides n (and n is odd), add up the squares
instead. Since (x + y)² + (x − y)² = 2x² + 2y², the sum of squares S of
all residues satisfies S + S ≡ 2S + 2S, so 2S ≡ 0 (mod n). With
S = (n − 1)n(2n − 1)/6 this needs 3 to divide (n − 1)(2n − 1), but
both factors are 2 modulo 3. `O(n)`.

For the first example the rows are 1, 3, 5, 2, 4 counting from 1,
another valid answer.

Pitfalls:

- the answer depends on n modulo 6, not on n being prime: 35 has a
  placement, 9 and 8 do not;
- the step 2 is the smallest that works; step 1 puts all queens on one
  diagonal;
- the output has up to 10⁵ numbers. A buffer can write them in batches.

The placements pass a checker for every n from 4 to 400 and for the
largest n, and the "No" answers agree with an independent accepted
implementation.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321969 · Java 1.8 №11321970 · Go 1.14 x64 №11322301 · Python 3.12 x64 №11322302 · Rust 1.75 x64 №11322303.

## Optimized solutions

The optimized versions print the odd row numbers and then the even ones using a small output buffer. This is the order of 2i modulo n (with one-based output) and requires no array of all placements.

Rust 1.75 x64, submission 11322002. Time 0.031 → 0.015 s, memory 5812 → 200 KB.

Python 3.12 x64, submission 11322003. Time 0.093 → 0.109 s, memory 6424 → 824 KB.

Go 1.14 x64, submission 11322004. Time 0.031 → 0.031 s, memory 1632 → 924 KB.

Java 1.8, submission 11322005. Time 0.109 → 0.093 s, memory 5368 → 504 KB.

G++ 13.2 x64, submission 11322006. Time 0.015 → 0.015 s, memory 1504 → 112 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1870_constructive.cpp](1870_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 1504 KB | 11321969 |
| [1870_constructive.go](1870_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1632 KB | 11322301 |
| [1870_constructive.java](1870_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.109 s | 5368 KB | 11321970 |
| [1870_constructive.py](1870_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.093 s | 6424 KB | 11322302 |
| [1870_constructive.rs](1870_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 5812 KB | 11322303 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1870_constructive_optimized.rs](1870_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(n) | AC | 0.015 s | 200 KB | 11322002 |
| [1870_constructive_optimized.py](1870_constructive_optimized.py) \* | Python 3.12 x64 | constructive | O(n) | AC | 0.109 s | 824 KB | 11322003 |
| [1870_constructive_optimized.go](1870_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 924 KB | 11322004 |
| [1870_constructive_optimized.java](1870_constructive_optimized.java) \* | Java 1.8 | constructive | O(n) | AC | 0.093 s | 504 KB | 11322005 |
| [1870_constructive_optimized.cpp](1870_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 112 KB | 11322006 |

\* The marked versions have room to improve in the ratings.
