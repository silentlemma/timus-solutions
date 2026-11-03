# 1917. Safe Removal of Threshold Groups

[Timus 1917](https://acm.timus.ru/problem.aspx?space=1&num=1917) · difficulty 242 · greedy

Original problem by Denis Dublennykh, from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each coin has a positive resistance threshold. A spell of strength s
destroys all remaining coins with threshold at most s, and produces
energy s times the number newly destroyed. Each spell must produce
at most p energy. Maximize the number of coins destroyed; among ways
achieving that maximum, minimize the number of spells.
Limits: 1 second, 64 MB.

## Input

n,p with 1≤n≤1000 and 1≤p≤1 000 000 000, followed by n thresholds
1≤aᵢ≤1 000 000. Input order is arbitrary.

## Output

Two integers: the maximum removable count and its minimum spell count.
If nothing can be removed, print `0 0`.

## Checking

Compare the two integer tokens exactly, in that order.

## Examples

```
5 4
4 1 4 1 2
```

```
3 2
```

## Solution

Sort the thresholds and group equal values. A group with c coins and
threshold t cannot be split: weaker spells remove none of it, while the
first spell of strength at least t removes it all.

If ct>p, that whole group can never be removed, even alone. A stronger
spell or additional coins only increases the energy. It also blocks
every higher threshold, since a spell removing those would include this
group. Thus the maximum removable prefix ends before the first such group.
All earlier groups can be removed separately, proving the bound attainable.

For the feasible prefix, form consecutive batches greedily. Keep the
number active of coins in the current batch. Add the next whole group
if (active+c)t≤p. Otherwise finish the previous nonempty batch and start
one with the new group. Flush a nonempty final batch once. Each batch's
strength can be its largest threshold, which minimizes its energy.
Check ct>p before starting another batch, and never count an empty spell.

### Why the longest batch is optimal

The first greedy batch is the longest feasible prefix, because both its
count and last threshold increase as groups are added. In any optimal
partition, replace the first batch by this greedy one. Erase the extra
coins it removes from later batches and discard batches that become empty.
Every remaining batch has no more coins and no larger threshold, so
it remains safe. The number of spells cannot increase. Apply the same
argument to the remaining groups to prove minimum spell count.

Sorting costs `O(n log n)` time; grouping and batching are linear.
Memory is `O(n)` including the input/sorted copy.

The example first removes the two threshold-1 coins using strength 1,
then the threshold-2 coin using strength 2. The two threshold-4 coins
would already produce energy 8>4 together, so they block further progress.
The result is three coins in two spells.

Do not split equal thresholds or skip an unsafe low group to remove a
higher one. Compare energy with ≤p, include all newly destroyed coins,
and reset the batch only after counting the previous nonempty spell.
An unsafe next group does not invalidate a pending earlier batch.
The objectives are ordered: maximize coins before minimizing spells.

## Optimized solutions

The grouped greedy is unchanged: equal values form an inseparable group, and the first unsafe group cannot be bypassed. Java sorts the primitive input in place with iterative heapsort, avoiding sorting helper classes, copied arrays and scratch storage. Bounded byte input and ASCII output replace token and formatting objects. Products used to test a group are evaluated in a wide integer type; auxiliary sorting storage is constant.

- `1917_greedy_optimized.java`: 0.109 s / 380 KB; base `1917_greedy.java`: 0.125 s / 648 KB; relative change: time -12.8%, memory -41.4%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1917_greedy.cpp`; covering source `1917_greedy.cpp`; time/memory places 1/9, other-author entries 42/42.

- Go: preferred teaching base `1917_greedy.go`; covering source `1917_greedy.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1917_greedy.java`; covering source `1917_greedy_optimized.java`; time/memory places 2/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1917_greedy.py`; covering source `1917_greedy.py`; time/memory places 1/1, other-author entries 6/6.

- Rust: preferred teaching base `1917_greedy.rs`; covering source `1917_greedy.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1917_greedy.cpp](1917_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.015 s | 416 KB | 11291446 |
| [1917_greedy.go](1917_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.031 s | 1112 KB | 11291447 |
| [1917_greedy.java](1917_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.125 s | 648 KB | 11291452 |
| [1917_greedy.py](1917_greedy.py) | Python 3.12 x64 | greedy | O(n log n) | AC | 0.078 s | 572 KB | 11291451 |
| [1917_greedy.rs](1917_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.031 s | 240 KB | 11291453 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1917_greedy_optimized.java](1917_greedy_optimized.java) \* | Java 1.8 | greedy | O(N log N) | AC | 0.109 s | 380 KB | 11309400 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
