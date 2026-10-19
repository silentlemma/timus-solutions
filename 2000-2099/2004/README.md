# 2004. A Short String Containing Every Binary Word

[Timus 2004](https://acm.timus.ru/problem.aspx?space=1&num=2004) · difficulty 762 · graphs, greedy

Original problem by Ilya Kuchumov, from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For every integer from 0 to `2^n−1`, take its exactly `n`-bit
representation, including leading zeros. Split it into an upper part of
`ceil(n/2)` bits and a lower part of `floor(n/2)` bits. Move the lower
part before the upper part, preserving the order within each. Find a
shortest binary string containing all resulting words as contiguous
substrings. Any shortest answer is allowed.

## Input

One integer `n`, `1 ≤ n ≤ 20`. Time limit 0.5 seconds, memory 64 MB.

## Output

One binary string of minimum possible length. Leading zeros are significant.

## Checking

A checker verifies that the answer is a binary string of length 2ⁿ + n −
1 containing every word of length n; any such string is accepted.

## Examples

```
1
```

```
10
```

For `n=1`, both words 0 and 1 must occur. The sample `10` and our output
`01` are both shortest.

## Solution

Swapping two fixed bit blocks is invertible: split the result after its
first `floor(n/2)` bits and swap back. Hence the transformed words are
precisely all `2^n` binary words, for odd and even `n` alike. The
function need not be evaluated.

A string of length `L` has only `L−n+1` windows of length `n`. Covering
`2^n` distinct words therefore requires `L≥2^n+n−1`. We construct an
answer attaining this bound.

Consider a directed graph whose vertices are `(n−1)`-bit words. Each
`n`-bit word is an edge from its prefix to its suffix, labelled by its
last bit. Each vertex has two incoming and two outgoing edges. For `n=1`
there is one vertex, the empty word, with two loops. An Euler tour
spells all words once by overlapping consecutive edges.

Start with `n` zero characters, using the all-zero loop at vertex zero.
Then repeatedly append 1 if the resulting `n`-bit word is unused;
otherwise append 0. Store used words in a byte array, and maintain the
current window by shifting and masking. Append exactly `2^n−1` more
characters.

Why can this greedy walk finish every edge without backtracking? At any
vertex other than the start, a walk cannot get stuck: used incoming
edges exceed used outgoing edges by one, while the total in-degree and
out-degree are equal. Thus an early stop would close a tour at zero. The
unused edges would then be balanced at every vertex. At any nonzero
vertex with unused outgoing edges, its zero edge must remain unused
because the one edge is preferred. Following that zero edge leads to
another vertex with an unused outgoing edge, by balance. Repeatedly
appending zero reaches vertex zero after at most `n−1` steps. This
contradicts being stuck there. The initial zero loop is the only
exception to the edge preference, and lies at that start vertex.
Therefore every edge is used, the constructed windows are all distinct,
and the lower bound is attained.

Time `O(2^n+n)` and memory `O(2^n+n)`, including the output and visited
array. The maximum output has 1,048,595 bits. No list of transformed
words or recursion stack is required.

Produce a linear string, so the overlapping prefix still contributes
`n−1` characters beyond a cycle of `2^n` edges. Mark the zero word used
before the greedy loop. Count positions in the visited array by the last
`n` bits, with mask `2^n−1`. Treat `n=1` normally. Do not compare a
valid answer to one specific expected string.

## Language notes

C++ reserves a string, Go uses `strings.Builder`, Java fills a character
array, Rust fills a byte vector, and Python appends to a byte array and
writes bytes directly. All indices and shifts fit 32-bit signed integers
at `n≤20`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2004_graphs_greedy.cpp](2004_graphs_greedy.cpp) | G++ 13.2 x64 | graphs, greedy | O(2^n + n) | AC | 0.015 s | 1964 KB |
| [2004_graphs_greedy.go](2004_graphs_greedy.go) | Go 1.14 x64 | graphs, greedy | O(2^n + n) | AC | 0.031 s | 4352 KB |
| [2004_graphs_greedy.java](2004_graphs_greedy.java) | Java 1.8 | graphs, greedy | O(2^n + n) | AC | 0.109 s | 6180 KB |
| [2004_graphs_greedy.py](2004_graphs_greedy.py) | Python 3.12 x64 | graphs, greedy | O(2^n + n) | AC | 0.375 s | 5736 KB |
| [2004_graphs_greedy.rs](2004_graphs_greedy.rs) | Rust 1.75 x64 | graphs, greedy | O(2^n + n) | AC | 0.031 s | 2096 KB |
