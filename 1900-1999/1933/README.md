# 1933. An Odd Round-Robin Pairing Matrix

[Timus 1933](https://acm.timus.ru/problem.aspx?space=1&num=1933) · difficulty 408 · constructive

Original problem from Open Ural FU Championship 2012 | by Alexander Ipatov (prepared by Oleg Dolgorukov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are R=2n+1 participants and R rounds. Each round assigns n disjoint
pairs and one unpaired leader. No pair may repeat, and each participant
must be leader exactly once. Construct the schedule as a symmetric
matrix recording the round assigned to every pair.
Limits: 1 second, 64 MB.

## Input

One integer n, 1≤n≤100.

## Output

R lines of R integers in 0..R. The diagonal must be zero. Off-diagonal
entry (i,j) gives the round, numbered 1..R, when participants i and j pair.
There are nR=C(R,2) pairing slots in total; with no repeats, every pair
occurs exactly once. Any schedule satisfying all requirements is valid.

## Checking

checker.py reads R² integer tokens and verifies the diagonal, ranges,
symmetry, n disjoint pairs per round, exactly one leader in each round,
and distinct leaders across rounds. It accepts different valid schedules,
including different round labels and participant permutations.

## Examples

```
1
```

```
0 1 2
1 0 3
2 3 0
```

## Solution

Use zero-based row and column indices i,j. Put zero on the diagonal and
A[i][j]=((i+j+R−1) mod R)+1 elsewhere. The added R keeps the expression
nonnegative in every language. Symmetry and the label range are immediate.

Fix participant i. As j ranges over all R indices, the expression gives
each round label once. Excluding j=i therefore leaves distinct labels
for all real partners and omits only L_i=((2i+R−1) mod R)+1.
Because R is odd, multiplication by 2 is invertible modulo R. Hence
the omitted labels L_i are all distinct, even when R is composite.
Every round consequently has exactly one absent participant; everyone
else appears once, and symmetry groups them into n disjoint pairs.
The absent participant leads. Each participant misses one round and
the missing rounds differ, so leadership rotates exactly once to each.
Every unordered pair receives a single matrix label and cannot repeat.
This proves the entire construction.

O(n²) time, matching the number of output entries. These implementations
build the full matrix, using O(n²) space, including any output buffer.

Oddness is sufficient; do not require R to be prime. A single zero belongs
only on each diagonal position. Pair labels must agree in both directions.
One leader per round is not enough unless every participant leads once.
Round and participant relabelings can change every entry while remaining
valid, so compare schedules structurally rather than byte for byte.

## Language notes

R≤201, labels≤201 and i+j+R−1≤600, so ordinary integer arithmetic suffices.
C++ uses a vector matrix and unsynchronized streams. Go writes through
a buffered writer. Java and Rust build output strings; Python joins each
row before printing. Each program emits R rows without trailing spaces.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1933_constructive.cpp](1933_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.015 s | 492 KB |
| [1933_constructive.go](1933_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.031 s | 1836 KB |
| [1933_constructive.java](1933_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.125 s | 2592 KB |
| [1933_constructive.py](1933_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.109 s | 744 KB |
| [1933_constructive.rs](1933_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 640 KB |
