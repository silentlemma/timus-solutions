# 2095. Count the days a repeated removal sieve keeps

[Timus 2095](https://acm.timus.ru/problem.aspx?space=1&num=2095) · difficulty 277 · math

Original problem by Dmitry Ivankov, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Days are numbered 1, 2, 3, … Every second day is a report; of the days
left, every third is a report; of those left, every fourth, and so on
forever. The days that are never removed are quiet. Count the quiet
days in [l; r]. The limits are 1 second and 64 MB.

## Input

l and r, 1 ≤ l ≤ r ≤ 10⁹.

## Output

The number of quiet days from l to r.

## Examples

### Example 1

Input:

```
1 10
```

Output:

```
3
```

## Solution

Let f(n) be the number of quiet days among the first n. The removals
always take positions in the list of remaining days, so among the first
c remaining days step k removes exactly ⌊c / k⌋ of them, and the
remaining days among the first n stay a prefix of the list. Hence
f(n) is found by c ← c − ⌊c / k⌋ for k = 2, 3, … while c ≥ k; once c < k
no further step touches the prefix. The count c shrinks roughly like
n / k, so the loop stops after about 2√(n/π) steps, some 3.6·10⁴ for 10⁹. The
answer is f(r) − f(l − 1).

In the example f(10): 10 → 5 → 4 → 3, and the quiet days are 1, 3
and 7.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2095_math.cpp](2095_math.cpp) | G++ 13.2 x64 | math | O(sqrt r) | AC | 0.015 s | 132 KB |
| [2095_math.go](2095_math.go) | Go 1.14 x64 | math | O(sqrt r) | AC | 0.031 s | 1076 KB |
| [2095_math.java](2095_math.java) | Java 1.8 | math | O(sqrt r) | AC | 0.125 s | 1584 KB |
| [2095_math.py](2095_math.py) | Python 3.12 x64 | math | O(sqrt r) | AC | 0.078 s | 368 KB |
| [2095_math.rs](2095_math.rs) | Rust 1.75 x64 | math | O(sqrt r) | AC | 0.015 s | 220 KB |
