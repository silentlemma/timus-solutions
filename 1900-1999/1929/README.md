# 1929. A Distinguished Triple with Feasible Remaining Teams

[Timus 1929](https://acm.timus.ru/problem.aspx?space=1&num=1929) · difficulty 385 · combinatorics

Original problem from Ural Regional School Programming Contest 2012 | by Olga Soboleva (prepared by Kirill Devyatkin).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n people, of whom m are special. Every team must consist of three
people and contain at least one special person. Count the unordered teams
containing person 1 that leave all other people partitionable into valid
teams. Each selected team counts once, regardless of the number of possible
remaining partitions. Limits: 1 second, 64 MB.

## Input

The first line contains n and m: 6≤n≤999, n divisible by 3, 1≤m≤n.
The second lists the m distinct special identifiers between 1 and n.
Their order is arbitrary; person 1 may or may not be special.

## Output

One integer, the number of feasible teams containing person 1.

## Checking

Exact comparison of the single integer token.

## Examples

```
6 4
2 3 4 6
```

```
10
```

## Solution

Let h be 1 if person 1 is special, otherwise 0. Among possible partners,
S=m−h are special and U=n−m−(1−h) are ordinary. Enumerate r=0,1,2,
the number of special partners. This removes h+r special people.
The selected team needs h+r≥1. There are t=n/3−1 remaining teams;
they can be formed exactly when m−h−r≥t.

Necessity follows because each remaining team needs its own special person.
For sufficiency, assign one distinct special person to each of the t teams.
Exactly 2t people remain for the 2t vacant positions. Fill them arbitrarily,
including any additional special people. No other constraints exist.

Thus each feasible r contributes C(S,r)·C(U,2−r). Impossible choices
contribute zero; C(a,0)=1, C(a,1)=a, C(a,2)=a(a−1)/2.
The three cases are disjoint and include every unordered partner pair
exactly once. Summing them therefore gives the required count.

O(m) time to read identifiers, O(1) counting work. Streaming C++, Go and
Java use O(1) auxiliary space; Python and Rust buffer O(m) input.

The selected team also needs a special person. Do not remove person 1 from
the wrong category or count ordered partners and role assignments.
The remaining condition is at least one special per team, not exactly one.
If m<n/3 the answer is zero. At m=n/3 every team has exactly one special;
the formula handles this without a separate branch. C(0,0) must equal 1.
Keep reading all identifiers even after finding person 1.

## Language notes

Signed 32-bit integers suffice: the answer is at most C(998,2)=497503
and the intermediate product a(a−1) is below one million. Go uses int,
Rust uses i32 for counts, and Python uses integers. Count unavailable
categories before multiplying: there may be zero ordinary partners.
No factorials, modular arithmetic, floating point or large integers are needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1929_combinatorics.cpp](1929_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(m) | AC | 0.015 s | 392 KB |
| [1929_combinatorics.go](1929_combinatorics.go) | Go 1.14 x64 | combinatorics | O(m) | AC | 0.031 s | 1100 KB |
| [1929_combinatorics.java](1929_combinatorics.java) | Java 1.8 | combinatorics | O(m) | AC | 0.125 s | 2404 KB |
| [1929_combinatorics.py](1929_combinatorics.py) | Python 3.12 x64 | combinatorics | O(m) | AC | 0.078 s | 492 KB |
| [1929_combinatorics.rs](1929_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(m) | AC | 0.046 s | 240 KB |
