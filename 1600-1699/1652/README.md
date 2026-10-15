# 1652. Banking Crisis

[Timus 1652](https://acm.timus.ru/problem.aspx?space=1&num=1652) · difficulty 2688 · matching

Original problem by Pavel Atnashev, from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n banks, each with a country and some free money, hold m interbank
debts. A bank counts as "responsible" if it lends to a bank of its own
country. Before that is checked, banks may buy whole debts from their
creditors, paying only out of their initial free money; sellers always
agree. Find the largest possible number of responsible banks.

## Input

n (2 ≤ n ≤ 1000), then n lines "country money" (1 ≤ country ≤ 100,
0 ≤ money ≤ 10⁹), then m (0 ≤ m ≤ 10000) and m lines
"creditor debtor sum" (0 ≤ sum ≤ 10⁹).

## Output

The largest number of responsible banks.

## Examples

### Example 1

Input:

```
5
1 100000
1 200000
1 300000
2 400000
2 500000
4
1 2 200000
1 3 200000
2 4 500000
3 5 500000
```

Output:

```
3
```

## Solution

A bank needs just one debt owed by a bank of its own country, so only
the final holder of each debt matters. Bank b can end up holding debt d
when d's debtor is in b's country, b is not the debtor itself, and
either b already holds d or d's sum fits b's money. Every debt has one
holder, so responsible banks are matched to distinct debts: the answer
is a maximum bipartite matching, computed for each country separately.
Debts left unmatched simply stay where they are, and buying more than
one debt never helps.

The graph can have ten million edges, but a bank's affordable debts form
a prefix of the debts sorted by sum, so they are never listed. Kuhn's
augmenting paths walk the prefix through a "next unseen debt" pointer
with path compression, so each debt is looked at once per search. Banks
that already hold a debt go first, then poorer banks, which leaves few
paths to fix. After a failed search the marks are kept: the matching did
not change, so the debts it reached still lead nowhere. `O(k · (n + m))`
for k successful searches, far less in practice.

Pitfalls:

- a bank cannot lend to itself, so it never holds a debt it owes, even
  if it could afford it (test 04);
- a debt owed by a bank of another country does not help;
- money from selling a debt cannot be spent, so each purchase is checked
  against the initial money only.

The answers match an exhaustive search over all holders on 150 small
markets and an independent accepted implementation on large ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1652_matching.cpp](1652_matching.cpp) | G++ 13.2 x64 | matching | O(k · (n + m)) | AC | 0.031 s | 720 KB |
| [1652_matching.go](1652_matching.go) | Go 1.14 x64 | matching | O(k · (n + m)) | AC | 0.046 s | 3456 KB |
| [1652_matching.java](1652_matching.java) | Java 1.8 | matching | O(k · (n + m)) | AC | 0.187 s | 6540 KB |
| [1652_matching.py](1652_matching.py) | Python 3.12 x64 | matching | O(k · (n + m)) | AC | 0.718 s | 4624 KB |
| [1652_matching.rs](1652_matching.rs) | Rust 1.75 x64 | matching | O(k · (n + m)) | AC | 0.031 s | 1684 KB |
