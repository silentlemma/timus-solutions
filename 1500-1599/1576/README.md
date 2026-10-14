# 1576. Telephone Tariffs

[Timus 1576](https://acm.timus.ru/problem.aspx?space=1&num=1576) · difficulty 147 · implementation

Original problem: folklore, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three tariffs: basic, a fee N1 plus C1 per minute; combined, a fee N2
that includes T minutes, plus C2 for each minute over T; unlimited, a
fee N3. Calls of at most 6 seconds are free, and longer calls are
rounded up to whole minutes. Given up to 1000 calls as mm:ss, print the
monthly bill under each tariff.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N1 and C1, then N2, T and C2, then N3, then K and the K call lengths.

## Output

Three lines in the format of the examples.

## Examples

### Example 1

Input:

```
135 1
220 10 1
300
5
00:05
00:10
09:59
07:00
01:01
```

Output:

```
Basic:     155
Combined:  230
Unlimited: 300
```

### Example 2

Input:

```
10 2
100 1 1
1000
1
03:00
```

Output:

```
Basic:     16
Combined:  102
Unlimited: 1000
```

## Solution

Add up the paid minutes: a call of s seconds adds nothing when s ≤ 6
and ⌈s / 60⌉ otherwise. With M minutes the bills are N1 + C1·M,
N2 + C2·max(0, M − T) and N3. They stay below 7·10⁷. `O(K)`.

Pitfalls:

- a call of exactly 6 seconds is free, one of 7 seconds costs a whole
  minute, and a call of exactly one minute costs one (test 03);
- the combined tariff charges nothing extra while the minutes stay
  within T, so the overage is never negative;
- the labels are padded to the same width: `Basic:` with five spaces,
  `Combined:` with two, `Unlimited:` with one.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1576_implementation.cpp](1576_implementation.cpp) | G++ 13.2 x64 | implementation | O(K) | AC | 0.015 s | 132 KB |
| [1576_implementation.go](1576_implementation.go) | Go 1.14 x64 | implementation | O(K) | AC | 0.015 s | 1168 KB |
| [1576_implementation.java](1576_implementation.java) | Java 1.8 | implementation | O(K) | AC | 0.109 s | 2244 KB |
| [1576_implementation.py](1576_implementation.py) | Python 3.12 x64 | implementation | O(K) | AC | 0.078 s | 508 KB |
| [1576_implementation.rs](1576_implementation.rs) | Rust 1.75 x64 | implementation | O(K) | AC | 0.015 s | 232 KB |
