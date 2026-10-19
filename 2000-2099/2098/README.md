# 2098. Pay cash or pay more for insurance

[Timus 2098](https://acm.timus.ru/problem.aspx?space=1&num=2098) · difficulty 325 · math

Original problem by Denis Dublennykh, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

After a minor accident a driver can pay b roubles in cash, or register
it and let the insurance pay. The insurance costs c now and grows by d
every year, so the next k years cost c + d, c + 2d, …, c + kd; after a
registered accident those k payments are p percent higher. Say which
option is cheaper (Insurance on a tie) and by how much. The limits are
1 second and 64 MB.

## Input

b (up to 10⁵), then c and d (up to 10⁴), then k and p (up to 100).

## Output

`Cash` or `Insurance`, then the saving with an absolute or relative
error of at most 10⁻⁶.

## Examples

### Example 1

Input:

```
10000
5000 1000
3 50
```

Output:

```
Cash
500.00
```

### Example 2

Input:

```
15000
2500 1000
4 25
```

Output:

```
Insurance
10000.00
```

## Solution

Both options pay the usual insurance S = k·c + d·k(k + 1)/2 for the next
k years. Cash adds b, registration adds S·p/100. Comparing 100·b with
S·p keeps everything in integers (at most about 5·10⁹), and their
difference divided by 100 is the saving, printed exactly with two
decimals.

In the first example S = 21000, so registration costs 10500 more while
cash costs 10000 more: Cash, by 500.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2098_math.cpp](2098_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 136 KB |
| [2098_math.go](2098_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1080 KB |
| [2098_math.java](2098_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1744 KB |
| [2098_math.py](2098_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 424 KB |
| [2098_math.rs](2098_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 228 KB |
