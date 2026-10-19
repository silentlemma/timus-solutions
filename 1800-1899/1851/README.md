# 1851. GOV-internship

[Timus 1851](https://acm.timus.ru/problem.aspx?space=1&num=1851) · difficulty 1708 · flow

Original problem by Mikhail Rubinchik, from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The distance from a pattern p to a string s is the sum of the Hamming
distances from p to every substring of s of length |p|. Some characters
of s and p are erased; restore them so that this distance is as small as
possible.

## Input

The string s and the pattern p, each nonempty, at most 1000 characters
of "0", "1" and "?", with |p| ≤ |s|; "?" marks an erased character.

## Output

The least distance, then s and p with every "?" replaced by "0" or "1".
Any optimal restoration is accepted.

## Examples

### Example 1

Input:

```
00?
1?
```

Output:

```
2
000
10
```

## Solution

Character p[i] is compared with s[j] once for every window that puts
them together, which happens exactly when 0 ≤ j − i ≤ |s| − |p|, and
each such pair costs 1 when the characters differ. With each character
being 0 or 1, this is a cut problem: put every erased character into a
graph, the 1s on the source side and the 0s on the sink side.

- A pair of known characters adds its cost directly.
- A pair of an erased character and a known 1 costs 1 if the erased one
  becomes 0: an arc of capacity 1 from the source to it; a known 0 gives
  an arc of capacity 1 to the sink. All such arcs of one character merge
  into one, and if a character has both, the smaller of the two is paid
  anyway and subtracted from both.
- A pair of two erased characters costs 1 when they are split: an
  undirected edge of capacity 1.

The cost of a restoration is the fixed part plus the capacity of the
cut it defines, so the answer is the fixed part plus a maximum flow,
found here by Dinic's algorithm, and the source side of the residual
network after the last search gives the restoration. There are at most
2000 erased characters and |p|·(|s| − |p| + 1) ≤ 250 500 pairs.

In the example p[0] = 1 meets s[0] = 0 and s[1] = 0, which costs 2
whatever happens. p[1] meets s[1] = 0 and s[2]: restoring both erased
characters as 0 costs nothing more, so the answer is 2.

Pitfalls:

- p[i] meets only s[i] … s[i + |s| − |p|], not every character of s;
- a source and a sink arc on one node can be cancelled before the flow,
  which keeps the flow small;
- any minimum cut is a valid answer, so the output is checked by
  recomputing the distance.

The restorations pass a checker that recomputes the distance and
compares it with the optimum, found by trying every restoration on
three hundred short cases and by an independent accepted implementation
on the large ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1851_flow.cpp](1851_flow.cpp) | G++ 13.2 x64 | flow | O(V^2 E) | AC | 0.031 s | 7004 KB |
| [1851_flow.go](1851_flow.go) | Go 1.14 x64 | flow | O(V^2 E) | AC | 0.031 s | 26920 KB |
| [1851_flow.java](1851_flow.java) | Java 1.8 | flow | O(V^2 E) | AC | 0.125 s | 6448 KB |
| [1851_flow.py](1851_flow.py) | Python 3.12 x64 | flow | O(V^2 E) | AC | 0.640 s | 31084 KB |
| [1851_flow.rs](1851_flow.rs) | Rust 1.75 x64 | flow | O(V^2 E) | AC | 0.046 s | 13644 KB |
