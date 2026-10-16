# 1799. Sasha and swag strings

[Timus 1799](https://acm.timus.ru/problem.aspx?space=1&num=1799) · difficulty 4373 · strings

Original problem by Oleksandr Kulkov, from the Petrozavodsk summer training camp 2015, Moscow IPT Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Build the trie of all suffixes of a string and merge every chain of
edges through nodes with a single child, without any end marker. On
each edge of this compressed tree count the distinct non-empty
substrings of its label, and sum these counts. Answer for each of
several strings.

## Input

n (1 ≤ n ≤ 10⁵), then n strings of lowercase letters with total length
at most 10⁵.

## Output

The sum for each string, one per line.

## Examples

### Example 1

Input:

```
3
umqra
umnik
merkurev
```

Output:

```
35
35
101
```

### Example 2

Input:

```
1
abaaa
```

Output:

```
17
```

## Solution

Equal subtrees of the suffix tree are merged in the suffix automaton,
so build the automaton instead and compress it the same way: keep the
start state and every state whose number of outgoing transitions is
not 1, and replace each path through the other states by one edge.
Like the tree, this drops the states where a suffix merely ends. An
edge from u to w that reads the label stands for as many tree edges as
there are paths from the start to u, counted in increasing order of
length. Each label is the substring s[l..r] that ends at the first
occurrence of w's strings, so what remains is the number of distinct
substrings of s[l..r] for every edge.

These range questions are answered offline, sorted by r. While the
prefix grows to r, count[p] is the number of distinct substrings of
s[0..r] whose last occurrence starts at p; then the answer for s[l..r]
is the sum of count[p] for p ≥ l. Appending a letter makes every
suffix of the prefix occur last at the new end: the states on the
suffix link path from the new prefix up to the start. They move as
whole chains of states that shared their previous last end. As in
link–cut trees, there are O(log n) such chains per letter on average.
For a chain the old starts form one range, so two Fenwick trees with
range add and range sum keep count. A segment tree over the Euler tour
of the suffix link tree gives the last end of a state, the latest
prefix in its subtree. `O(n log² n)` over all strings.

In the second example the compressed tree has the edges a, aa, baaa
and baaa, with 1, 2, 7 and 7 distinct substrings. The two baaa edges
come from one automaton edge reached by two paths from the start.

Pitfalls:

- the end of a suffix does not stop the compression: for aa the tree
  is a single edge aa;
- equal labels on different edges both count, which the path counts
  in the automaton take care of;
- the sum exceeds 32 bits;
- with up to 10⁵ strings, every array must be sized by its own string,
  not by the maximum.

The answers agree with an explicit compressed suffix trie on more than
a thousand short strings, and with an independent accepted
implementation on long random, periodic and Fibonacci strings. The
Python solution runs on PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1799_strings.cpp](1799_strings.cpp) | G++ 13.2 x64 | strings | O(n log^2 n) | AC | 0.250 s | 55692 KB |
| [1799_strings.go](1799_strings.go) | Go 1.14 x64 | strings | O(n log^2 n) | AC | 0.437 s | 94932 KB |
| [1799_strings.java](1799_strings.java) | Java 1.8 | strings | O(n log^2 n) | AC | 0.484 s | 50828 KB |
| [1799_strings.py](1799_strings.py) | PyPy 3.10 x64 | strings | O(n log^2 n) | AC | 1.218 s | 191384 KB |
| [1799_strings.rs](1799_strings.rs) | Rust 1.75 x64 | strings | O(n log^2 n) | AC | 0.312 s | 99724 KB |
