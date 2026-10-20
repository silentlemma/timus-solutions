# 2134. Stamping a document until k cells are painted twice

[Timus 2134](https://acm.timus.ru/problem.aspx?space=1&num=2134) · difficulty 1714 · simulation

Original problem by Kirill Borozdin, from the “Later is better than never” contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A stamp with an a × b pattern of black cells is pressed q times on an
n × m document at given positions. A cell painted more than once is
repainted. Find the first stamp after which at least k cells are
repainted, or print the final document if that never happens. The
limits are 1 second and 256 MB.

## Input

n, m and k, 1 ≤ n, m ≤ 1000, 1 ≤ k ≤ 100, then a and b, the pattern,
then q, 1 ≤ q ≤ 10⁵, and the q positions.

## Output

"Wasted after stamp #s", or the document as n lines of "." and "#".

## Examples

### Example 1

Input:

```
4 3 2
3 2
#.
.#
..
2
1 1
2 2
```

Output:

```
#..
.#.
..#
...
```

### Example 2

Input:

```
4 3 1
3 2
#.
.#
..
2
1 1
2 2
```

Output:

```
Wasted after stamp #2
```

## Solution

Simply paint every black cell of every stamp, keeping for each document
cell whether it was painted 0, 1 or at least 2 times and the number of
repainted cells; stop as soon as that number reaches k. This is fast
enough because of a counting argument.

While the document is still legible, fewer than k cells are in the
state "at least 2". So every stamp touches at most k − 1 such cells,
and each of its other cells either goes from 0 to 1, which happens at
most nm times in total, or from 1 to 2, which happens fewer than k
times. Hence all stamps together touch at most q(k − 1) + nm + k cells.
A position used for the third time can be skipped outright: all its
cells are already repainted. The work is O(ab + nm + qk), about 10⁷
steps.

In the examples both stamps paint the cell (2, 2). With k = 2 one
repainted cell is allowed and the document is printed; with k = 1 it is
wasted after the second stamp.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2134_simulation.cpp](2134_simulation.cpp) | G++ 13.2 x64 | simulation | O(ab + nm + qk) | AC | 0.046 s | 6728 KB |
| [2134_simulation.go](2134_simulation.go) | Go 1.14 x64 | simulation | O(ab + nm + qk) | AC | 0.078 s | 34136 KB |
| [2134_simulation.java](2134_simulation.java) | Java 1.8 | simulation | O(ab + nm + qk) | AC | 0.125 s | 9176 KB |
| [2134_simulation.py](2134_simulation.py) | Python 3.12 x64 | simulation | O(ab + nm + qk) | AC | 0.421 s | 49268 KB |
| [2134_simulation.rs](2134_simulation.rs) | Rust 1.75 x64 | simulation | O(ab + nm + qk) | AC | 0.031 s | 11968 KB |
