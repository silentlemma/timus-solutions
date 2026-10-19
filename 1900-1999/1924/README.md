# 1924. A Sign Game with Fixed Parity

[Timus 1924](https://acm.timus.ru/problem.aspx?space=1&num=1924) · difficulty 39 · math

Original problem: folklore, from Ural Regional School Programming Contest 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The integers 1 through n appear in order. Two teams alternate placing
either + or − in an unused gap between consecutive integers. The first
team, `black`, wants the completed expression to be even; `grimy` wants
it odd. Both play optimally and black moves first. Determine the winner.
For n=1 there are no gaps, and the expression is simply 1.
Limits: 1 second, 64 MB.

## Input

One integer n, 1≤n≤50.

## Output

Print exactly `black` if the even-result team wins, otherwise `grimy`.

## Checking

Compare the single word token exactly, including lowercase spelling.

## Examples

```
1
```

```
grimy
```

```
4
```

```
black
```

## Solution

Changing the sign before integer x from + to − changes the result by
−2x, an even number. Thus every complete expression has the same parity
as the all-plus sum S=n(n+1)/2. The chosen gaps, signs and move order
cannot affect the winner. Print black when S is even, grimy when it is odd.
This also handles the no-move case n=1 correctly.

The argument covers every possible completion, so optimal strategies
cannot alter the conclusion; no game search is needed.

O(1) time and O(1) auxiliary space.

Subtracting an odd integer still contributes odd parity. Do not simulate
turns or infer a winner from which team moves last. The empty set of
gaps at n=1 does not mean a draw. Divide the product before testing parity.

## Language notes

All five versions use integer arithmetic and exact division by 2.
The product n(n+1) is at most 2550 and the sum at most 1275, so ordinary
integer types suffice. Python and Rust read the input as text; C++, Go
and Java read the single integer through standard input facilities.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1924_math.cpp](1924_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 380 KB |
| [1924_math.go](1924_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1100 KB |
| [1924_math.java](1924_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1616 KB |
| [1924_math.py](1924_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 396 KB |
| [1924_math.rs](1924_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB |
