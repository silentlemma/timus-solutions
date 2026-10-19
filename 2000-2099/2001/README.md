# 2001. Mathematicians and Berries

[Timus 2001](https://acm.timus.ru/problem.aspx?space=1&num=2001) · difficulty 22 · math

Original problem by Oleg Merkurev. (Prepared by Kirill Devyatkin), from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two baskets are weighed three times. Initially each contains its own
berries. Next all berries from the second basket are transferred into
the first, and both baskets are weighed. Finally all berries in the
first are moved into the second, and both are weighed again. Recover the
original berry mass in each basket; the baskets themselves keep their
mass throughout.

## Input

Three pairs `a1 b1`, `a2 b2`, `a3 b3`, in chronological order. Each
reading is an integer from 0 to 10000. The readings describe the stated
transfers. Time 0.5 seconds, memory 64 MB.

## Output

The original mass of berries in the first and second basket, in that order.

## Checking

Outputs are compared token by token.

## Examples

```
1 2
2 1
0 3
```

```
1 1
```

The first basket is empty at the last weighing, so its own mass is 0.
The second is empty at the middle weighing, so its own mass is 1.
Subtracting these from the initial readings 1 and 2 gives 1 and 1.

## Solution

Let empty basket masses be `c,d`, and initial berry masses be `x,y`. The
initial readings are `a1=c+x`, `b1=d+y`. After the second basket is
emptied, `b2=d`. After the first basket is emptied, `a3=c`. Therefore
the unique answer is `x=a1−a3`, `y=b1−b2`.

Substitution proves both differences equal precisely the original
contents. The other two readings satisfy `a2=c+x+y`, `b3=d+x+y`; they
are consumed from the input but are unnecessary for recovery. No
division, search or rounding is involved.

Time `O(1)` and memory `O(1)` for the fixed six readings. Differences
lie in 0..10000 for valid data, so 32-bit signed integers suffice.

Subtract the mass of the same empty basket: `a3` for the first, `b2` for
the second. The combined readings `a2,b3` still include a basket.
Preserve output order and handle zero contents or zero basket masses
normally.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2001_math.cpp](2001_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB |
| [2001_math.go](2001_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1088 KB |
| [2001_math.java](2001_math.java) | Java 1.8 | math | O(1) | AC | 0.156 s | 388 KB |
| [2001_math.py](2001_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 384 KB |
| [2001_math.rs](2001_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 228 KB |
