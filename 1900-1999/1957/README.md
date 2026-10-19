# 1957. All Possible Final Standings

[Timus 1957](https://acm.timus.ru/problem.aspx?space=1&num=1957) · difficulty 4747 · math

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Denis Dublennykh).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Four teams play each other once, for six matches total. Some scores are
known; every remaining score may contain arbitrarily many goals. A win
earns 3 points, a draw 1 each, a loss 0. Rank by points, then by goals
scored minus goals conceded. Teams equal in both measures can be ordered
arbitrarily by drawing lots. List every possible final order. Limits: 1 s, 64 MB.

## Input

First n, 0≤n≤6, the number of completed matches. Each of the next n lines
contains a,b,c,d: 1≤a<b≤4 and 0≤c,d≤10, with c goals by a and d by b.
No pair appears twice. The bound 10 applies only to completed scores.

## Output

First m, the number of possible distinct orders, 1≤m≤24. Then m permutations
of 1,2,3,4: the teams from first to fourth place. Print them once each in
lexicographic order. Only places distinguish outcomes, not future scores.

## Checking

Outputs are compared token by token.

## Examples

```
5
1 2 1 0
1 3 2 1
1 4 3 2
2 3 1 0
2 4 5 4
```

```
2
1 2 3 4
1 2 4 3
```

## Solution

Enumerate the three results of each remaining match: draw, first team wins,
second team wins. This fixes all points. A drawn game's goal difference
is zero. For each decisive remaining game, write the winner's margin as
1+x, where x is a nonnegative integer; a score of (1+x):0 realizes it.
Include the unit margin in the base goal differences g, and keep x unknown.

Try all 24 permutations. Reject one immediately if its points increase at
an adjacent pair. At adjacent equal-point teams a before b, require
final_g[a]≥final_g[b]. These at most three inequalities, together with x≥0,
form A·x≤b in at most six integer variables. Equality is allowed because
the lottery can realize either order. Adjacent comparisons suffice by
transitivity inside each tied block.

### Exact integer feasibility

Normalize every inequality by the positive gcd h of its coefficients:
divide the coefficients by h and replace its bound b by floor(b/h).
This is equivalent for integer variables, including negative b. A zero
left side with negative bound is impossible; otherwise discard it.
For repeated coefficient vectors, keep the smallest bound.

Eliminate a variable x whose positive coefficients are all 1, or whose
negative coefficients are all −1. Write a lower and upper constraint as
−p·x+L≤bL and q·x+U≤bU, with p,q>0. Remove them in favor of every pairwise
combination q·L+p·U≤q·bL+p·bU; keep rows not containing x.

Necessity follows by adding scaled inequalities. For sufficiency, if all
lower coefficients are −1, each lower bound is an integer once the other
variables are integers. Choose their largest value: the combined rows
ensure that it satisfies every upper bound. If all upper coefficients are
1, choose their smallest integer upper bound instead. A missing side is
unbounded and causes no obstruction. Thus each projection preserves
integer feasibility, unlike unrestricted real Fourier–Motzkin elimination.
Normalize again and repeat. All constant rows passing means feasible.

Why does a suitable variable always exist here? This is a finite
property of the four-team coefficient family, not a guess about
constants. Relabel the teams by the candidate order. Each of the six
pairs has no variable or one of two directed margin variables: 3⁶
choices. Any of the three adjacent tied-point comparisons may be
present: 2³ choices. The script [tests/gen.py](tests/gen.py) checks all
5832 families and every possible elimination path: 13 286 distinct
projected systems and 44 054 steps, and no path gets stuck, whatever the
order of variables and tie-breaks. Constants do not change this trace:
dividing by the gcd, merging parallel rows and projecting depend only on
the coefficients, unless a contradiction already proves infeasibility.
So the only special property the solution relies on is proved by a
finite check.

Therefore a permutation is retained exactly when some integer future
scores realize it. Print retained permutations in their generated lexicographic order.

For r=6−n remaining games, at most 3ʳ result patterns and 24 orders.
Elimination has at most six steps; normalized systems have at most 14
distinct inequalities and coefficients of magnitude at most 31. Its work
is a fixed constant E for four teams: O(3ʳ·24·E) time and O(1) space.
Even before gcd division, coefficients are at most 2·31². Starting with
bounds of magnitude ≤66, six projections give at most 66·62⁶<2⁴².
Signed 64-bit arithmetic suffices. Use floor division for negative bounds.
Never cap future scores at 10, ignore goal difference, forbid lotteries,
or accept a real-valued margin in place of an integer margin.

## Language notes

All five versions use the same exact integer projection. Python integers
are unbounded; C++, Go, Java and Rust use 64-bit bounds and coefficients.
Go 1.14 and Java 8 implement lexicographic permutation generation. Java
uses Math.floorDiv and Rust div_euclid with positive divisors. C++ and Go
correct truncating division when a negative remainder occurs. Rust uses
only the standard library. CPython selection is verified by resource tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1957_math.cpp](1957_math.cpp) | G++ 13.2 x64 | math | O(3^(6-n)) | AC | 0.015 s | 448 KB |
| [1957_math.go](1957_math.go) | Go 1.14 x64 | math | O(3^(6-n)) | AC | 0.031 s | 1152 KB |
| [1957_math.java](1957_math.java) | Java 1.8 | math | O(3^(6-n)) | AC | 0.109 s | 620 KB |
| [1957_math.py](1957_math.py) | Python 3.12 x64 | math | O(3^(6-n)) | AC | 0.109 s | 1144 KB |
| [1957_math.rs](1957_math.rs) | Rust 1.75 x64 | math | O(3^(6-n)) | AC | 0.062 s | 256 KB |
