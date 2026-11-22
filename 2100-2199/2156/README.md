# 2156. Splitting the differences around a circle into equal halves

[Timus 2156](https://acm.timus.ru/problem.aspx?space=1&num=2156) · difficulty 656 · math, constructive

Original problem by Semyon Trifochkin, from the Ural Team Programming Contest 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n friends with interest values a₁ … aₙ sit around a table, and the
conversation between neighbours i and i + 1 (n and 1 for the last one)
has interest |aᵢ − aᵢ₊₁|. Split the n conversations into two non-empty
sets with equal total interest, or print NO. Any valid split is
accepted. The limits are 1 second and 256 MB.

## Input

n, 3 ≤ n ≤ 10⁵, then a₁ … aₙ, 1 ≤ aᵢ ≤ 10⁹.

## Output

YES, then the size and the numbers of the first set and of the second
set, or NO.

## Checking

A checker verifies that the two sets are non-empty, split all
conversations and have equal sums.

## Examples

### Example 1

Input:

```
3
1 2 3
```

Output:

```
YES
2
1 2
1
3
```

## Solution

The answer is always YES. Going once around the table, the signed
differences aᵢ − aᵢ₊₁ add up to 0. So the conversations where the value
falls (aᵢ > aᵢ₊₁) have the same total interest as those where it rises,
and conversations between equal neighbours have interest 0 and can join
either side.

If the values are not all equal, there is at least one fall and one
rise, so both sets are non-empty. If they are all equal, every
conversation has interest 0, and one conversation against the other
n − 1 works. The work is O(n).

In the example the values fall only from 3 back to 1, so conversation 3
(interest 2) balances conversations 1 and 2 (interest 1 each).

## Optimized solutions

`2156_math_constructive_optimized.cpp`. Keep the exact circular-drop partition. Read heights through a 4 KiB fread buffer, retaining only the first and previous heights, and mark descending edges in a bitset. If every height is equal, choose the first edge for one group. Scan the bitset twice to emit both groups through a 4 KiB fwrite buffer, without an input array or vectors of indices. Time O(n), n bits plus fixed buffers; the guaranteed valid partition and edge numbering are unchanged.

Exact-source Accepted #11326979: 0.015 s / 136 KB. Saved G++ 13.2 sample, 2026-11-20: time rank 1/33, memory rank 1/33. Teaching sources remain unchanged.

Read the values in order, keeping only the first and previous values. A bitset marks the falling edges. Two scans of the bitset print both groups without keeping the input array or building lists of indices.

Go uses one Boolean flag per edge and writes indices through a fixed-size buffer.

Python reads and writes in blocks and stores one byte per edge.

Rust uses one Boolean flag per edge and writes indices through a fixed-size buffer.

Java buffers input and output and keeps one Boolean flag per edge. It uses 656 KB instead of 9008 KB and takes 0.156 s instead of 0.140 s.

**Timus submissions for the optimized versions**

`2156_math_constructive_optimized.cpp` (G++ 13.2 x64) №11326979 · `2156_math_constructive_optimized.go` (Go 1.14 x64) №11317380 · `2156_math_constructive_optimized.java` (Java 1.8) №11317394 · `2156_math_constructive_optimized.py` (Python 3.12 x64) №11317384 · `2156_math_constructive_optimized.rs` (Rust 1.75 x64) №11317388.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321927 · Java 1.8 №11321928 · Python 3.12 x64 №11321930 · Rust 1.75 x64 №11321931.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2156_math_constructive.cpp](2156_math_constructive.cpp) | G++ 13.2 x64 | math, constructive | O(n) | AC | 0.093 s | 2652 KB | 11321927 |
| [2156_math_constructive.go](2156_math_constructive.go) | Go 1.14 x64 | math, constructive | O(n) | AC | 0.109 s | 8676 KB | 11322054 |
| [2156_math_constructive.java](2156_math_constructive.java) | Java 1.8 | math, constructive | O(n) | AC | 0.171 s | 8996 KB | 11321928 |
| [2156_math_constructive.py](2156_math_constructive.py) | Python 3.12 x64 | math, constructive | O(n) | AC | 0.156 s | 21304 KB | 11321930 |
| [2156_math_constructive.rs](2156_math_constructive.rs) | Rust 1.75 x64 | math, constructive | O(n) | AC | 0.078 s | 8860 KB | 11321931 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2156_math_constructive_optimized.cpp](2156_math_constructive_optimized.cpp) | G++ 13.2 x64 | math, constructive | O(n) | AC | 0.015 s | 136 KB | 11326979 |
| [2156_math_constructive_optimized.go](2156_math_constructive_optimized.go) \* | Go 1.14 x64 | math, constructive | O(n) | AC | 0.031 s | 1068 KB | 11317380 |
| [2156_math_constructive_optimized.py](2156_math_constructive_optimized.py) | Python 3.12 x64 | math, constructive | O(n) | AC | 0.125 s | 1164 KB | 11317384 |
| [2156_math_constructive_optimized.rs](2156_math_constructive_optimized.rs) \* | Rust 1.75 x64 | math, constructive | O(n) | AC | 0.046 s | 304 KB | 11317388 |
| [2156_math_constructive_optimized.java](2156_math_constructive_optimized.java) \* | Java 1.8 | math, constructive | O(n) | AC | 0.156 s | 656 KB | 11317394 |

\* The accepted C++ version still has room to improve in the target ranking. The Go rating has no comparable submissions from other participants in this snapshot. The Rust rating has no comparable submissions from other participants in this snapshot. Java meets the memory criterion and can improve its time rank.
