# 1483. Table Football

[Timus 1483](https://acm.timus.ru/problem.aspx?space=1&num=1483) · difficulty 384 · math

Original problem by Sergey Pupyrev, from the Ural State University Championship, October 7, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N teams (1 ≤ N ≤ 1000) play a round robin: every pair meets once, a
win gives 3 points, a draw 1 and a loss 0. Teams with equal points
share a place. One team finished first and another last. Find the
smallest number of points the first team could have and the largest
number the last team could have.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The two numbers.

## Examples

### Example 1

Input:

```
2
```

Output:

```
1 1
```

## Solution

Every match gives out at least 2 points, as a draw, and at most 3, as a
win. So the teams share at least N(N − 1) points and the leader has at
least the average N − 1; if every match is drawn, every team has
exactly N − 1.

The teams share at most 3·N(N − 1)/2 points, so the last team has at
most ⌊3(N − 1)/2⌋. For odd N every team can win exactly half of its
N − 1 matches, which gives everyone 3(N − 1)/2. For even N, let the
teams draw in pairs, one draw each, and split the remaining matches so
that every team wins half of its other N − 2: everyone gets
3(N − 2)/2 + 1 = ⌊3(N − 1)/2⌋. `O(1)`.

Pitfalls:

- with one team there are no matches: 0 and 0 (test 02);
- for even N the bound needs one draw per team, since all-decisive
  results give multiples of 3 (test 04);
- the two answers are optimised separately, not in one tournament
  (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1483_math.cpp](1483_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.001 s | 128 KB |
| [1483_math.go](1483_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1084 KB |
| [1483_math.java](1483_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1588 KB |
| [1483_math.py](1483_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 320 KB |
| [1483_math.rs](1483_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB |
