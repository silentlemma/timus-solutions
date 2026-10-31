# 1521. War Games 2

[Timus 1521](https://acm.timus.ru/problem.aspx?space=1&num=1521) · difficulty 121 · fenwick

Original problem by Ilya Grebnov, Nikita Rybak and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N soldiers (1 ≤ N ≤ 100000), numbered 1 to N, march in a circle. In
each round one soldier leaves: first soldier K (1 ≤ K ≤ N), then each
time the soldier K places ahead of the one who left last, counting only
those still marching. Print the soldiers in the order they leave.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and K.

## Output

The numbers of the soldiers in the order they leave.

## Examples

### Example 1

Input:

```
5 3
```

Output:

```
3 1 5 2 4
```

## Solution

Number the soldiers still marching 0, 1, … in circle order. If the last
one to leave had rank r among them, the next one has rank
(r + K − 1) mod (soldiers left), since the leaver's place is taken by
the soldier behind. A Fenwick tree holds 1 for each soldier still
marching; descending it by powers of two finds the soldier of a given
rank in `O(log N)`, and removing a soldier is a point update.
`O(N log N)` in all.

Pitfalls:

- deleting from a plain list costs `O(N)` per round, `O(N²)` in all,
  too slow for 100000 soldiers (gen1);
- K = 1 sends the soldiers out in order (test 03, gen5);
- K = N starts from the last soldier (test 04, gen4).

## Optimized solutions

The optimized C++ solution fills the tree directly, each node with the
length of its range, since every soldier marches at the start, and
removes the soldier during the search itself: the nodes where the
descent does not step forward are exactly the nodes whose range holds
the soldier found, so it decrements them on the way down instead of
making a second pass. It keeps the tree in a static array and prints
each number with `printf` as soon as it is found instead of collecting
the output in a string: {1521_fenwick_optimized.cpp}.

The optimized Go solution fills the tree directly, each node with the
length of its range, since every soldier marches at the start, and
removes the soldier during the search itself: the nodes where the
descent does not step forward are exactly the nodes whose range holds
the soldier found, so it decrements them on the way down instead of
making a second pass. The counts are `int32`, which holds them since
they are at most N ≤ 100000; N and K are read byte by byte instead of
`fmt.Scan`, and the numbers are formatted with `strconv.AppendInt` into
one reused buffer: {1521_fenwick_optimized.go}.

The optimized Java solution fills the tree directly, each node with the
length of its range, since every soldier marches at the start, and
removes the soldier during the search itself: the nodes where the
descent does not step forward are exactly the nodes whose range holds
the soldier found, so it decrements them on the way down instead of
making a second pass. It reads N and K digit by digit from `System.in`
instead of `BufferedReader` and `StringTokenizer`, and writes the digits
through a 4 KB `BufferedOutputStream` instead of collecting the output
in a `StringBuilder`: {1521_fenwick_optimized.java}.

The optimized Python solution fills the tree directly, each node with
the length of its range, since every soldier marches at the start, and
removes the soldier during the search itself: the nodes where the
descent does not step forward are exactly the nodes whose range holds
the soldier found, so it decrements them on the way down instead of
making a second pass. The tree is an `array` of 32-bit unsigned
integers, which holds the counts since they are at most N ≤ 100000,
instead of a list of Python integers, and the answers are printed in
batches of 1024 instead of being kept until the end:
{1521_fenwick_optimized.py}.

The optimized Rust solution fills the tree directly, each node with the
length of its range, since every soldier marches at the start, and
removes the soldier during the search itself: the nodes where the
descent does not step forward are exactly the nodes whose range holds
the soldier found, so it decrements them on the way down instead of
making a second pass. The counts are `u32`, which holds them since they
are at most N ≤ 100000, instead of `usize`, and the numbers go through a
`BufWriter` instead of being collected in a `String`:
{1521_fenwick_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1521_fenwick_optimized.cpp`: time reduction -48.39%; memory reduction
  +75.84%; base: `1521_fenwick.cpp`.

- `1521_fenwick_optimized.go`: time reduction +25.81%; memory reduction
  +46.34%; base: `1521_fenwick.go`.

- `1521_fenwick_optimized.java`: time reduction +26.90%; memory
  reduction +82.85%; base: `1521_fenwick.java`.

- `1521_fenwick_optimized.py`: time reduction +4.84%; memory reduction
  +88.83%; base: `1521_fenwick.py`.

- `1521_fenwick_optimized.rs`: time reduction +0.00%; memory reduction
  +74.68%; base: `1521_fenwick.rs`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1521_fenwick.cpp](1521_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(N log N) | AC | 0.031 s | 2136 KB | 11287371 |
| [1521_fenwick.go](1521_fenwick.go) | Go 1.14 x64 | fenwick | O(N log N) | AC | 0.062 s | 2460 KB | 11287372 |
| [1521_fenwick.java](1521_fenwick.java) | Java 1.8 | fenwick | O(N log N) | AC | 0.171 s | 5016 KB | 11287374 |
| [1521_fenwick.py](1521_fenwick.py) | Python 3.12 x64 | fenwick | O(N log N) | AC | 0.640 s | 12028 KB | 11287373 |
| [1521_fenwick.rs](1521_fenwick.rs) | Rust 1.75 x64 | fenwick | O(N log N) | AC | 0.031 s | 2512 KB | 11287375 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1521_fenwick_optimized.cpp](1521_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(N log N) | AC | 0.046 s | 516 KB | 11304369 |
| [1521_fenwick_optimized.go](1521_fenwick_optimized.go) | Go 1.14 x64 | fenwick | O(N log N) | AC | 0.046 s | 1320 KB | 11304370 |
| [1521_fenwick_optimized.java](1521_fenwick_optimized.java) \* | Java 1.8 | fenwick | O(N log N) | AC | 0.125 s | 860 KB | 11304371 |
| [1521_fenwick_optimized.py](1521_fenwick_optimized.py) \* | Python 3.12 x64 | fenwick | O(N log N) | AC | 0.609 s | 1344 KB | 11304372 |
| [1521_fenwick_optimized.rs](1521_fenwick_optimized.rs) | Rust 1.75 x64 | fenwick | O(N log N) | AC | 0.031 s | 636 KB | 11304373 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
