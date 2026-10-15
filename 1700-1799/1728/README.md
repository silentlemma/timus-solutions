# 1728. Curse on Team.GOV

[Timus 1728](https://acm.timus.ru/problem.aspx?space=1&num=1728) · difficulty 526 · implementation

Original problem by Eugene Kurpilyansky (idea by Mikhail Rubinchik), from the Ural Regional School Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Efremov and Kantorov pick a third member from a list of candidates. A
team's strength is the sum of its members' ratings. If the chosen team
has already played in some earlier tournament, Efremov stays away; if
the team without him has played too, it is disqualified. Choose the
candidate that gives the strongest team that plays, or report that
every choice is disqualified.

## Input

n (1 ≤ n ≤ 100) earlier teams, each as a size from 1 to 3 and the
surnames in alphabetical order; every team has Kantorov, and every team
of three has Efremov. Then the ratings of Efremov and Kantorov, m
(1 ≤ m ≤ 100) and m candidates with their ratings. Ratings are from 1
to 666.

## Output

`Win` and a candidate giving the strongest team, or `Fail`. Any best
candidate is accepted.

## Examples

### Example 1

Input:

```
6
3 Efremov Kantorov Rubinchik
2 Efremov Kantorov
3 Efremov Kantorov Kokovin
3 Burmistrov Efremov Kantorov
3 Efremov Kantorov Pervukhin
2 Kantorov Pervukhin
100 10
6
Fominykh 200
Komarov 34
Pervukhin 250
Golubev 23
Soboleva 50
Gein 50
```

Output:

```
Win
Fominykh
```

### Example 2

Input:

```
2
3 Efremov Fominykh Kantorov
2 Fominykh Kantorov
99 666
1
Fominykh 100
```

Output:

```
Fail
```

## Solution

Keep every earlier team as a set of names. For each candidate c: if
{Efremov, Kantorov, c} is new, all three play and the strength is the
sum of three ratings; otherwise, if {Kantorov, c} is new, the two play
without Efremov; otherwise c is no use. Take the strongest of the
candidates left, or `Fail` if none is. `O(n + m)` set lookups.

In the first example Fominykh brings 100 + 10 + 200 = 310. Pervukhin
has played with both and also with Kantorov alone, so that team would
be disqualified.

Pitfalls:

- a team compares as a set of names, not by the candidate alone: a
  candidate who played only with Kantorov still brings Efremov along;
- the two-person teams of Efremov and Kantorov, or Kantorov alone, never
  match a team with a candidate;
- a stronger candidate who keeps Efremov away can lose to a weaker one
  who does not.

The checker recomputes every candidate's strength and accepts any best
one. Answers match an independent accepted implementation on 200
random cases.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1728_implementation.cpp](1728_implementation.cpp) | G++ 13.2 x64 | implementation | O(n + m) | AC | 0.031 s | 476 KB |
| [1728_implementation.go](1728_implementation.go) | Go 1.14 x64 | implementation | O(n + m) | AC | 0.031 s | 1156 KB |
| [1728_implementation.java](1728_implementation.java) | Java 1.8 | implementation | O(n + m) | AC | 0.140 s | 2172 KB |
| [1728_implementation.py](1728_implementation.py) | Python 3.12 x64 | implementation | O(n + m) | AC | 0.109 s | 548 KB |
| [1728_implementation.rs](1728_implementation.rs) | Rust 1.75 x64 | implementation | O(n + m) | AC | 0.046 s | 464 KB |
