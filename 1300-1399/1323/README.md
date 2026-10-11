# 1323. Classmates

[Timus 1323](https://acm.timus.ru/problem.aspx?space=1&num=1323) · difficulty 829 · bitmask

Original problem: idea by Evgeny Kobzev, prepared by Pavel Atnashev and Alexander Mironenko, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A class of N ≤ 10 students has M pairs who can phone each other, in
either direction, and the news can reach everyone this way. At first
only the class monitor knows the news. A call takes exactly one minute,
and in a minute each student who already knows can make one call. Plan
the calls so that everyone hears the news exactly once, as early as
possible.

Time limit: 1.5 seconds. Memory limit: 64 MB.

## Input

N, then M, then M lines with two names each, then the name of the class
monitor. Names are different and have up to 20 Latin letters.

## Output

The number of minutes, then for each minute the number of calls made in
it followed by those calls, one per line as the caller's name and the
callee's name. Any optimal plan is accepted.

## Checking

The checker compares the number of minutes with the minimum and then
replays the plan: every call must use a pair from the input, the caller
must have known the news before that minute, nobody may call twice in a
minute or be called twice at all, and at the end everyone must know.

## Examples

### Example 1

Input:

```
6
7
Tanya Lena
Tanya Katya
Tanya Masha
Lena Natasha
Lena Vitya
Natasha Vitya
Masha Vitya
Tanya
```

Output:

```
3
1
Tanya Lena
2
Tanya Masha
Lena Vitya
2
Vitya Natasha
Tanya Katya
```

## Solution

What can happen next depends only on who already knows, so the state is
a set of students, at most 2¹⁰ of them. From a set S, one minute can add
any set T of students outside S if every student of T can be given a
different caller in S who knows them. That is a bipartite matching from
T into S, found by augmenting paths. A breadth-first search over the
sets, trying every subset T of the uninformed neighbours of S, reaches
the full class in the smallest number of minutes. Remembering the set
and the matching that led to each state gives the plan.

Only sets that contain the class monitor are reached, and the subsets T
of the rest add up to at most 3⁹ pairs (S, T), each with a matching on
at most ten people, taking O(N³), for O(3^N·N³) time overall.

Pitfalls:

- with one student the answer is 0 and there are no groups (test 02);
- the plan has to start from the class monitor, who can appear second
  in a pair (test 03);
- pairs can be listed in both directions (test 07);
- calling the nearest people first is not always best: the branch with
  more people behind it has to be reached first (test 08).

The minimum times were compared with a search that lets every informed
student call any neighbour or nobody each minute, on 300 random classes
of up to 7 students, and every plan was replayed by the checker.

## Language notes

- All five solutions run the same search with the same matching.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1323_bitmask.cpp](1323_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(3^N·N³) | AC | 0.015 s | 476 KB |
| [1323_bitmask.go](1323_bitmask.go) | Go 1.14 x64 | bitmask | O(3^N·N³) | AC | 0.031 s | 2636 KB |
| [1323_bitmask.java](1323_bitmask.java) | Java 1.8 | bitmask | O(3^N·N³) | AC | 0.109 s | 1596 KB |
| [1323_bitmask.py](1323_bitmask.py) | Python 3.12 x64 | bitmask | O(3^N·N³) | AC | 0.171 s | 912 KB |
| [1323_bitmask.rs](1323_bitmask.rs) | Rust 1.75 x64 | bitmask | O(3^N·N³) | AC | 0.031 s | 480 KB |
