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

## Language notes

Python groups sorted values with `groupby`; the other ports scan runs of
equal values. Native ports use 64-bit energy products. Under the given
bounds a product is at most 1000·1 000 000=10⁹, but widening explicitly
keeps multiplication unambiguous. Java and Go use buffered input;
all ports output only the two requested counts.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1917_greedy.cpp](1917_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.015 s | 416 KB |
| [1917_greedy.go](1917_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.031 s | 1112 KB |
| [1917_greedy.java](1917_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.125 s | 648 KB |
| [1917_greedy.py](1917_greedy.py) | Python 3.12 x64 | greedy | O(n log n) | AC | 0.078 s | 572 KB |
| [1917_greedy.rs](1917_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.031 s | 240 KB |
