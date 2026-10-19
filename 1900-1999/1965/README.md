# 1965. Two Monotone Subsequences

[Timus 1965](https://acm.timus.ru/problem.aspx?space=1&num=1965) · difficulty 1004 · dp

Original problem from Open Ural FU Personal Contest 2013 | by Sergey Pupyrev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Partition a permutation of 1,…,n into two nonempty subsequences, each
strictly monotone. Each subsequence may independently increase or decrease;
both may have the same direction. Preserve the relative input order inside
each group, and use every value exactly once. Output any valid partition,
or report that none exists. Limits: 1 second, 64 MB.

## Input

n, with 3≤n≤100,000, followed by n distinct integers between 1 and n.

## Output

If possible, output two group sizes on the first line, each between 1
and n−1. The second and third lines contain the respective groups in input
order. Any valid answer is accepted. Otherwise output the word `Fail`.
A singleton group is monotone in either direction.

## Checking

A checker verifies that the two groups are nonempty, cover every value
once, keep the input order and are each strictly monotone; any valid
split is accepted. `Fail` must match the stored answer.

## Examples

```
8
8 7 1 6 4 3 5 2
```

```
3 5
1 4 5
8 7 6 3 2
```

```
6
3 5 1 2 6 4
```

```
3 3
3 5 6
1 2 4
```

```
6
3 5 2 1 6 4
```

```
Fail
```

## Solution

In the first sample, 1,4,5 increases and 8,7,6,3,2 decreases; both keep
their input order and cover all values. The second sample needs no
opposite-direction assumption: 3,5,6 and 1,2,4 both increase. For the
third sample every assignment fails; the two-state process below rejects
all direction pairs.

Try the four fixed direction pairs (+,+), (−,−), (+,−), (−,+), where +
means increasing. For one pair, process values from left to right. The
last processed value v belongs to exactly one group, called the owner.
Its group's last value is already v. Therefore a state only needs its
owner and the last value of the other group.

For each of the two owners, keep the best other-group last value: smaller
is better if that other group increases, larger if it decreases. A better
last value permits every future append permitted by a worse one. The
owner's last value is identical in these states, so the worse state can
never be needed. Keep a predecessor owner for reconstruction.

For the next value x there are two transitions. Append to the same owner
if x follows v in that group's direction; the other last stays unchanged.
Or append to the other group if x follows its stored last; the new owner
is that group and the new other last is v. Among transitions with the
same new owner, retain only the dominant last value. If neither owner
is reachable, this direction pair is impossible.

Initially the first value may belong to either owner. Represent an empty
increasing group by last value 0, and an empty decreasing group by n+1;
every input value can follow these sentinels. At the end, choose a reachable
owner and trace predecessor owners backward. Reconstruct each group in
forward input order.

Empty groups do not break the dominance argument. If reconstruction leaves
one group empty, the entire permutation is monotone in the other group.
Move its last element into the empty group: the original group still has
n−1≥2 elements and the singleton is monotone in either requested direction.
This produces two nonempty groups without losing validity.

Inductively, the retained states represent all possible continuations for
each fixed pair. The transitions cover both possible owners of every new
element, and dominance discards only weaker continuations. Thus a failed
pair has no valid partition, and failure of all four pairs proves `Fail`.

`O(n)` time and `O(n)` space. There are four direction pairs, two states
per position, and a constant number of transitions. Predecessor owners
require two byte arrays per attempt; groups and input also use linear space.

Both groups may increase or both decrease. Greedily committing each value
to one group loses possibilities; keep both owners. Dominance is measured
in the other group's direction. Save the predecessor of the winning
transition, not just its tail value. Output values rather than indices,
preserve input order, and repair an empty group only after reconstruction.
Do not compare a candidate partition token-for-token with one sample answer.

## Language notes

Python 3.12 uses None for an unreachable state and bytearray predecessors.
C++/Go/Java/Rust use −1 for unreachable tails, since valid tails and empty
sentinels are nonnegative. C++ and Go use byte arrays, Java byte[][] and
Rust Vec<u8>. Java uses buffered integer input and StringBuilder output.
Rust indices use usize and signed tail values use i32. No recursion is used.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1965_dp.cpp](1965_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.031 s | 1880 KB |
| [1965_dp.go](1965_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.109 s | 8772 KB |
| [1965_dp.java](1965_dp.java) | Java 1.8 | dp | O(n) | AC | 0.140 s | 6604 KB |
| [1965_dp.py](1965_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.265 s | 11748 KB |
| [1965_dp.rs](1965_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.031 s | 3516 KB |
