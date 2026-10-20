# 2192. A forest route where every path pays more for mushrooms

[Timus 2192](https://acm.timus.ru/problem.aspx?space=1&num=2192) · difficulty 1041 · graphs

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A forest has N glades and M one-way paths without cycles; path i
carries sᵢ mushrooms and wᵢ berries. On day j a mushroom sells for aⱼ
and a berry for bⱼ. For each of Q days, tell whether some route from
glade 1 to glade N has aⱼ sᵢ > bⱼ wᵢ on every path it takes. The limits
are 2 seconds and 256 MB.

## Input

N, M and Q, 2 ≤ N ≤ 10⁵, 1 ≤ M, Q ≤ 10⁵. Then M lines uᵢ vᵢ sᵢ wᵢ with
glade numbers up to 10⁵ and 1 ≤ sᵢ, wᵢ ≤ 10⁹, and Q lines aⱼ bⱼ,
1 ≤ aⱼ, bⱼ ≤ 10⁹. No two paths join the same pair of glades.

## Output

YES or NO for each day.

## Examples

### Example 1

Input:

```
3 3 3
1 2 2 4
2 3 3 9
1 3 10 50
58 9
60 23
61 9
```

Output:

```
YES
NO
YES
```

## Solution

The condition on one path is sᵢ / wᵢ > bⱼ / aⱼ, so a route works on a
day exactly when its smallest ratio sᵢ / wᵢ beats bⱼ / aⱼ. The days only
need one number from the forest: the largest possible smallest ratio
over all routes from 1 to N.

Because the paths form no cycle, this bottleneck value is a dynamic
programming over a topological order, found with Kahn's algorithm:
best(1) is infinite, and a path u → v offers v the value
min(best(u), s / w), of which v keeps the largest. Ratios are kept as
numerator and denominator and compared by cross multiplication, which
stays below 10¹⁸; infinity is 1 / 0. Glade numbers may exceed N, so the
arrays are sized by the largest number seen.

A day is then YES when N is reachable and aⱼ · s > bⱼ · w for the
best ratio s / w, and the strict inequality makes a tie a NO.

In the example the direct path has ratio 1 / 5 and the route through 2
has min(1 / 2, 1 / 3) = 1 / 3, so the bottleneck is 1 / 3. The days ask
9 / 58, 23 / 60 and 9 / 61 against it, and only 23 / 60 is too big.

The order and the queries take O(N + M + Q).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2192_graphs.cpp](2192_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M + Q) | AC | 0.453 s | 10692 KB |
| [2192_graphs.go](2192_graphs.go) | Go 1.14 x64 | graphs | O(N + M + Q) | AC | 0.125 s | 15996 KB |
| [2192_graphs.java](2192_graphs.java) | Java 1.8 | graphs | O(N + M + Q) | AC | 0.140 s | 10520 KB |
| [2192_graphs.py](2192_graphs.py) | Python 3.12 x64 | graphs | O(N + M + Q) | AC | 0.500 s | 77964 KB |
| [2192_graphs.rs](2192_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M + Q) | AC | 0.078 s | 28904 KB |
