# 1280. Topological sorting

[Timus 1280](https://acm.timus.ru/problem.aspx?space=1&num=1280) · difficulty 140 · graphs

Original problem by Sergey Volchenkov, Vladimir Pinaev and Michael Kopachev, from the Central Russia regional quarterfinal of the ACM ICPC 2003–2004, Rybinsk, October 15–16, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are 1 ≤ N ≤ 1000 subjects and 0 ≤ M ≤ 100 000 rules "s u":
subject s must be studied before subject u. Is the given order of all N
subjects consistent with every rule?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, the M rules, then the order of the N subjects. Subjects are
numbered from 1 to N.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
5 6
1 3
1 4
3 5
5 2
4 2
1 2
1 3 4 5 2
```

Output:

```
YES
```

### Example 2

Input:

```
5 6
1 3
1 4
3 5
5 2
4 2
1 2
1 2 4 5 3
```

Output:

```
NO
```

## Solution

There is no need to sort anything: record the place of each subject in
the given order and check that every rule goes forward, that is, s
comes before u. If the rules contain a cycle, some rule on it must go
backwards in any order, so the check already says `NO`, as the
statement wants. `O(N + M)`.

Pitfalls:

- one violated rule is enough for `NO`; the plan in test 02 violates
  three rules: 3 → 5, 5 → 2, and 4 → 2;
- a rule may lead from a subject to itself, which no order satisfies
  (test 04);
- rules may repeat (test 07);
- with no rules every order is right (test 06).

## Optimized solutions

The optimized C++ solution parses the numbers by hand from a 4 KB buffer
instead of `scanf` and keeps the rules as a bit matrix, one
`std::bitset` row per subject, instead of two `int` arrays of up to
100 000 rules. For `N ≤ 1000` the matrix takes about 125 KB, and
repeated rules share one bit. The check then tests all `N²` pairs of
subjects, at most a million bits: {1280_graphs_optimized.cpp}.

The optimized Go solution parses the numbers byte by byte from the
`bufio.Reader` instead of `fmt.Fscan` and keeps the ends of the rules in
two `uint16` slices, which hold subject numbers up to 1000, instead of
`int` slices four times as large: {1280_graphs_optimized.go}.

The optimized Java solution parses the numbers by hand from a 4 KB
buffer instead of `StreamTokenizer` and keeps the rules as a bit matrix
in a `long` array, `N` rows of `⌈N / 64⌉` words, about 125 KB for
`N ≤ 1000`, instead of two `int` arrays of up to 100 000 rules. The
check then tests all `N²` pairs of subjects:
{1280_graphs_optimized.java}.

The optimized Python solution reads the input in 8 KB chunks and
converts the tokens chunk by chunk instead of splitting the whole input
at once, and keeps the ends of the rules in an `array("H")` of unsigned
16-bit numbers, which hold subject numbers up to 1000, instead of a list
of tuples: {1280_graphs_optimized.py}.

The optimized Rust solution parses the numbers by hand from a 4 KB
buffer instead of reading the whole input into a `String`, and keeps the
rules as `(u16, u16)` pairs, which hold subject numbers up to 1000,
instead of `(usize, usize)` pairs four times as large:
{1280_graphs_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1280_graphs_optimized.cpp`: time reduction +86.24%; memory reduction
  +76.23%; base: `1280_graphs.cpp`.

- `1280_graphs_optimized.go`: time reduction +75.20%; memory reduction
  +61.24%; base: `1280_graphs.go`.

- `1280_graphs_optimized.java`: time reduction +0.00%; memory reduction
  +57.10%; base: `1280_graphs.java`.

- `1280_graphs_optimized.py`: time reduction +0.00%; memory reduction
  +92.63%; base: `1280_graphs.py`.

- `1280_graphs_optimized.rs`: time reduction +0.00%; memory reduction
  +84.16%; base: `1280_graphs.rs`.

## Language notes

- All languages store the places in an array and check every rule
  against them.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1280_graphs.cpp](1280_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.109 s | 976 KB | 11284403 |
| [1280_graphs.go](1280_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.125 s | 3416 KB | 11284414 |
| [1280_graphs.java](1280_graphs.java) | Java 1.8 | graphs | O(N + M) | AC | 0.140 s | 1324 KB | 11284421 |
| [1280_graphs.py](1280_graphs.py) | Python 3.12 x64 | graphs | O(N + M) | AC | 0.171 s | 24372 KB | 11284417 |
| [1280_graphs.rs](1280_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.015 s | 3688 KB | 11284425 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1280_graphs_optimized.cpp](1280_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(N² + M) | AC | 0.015 s | 232 KB | 11304469 |
| [1280_graphs_optimized.go](1280_graphs_optimized.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.031 s | 1324 KB | 11304470 |
| [1280_graphs_optimized.java](1280_graphs_optimized.java) \* | Java 1.8 | graphs | O(N² + M) | AC | 0.140 s | 568 KB | 11304471 |
| [1280_graphs_optimized.py](1280_graphs_optimized.py) \* | Python 3.12 x64 | graphs | O(N + M) | AC | 0.171 s | 1796 KB | 11304472 |
| [1280_graphs_optimized.rs](1280_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.015 s | 584 KB | 11304473 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
