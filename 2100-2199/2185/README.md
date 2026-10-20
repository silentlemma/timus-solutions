# 2185. Running many start values through add-if-negative, subtract-otherwise

[Timus 2185](https://acm.timus.ru/problem.aspx?space=1&num=2185) · difficulty 2681 · math

Original problem by Artyom Stepanov and Artyom Abaturov, from the Ural School Programming Contest 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An array a₁ … a_n is applied to a number x element by element: if x < 0
the element is added, otherwise it is subtracted. Report the final value
for each of q start values. The limits are 1.5 seconds and 512 MB.

## Input

n and q, 1 ≤ n, q ≤ 10⁶, then the array with |aᵢ| ≤ 10⁶ and q start
values with |xᵢ| ≤ 10⁶.

## Output

The final value for each start.

## Examples

### Example 1

Input:

```
3 2
3 1 2
4
-3
```

Output:

```
-2
1
```

### Example 2

Input:

```
3 4
2 1 4
10
-5
2
6
```

Output:

```
3
2
3
-1
```

## Solution

Write ~x = −x − 1. One step commutes with it: if x ≥ 0 then ~x < 0, and
~x + a = −(x − a) − 1 = ~(x − a). So the whole walk satisfies
f(~x) = ~f(x), and a negative start is answered from the nonnegative
start ~x. It remains to run all starts 0 … V at once, V ≤ 10⁶.

Keep an interval [L, R] of starts whose current values are all on the
same side of zero, so they all equal start + offset and one step only
moves the offset. When a step makes the interval straddle zero at the
start c = −offset, the starts below c have negative values and those
from c on have nonnegative ones. A start s below c currently holds
s + offset = ~((2c − 1 − s) + offset), the complement of its mirror
2c − 1 − s on the other side. So the smaller side is cut off with a
note to copy the complement of its mirror, which lies in the larger
side that stays, and since the commuting rule holds for every later
step, the relation still holds at the end.

At the end the kept interval gets start + offset, and the cut pieces
are filled in reverse order of cutting, each from mirrors that are
already known. Every start is cut at most once.

In the first example 4 goes to 1, 0 and then −2, and −3 = ~2, where 2
goes to −1, 0 and −2, so −3 ends at ~(−2) = 1.

The walk takes O(n), the filling O(V), and the queries O(q).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2185_math.cpp](2185_math.cpp) | G++ 13.2 x64 | math | O(n + q + V) | AC | 0.218 s | 28892 KB |
| [2185_math.go](2185_math.go) | Go 1.14 x64 | math | O(n + q + V) | AC | 0.218 s | 99692 KB |
| [2185_math.java](2185_math.java) | Java 1.8 | math | O(n + q + V) | AC | 0.703 s | 48808 KB |
| [2185_math.py](2185_math.py) | PyPy 3.10 x64 | math | O(n + q + V) | AC | 1.000 s | 229996 KB |
| [2185_math.rs](2185_math.rs) | Rust 1.75 x64 | math | O(n + q + V) | AC | 0.156 s | 62972 KB |
