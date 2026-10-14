# 1557. Network Attack

[Timus 1557](https://acm.timus.ru/problem.aspx?space=1&num=1557) · difficulty 1699 · graphs

Original problem from the Novosibirsk SU Contest at the Petrozavodsk Training Camp, September 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A connected network has N servers (N ≤ 2000) and M channels
(M ≤ 100000); channels may join a server to itself, and several may join
the same pair. Two hackers each destroy one channel, two different
channels in all. Count the unordered pairs of channels whose removal
leaves two servers with no connection between them.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N and M, then the two servers of each channel.

## Output

The number of pairs.

## Examples

### Example 1

Input:

```
3 3
1 2
2 3
3 1
```

Output:

```
3
```

## Solution

Take a spanning tree. Every channel outside the tree closes one cycle,
the tree path between its ends plus itself. Removing a set of channels
disconnects the network exactly when some tree channel is removed while
every cycle through it loses a channel too.

Give every channel outside the tree a random 64-bit label, and give
each tree channel the XOR of the labels of the cycles through it. Two
channels form a cut exactly when they lie on the same set of cycles,
that is, when their labels are equal; a bridge lies on no cycle and gets
label 0. The XOR for the tree channel above a server is the XOR of all
the outside labels with one end in its subtree, so one pass from the
leaves up fills all labels.

A bridge cuts the network together with any other channel, which gives
C(M, 2) − C(M − B, 2) pairs for B bridges. The other channels add
C(c, 2) for every group of c equal non-zero labels. A self-loop gets a
label of its own and never takes part in a cut. The labels come from
splitmix64 applied to the channel number, so the run is deterministic,
and two labels collide by chance with probability below 10⁻⁹. All runs
take O(N + M log M) time. The results were checked against a brute force
over all pairs on 400 small networks.

Pitfalls:

- the pairs are unordered: in the example the three pairs of the
  triangle give 3, not 6;
- with a single channel there is no pair at all (test 08);
- C(M, 2) is about 5·10⁹ and needs 64 bits, although the answer itself
  is at most about 2·10⁸ (test gen3);
- two channels between the same servers do not form a cut while a third
  path joins them (test 07).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1557_graphs.cpp](1557_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M log M) | AC | 0.093 s | 3968 KB |
| [1557_graphs.go](1557_graphs.go) | Go 1.14 x64 | graphs | O(N + M log M) | AC | 0.140 s | 13124 KB |
| [1557_graphs.java](1557_graphs.java) | Java 1.8 | graphs | O(N + M log M) | AC | 0.109 s | 3800 KB |
| [1557_graphs.py](1557_graphs.py) | Python 3.12 x64 | graphs | O(N + M log M) | AC | 0.390 s | 50944 KB |
| [1557_graphs.rs](1557_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M log M) | AC | 0.015 s | 9060 KB |
