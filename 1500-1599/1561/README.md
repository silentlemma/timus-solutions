# 1561. Winnie the Pooh

[Timus 1561](https://acm.timus.ru/problem.aspx?space=1&num=1561) · difficulty 2838 · math

Original problem from the Novosibirsk SU Contest at the Petrozavodsk Training Camp, September 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Winnie eats every barrel of one sort of honey in the same whole number
of days, unknown for each sort. Up to 1000 queries come in order:
`Add` brings a new sort, `Learn A0 … Ak S E` says that eating A0 barrels
of sort 0, …, Ak of sort k from weekday S ends on weekday E, and
`Eat A0 … Ak S` asks on which weekday such a meal from S ends
(0 ≤ Ai ≤ 10⁶). Answer each `Eat` with the weekday if the facts so far
fix it, `Don't know` if they allow several, and `Already crazy` if the
facts so far contradict each other.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The number of queries, then one query per line, weekdays written as
Monday … Sunday.

## Output

One line for each `Eat` query.

## Examples

### Example 1

Input:

```
9
Add
Add
Learn 5 2 Saturday Monday
Eat 3 3 Tuesday
Add
Learn 0 9 4 Friday Thursday
Eat 3 0 6 Sunday
Learn 3 2 10 Saturday Friday
Eat 3 4 11 Monday
```

Output:

```
Don't know
Saturday
Already crazy
```

## Solution

Only the number of days modulo 7 matters for the weekday, and any
residue is possible, since a sort may take 7 days. So the unknowns are
x₀, x₁, … in the field of residues modulo 7, a fact is the linear
equation A0·x₀ + … + Ak·xk = E − S, and a meal from S ends on
S + A0·x₀ + … + Ak·xk.

The facts are kept as an echelon basis: each row has a 1 at its first
non-zero place, its pivot, and no two rows share a pivot. A new vector
is reduced by subtracting multiples of the rows in increasing order of
their pivots, together with their right sides. A fact that reduces to
zero is either redundant or, with a non-zero right side, a
contradiction, after which every meal is answered `Already crazy`;
otherwise it becomes a new row. A meal is fixed exactly when its vector
reduces to zero, and then the right side collected on the way is its
length. Each reduction takes O(R·K) for R rows and K sorts, about
2·10⁷ steps at worst. The results were checked against trying all
residues on random small tests.

Pitfalls:

- a fact about a meal of no barrels is a contradiction unless S = E
  (test 03);
- multiples of 7 barrels say nothing about the days per barrel
  (test 04);
- once the facts contradict each other, every later meal is answered
  `Already crazy`, but the meals before stay answered (test 05);
- sorts may appear after a fact was learned, so stored rows are shorter
  than later vectors;
- Python runs under PyPy: the largest tests take about 1.1 s with
  CPython against a limit of 2 s, and about 0.3 s with PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1561_math.cpp](1561_math.cpp) | G++ 13.2 x64 | math | O(N^2 K) | AC | 0.328 s | 1076 KB |
| [1561_math.go](1561_math.go) | Go 1.14 x64 | math | O(N^2 K) | AC | 0.171 s | 5804 KB |
| [1561_math.java](1561_math.java) | Java 1.8 | math | O(N^2 K) | AC | 0.421 s | 8276 KB |
| [1561_math.py](1561_math.py) | PyPy 3.10 x64 | math | O(N^2 K) | AC | 0.750 s | 29076 KB |
| [1561_math.rs](1561_math.rs) | Rust 1.75 x64 | math | O(N^2 K) | AC | 0.125 s | 2880 KB |
