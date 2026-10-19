# 1908. Click Costs in a Pruned Choice Tree

[Timus 1908](https://acm.timus.ru/problem.aspx?space=1&num=1908) · difficulty 2118 · dp, trees

Original problem by Denis Dublennykh, prepared by Alexander Fetisov, from Ural Championship 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each given string specifies a root-to-ending sequence of choices in a tree.
Explore every ending, restarting at the root for free after each ending.
A child option disappears as soon as every ending below it has been explored.
Choosing an available edge costs one click. Another button costs one click
and follows the current forced chain to the nearest branch or ending;
pressing it at a branch does nothing. Minimize the total clicks.
Limits: 1 second, 64 MB.

## Input

First n, 1≤n≤100 000, then n nonempty strings of lowercase Latin letters.
No string is a prefix of another. Their total length S is at most 100 000.

## Output

Print the minimum number of clicks required to explore all endings.

## Checking

One exact integer, checked token by token.

## Examples

```
3
aza
azc
b
```

```
4
```

## Solution

Build a trie. For every node v, calculate its leaf count N[v] and two costs:
A[v] starts each reading normally at v; B[v] supplies a free initial skip
from v on each reading, including restarts. This free skip stops at the
first current branch or ending; it does not apply after later choices.
A leaf has N=1 and A=B=0.

An optimal order can finish child subtrees one at a time. Take the child
containing the final ending and move all its earlier readings after the
other children, preserving relative order within every child. The other
children still see that last child available, so their entry costs cannot
increase. The moved readings can only gain earlier forced-chain skipping.
Now group the remaining children recursively.

For a non-last child c, this node remains a branch: each of its N[c]
readings pays one choice, then incurs the normal cost A[c]. For the last
child, normal entry pays one skip per reading, which also supplies the
child's initial skip: cost N[c]+B[c]. Supplied entry needs only B[c].
Consequently, with T=Σc(A[c]+N[c]),

```text
N[v] = sum N[c]
A[v] = T - max (A[c] - B[c])
B[v] = T - max (N[c] + A[c] - B[c])
```

Maximize separately: the best last child can differ between the two modes.
For example, the endings aa,ab,ac,ad,bxa,bxb have A[root]=11 and B[root]=8,
with different optimal last children. Prepending a common z makes the
actual answer 6+8=14. A unary node follows the same formulas and merges
arbitrarily long forced chains into one skip. Return A at the actual root.

New trie nodes always receive larger indices than their parents. Process
indices backward for an iterative postorder, avoiding stack overflow on
a 100 000-character word. Store children as linked sibling lists; a lookup
checks at most 26 labels. Construction and DP take O(S) time for this fixed
alphabet, with O(S) storage. Explicitly selecting every original choice
uses at most S clicks, so all DP counts and intermediate sums fit 32 bits.

In the sample, choose b, skip to the remaining a/z branch, choose c,
then skip the last forced path. These four clicks explore every ending.

## Language notes

All implementations use iterative insertion and reverse-index DP.
C++, Go 1.14 and Rust 1.75 store node records; Java 8 uses primitive arrays
and buffered input. Python 3.12 uses packed integer arrays and byte labels,
avoiding a dictionary or a 26-element list for every node. Strings and input
tokens contain only O(S) data. No recursion proportional to word length is used.

The answers agree with a BFS over the states of the interface on 978
cases, among them every prefix-free set of binary strings of length at
most three.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1908_dp_trees.cpp](1908_dp_trees.cpp) | G++ 13.2 x64 | dp, trees | O(S) | AC | 0.015 s | 2504 KB |
| [1908_dp_trees.go](1908_dp_trees.go) | Go 1.14 x64 | dp, trees | O(S) | AC | 0.031 s | 7092 KB |
| [1908_dp_trees.java](1908_dp_trees.java) | Java 1.8 | dp, trees | O(S) | AC | 0.093 s | 3480 KB |
| [1908_dp_trees.py](1908_dp_trees.py) | Python 3.12 x64 | dp, trees | O(S) | AC | 0.265 s | 3276 KB |
| [1908_dp_trees.rs](1908_dp_trees.rs) | Rust 1.75 x64 | dp, trees | O(S) | AC | 0.046 s | 4992 KB |
