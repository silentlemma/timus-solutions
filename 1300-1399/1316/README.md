# 1316. Electronic Auction

[Timus 1316](https://acm.timus.ru/problem.aspx?space=1&num=1316) · difficulty 427 · fenwick

Original problem: idea by Pavel Atnashev, prepared by Pavel Atnashev and Pavel Egorov, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An exchange log has up to 100 000 operations:

- `BID X`: a buyer is ready to buy one piece at price X;
- `DEL X`: a bid at price X is withdrawn;
- `SALE X K`: K pieces are offered at price X, and the first K bids of
  X or more get one piece each; the rest are melted down.

A bid stays active after buying, until it is withdrawn. Prices are from
0.01 to 10 000.00 with at most two decimals, K ≤ 100 000, and the log
ends with `QUIT`. The exchange earns 0.01 per piece sold. Print its
total.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The log, one operation per line, ending with `QUIT`.

## Output

The exchange's earnings with two decimals.

## Examples

### Example 1

Input:

```
BID 0.01
BID 10000
BID 5000
BID 5000
SALE 7945.14 3
DEL 5000
SALE 3487.45 3
SALE 0.01 3
QUIT
```

Output:

```
0.06
```

## Solution

A sale sells min(K, number of active bids at X or more) pieces, so all
that is needed is a count of active bids by price, with "how many at
X or more" as a query.

Prices are read exactly as whole cents, from 1 to 1 000 000. Index the
cents from the highest price down: then "at X or more" is a prefix,
and a Fenwick tree keeps the counts. A bid adds 1 at its price, a
withdrawal subtracts 1, and a sale reads a prefix sum. `O(P + N log P)`
for N operations and P price indices.

The pieces sold are counted in an integer, and since every piece earns
one cent, that count divided by 100, with two decimals, is the answer.

Pitfalls:

- a bid of exactly X buys (test 04), and a bid stays active for later
  sales until it is withdrawn (test 07);
- 50 000 bids and 49 999 sales of 100 000 pieces sell 2.49995 · 10⁹
  pieces, more than 2³¹, so signed 32-bit counters overflow (test gen5);
- prices may come with one decimal or none, like `5.5` or `10000`
  (tests 04 and 05);
- floating-point earnings like 0.01 · count can print a cent too few,
  which whole cents avoid.

The totals were compared with a plain count over all active bids on
300 random logs.

## Optimized solutions

The C++ revision retains compression of BID prices and the replayed Fenwick tree. A fixed 16 KB byte reader parses commands, decimal prices and sale amounts without scanf. Exact integer-cent conversion and eligibility of bids equal to the sale price are unchanged.

Exact-source Accepted (G++ 13.2 x64, #11326642: 0.015 s / 1320 KB); teaching base `1316_fenwick.cpp`: 0.171 s / 3652 KB. The previous optimized measurement was 0.156 s / 1344 KB. In the saved 20 November 2026 comparison, time place is 1/85, memory place 1/85; below 1 MiB the policy evaluates the time rank only.

The new C++, Go and Rust implementations compress only prices occurring in BID operations. Store the log, sort and deduplicate those prices, then replay the operations with a Fenwick tree. A sale at X subtracts the number of strictly cheaper bids from the total active count, so equal-price bids remain eligible; a sale never removes bids. Prices are parsed as integer cents, and earnings use a 64-bit integer or a Python integer. For at most N operations this takes O(N log N) time and O(N) storage instead of a million price slots. C++, Go and Rust reserve capacity for the 100000-operation bound. Python instead streams operations straight into a dense Python-list Fenwick over P=1000000 cent values, using reversed index P−price+1. This simpler online version needs no operation log, sorting, dictionary or binary search. Its O(P+N log P) time and O(P) slots trade a fixed table for much less retained input, and list access avoids typed-array boxing. Go uses standard handles; Rust uses bounded C-runtime I/O and a C entry point. The ordinary implementations and the already-admitted Java base are retained.

The accepted Python 3.12 x64 run takes 0.5 s versus 0.437 s for the base and uses 8 324 KB versus 32560 KB.

The accepted base implementations [1316_fenwick.java](1316_fenwick.java) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- Python ranks only the prices that appear in the log, which keeps the
  tree small; the other languages index all million prices directly.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1316_fenwick.cpp](1316_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(P + N log P) | AC | 0.171 s | 3652 KB | 11284923 |
| [1316_fenwick.go](1316_fenwick.go) | Go 1.14 x64 | fenwick | O(P + N log P) | AC | 0.062 s | 11012 KB | 11284924 |
| [1316_fenwick.java](1316_fenwick.java) \* | Java 1.8 | fenwick | O(P + N log P) | AC | 0.156 s | 9428 KB | 11284926 |
| [1316_fenwick.py](1316_fenwick.py) | Python 3.12 x64 | fenwick | O(N log P) | AC | 0.437 s | 32560 KB | 11284925 |
| [1316_fenwick.rs](1316_fenwick.rs) | Rust 1.75 x64 | fenwick | O(P + N log P) | AC | 0.031 s | 10996 KB | 11284927 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1316_fenwick_optimized.cpp](1316_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(N log N) | AC | 0.015 s | 1320 KB | 11326642 |
| [1316_fenwick_optimized.go](1316_fenwick_optimized.go) | Go 1.14 x64 | fenwick | O(N log N) | AC | 0.046 s | 3080 KB | 11314836 |
| [1316_fenwick_optimized.rs](1316_fenwick_optimized.rs) | Rust 1.75 x64 | fenwick | O(N log N) | AC | 0.015 s | 1628 KB | 11314919 |
| [1316_fenwick_optimized.py](1316_fenwick_optimized.py) \* | Python 3.12 x64 | fenwick | O(P + N log P) | AC | 0.5 s | 8324 KB | 11315039 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
