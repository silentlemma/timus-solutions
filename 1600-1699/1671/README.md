# 1671. Anansi's Cobweb

[Timus 1671](https://acm.timus.ru/problem.aspx?space=1&num=1671) · difficulty 105 · dsu

Original problem by Dmitry Poletaev (prepared by Alex Samsonov), from the Ural SU Contest at the Petrozavodsk Summer Training Camp, August 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cobweb has N knots and M threads between pairs of knots. Q of the
threads are cut one by one in a given order. After each cut, print how
many pieces (connected parts) the web falls into.

## Input

N and M (2 ≤ N ≤ 100000, 1 ≤ M ≤ 100000), the M threads as pairs of
different knots numbered from 1 to N, then Q (1 ≤ Q ≤ M) and the
numbers of the threads to cut, all different; the threads are numbered
from 1 to M in input order.

## Output

The Q numbers of pieces, separated by spaces.

## Examples

### Example 1

Input:

```
4 4
1 2
2 3
1 3
3 4
3
2 4 3
```

Output:

```
1 2 3
```

### Example 2

Input:

```
3 1
1 2
1
1
```

Output:

```
3
```

## Solution

Cutting is hard to follow, but joining is easy with a disjoint set
union, so the process runs backwards. Start from the web as it is after
all the cuts: join every thread that is never cut. Then go through the
cuts from the last to the first: the current number of pieces is the
answer after that cut, and then the thread goes back in. Each join that
connects two different sets lowers the count by one. With path
compression this is `O((N + M) log N)`.

Pitfalls:

- the same two knots may be joined by several threads, and cutting one
  of them changes nothing (test 03);
- the answer after a cut is the count before putting that thread back.

The answers match a recount of the pieces by search after every cut on
200 small random webs.

## Optimized solutions

The optimized C++ solution parses the numbers by hand from 8 KB blocks
read with `fread` instead of calling `scanf` for each, joins by size,
with a root holding minus the size of its set, so that the trees stay
shallow, writes each answer over the cut it belongs to once that cut is
processed instead of keeping a second array, and prints the answers with
`printf` instead of collecting them in a string:
{1671_dsu_optimized.cpp}.

The optimized Go solution parses the numbers byte by byte from a 64 KB
buffered reader and prints them with `strconv` through a 64 KB writer,
instead of `fmt.Fscan` and `fmt.Fprint`; the union-find is the same:
{1671_dsu_optimized.go}.

The optimized Java solution parses the numbers by hand from 8 KB blocks
instead of `StreamTokenizer`, joins by size, with a root holding minus
the size of its set, so that the trees stay shallow, writes each answer
over the cut it belongs to once that cut is processed instead of keeping
a second array, and prints the digits through an 8 KB byte buffer
instead of collecting the output in a `StringBuilder`:
{1671_dsu_optimized.java}.

The optimized Python solution reads the input line by line and keeps the
ends of the threads and the cuts in arrays of 32-bit unsigned integers,
which hold them since they are at most 100000, instead of keeping every
token of the input as a byte string; it joins by size, with a root
holding minus the size of its set, so that the trees stay shallow, and
writes each answer over the cut it belongs to once that cut is processed
instead of building a second list: {1671_dsu_optimized.py}.

The optimized Rust solution parses the numbers straight from the input
bytes instead of collecting them all into a vector first, keeps the
threads as pairs of `u32` and the parents as `i32`, which hold them
since N and M are at most 100000, instead of `usize`, joins by size,
with a root holding minus the size of its set, so that the trees stay
shallow, writes each answer over the cut it belongs to once that cut is
processed, and prints through a `BufWriter` instead of joining a vector
of strings: {1671_dsu_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1671_dsu_optimized.cpp`: time reduction +83.42%; memory reduction
  +50.73%; base: `1671_dsu.cpp`.

- `1671_dsu_optimized.go`: time reduction +81.87%; memory reduction
  +21.86%; base: `1671_dsu.go`.

- `1671_dsu_optimized.java`: time reduction +10.71%; memory reduction
  +67.75%; base: `1671_dsu.java`.

- `1671_dsu_optimized.py`: time reduction -4.57%; memory reduction
  +70.52%; base: `1671_dsu.py`.

- `1671_dsu_optimized.rs`: time reduction +32.61%; memory reduction
  +65.71%; base: `1671_dsu.rs`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1671_dsu.cpp](1671_dsu.cpp) | G++ 13.2 x64 | dsu | O((N + M) log N) | AC | 0.187 s | 2736 KB | 11304020 |
| [1671_dsu.go](1671_dsu.go) | Go 1.14 x64 | dsu | O((N + M) log N) | AC | 0.171 s | 7576 KB | 11304036 |
| [1671_dsu.java](1671_dsu.java) | Java 1.8 | dsu | O((N + M) log N) | AC | 0.140 s | 6400 KB | 11304022 |
| [1671_dsu.py](1671_dsu.py) | Python 3.12 x64 | dsu | O((N + M) log N) | AC | 0.328 s | 35904 KB | 11304037 |
| [1671_dsu.rs](1671_dsu.rs) | Rust 1.75 x64 | dsu | O((N + M) log N) | AC | 0.046 s | 11480 KB | 11304038 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1671_dsu_optimized.cpp](1671_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O((N + M) log N) | AC | 0.031 s | 1348 KB | 11304032 |
| [1671_dsu_optimized.go](1671_dsu_optimized.go) | Go 1.14 x64 | dsu | O((N + M) log N) | AC | 0.031 s | 5920 KB | 11304261 |
| [1671_dsu_optimized.java](1671_dsu_optimized.java) \* | Java 1.8 | dsu | O((N + M) log N) | AC | 0.125 s | 2064 KB | 11304033 |
| [1671_dsu_optimized.py](1671_dsu_optimized.py) \* | Python 3.12 x64 | dsu | O((N + M) log N) | AC | 0.343 s | 10584 KB | 11304034 |
| [1671_dsu_optimized.rs](1671_dsu_optimized.rs) | Rust 1.75 x64 | dsu | O((N + M) log N) | AC | 0.031 s | 3936 KB | 11304035 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
