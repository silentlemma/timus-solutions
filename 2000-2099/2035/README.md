# 2035. Splitting a total under two upper bounds

[Timus 2035](https://acm.timus.ru/problem.aspx?space=1&num=2035) · difficulty 78 · math

Original problem by Kirill Borozdin, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given integers `X,Y,C` with `0 ≤ X,Y,C ≤ 1000000000`, find any integers
`A,B` satisfying `0 ≤ A ≤ X`, `0 ≤ B ≤ Y` and `A+B=C`.
Time limit: 0.5 seconds; memory limit: 64 MB.

## Input

One line with `X Y C`. There is one instance and no test-count prefix.

## Output

Any valid pair `A B`, or the exact word `Impossible` if no pair exists.
The pair `0 0` is valid when `C=0`.

## Checking

A checker verifies both bounds and the sum; `Impossible` is accepted
only when no pair exists. Any valid pair is accepted.

## Examples

```
2 7 5
```

```
2 3
```

```
9 15 100
```

```
Impossible
```

## Solution

Choose `A=min(X,C)` and let `B=C-A`. If `B≤Y`, output the pair; otherwise
output `Impossible`.

The chosen `A` is nonnegative and no larger than either `X` or `C`.
Thus `B≥0`, and the sum equals `C` by construction. Checking `B≤Y`
completes all required inequalities.

For completeness, every valid first summand must obey `A≤X` and `A≤C`,
so it is at most our choice. Its second summand is consequently at least
our `B`. We minimize the required second summand: if even this value exceeds
`Y`, no possible pair can work. This proves the impossibility branch too.

Equivalently, all solutions correspond to
`max(0,C-Y) ≤ A ≤ min(X,C)`, with `B=C-A`. This interval is nonempty exactly
when `C≤X+Y` under the given nonnegative bounds.

For `2 7 5`, choosing `A=2` gives `B=3` within its bound. Pairs `0 5` and
`1 4` would also be valid. For `9 15 100`, the maximum total is `24`, so
no pair can reach `100`.

Time and working space are both `O(1)`: only a comparison, subtraction and
bound check are needed.

Pitfalls:

- All three input bounds are nonnegative and inclusive.
- Choosing `A=X` without capping it by `C` could make `B` negative.
- Zero summands and the zero pair are legitimate.
- Any feasible pair is accepted, not only the sample pair.
- Preserve the exact spelling and case of `Impossible`.

## Language notes

C++ and Java use signed 64-bit values, Go `int64`, Rust `u64`, and Python
exact integers. Rust subtraction is safe because `A≤C`. Even `X+Y≤2000000000`
fits signed 32 bits under these bounds; wider types simply keep the arithmetic
straightforward. Every port distinguishes a valid zero pair from missing output.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2035_math.cpp](2035_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 400 KB |
| [2035_math.go](2035_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1088 KB |
| [2035_math.java](2035_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 488 KB |
| [2035_math.py](2035_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB |
| [2035_math.rs](2035_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB |
