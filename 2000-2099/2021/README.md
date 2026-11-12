# 2021. Postponing a Certain Winner

[Timus 2021](https://acm.timus.ru/problem.aspx?space=1&num=2021) · difficulty 462 · sorting

Original problem by Oleg Dolgorukov, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two teams have `n` participants each. Every participant has a predetermined
integer score between 0 and 6. Arrange `n` rounds, each with one participant
from each team, using everybody exactly once. Both scores of a round are
revealed simultaneously. The team with the greater final total wins; equal
totals give a draw. The audience initially knows only the score bounds.

Choose the two orders to delay as long as possible the first round after
which the announced scores guarantee a winning team. After `k` rounds, with
`r=n−k` rounds left and score difference `d`, victory is guaranteed exactly
when `|d| > 6r`. Equality still permits a draw. If no victory is guaranteed
earlier, the whole outcome becomes known after the final round.

There are `2 ≤ n ≤ 1,000` participants per team, with individual scores
`0 ≤ score ≤ 6`. Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line contains `n`. The next line gives the first team's `n` scores,
and the third gives the second team's. Each team numbers its participants
independently from 1 to `n` in input order.

## Output

Print `n` lines. Each contains the first and second team IDs chosen for that
round. Each ID must appear once in its own column. Any globally optimal
pair of orders is allowed.

## Checking

A checker verifies both permutations, replays the scores and accepts any
orders whose first certain round is the latest possible.

## Examples

```
5
0 1 4 3 6
6 5 1 3 0
```

```
5 1
1 5
4 4
2 3
3 2
```

## Solution

Compare the **final totals**, which do not depend on the order. If the first
team has the greater total, sort its participants by increasing score and
the second team's by decreasing score. If the second team wins, reverse
these directions. If the totals tie, any orders work; we sort both increasingly.
Pair the two resulting lists position by position, keeping original IDs.

To prove optimality, suppose the first team wins by a final difference
`D > 0`. After any prefix with `r` rounds left, let `R` be the
difference the actual remaining participants will add. Since each round
contributes between −6 and 6, `R ≤ 6r`, so `d = D−R ≥ D−6r > −6r`. The
eventual losing team therefore cannot already have a guaranteed win
under any ordering of these participants. Only the upper barrier `d >
6r` matters.

For every prefix length `k`, the increasing first order has the smallest
possible sum of `k` first-team scores. The decreasing second order has the
largest possible opposing sum. Together they minimize `d(k)` among **all**
orders, simultaneously for every `k`. If this schedule first makes victory
certain at round `k<n`, every other schedule has difference at least as
large at that same round, so its winner is certain by then too. None can
delay certainty longer. Reaching the final round already achieves the
largest possible delay. The proof for a second-team win is symmetric.

If `D=0`, every prefix satisfies `d=−R`, hence `|d|≤6r`. No order can
guarantee a winner before the final draw is revealed, so every order is optimal.
Large temporary leads by the eventual loser are harmless: the actual bounded
remaining scores prevent them from exceeding the certainty barrier.

In the sample the final totals are 14 and 15. The displayed first four
rounds give equal scores to both teams, and the last round gives 4 versus 5.
The winning team is revealed only in round five, which is optimal.

Sorting two ID arrays takes `O(n log n)` time and `O(n)` space. Final
totals and prefix differences have magnitude at most 6,000, so ordinary
integers suffice.

Pitfalls:

- Decide sort directions from the final totals, not the current running lead.
- Use the strict certainty test `|d| > 6r`; equality still allows a draw.
- Reveal a pair's scores together and use each participant once in its own team.
- Output original one-based IDs, not scores or positions in sorted arrays.
- Accept any optimal order, including arbitrary orders when the final
  totals tie.

## Optimized solutions

The new C++, Go and Rust sources replace comparison sorting with S=7 score buckets. Prepending original IDs to a linked list per score uses one 16-bit next pointer per participant. Compare final totals, enumerate the winner’s buckets increasingly and the loser’s decreasingly; for a draw enumerate both increasingly. Maintain a bucket cursor per team and pop one ID per round, so each participant and bucket is visited once: O(n+S) time and O(n+S) storage. The original prefix-minimization proof still applies; within equal scores any ID order is valid. Go/Rust use bounded output buffers of 10000 bytes, enough for 1000 rows of two at-most-four-digit IDs. All simple files remain; Java/Python reuse their admitted bases.

The accepted base implementations [2021_sorting.java](2021_sorting.java), [2021_sorting.py](2021_sorting.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

All ordinary versions comparison-sort original IDs by score, using ID tie breaks for deterministic output. New C++/Go/Rust use seven linked score buckets; their order among equal scores can differ and remains valid.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2021_sorting.cpp](2021_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 472 KB | 11292703 |
| [2021_sorting.go](2021_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.015 s | 1252 KB | 11292708 |
| [2021_sorting.java](2021_sorting.java) \* | Java 1.8 | sorting | O(n log n) | AC | 0.156 s | 2812 KB | 11292721 |
| [2021_sorting.py](2021_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.093 s | 764 KB | 11292714 |
| [2021_sorting.rs](2021_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.015 s | 340 KB | 11292728 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2021_sorting_greedy.cpp](2021_sorting_greedy.cpp) | G++ 13.2 x64 | sorting, greedy | O(n + S) | AC | 0.015 s | 88 KB | 11315199 |
| [2021_sorting_greedy.go](2021_sorting_greedy.go) \* | Go 1.14 x64 | sorting, greedy | O(n + S) | AC | 0.015 s | 284 KB | 11315209 |
| [2021_sorting_greedy.rs](2021_sorting_greedy.rs) \* | Rust 1.75 x64 | sorting, greedy | O(n + S) | AC | 0.015 s | 56 KB | 11315222 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
