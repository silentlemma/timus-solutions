# 1493. One Step from Happiness

[Timus 1493](https://acm.timus.ru/problem.aspx?space=1&num=1493) · difficulty 47 · implementation

Original problem by Vladimir Yakovlev, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A ticket has a six-digit number, leading zeros included; it is lucky if
its first three digits and its last three digits have equal sums. The
given ticket's two sums differ by exactly one. Print "Yes" if the
previous or the next ticket is lucky, and "No" otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The six digits of the ticket.

## Output

"Yes" or "No".

## Examples

### Example 1

Input:

```
715068
```

Output:

```
Yes
```

### Example 2

Input:

```
445219
```

Output:

```
No
```

### Example 3

Input:

```
012200
```

Output:

```
Yes
```

## Solution

Check the two neighbours directly: take the number minus one and plus
one, write each with six digits, and compare the sums of the halves.
The sums of the given ticket differ, so it is neither 000000 nor 999999,
and both neighbours are real tickets. Carries can change several digits
at once, which is why the neighbours are recomputed rather than
adjusted by one digit. `O(1)`.

Pitfalls:

- the number may start with zeros, and they still count as digits
  (test 03); a reader that treats a leading 0 as octal breaks it;
- a carry or a borrow across the middle changes both halves, as from
  100000 to 099999 (tests 06, 08, 09);
- the neighbours 000000 and 999999 are lucky tickets too (tests 04, 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1493_implementation.cpp](1493_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 124 KB |
| [1493_implementation.go](1493_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB |
| [1493_implementation.java](1493_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1596 KB |
| [1493_implementation.py](1493_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.062 s | 376 KB |
| [1493_implementation.rs](1493_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.062 s | 224 KB |
