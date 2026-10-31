# 1982. Minimum forest reaching supplied vertices

[Timus 1982](https://acm.timus.ru/problem.aspx?space=1&num=1982) · difficulty 128 · graphs, greedy

Original problem by Mikhail Rubinchik, from the Open Ural FU Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A complete undirected graph has `n` vertices and a nonempty set of `k`
already supplied vertices. Choose edges of minimum total cost so that
every vertex can reach at least one supplied vertex. The supplied
vertices themselves may remain in different connected components.

All input values are integers, `1≤k≤n≤100`. The cost matrix is
symmetric, has zero diagonal, and has off-diagonal entries from 1 to
`10⁵`. Time limit: 0.5 seconds; memory limit: 64 MB.

## Input

Read `n k`, then `k` distinct supplied vertex numbers from 1 to `n`,
followed by the `n×n` cost matrix.

## Output

The minimum total cost, as one integer.

## Checking

Outputs are compared token by token.

## Examples

Input:

```
4 2
1 4
0 2 4 3
2 0 5 2
4 5 0 1
3 2 1 0
```

Output:

```
3
```

## Solution

Add an imaginary vertex joined to every supplied vertex by a zero-cost
edge. A minimum spanning tree in this augmented graph solves the
problem. Indeed, any feasible original network becomes connected after
adding these zero-cost edges, so an augmented spanning tree can cost no
more. Conversely, deleting the imaginary vertex from an augmented
spanning tree leaves components each containing a supplied vertex and
preserves all paid edge costs. The two optima are equal.

Implement dense Prim without explicitly storing the imaginary vertex.
Give every supplied vertex an initial key of zero and every other vertex
an infinite key. This is exactly the state after processing the
imaginary vertex. Repeatedly select the unused vertex with the smallest
key, add its key to the answer, and relax all unused vertices with the
selected matrix row.

The key of an unused vertex is the cheapest edge connecting it to the
processed part of the augmented tree. Prim's cut property makes each
selected edge safe. The initialization includes every supplied vertex,
so existing supply is accounted for everywhere. After all vertices are
processed, the accumulated cost is the augmented MST cost, hence the
required optimum.

Another useful view is a rooted forest. Positive-cost cycles can be
removed. If one tree contains several supplied vertices, remove an edge
separating two of them and keep both sides supplied. Thus an optimum can
have exactly `k` components and `n−k` paid edges. When `k=n`, its cost
is zero.

In the example, choose edge 1–2 of cost 2 and edge 3–4 of cost 1. Both
components contain a supplied vertex, and the total is 3.

There are `n` minimum-key scans and `n` row relaxations, each taking
`O(n)`, so time is `O(n²)`. Storing the input matrix takes `O(n²)`
memory; keys and flags take `O(n)` additional memory. The answer is at
most `(n−k)·10⁵≤9,900,000`.

Pitfalls:

- Initialize all supplied vertices with zero keys, regardless of their
  input order.
- An unsupplied vertex must not receive an initial zero key.
- New edges may connect unsupplied vertices to each other; those
  connections can reduce the total.
- The zero matrix diagonal is not a free connection to a different vertex.
- If all vertices are already supplied, no paid edge is needed.

## Optimized solutions

The optimized C++ solution parses the numbers by hand from a 4 KB buffer
that it refills with `fread`, instead of `iostream`, and keeps the costs
in a fixed 100 × 100 matrix of `int` instead of a vector of `long long`
rows. Since `n≤100` and every cost is at most `10⁵`, the keys and the
answer, at most 9,900,000, fit in `int` too, and `10⁵ + 1` serves as
infinity: {1982_greedy_optimized.cpp}.

The optimized Python solution takes the tokens line by line from a
generator over `sys.stdin.buffer` instead of splitting the whole input
at once, and stores each row of costs in an `array("I")` of 32-bit
unsigned numbers instead of a list of integer objects; costs up to `10⁵`
fit there. It also picks the vertex with the least key by a plain loop
instead of building a tuple for every candidate, and uses `10⁵ + 1` as
infinity: {1982_greedy_optimized.py}.

The optimized Rust solution parses the numbers from a 4 KB `BufReader`
that refills itself, instead of reading the whole input into a string,
and keeps the costs in one flat vector of `u32` instead of a vector of
`u64` rows. Since `n≤100` and every cost is at most `10⁵`, the keys and
the answer, at most 9,900,000, fit in `u32` too, and `10⁵ + 1` serves
as infinity: {1982_greedy_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1982_greedy_optimized.cpp`: time reduction +0.00%; memory reduction
  +76.61%; base: `1982_greedy.cpp`.

- `1982_greedy_optimized.py`: time reduction -19.23%; memory reduction
  +65.15%; base: `1982_greedy.py`.

- `1982_greedy_optimized.rs`: time reduction -106.67%; memory reduction
  +46.36%; base: `1982_greedy.rs`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1982_greedy.go](1982_greedy.go).

All five versions use the same dense Prim algorithm with integer costs.
The input matrix is stored completely. C++, Go, Java and Rust use wide
integer totals and keys; Python uses exact integers.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1982_greedy.cpp](1982_greedy.cpp) | G++ 13.2 x64 | greedy | O(n^2) | AC | 0.015 s | 496 KB | 11292336 |
| [1982_greedy.go](1982_greedy.go) | Go 1.14 x64 | greedy | O(n^2) | AC | 0.031 s | 1260 KB | 11292337 |
| [1982_greedy.java](1982_greedy.java) | Java 1.8 | greedy | O(n^2) | AC | 0.093 s | 552 KB | 11304431 |
| [1982_greedy.py](1982_greedy.py) | Python 3.12 x64 | greedy | O(n^2) | AC | 0.078 s | 1492 KB | 11292338 |
| [1982_greedy.rs](1982_greedy.rs) | Rust 1.75 x64 | greedy | O(n^2) | AC | 0.015 s | 440 KB | 11292340 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1982_greedy_optimized.cpp](1982_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n^2) | AC | 0.015 s | 116 KB | 11304427 |
| [1982_greedy_optimized.py](1982_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(n^2) | AC | 0.093 s | 520 KB | 11304429 |
| [1982_greedy_optimized.rs](1982_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(n^2) | AC | 0.031 s | 236 KB | 11304428 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
