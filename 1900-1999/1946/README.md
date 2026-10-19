# 1946. Counting Sorted Goal Tables

[Timus 1946](https://acm.timus.ru/problem.aspx?space=1&num=1946) · difficulty 1831 · dp

Original problem from Open Ural FU Personal Contest 2012 | by Alexander Ipatov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n players each meet every other player once. Each match distributes exactly
three goals between its two players: 3:0, 2:1, 1:2 or 0:3. Add every
player's goals and sort the totals in nonincreasing order. Count distinct
resulting lists, ignoring player names and how the same list was produced.
Limits: 1 second, 64 MB.

## Input

One integer n, 2≤n≤50.

## Output

The number of distinct lists, modulo 1000000007.

## Checking

Outputs are compared token by token.

## Examples

```
3
```

```
8
```

## Solution

Count reversed lists a₁≤…≤a_n instead. Write T=3n(n−1)/2 and
L(k)=3k(k−1)/2. A sorted nonnegative integer list is feasible precisely
when its total is T and each prefix of k values has sum at least L(k).
Every score is at most M=3(n−1).

Necessity: any k players have k(k−1)/2 internal matches whose three
goals stay inside the subset. Other matches add nonnegative goals.
The smallest k scores therefore satisfy the inequality.

For sufficiency, make a flow network. Source→match nodes have capacity 3;
each match→its two players has capacity T+1; player j→sink has capacity
a_j. Consider a cut of capacity at most T and let S be its source-side
players. A source-side match must have both endpoints in S, or it crosses
a T+1 arc. For fixed S the cheapest cut puts every internal match there.
Its capacity is 3·(C(n,2)−C(|S|,2))+Σ_{j∈S}a_j, at least T by the
smallest-prefix inequality. Thus every cut has capacity at least T.
An integral flow of value T exists. Every match distributes three integer
goals and every player receives the prescribed total, proving sufficiency.

Let dp_i[P][v] count nondecreasing prefixes of i scores, sum P and last
value v, satisfying all lower bounds. Start with dp₀[0][0]=1. The prefix
average cannot exceed the final average, so store only
L(i)≤P≤U(i)=floor(Ti/n). A new score x must not decrease the last score:

dp_(i+1)[P+x][x] = Σ_{v≤x} dp_i[P][v].

For each old sum, compute this prefix sum by scanning x. The predecessor
sum is uniquely fixed by the new sum and x, so write the cell rather
than adding to a cell from another old sum. Use two zeroed rolling layers.
The last-score dimension is 0..M.

Useful exact bounds for the scan are

first=max(0,L(i+1)−P,ceil(P/i) when i>0),
last=min(M,U(i+1)−P,floor((T−P)/(n−i))).

The old last score is at least the old prefix average; all n−i remaining
scores, including x, will be at least x. These bounds remove only prefixes
that cannot complete the sorted list. Initialize the running sum below
first, then add dp_i[P][x] before writing each cell. Finally sum all last
scores in dp_n[T]. Each sorted list follows one path, so no player-label
factor or match-result multiplicity is introduced.

O(n⁴) time and O(n³) space: n layers, O(n²) possible sums and O(n) last
scores. Prefix sums avoid another factor n. At n=50 the largest sum
interval has 938 rows and 148 score columns, 138824 cells per layer.

Count sorted score tables, not 4^(number of matches), labeled vectors or
only total-sum partitions. Prefix inequalities are essential. Scores may
tie and zero is allowed. Use integer floor/ceiling, include x=v in the
prefix sum, clear reused buffers, and avoid 32-bit prefix overflow.

## Language notes

Native versions reuse two flat 32-bit buffers, clearing the next one each
round; Python uses lists. Raw prefix and final row sums require 64 bits:
up to 148·(MOD−1)=148000000888. Reduce modulo when storing a cell;
Python integers handle the raw sums directly. All index products fit 32 bits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1946_dp.cpp](1946_dp.cpp) | G++ 13.2 x64 | dp | O(n^4) | AC | 0.015 s | 1468 KB |
| [1946_dp.go](1946_dp.go) | Go 1.14 x64 | dp | O(n^4) | AC | 0.031 s | 2216 KB |
| [1946_dp.java](1946_dp.java) | Java 1.8 | dp | O(n^4) | AC | 0.140 s | 1528 KB |
| [1946_dp.py](1946_dp.py) | Python 3.12 x64 | dp | O(n^4) | AC | 0.390 s | 5156 KB |
| [1946_dp.rs](1946_dp.rs) | Rust 1.75 x64 | dp | O(n^4) | AC | 0.046 s | 1316 KB |
