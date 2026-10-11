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

## Language notes

- Python ranks only the prices that appear in the log, which keeps the
  tree small; the other languages index all million prices directly.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1316_fenwick.cpp](1316_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(P + N log P) | AC | 0.171 s | 3652 KB |
| [1316_fenwick.go](1316_fenwick.go) | Go 1.14 x64 | fenwick | O(P + N log P) | AC | 0.062 s | 11012 KB |
| [1316_fenwick.java](1316_fenwick.java) | Java 1.8 | fenwick | O(P + N log P) | AC | 0.156 s | 9428 KB |
| [1316_fenwick.py](1316_fenwick.py) | Python 3.12 x64 | fenwick | O(N log P) | AC | 0.437 s | 32560 KB |
| [1316_fenwick.rs](1316_fenwick.rs) | Rust 1.75 x64 | fenwick | O(P + N log P) | AC | 0.031 s | 10996 KB |
