# 1901. Space Elevators

[Timus 1901](https://acm.timus.ru/problem.aspx?space=1&num=1901) · difficulty 519 · greedy

Original problem by Alex Samsonov, from Ural Championship 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose an order for n positive weights. A two-seat elevator processes
the queue as follows. If its first two waiting values sum to at most
s, they share a trip. Otherwise the first goes alone and the second
remains at the front. A final value goes alone.

Maximize the number of trips and print a queue attaining it. Each
weight individually fits. The limits are 1 second and 64 MB.

## Input

The first line contains n and s, with 1 ≤ n ≤ 100 000 and
1 ≤ s ≤ 10⁹. The next line contains n weights vᵢ, with 1 ≤ vᵢ ≤ s.

## Output

Print the maximum trip count, then all n weights in a queue producing
that count. Preserve the input multiset, including repeated weights.
Any optimal queue is accepted.

## Checking

A checker verifies the multiset, simulates the boarding rules, and
checks that the stated trip count equals both the simulation and the
optimal objective. The order need not match the example.

## Examples

### Example 1

Input:

```
6 6
1 2 3 3 4 5
```

Output:

```
5
2 5 1 3 4 3
```

## Solution

Sort the weights and keep two ends. If minimum + maximum > s, append
minimum, maximum and remove both, adding two trips. The maximum is
also incompatible with the next remaining minimum, so both really
depart alone. Otherwise append the two smallest values as one trip.
An odd final value contributes one trip.

Here is an exchange proof for the second choice and the optimal bound
for the first. Call a sum greater than s incompatible. A queue with
q shared trips has n − q trips.

An optimal queue can be put in canonical form: its 2q smallest values
are paired at the beginning, and its remaining values follow a path
of incompatible neighbors. Moreover, all those 2q small values are
mutually compatible. To prove this, mark the second member of every
shared trip. Adjacent unmarked positions are incompatible. Move the
q smallest weights into the marked positions; unmarked weights only
increase, preserving their incompatible runs. Thus the largest n − q
weights have a cover of at most q + 1 incompatible paths.

A neighbor of the minimum in this graph is incompatible with every
other vertex. Deleting the minimum reduces a cover of several paths
by one: its universal neighbor joins another path, or its two universal
neighbors splice another path in its place. With one path, simply
bypass the minimum. Delete the q smallest unmarked values this way;
the largest n − 2q form one path, possibly empty.

Any 2r smallest values, r ≤ q, admit r compatible pairs: take r
original pairs and replace their sorted participants by the globally
smaller values. If the largest two among the first 2q were incompatible,
prefix them to the tail path and pair the first 2q − 2. This would use
only q − 1 shared trips, a contradiction. Hence the small prefix is
mutually compatible, proving the canonical form.

When minimum + maximum ≤ s, the minimum is compatible with everyone.
For at least two values, an all-singleton queue is therefore impossible,
so q ≥ 1. The canonical optimum starts with the two smallest paired.
Removing this complete trip leaves an optimal subproblem.

When minimum + maximum > s, prefixing them gives two single trips.
For the matching upper bound, consider a canonical optimum. If q > 0,
remove the minimum from its paired prefix and the maximum from its tail.
Keep q − 1 small pairs. Place the freed small value between the at-most-
two remaining tail paths. At most one new pair forms at these boundaries:
once that value pairs on one side it cannot pair again. The remainder
uses at most q pairs, losing at most two trips.

If q = 0, deleting the extremes from its incompatible path leaves at
most three pieces. The minimum's surviving neighbors are universal
endpoints: use them to join these pieces into one path. If the extremes
were adjacent, one universal endpoint suffices. Endpoint and empty
cases are immediate. The remainder still uses only single trips.
Thus both greedy choices preserve an optimum.

Sorting costs `O(n log n)` time, and the scan costs `O(n)`. Input and
the constructed queue use `O(n)` memory.

In the example the groups are [2], [5, 1], [3], [4], [3], giving five
trips. One shared trip is unavoidable, since weight 1 is compatible
with every other value.

Pitfalls:

- equality with s means a shared trip;
- after emitting two incompatible extremes, both must depart alone;
- the objective is the maximum, not the usual minimum number of trips;
- duplicate weights must appear with their original multiplicities.

The greedy agrees with a search over all 2 601 556 queues of 4 998 small
multisets, and with a separate DP on 5003 random cases.

## Language notes

All versions sort once and buffer the constructed queue. Python uses
CPython 3.12. Even the sum of two maximum input weights fits a signed
32-bit integer, while the trip count never exceeds n.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1901_greedy.cpp](1901_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.031 s | 1224 KB |
| [1901_greedy.go](1901_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.046 s | 5640 KB |
| [1901_greedy.java](1901_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.125 s | 6444 KB |
| [1901_greedy.py](1901_greedy.py) | Python 3.12 x64 | greedy | O(n log n) | AC | 0.281 s | 11644 KB |
| [1901_greedy.rs](1901_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.031 s | 2108 KB |
