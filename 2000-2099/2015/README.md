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

## Language notes

Sharing a one-room apartment is forbidden. Check both budgets; a rich
friend cannot pay more than half for the other person. Do not floor an
odd half-rent or add a solo benefit to a shared score. Solo benefits
differ by room count. Zero friends and zero benefits are valid. All five
ports use exact integer comparisons and the same enumeration order;
their internal absent choice is separate from a valid solo choice.
Python uses CPython and needs no optimization for the bounded search.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2015_bruteforce.cpp](2015_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(m (n + 1)) | AC | 0.015 s | 404 KB |
| [2015_bruteforce.go](2015_bruteforce.go) | Go 1.14 x64 | bruteforce | O(m (n + 1)) | AC | 0.015 s | 1136 KB |
| [2015_bruteforce.java](2015_bruteforce.java) | Java 1.8 | bruteforce | O(m (n + 1)) | AC | 0.125 s | 424 KB |
| [2015_bruteforce.py](2015_bruteforce.py) | Python 3.12 x64 | bruteforce | O(m (n + 1)) | AC | 0.078 s | 584 KB |
| [2015_bruteforce.rs](2015_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(m (n + 1)) | AC | 0.031 s | 240 KB |
