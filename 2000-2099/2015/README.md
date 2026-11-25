# 2015. Choosing an Affordable Apartment and Living Arrangement

[Timus 2015](https://acm.timus.ru/problem.aspx?space=1&num=2015) · difficulty 300 · bruteforce

Original problem by Eugene Kurpilyansky, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose an apartment and either live alone or share with one listed
friend. Living alone is allowed in a one-room or two-room apartment;
sharing is allowed only in a two-room apartment. Alone, pay the whole
rent. When sharing, both people pay exactly half, and each payment must
fit that person's budget. The score is the apartment's benefit plus
either the corresponding room-count benefit of living alone or the
chosen friend's benefit. Find any affordable choice of maximum score. If
none is affordable, report that no apartment can be rented.

## Input

First the own budget and two benefits of living alone, for one and two
rooms respectively. Then `n`, `0 ≤ n ≤ 256`, and `n` rows of friend
budget and benefit. Then `m`, `1 ≤ m ≤ 256`, and `m` rows of room count
(1 or 2), full rent and apartment benefit. Every budget and rent is an
integer from 1 to 100,000; every benefit is from 0 to 100,000. Friends
and apartments have 1-based IDs in input order. Time limit 1 second,
memory 64 MB.

## Output

For apartment `i` alone print `You should rent the apartment #i alone.`.
With friend `j`, print `You should rent the apartment #i with the friend
#j.`. If no choice is affordable, print `Forget about apartments. Live
in the dormitory.`. Replace `i` and `j` by the actual IDs; keep
spelling, spaces, `#` signs and final period.

## Checking

A checker verifies the sentence, the numbers, the rooms and both budgets
and compares the score with the optimum; any optimal choice is accepted,
and the refusal only when nothing is affordable.

## Examples

```
10000 50 70
1
10000 100
2
1 10000 200
2 30000 500
```

```
You should rent the apartment #1 alone.
```

```
30000 0 1
1
10000 1001
3
1 20000 2000
2 30000 2000
2 10000 1001
```

```
You should rent the apartment #3 with the friend #1.
```

```
1000 0 0
0
1
1 10000 1000
```

```
Forget about apartments. Live in the dormitory.
```

In the first case only apartment 1 is affordable, with score
`50+200=250`; even splitting apartment 2 costs too much. In the second,
the best solo score is 2001, but apartment 3 with friend 1 gives
`1001+1001=2002`. In the last case the only apartment is unaffordable.

## Solution

Enumerate apartments in input order. If the full rent fits the own
budget, consider the solo score `apartment_benefit +
solo_benefit[rooms−1]`. For a two-room apartment, also enumerate every
friend. Sharing is affordable exactly when `rent≤2·own_budget` and
`rent≤2·friend_budget`; its score is `apartment_benefit +
friend_benefit`. These doubled comparisons handle odd rents exactly
without division or floating point.

Maintain the best score and its two IDs. Initialize the score to −1,
below every possible feasible score. Replace the choice only for a
strictly greater score; this makes ties deterministic but is not
required by the judge. A solo choice has friend ID zero internally. If
no candidate ever updates the score, output the no-apartment sentence.

Every legal arrangement is either one apartment alone or one two-room
apartment with exactly one listed friend. The loops consider all these
possibilities and reject exactly those whose payments exceed a budget.
Each retained candidate's score uses precisely the two relevant
benefits. Inductively the saved choice has maximum score among
considered feasible candidates. At the end it is therefore a global
optimum, or none exists. Starting below zero ensures that an affordable
zero-score option is selected rather than mistaken for impossibility.

At most `m(n+1) ≤ 65,792` candidates are considered: time `O(m(n+1))`,
including `n=0`. The input uses `O(n+m)` space and selection needs
`O(1)` extra space. Scores and doubled budgets are at most 200,000, so
ordinary signed integers suffice. An alternative is sorting friends by
budget and querying the largest affordable benefit, but enumeration
already fits these bounds.

## Optimized solutions

`2015_sorting_binary_search.java`. Replace scanning every friend for every apartment by sorting friend budgets and building suffix argmax indices by friend benefit. For each two-room apartment, binary-search the first budget at least ceil(rent/2), then inspect one suffix-best friend; separately test living alone and the own-budget constraint. Original friend IDs and smallest-ID benefit ties are preserved, as are first-apartment/alone ties. Apartments are processed as they arrive, without storing their table. With N friends,M apartments and primitive sort S(N), time O(N+S(N)+M log(N+1)), usually O(N log N+M log(N+1)), space O(N). Zero friends is supported. The different algorithm is named sorting_binary_search; the brute-force teaching source remains.

Compared with `2015_bruteforce.java`: time 0.109 s → 0.093 s; memory 368 KB → 544 KB.

C++ and Rust sort friends by budget and precompute the friend with the greatest benefit in each suffix. For a two-room apartment, binary search finds the first friend who can afford half its rent. The suffix summary then gives the best eligible companion. C++ stores separate suffix indices. Rust keeps the budget order and overwrites benefit and identifier fields with the best suffix choice. Rust stores friends in a fixed array with 16-bit identifiers and uses fixed byte buffers for input and decimal output through the C runtime.

The accepted base implementations [2015_bruteforce.go](2015_bruteforce.go), [2015_bruteforce.java](2015_bruteforce.java), [2015_bruteforce.py](2015_bruteforce.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`2015_sorting_binary_search.java`: time place 8/75, memory place 7/75 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2015_bruteforce.cpp](2015_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(m (n + 1)) | AC | 0.015 s | 404 KB | 11292526 |
| [2015_bruteforce.go](2015_bruteforce.go) | Go 1.14 x64 | bruteforce | O(m (n + 1)) | AC | 0.015 s | 1136 KB | 11292536 |
| [2015_bruteforce.java](2015_bruteforce.java) \* | Java 1.8 | bruteforce | O(m (n + 1)) | AC | 0.109 s | 368 KB | 11325564 |
| [2015_bruteforce.py](2015_bruteforce.py) \* | Python 3.12 x64 | bruteforce | O(m (n + 1)) | AC | 0.078 s | 584 KB | 11292543 |
| [2015_bruteforce.rs](2015_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(m (n + 1)) | AC | 0.031 s | 240 KB | 11292565 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2015_binary_search_sorting.cpp](2015_binary_search_sorting.cpp) | G++ 13.2 x64 | binary_search, sorting | O((n+m) log(n+2)) | AC | 0.001 s | 116 KB | 11310956 |
| [2015_sorting_binary_search.rs](2015_sorting_binary_search.rs) \* | Rust 1.75 x64 | sorting, binary_search | O((n+m) log(n+2)) | AC | 0.015 s | 68 KB | 11311237 |
| [2015_sorting_binary_search.java](2015_sorting_binary_search.java) | Java 1.8 | sorting, binary_search | O(N+S(N)+M log(N+1)) | AC | 0.093 s | 544 KB | 11325029 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
