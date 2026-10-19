# 1829. Routing Tables

[Timus 1829](https://acm.timus.ru/problem.aspx?space=1&num=1829) · difficulty 2969 · sorting

Original problem by Igor Andrianov, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A routing table row holds a network d, a mask m (ones, then zeros) and
a gateway g. A packet to address a goes to the gateway of the matching
row (d and m = a and m) with the longest mask; for every address at
most one row is the longest match. Two tables are equivalent if every
address goes to the same gateway, or to none, under both. Decide
whether two given tables are equivalent.

## Input

The number of rows of the first table, its rows "d m g" with dotted
addresses, then the second table the same way. At most 65536 rows in
total.

## Output

"YES" if the tables are equivalent, "NO" otherwise.

## Examples

### Example 1

Input:

```
4
192.168.0.0 255.255.255.0 192.168.14.1
192.168.1.0 255.255.255.0 192.168.14.1
192.168.2.0 255.255.255.0 192.168.14.2
192.168.3.0 255.255.255.0 192.168.14.2
2
192.168.0.0 255.255.252.0 192.168.14.1
192.168.2.0 255.255.254.0 192.168.14.2
```

Output:

```
YES
```

### Example 2

Input:

```
1
192.168.0.0 255.255.255.0 192.168.14.1
2
192.168.0.0 255.255.255.0 192.168.14.1
172.16.0.0 255.255.0.0 172.16.0.1
```

Output:

```
NO
```

## Solution

A row covers the aligned block of addresses from d and m to
(d and m) or not m, and any two blocks are either nested or apart. So a
table is a laminar family of intervals on the line 0 … 2³² − 1, and an
address is routed by the innermost block holding it.

Turn each table into its routing function written as pieces: sort the
blocks by start, larger first on ties, and sweep with a stack of open
blocks. Before a block opens, the stretch since the last cut belongs to
the block on top of the stack; when the sweep passes the end of the top
block, its remaining stretch is emitted and it is popped. Pieces are
merged with the previous one when they touch and share a gateway, and
addresses outside every block are simply left out. Two tables are
equivalent exactly when these canonical lists are equal. Sorting
dominates: `O(n log n)`.

In the first example both tables give the pieces 192.168.0.0 …
192.168.1.255 to .14.1 and 192.168.2.0 … 192.168.3.255 to .14.2; in
the second the extra 172.16.0.0/16 piece makes them differ.

Pitfalls:

- the written network address may have bits outside its mask; only d
  and m matters;
- a row may repeat the gateway its enclosing block would give, so the
  tables must be compared after merging, not row by row;
- a default route 0.0.0.0 0.0.0.0 covers all 2³² addresses, so the
  bounds need 64-bit integers.

The answers agree with a direct longest-match check at every block
boundary on a few hundred small tables and with an independent accepted
implementation on the large ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1829_sorting.cpp](1829_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.171 s | 2632 KB |
| [1829_sorting.go](1829_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.156 s | 7464 KB |
| [1829_sorting.java](1829_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.250 s | 9296 KB |
| [1829_sorting.py](1829_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.515 s | 23092 KB |
| [1829_sorting.rs](1829_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.046 s | 6584 KB |
