# 2014. Credit Debt from Out-of-Order Transactions

[Timus 2014](https://acm.timus.ru/problem.aspx?space=1&num=2014) · difficulty 547 · segment_tree

Original problem by Nick Burlakov, prepared by Olga Soboleva, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Cash and credit balance initially equal zero. Income adds cash. Spending
uses available cash first; any shortfall decreases the credit balance.
Later income stays as cash and does not repay credit. Transaction
reports arrive in arbitrary order, but their timestamps specify when
they happened. After every received report, recompute the credit balance
using only the known reports in chronological order. Output zero or a
negative debt balance.

## Input

First `n`, `1 ≤ n ≤ 100,000`. Each next line contains a signed amount
`−c` or `+c`, `1 ≤ c ≤ 50,000`, followed by a timestamp `dd.MM hh:mm`.
All timestamps belong to one non-leap year and are distinct. Reports are
listed in receipt order. Time limit 1 second, memory 64 MB.

## Output

Print `n` integers, one per received report: the currently reconstructed
credit balance. Do not take its absolute value. Unique integer tokens
are compared token by token.

## Checking

Outputs are compared token by token.

## Examples

```
5
-1000 10.09 21:00
+500 09.09 14:00
+1000 02.09 00:00
-1000 17.09 21:00
+500 18.09 13:00
```

```
-1000
-500
0
-500
-500
```

The first expense alone creates balance −1000. Learning about earlier
income raises it to −500, then another earlier income removes that debt
entirely. The next expense produces −500. The final income happened
after the shortage, so it creates cash and leaves debt −500.

## Solution

For chronological cumulative amount `S`, let `D` be the smallest prefix
sum seen, including the empty prefix zero. Then credit balance is `D`
and cash is `S−D`. Initially both identities hold. Income raises `S` and
cash without lowering the minimum. An affordable expense leaves `D`
unchanged; an unaffordable one makes the new `S` smaller than `D`,
spends all cash and sets the new debt to that smaller value. This proves
the identities and reduces the answer to a minimum prefix sum.

Read all timestamps and sort the event indices chronologically. A
numeric key ordered by month, day, hour, minute suffices; sorting the
literal day-first date string does not. Assign each event a rank. Build
a segment tree on these ranks, initially all zero. Future reports
contribute zero: pre-reading their coordinates does not use their
amounts. Process events in receipt order, setting each leaf to its
signed amount and printing the root's minimum prefix.

A segment stores total sum `S` and minimum prefix `P`, with empty prefix
included. For left part A followed by right part B, combine as
`S=A.S+B.S` and `P=min(A.P,A.S+B.P)`. Every prefix either ends inside A
or contains all of A and a prefix of B, so this rule is exact. A leaf of
amount `v` stores `(v,min(0,v))`; an unseen or padded leaf stores
`(0,0)`. Induction over the tree proves each node's summary. Therefore
every root after an update describes exactly the currently known
chronological sequence, and the cash/debt identity proves the printed
balance correct.

Sorting and all updates take `O(n log n)` time; the iterative tree and
input arrays use `O(n)` space. Totals and debt can reach magnitude
`100,000·50,000=5,000,000,000`, so use 64-bit integers. An alternative
is lazy suffix addition over chronological prefix balances, maintaining
their global minimum.

## Language notes

Receipt order differs from transaction order. Later income does not
repay existing debt, while newly discovered earlier income can revise
it. Include prefix zero, keep the debt negative, and use month before
day in the key. Unique timestamps mean point assignment is sufficient.
Python uses a rank array and parallel tree lists; it runs under PyPy:
under CPython 3.12 it exceeds the time limit on the judge's test 15,
while PyPy 3.10 is accepted in 0.39 s. C++, Go, Java and Rust use wide
sums. Java sorts primitive packed key/index pairs in a long array,
avoiding boxed indices; the packing also uses 64-bit arithmetic. Parsers
handle both signs and the date/time separators.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2014_segment_tree.cpp](2014_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(n log n) | AC | 0.140 s | 6820 KB |
| [2014_segment_tree.go](2014_segment_tree.go) | Go 1.14 x64 | segment_tree | O(n log n) | AC | 0.093 s | 10724 KB |
| [2014_segment_tree.java](2014_segment_tree.java) | Java 1.8 | segment_tree | O(n log n) | AC | 0.250 s | 14608 KB |
| [2014_segment_tree.py](2014_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(n log n) | AC | 0.390 s | 21900 KB |
| [2014_segment_tree.rs](2014_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(n log n) | AC | 0.046 s | 10268 KB |
